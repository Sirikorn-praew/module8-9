import sys
import copy
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime,
                            QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent, QThread, Signal, QRegExp, QEventLoop)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase,
                           QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

import chess
import setting_chess
# from position import Position
from pychess.gameState import GameState
from pychess.chessAgent import ChessAgent
# from pychess.ui_board import Ui_ChessBoard

# SQR_SIZE = 720/8


class ChessBoard(QFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.sqr_size = 720/8

        self.parent = parent

        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setContentsMargins(0, 0, 0, 0)

        self.layout = QGridLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        self.draw_squares()
        self.setLayout(self.layout)

        self.gamestate = GameState(setting_chess.starting_fen)
        # self.user_is_white = self.parent.user_is_white
        self.agent = ChessAgent(self.gamestate, 5)
        self.search_thread = SearchThread(self)
        self.agent_play = False
        self.user_is_white = True
        self.autosave = True
        self.saved = True

        self.undone_stack = []

    def resizeEvent(self, event):
        if event.size().width() > event.size().height():
            self.resize(event.size().height(), event.size().height())
            self.sqr_size = int(event.size().height() / 8)
        else:
            self.resize(event.size().width(), event.size().width())
            self.sqr_size = int(event.size().width() / 8)

    def start_game(self):
        if self.gamestate.colour() == self.user_is_white:
            self.disable_pieces()
            self.search_thread.start()
        else:
            self.enable_pieces()

    def start_game_process(self):
        if self.agent_play or self.gamestate.colour() == self.user_is_white:
            self.disable_pieces()
            self.search_thread.start()
        else:
            self.enable_pieces()

    def draw_squares(self):
        for row, rank in enumerate('87654321'):
            for col, file in enumerate('abcdefgh'):
                square = QWidget(self)
                square.setObjectName(file + rank)
                if self.sqr_size != 720/8:
                    square.setSizePolicy(self.sqr_size,
                                         self.sqr_size)
                else:
                    square.setSizePolicy(QSizePolicy.Expanding,
                                         QSizePolicy.Expanding)
                if row % 2 == col % 2:
                    square.setStyleSheet('background-color: #F4EAD1')  # F0DFB5
                else:
                    square.setStyleSheet('background-color: #6390B5')
                self.layout.addWidget(square, row, col)

    def place_piece(self, sqr_name, piece):
        col, row = setting_chess.square_to_coords[sqr_name]

        piece_label = PieceLabel(self, piece)
        self.layout.addWidget(piece_label, row, col)

    def piece_at_square(self, sqr_index):
        square = self.findChild(QWidget, chess.square_name(sqr_index))
        square_pos = self.layout.getItemPosition(self.layout.indexOf(square))
        for piece in self.findChildren(QLabel):
            piece_pos = self.layout.getItemPosition(self.layout.indexOf(piece))
            if square_pos == piece_pos:
                return piece

    def set_fen(self, fen):
        # self.position = Position(fen)
        self.gamestate = GameState(fen)
        self.agent = ChessAgent(self.gamestate, 5)
        # self.search = Search(self.position)
        self.refresh_from_state()

    def set_gamestate(self, gamestate):
        self.gamestate = gamestate
        self.agent = ChessAgent(self.gamestate, 5)
        # self.position = position
        # self.search = Search(self.position)
        self.refresh_from_state()

    def clear(self):
        all_pieces = self.findChildren(QLabel)
        for piece in all_pieces:
            piece.setParent(None)  # Delete piece

    def refresh_from_state(self):
        QApplication.processEvents()

        self.clear()

        for sqr_index in range(64):
            piece = self.gamestate.boardPlay.piece_at(sqr_index)
            sqr_name = chess.SQUARE_NAMES[sqr_index]

            if piece:
                pieceInt = setting_chess.piece_string_to_int[str(piece)]
                self.place_piece(sqr_name, pieceInt)

    def reset(self):
        self.set_fen(setting_chess.starting_fen)
        self.refresh_from_state()

        self.gamestate.undo_info.clear()
        self.undone_stack.clear()

    def highlight(self, sq):
        # If square index given, convert to SAN
        if not setting_chess.regex_square.match(str(sq)):
            sq = chess.square_name(sq)

        square = self.findChild(QWidget, sq)

        col, row = setting_chess.square_to_coords[sq]

        if row % 2 == col % 2:  # light square
            square.setStyleSheet('background-color: #b0b3b6')  # F7EC74
        else:  # dark square
            square.setStyleSheet('background-color: #656a6e')  # DAC34B

    def unhighlight(self, sq):
        # If square index given, convert to SAN
        if not setting_chess.regex_square.match(str(sq)):
            sq = chess.square_name(sq)

        square = self.findChild(QWidget, sq)

        col, row = setting_chess.square_to_coords[sq]

        if row % 2 == col % 2:  # light square
            square.setStyleSheet('background-color: #F4EAD1')
        else:  # dark square
            square.setStyleSheet('background-color: #6390B5')

    def unhighlight_all(self):
        for sqr_index in range(64):
            self.unhighlight(sqr_index)

    def moves_from_square(self, sqr_index):
        moves = []
        legal_moves = self.gamestate.boardPlay.legal_moves

        for move in legal_moves:
            if move.from_square == sqr_index:
                moves.append(chess.square_name(move.to_square))

        return moves

    def disable_pieces(self):
        for piece in self.findChildren(QLabel):
            piece.is_enabled = False

    def enable_pieces(self):
        for piece in self.findChildren(QLabel):
            piece.is_enabled = True

    def piece_glide(self, piece, dst_index):
        piece.raise_()
        dst_square = self.findChild(QWidget, chess.square_name(dst_index))
        self.glide = QPropertyAnimation(piece, b'pos')
        self.glide.setDuration(500)
        self.glide.setEndValue(dst_square.pos())
        self.glide.start()

        # Start local event loop, so program waits until glide is completed
        loop = QEventLoop()
        self.glide.finished.connect(loop.quit)
        loop.exec_()

    def do_rook_castle(self, king_dst, is_undo):
        if king_dst == 2:
            rook_src = 0
            rook_dst = 3
        elif king_dst == 6:
            rook_src = 7
            rook_dst = 5
        elif king_dst == 58:
            rook_src = 56
            rook_dst = 59
        elif king_dst == 62:
            rook_src = 63
            rook_dst = 61

        if is_undo:
            rook = self.piece_at_square(rook_dst)
            self.piece_glide(rook, rook_src)
        else:
            rook = self.piece_at_square(rook_src)
            self.piece_glide(rook, rook_dst)

    def move_glide(self, move, is_undo):

        src_index = move.from_square
        dst_index = move.to_square

        if not is_undo:
            piece = self.piece_at_square(src_index)
        else:
            piece = self.piece_at_square(dst_index)

        self.piece_glide(piece, src_index if is_undo else dst_index)

        if self.gamestate.is_castling(move):
            self.do_rook_castle(dst_index, is_undo)

    def player_move(self, move):
        self.disable_pieces()
        self.parent.info.button_frame.disable_buttons()

        self.gamestate.make_move(move)
        self.refresh_from_state()

        # After a move has been made, the player can no longer redo moves that were undone previously
        self.undone_stack.clear()

        self.parent.info.move_frame.update_moves()

        if self.gamestate.is_game_over():
            self.game_over()
            print("game over")
        else:
            self.saved = False
            self.search_thread.start()  # Start search thread for computer's move

    def computer_move(self, move):
        self.move_glide(move, False)

        self.gamestate.make_move(move)
        self.refresh_from_state()

        self.parent.info.move_frame.update_moves()

        if self.gamestate.is_game_over():
            self.game_over()
        else:
            if self.autosave:
                self.save()
            else:
                self.saved = False

            if self.agent_play:
                self.search_thread.start()
            else:
                self.enable_pieces()

        self.parent.info.button_frame.enable_buttons()

    def game_over(self):
        # user = self.parent.user

        # legal_moves = list(filter(self.position.is_legal,
        #                           self.position.get_pseudo_legal_moves()))

        # if not legal_moves:
        #     # Checkmate
        #     if self.position.is_in_check():
        #         text = "{} wins by checkmate".format(
        #             "White" if self.position.colour else "Black")
        #         if user:
        #             user.add_win() if self.user_is_white == bool(
        #                 self.position.colour) else user.add_loss()
        #     # Stalemate
        #     else:
        #         text = "Draw by stalemate"
        #         if user:
        #             user.add_draw()
        # # Fifty-move rule
        # elif self.position.halfmove_clock >= 100:
        #     text = "Draw by fifty-move rule"
        #     if user:
        #         user.add_draw()
        # # Threefold repetition
        # elif self.position.is_threefold_repetition():
        #     text = "Draw by threefold repetition"
        #     if user:
        #         user.add_draw()
        # elif self.position.is_insufficient_material():
        #     text = "Draw by insufficient material"
        #     if user:
        #         user.add_draw()

        # Checkmate
        if self.gamestate.boardPlay.is_checkmate():
            text = "{} wins by Checkmate".format(
                "Black" if not self.gamestate.colour() else "White")
        # elif self.gamestate.boardPlay.is_check():
        #     print("check")

        # Stalemate
        elif self.gamestate.boardPlay.is_stalemate():
            text = "Draw by Stalemate"

        elif self.gamestate.boardPlay.is_insufficient_material():
            text = "Draw by insufficient material"

        # Fifty-move rule
        elif self.gamestate.boardPlay.is_fifty_moves():
            text = "Draw by fifty-move rule"

        # Threefold repetition
        elif self.gamestate.boardPlay.can_claim_threefold_repetition():
            text = "Draw by threefold repetition"
         # elif board.is_game_over():
        #     print("Game Over!")
        text = text + '\n' + \
            f"\nResult: [W] {self.gamestate.boardPlay.result()} [B]"

        msg_box = QMessageBox()
        msg_box.setWindowIcon(QIcon('./icons/chessMenu/chessIcon.png'))
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setWindowTitle("Chess")
        msg_box.setIconPixmap(QPixmap('./icons/chessMenu/game-over.png'))
        msg_box.setText(text)
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec_()

        self.saved = True

    def save(self):
        self.parent.saved_game = copy.deepcopy(self.gamestate)
        self.saved = True


# Search algorithm must be run in a separate thread to the main event loop, to prevent the GUI from freezing
class SearchThread(QThread):
    move_signal = Signal(chess.Move)

    def __init__(self, board):
        super().__init__()

        self.board = board
        self.move_signal.connect(self.board.computer_move)

    def run(self):
        self.board.disable_pieces()

        move = self.board.agent.playMove(debug=True)

        # if self.board.difficulty == 1:
        #     move = self.board.search.iter_search(max_depth=1)  # Depth 1 search
        # elif self.board.difficulty == 2:
        #     move = self.board.search.iter_search(max_depth=2)  # Depth 2 search
        # elif self.board.difficulty == 3:
        #     move = self.board.search.iter_search(
        #         time_limit=0.1)  # 0.1 second search
        # elif self.board.difficulty == 4:
        #     move = self.board.search.iter_search(
        #         time_limit=1)  # 1 second search
        # elif self.board.difficulty == 5:
        #     move = self.board.search.iter_search(
        #         time_limit=5)  # 5 second search

        self.board.gamestate = self.board.agent.gamestate

        self.move_signal.emit(move)


class PieceLabel(QLabel):
    def __init__(self, parent, piece):
        super().__init__(parent)

        self.piece = piece

        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setMinimumSize(1, 1)

        # Make label transparent, so square behind piece is visible
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.board = parent
        self.is_white = False if self.piece >> 3 else True
        self.is_enabled = True
        self.sqr_size = self.board.sqr_size

        self.src_pos = None
        self.mouse_pos = None
        self.src_square = None
        self.dst_square = None
        self.legal_moves = None
        self.legal_dst_squares = None

        # Store original piece image
        pixmap = QPixmap('./assets/pieces/{}{}.png'.format('w' if self.is_white else 'b',
                                                           setting_chess.piece_int_to_string[self.piece].lower()))
        if self.sqr_size != 720/8:
            pixmap = pixmap.scaled(
                self.sqr_size, self.sqr_size, QtCore.Qt.KeepAspectRatio, Qt.FastTransformation)
        self.setPixmap(pixmap)

        # When label is scaled, also scale image inside the label
        self.setScaledContents(True)

        self.setMouseTracking(True)

        self.show()

    def resizeEvent(self, event):
        if event.size().width() > event.size().height():
            self.resize(event.size().height(), event.size().height())
        else:
            self.resize(event.size().width(), event.size().width())

    def enterEvent(self, event):
        if self.is_enabled:
            if self.board.user_is_white == self.is_white:
                # Set open hand cursor while hovering over a piece
                QApplication.setOverrideCursor(Qt.OpenHandCursor)

    def leaveEvent(self, event):
        # Set arrow cursor while not hovering over a piece
        QApplication.setOverrideCursor(Qt.ArrowCursor)

    def mousePressEvent(self, event):
        if self.is_enabled:
            if event.buttons() == Qt.LeftButton:
                if self.board.user_is_white == self.is_white:
                    # Set closed hand cursor while dragging a piece
                    QApplication.setOverrideCursor(Qt.ClosedHandCursor)

                    # Raise piece to the front
                    self.raise_()

                    # Store mouse position and square position, relative to the chessboard
                    self.mouse_pos = self.mapToParent(
                        self.mapFromGlobal(event.globalPos()))
                    self.src_pos = self.mapToParent(self.rect().topLeft())

                    # Snap to cursor
                    offset = self.rect().topLeft() - self.rect().center()
                    self.move(self.mouse_pos + offset)

                    # Identify origin square
                    all_squares = self.board.findChildren(
                        QWidget, QRegExp(r'[a-h][1-8]'))
                    for square in all_squares:
                        if square.pos() == self.src_pos:
                            self.src_square = square
                            break

                    # Identify legal moves
                    sqr_index = chess.parse_square(
                        self.src_square.objectName())
                    # sqr_index = common.san_to_index[self.src_square.objectName(
                    # )]
                    self.legal_dst_squares = self.board.moves_from_square(
                        sqr_index)

                    # Only need destination square for each move
                    # self.legal_dst_squares = list(
                    #     map(lambda move: common.index_to_san[move & 0x3F], self.legal_moves))

                    # Highlight origin and destination squares
                    self.board.highlight(sqr_index)
                    for dst_square in self.legal_dst_squares:
                        self.board.highlight(dst_square)

    def mouseMoveEvent(self, event):
        if self.is_enabled:
            if event.buttons() == Qt.LeftButton:
                if self.board.user_is_white == self.is_white:
                    # Update mouse position, relative to the chess board
                    self.mouse_pos = self.mapToParent(
                        self.mapFromGlobal(event.globalPos()))

                    # Calculate offset from centre to top-left of square
                    offset = self.rect().topLeft() - self.rect().center()

                    # Calculate new x position, not allowing the piece to go outside the board
                    if self.mouse_pos.x() < self.board.rect().left():
                        new_pos_x = self.board.rect().left() + offset.x()
                    elif self.mouse_pos.x() > self.board.rect().right():
                        new_pos_x = self.board.rect().right() + offset.x()
                    else:
                        new_pos_x = self.mouse_pos.x() + offset.x()

                    # Calculate new y position, not allowing the piece to go outside the board
                    if self.mouse_pos.y() < self.board.rect().top():
                        new_pos_y = self.board.rect().top() + offset.y()
                    elif self.mouse_pos.y() > self.board.rect().bottom():
                        new_pos_y = self.board.rect().right() + offset.y()
                    else:
                        new_pos_y = self.mouse_pos.y() + offset.y()

                    # Move piece to new position
                    self.move(new_pos_x, new_pos_y)

    def mouseReleaseEvent(self, event):
        if self.is_enabled:
            if self.board.user_is_white == self.is_white:
                # Set open hand cursor when piece is released
                QApplication.setOverrideCursor(Qt.OpenHandCursor)

                self.board.unhighlight_all()

                # If mouse not released on board, move piece back to origin square, and return
                if not self.board.rect().contains(self.board.mapFromGlobal(event.globalPos())):
                    self.move(self.src_pos)
                    return

                # Identify destination square
                all_squares = self.board.findChildren(
                    QWidget, QRegExp(r'[a-h][1-8]'))
                for square in all_squares:
                    if square.rect().contains(square.mapFromGlobal(event.globalPos())):
                        self.dst_square = square
                        break

                if self.dst_square.objectName() in self.legal_dst_squares:  # If legal move
                    # Snap to destination square
                    self.board.layout.removeWidget(self)
                    row = self.dst_square.y() // self.board.sqr_size
                    col = self.dst_square.x() // self.board.sqr_size
                    self.board.layout.addWidget(self, row, col)

                    src_sqr_index = chess.parse_square(
                        self.src_square.objectName())
                    dst_sqr_index = chess.parse_square(
                        self.dst_square.objectName())

                    # from_to = self.src_square.objectName() + self.dst_square.objectName()
                    # print(from_to)

                    #  If enemy piece is at destination square, remove it from the board (capture)
                    piece_label = self.board.piece_at_square(dst_sqr_index)
                    if piece_label:
                        if piece_label.is_white != self.is_white:
                            piece_label.setParent(None)

                    # for move in self.legal_moves:
                    #     if move & 0xFFF == from_to:
                    #         move_made = move

                #     move_type = move_made & (0x3 << 14)
                    # move_made = chess.Move.from_uci(from_to)
                    move_made = self.board.gamestate.boardPlay.find_move(
                        src_sqr_index, dst_sqr_index)
                    # print(self.board.gamestate.boardPlay)
                    # print(move_made.promotion)

                    if move_made.promotion is not None:
                        promotion_prompt = QMessageBox()
                        promotion_prompt.setWindowIcon(
                            QIcon('./icons/chessMenu/chessIcon.png'))
                        promotion_prompt.setIcon(QMessageBox.Question)
                        promotion_prompt.setWindowTitle("Chess")
                        promotion_prompt.setText("Choose promotion piece.")
                        knight_btn = promotion_prompt.addButton(
                            "Knight", QMessageBox.AcceptRole)
                        bishop_btn = promotion_prompt.addButton(
                            "Bishop", QMessageBox.AcceptRole)
                        rook_btn = promotion_prompt.addButton(
                            "Rook", QMessageBox.AcceptRole)
                        queen_btn = promotion_prompt.addButton(
                            "Queen", QMessageBox.AcceptRole)
                        promotion_prompt.exec()

                        if promotion_prompt.clickedButton() == knight_btn:
                            move_made = self.board.gamestate.boardPlay.find_move(
                                src_sqr_index, dst_sqr_index, 2)
                            self.setPixmap(
                                QPixmap('./assets/pieces/{}.png'.format('wn' if self.is_white else 'bn')))
                        elif promotion_prompt.clickedButton() == bishop_btn:
                            move_made = self.board.gamestate.boardPlay.find_move(
                                src_sqr_index, dst_sqr_index, 3)
                            self.setPixmap(
                                QPixmap('./assets/pieces/{}.png'.format('wb' if self.is_white else 'bb')))
                        elif promotion_prompt.clickedButton() == rook_btn:
                            move_made = self.board.gamestate.boardPlay.find_move(
                                src_sqr_index, dst_sqr_index, 4)
                            self.setPixmap(
                                QPixmap('./assets/pieces/{}.png'.format('wr' if self.is_white else 'br')))
                        elif promotion_prompt.clickedButton() == queen_btn:
                            move_made = self.board.gamestate.boardPlay.find_move(
                                src_sqr_index, dst_sqr_index, 5)
                            self.setPixmap(
                                QPixmap('./assets/pieces/{}.png'.format('wq' if self.is_white else 'bq')))
                    elif self.board.gamestate.is_castling(move_made):
                        self.board.do_rook_castle(dst_sqr_index, False)

                    self.board.player_move(move_made)
                else:
                    # Snap back to origin square
                    self.move(self.src_pos)
