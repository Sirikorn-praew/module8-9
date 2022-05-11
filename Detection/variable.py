import chess
import numpy as np
class get_matrix_variable():

    # init method or constructor
    def __init__(self):
        self.clear_image =[]
        self.matrix =[]
        # self.color_img = []
        # self.corner = []
        self.new_matrix_to_crop=[]
        self.new_matrix=[]

        self.list_of_image_old=[]
        self.list_of_image_new=[]
        self.index_not_empty=[]
        self.fen=''
        self.color_play=1 #defult1is black

        self.thresh=0

    def grouping(self):
        print('test')
class to_trackback():
    def __init__(self):
        # self.old_pred_empty = []
        self.count=0

        self.move_change =[]
        self.centroid=None

        self.color_threshold='H'

        #Old
        self.fen_before='rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
        self.board_old=chess.Board(self.fen_before)
        self.board_list_old=list(str(self.board_old).replace(' ', '').replace('\n', ''))
        # self.board_list_square_old=np.reshape(self.board_list_old, (8, 8))
        self.old_pred_empty = [1,  1,  1,  1,  1,  1,  1,  1, 
                               1,  1,  1,  1,  1,  1,  1,  1,
                               0,  0,  0,  0,  0,  0,  0,  0, 
                               0,  0,  0,  0,  0,  0,  0,  0,
                               0,  0,  0,  0,  0,  0,  0,  0,
                               0,  0,  0,  0,  0,  0,  0,  0,
                               1,   1,  1,  1,  1, 1,  1,  1, 
                               1,   1,  1,  1,  1, 1,  1,  1]

        #New
        self.new_pred_empty = []
        self.board_list_new=['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r',
                            'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p',
                            '.', '.', '.', '.', '.', '.', '.', '.',
                            '.', '.', '.', '.', '.', '.', '.', '.',
                            '.', '.', '.', '.', '.', '.', '.', '.',
                            '.', '.', '.', '.', '.', '.', '.', '.',
                            'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P',
                            'R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        # self.board_list_new=list(str(self.board_new).replace(' ', '').replace('\n', ''))
        # self.board_list_square_new=np.reshape(self.board_list_new, (8, 8))
        # ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r',
        #                      'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p',
        #                      '.', '.', '.', '.', '.', '.', '.', '.',
        #                      '.', '.', '.', '.', '.', '.', '.', '.',
        #                      '.', '.', '.', '.', '.', 'P', '.', '.',
        #                      '.', '.', '.', '.', '.', '.', '.', '.',
        #                      'P', 'P', 'P', 'P', 'P', '.', 'P', 'P',
        #                      'R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']#list(str(self.board).replace(' ', '').replace('\n', ''))
        # self.board_list_new=[]
        # 
        # # self.board_list_square_new=np.reshape(self.board_list_new, (8, 8))
        self.board_color_old=[1,   1,  1,  1,  1,  1,  1,  1, 
                              1,   1,  1,  1,  1,  1,  1,  1,
                              -1, -1, -1, -1, -1, -1, -1, -1, 
                              -1, -1, -1, -1, -1, -1, -1, -1,
                              -1, -1, -1, -1, -1,  -1, -1, -1,
                              -1, -1, -1, -1, -1, -1, -1, -1,
                              0,   0,  0,  0,  0, 0,  0,  0, 
                              0,   0,  0,  0,  0,  0,  0,  0]
        self.board_color_new=[1,   1,  1,  1,  1,  1,  1,  1, 
                              1,   1,  1,  1,  1,  1,  1,  1,
                              -1, -1, -1, -1, -1, -1, -1, -1, 
                              -1, -1, -1, -1, -1, -1, -1, -1,
                              -1, -1, -1, -1, -1,  -1, -1, -1,
                              -1, -1, -1, -1, -1, -1, -1, -1,
                              0,   0,  0,  0,  0, 0,  0,  0, 
                              0,   0,  0,  0,  0,  0,  0,  0]
        # self.board_color_new=[]
        # def square(self):
        #     self.board_list_square_new=np.reshape(self.board_list_new, (8, 8))
        # self.matrix =[]

# t=to_trackback()
# print(t.board_list)
# both objects have different self which
# contain their attributes
# audi = car("audi a4", "blue")
# ferrari = car("ferrari 488", "green")

# audi.show()     # same output as car.show(audi)
# ferrari.show()  # same output as car.show(ferrari)
