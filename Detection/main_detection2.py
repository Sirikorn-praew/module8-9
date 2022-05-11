from Detection import DetectAllPoints as dtp
from Detection import DetectionFunctions as df
from Detection import color_classify
from Detection import variable


# cap_side = MediaPipe_check_Hand(1)

import chess
# import DetectAllPoints as dtp
# import DetectionFunctions as df
# import color_classify
# import variable


from PIL import Image
import cv2
import base64
import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import os
import math
import copy
import tensorflow as tf
import mediapipe as mp
# import keras


# mp_hands = mp.solutions.hands

# tb=variable.to_trackback
# tb_top=tb()

# get_m = variable.get_matrix_variable
# top_data = get_m()
# side_data = get_m()

# cap_top = MediaPipe_check_Hand()
# # cap_side = MediaPipe_check_Hand(1)
# modelE4_top = EfficientNetModel(
#     '.\Detection\checkpoint_top', (380, 380))
# modelE4 = EfficientNetModel(
#     '.\Detection\checkpoint_data', (380, 380))

class MediaPipe_check_Hand:
    def __init__(self):
        # loading trained model
        print('start mp')

    def check_hand(self, image):
        leng = 200
        # self.ret, self.frame = self.openCam.read()
        self.frame = image[0:image.shape[0], leng:image.shape[1]-leng]
        # self.ret, self.frame = self.openCam.read()
        # self.frame = image.copy()

        with mp_hands.Hands(
                min_detection_confidence=0.7,  # 0.7
                min_tracking_confidence=0.5) as hands:
            # if not self.ret:
            #     print("Ignoring empty camera frame.")
            #     return None
            # Flip the image horizontally for a later selfie-view display, and convert
            # the BGR image to RGB.
            self.frame = cv2.cvtColor(
                cv2.flip(self.frame, 1), cv2.COLOR_BGR2RGB)
            # To improve performance, optionally mark the image as not writeable to
            # pass by reference.
            self.frame.flags.writeable = False
            results = hands.process(self.frame)

            # Draw the hand annotations on the image.
            self.frame.flags.writeable = True
            self.frame = cv2.cvtColor(self.frame, cv2.COLOR_RGB2BGR)
            if not results.multi_hand_landmarks:
                return 'No Hand'
            else:
                return 'Hand'


mp_hands = mp.solutions.hands

tb = variable.to_trackback
tb_top = tb()

get_m = variable.get_matrix_variable
top_data = get_m()
side_data = get_m()

cap_top = MediaPipe_check_Hand()


class EfficientNetModel:
    def __init__(self, checkpoint_file_path, input_shape):
        # loading trained model
        self.checkpoint_file_path = checkpoint_file_path
        self.model = tf.keras.models.load_model(self.checkpoint_file_path)
        # self.model.summary()
        # self.target = sorted(list_of_target_name.copy())
        # print(self.target)
        self.input_shape = input_shape

    def read_image(self, image_path):
        return cv2.imread(image_path)

    def resize_image(self, image):
        return cv2.resize(image, (self.input_shape[1], self.input_shape[0]), interpolation=cv2.INTER_CUBIC)

    def make_prediction(self, image):
        resized_image = self.resize_image(image)
        image_array = np.array([resized_image])
        return tf.argmax(self.model.predict(image_array), axis=1)


# modelE4_top = EfficientNetModel(
#     '.\Detection\checkpoint_top', (380, 380))


# print(model.summary)
# print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))
# print(model_hyper_load.summary())


def distance_of_two_point(point1, point2):
    return math.sqrt(((point1[0] - point2[0]) ** 2) + ((point1[1] - point2[1]) ** 2))


def crop_perspective_for_dataset(list_of_four_point_input, image):
    list_of_four_point = list_of_four_point_input.copy()
    tl_score = list_of_four_point[0][0] + list_of_four_point[0][1]
    # br_score = list_of_four_point[0][0] + list_of_four_point[0][1]
    tl = list_of_four_point[0]
    # br = list_of_four_point[0]
    for point in list_of_four_point:
        if point[0] + point[1] < tl_score:
            tl_score = point[0] + point[1]
            tl = point
    list_of_four_point.remove(tl)
    max_distance = distance_of_two_point(tl, list_of_four_point[0])
    br = list_of_four_point[0]
    for point in list_of_four_point:
        if distance_of_two_point(tl, point) > max_distance:
            max_distance = distance_of_two_point(tl, point)
            br = point
    list_of_four_point.remove(br)
    tr = list_of_four_point[0]
    for point in list_of_four_point:
        if point[1] < tr[1]:
            tr = point
    list_of_four_point.remove(tr)
    bl = list_of_four_point[0]

    # # now that we have our rectangle of points, let's compute
    # # the width of our new image
    # (tl, tr, br, bl) = rect
    widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
    widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
    # ...and now for the height of our new image
    heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
    heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
    # take the maximum of the width and height values to reach
    # our final dimensions
    # print(int(widthA), int(widthB))
    # print(int(heightA), int(heightB))
    maxWidth = max(int(widthA), int(widthB))
    maxHeight = max(int(heightA), int(heightB))
    # construct our destination points which will be used to
    # map the screen to a top-down, "birds eye" view
    dst = np.array(
        [[0, 0], [maxWidth - 1, 0], [maxWidth - 1, maxHeight - 1], [0, maxHeight - 1]],
        dtype="float32",
    )
    # calculate the perspective transform matrix and warp
    # the perspective to grab the screen
    rect = np.array([tl, tr, br, bl], dtype="float32")
    M = cv2.getPerspectiveTransform(rect, dst)
    warp = cv2.warpPerspective(image, M, (maxWidth, maxHeight))
    return warp


def crop_for_dataset_piece(list_of_four_point, image, head_offset):
    min_x = list_of_four_point[0][0]
    max_x = list_of_four_point[0][0]
    min_y = list_of_four_point[0][1]
    max_y = list_of_four_point[0][1]
    # print(min_x, max_x, min_y, max_y)
    for point in list_of_four_point:
        if point[0] < min_x:
            min_x = point[0]
        if point[0] > max_x:
            max_x = point[0]
        if point[1] < min_y:
            min_y = point[1]
        if point[1] > max_y:
            max_y = point[1]
    # cropped_image = image[(min_y-head_offset):max_y, min_x:max_x]
    cropped_image = image[
        int(min_y - head_offset): int(max_y), int(min_x): int(max_x)
    ]
    return cropped_image


def dectect_chessboard_point(images):
    matrix_all = []
    for image in images:
        clear_image, encoded_image, matrix = dtp.getMatrixFromImage(image)
        matrix_all.append(matrix)
    return matrix_all[0], matrix_all[1]


def lineFromPoints(P, Q):
    a = Q[1] - P[1]
    b = P[0] - Q[0]
    c = a * (P[0]) + b * (P[1])
    return a, b, c


def new_point_from_distance(point_one, point_two, d):
    dx = point_two[0] - point_one[0]
    dy = point_two[1] - point_one[1]

    distance = math.sqrt(dx**2 + dy**2)

    angle = math.atan2(dy, dx)

    a = math.cos(angle) * d  # (distance/5)
    b = math.sin(angle) * d  # (distance/5)

    x_a = point_one[0] - a
    y_b = point_one[1] - b

    return [round(x_a), round(y_b)]


# def new_point_by_distance(x1, y1, x2, y2):
#     length = 10
#     lenAB = math.sqrt(pow(x1 - x2, 2.0) + pow(y1 - y2, 2.0))
#     length = lenAB+10
#     x_new = x2 + (x2 - x1) / lenAB * length
#     y_new = y2 + (y2 - y1) / lenAB * length
#     return[x_new, y_new]


def plot_point(image, matrix):
    count = 0
    for side in matrix:
        count_row = 0
        for point in side:
            # print(point)
            image = cv2.circle(
                image,
                (math.floor(point[0]), math.floor(point[1])),
                radius=2,
                color=(0, count * 50, 0),
                thickness=-1,
            )
            cv2.putText(
                image,
                str(count) + str(count_row),
                (math.floor(point[0]), math.floor(point[1])),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.4,
                (0, 0, 255),
                1,
            )
            count_row += 1
        count += 1
    # cv2.imshow("plot", image)


def collect_side_point(matrix):
    side_1 = []
    side_2 = []
    side_3 = []
    side_4 = []
    for point in range(9):
        side_1.append(matrix[0][point])
        side_2.append(matrix[point][8])
        side_3.append(matrix[8][point])
        side_4.append(matrix[point][0])
        # print(point)
    side_point = [side_1, side_2, side_3, side_4]
    return side_point


def pair_point_to_find_side(img, side_point):
    plot_point(img, side_point)
    side_pair_point = []
    for side in range(2):
        set_of_pair = []
        for point in range(1, 8):
            pair_point = [side_point[side][point], side_point[side + 2][point]]
            # print(side, side + 2, point, pair_point)
            set_of_pair.append(pair_point)
        side_pair_point.append(set_of_pair)
    # print(side_pair_point)
    return side_pair_point


def get_four_side_color(image, side_pair_point):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    color_of_side = [[], [], [], []]
    # print(image.shape)
    for pair in range(len(side_pair_point)):
        point_on_side1 = []
        point_on_side2 = []
        for point in side_pair_point[pair]:

            point1 = point[0]
            point2 = point[1]

            new_point1 = new_point_from_distance(
                (point2[0], point2[1]), (point1[0], point1[1]), 5
            )
            # print(pair, new_point1, point1[0], point1[1], point2[0], point2[1])
            # print(gray.shape,new_point1[1],new_point1[0])
            # print(gray[int(new_point1[1]), int(new_point1[0])])
            point_on_side1.append(gray[int(new_point1[1])][int(new_point1[0])])

            new_point2 = new_point_from_distance(
                (point1[0], point1[1]), (point2[0], point2[1]), 5
            )
            # print(pair+2, new_point2, point1[0],
            #   point1[1], point2[0], point2[1])
            point_on_side2.append(gray[int(new_point2[1])][int(new_point2[0])])
            if pair == 0:
                image = cv2.circle(
                    image,
                    (math.floor(new_point1[0]), math.floor(new_point1[1])),
                    radius=1,
                    color=(0, 0, 0),
                    thickness=-1,
                )
                image = cv2.circle(
                    image,
                    (math.floor(new_point2[0]), math.floor(new_point2[1])),
                    radius=1,
                    color=(255, 255, 255),
                    thickness=-1,
                )
            elif pair == 1:
                image = cv2.circle(
                    image,
                    (math.floor(new_point1[0]), math.floor(new_point1[1])),
                    radius=1,
                    color=(255, 0, 0),
                    thickness=-1,
                )
                image = cv2.circle(
                    image,
                    (math.floor(new_point2[0]), math.floor(new_point2[1])),
                    radius=1,
                    color=(0, 255, 0),
                    thickness=-1,
                )

        color_of_side[pair] = point_on_side1
        color_of_side[pair + 2] = point_on_side2
    # cv2.imshow("find_side", image)
    return color_of_side


def evaluate_board_side(color_of_side):
    avg_color = []
    for side in range(len(color_of_side)):
        avg_color.append(sum(color_of_side[side]) / len(color_of_side[side]))

    if abs(avg_color[0] - avg_color[2]) > abs(avg_color[1] - avg_color[3]):
        if avg_color[0] > avg_color[2]:
            print("2 is white, 0 is black")
            first_corner = 8
        else:
            print("0 is white, 2 is black")
            first_corner = 72
    else:
        if avg_color[1] > avg_color[3]:
            print("3 is white, 1 is black")
            first_corner = 80
        else:
            print("1 is white, 3 is black")
            first_corner = 0
    return first_corner


def new_point_position(first_corner, matrix):
    # first_position = [0, 0]
    # if first_corner in [72, 80]:
    #     first_position[0] = 8
    # if first_corner in [8, 80]:
    #     first_position[1] = 8
    if first_corner == 8:
        matrix = np.rot90(matrix)
    if first_corner == 72:
        matrix = np.rot90(matrix, k=3)
    if first_corner == 80:
        matrix = np.rot90(matrix, k=2)
    # print('first_position',first_position)
    reverse_matrix = copy.deepcopy(matrix)
    for row in range(9):
        for column in range(9):
            reverse_matrix[row][column] = matrix[column][row]
    return reverse_matrix


def grouping_four_point(matrix):
    list_of_four_point_input = []
    # print('test',matrix)
    for row in range(8):
        for column in range(8):
            four_point = []
            four_point.append([matrix[row][column][0], matrix[row][column][1]])
            four_point.append([matrix[row][column + 1][0],
                               matrix[row][column + 1][1]])
            four_point.append([matrix[row + 1][column][0],
                               matrix[row + 1][column][1]])
            four_point.append([matrix[row + 1][column + 1][0],
                               matrix[row + 1][column + 1][1]])
            list_of_four_point_input.append(four_point)
            # print(row, column, matrix[row][column], "four_point", four_point)
    # print('matrix')
    return list_of_four_point_input


def finding_new_matrix(image):
    # image = cv2.imread(file)
    clear_image, matrix = dtp.getMatrixFromImage(image)

    corner = [matrix[0][0], matrix[0][8], matrix[8][0], matrix[8][8]]

    side_point = collect_side_point(copy.deepcopy(matrix))
    side_pair_point = pair_point_to_find_side(
        copy.deepcopy(clear_image), side_point)
    color_set_side = get_four_side_color(
        copy.deepcopy(clear_image), side_pair_point)
    first_corner = evaluate_board_side(color_set_side)
    print('first_corner', first_corner)
    new_matrix = new_point_position(first_corner,  copy.deepcopy(matrix))
    list_of_grouping_four_point = grouping_four_point(
        copy.deepcopy(new_matrix))
    new_image_point = df.color_points(clear_image.copy(), new_matrix.copy())
    # cv2.imshow('new_plot',new_image_point)
    # cv2.imwrite(
    #     'D:\Year4_2\module89\AI detection\Demo\picture\camera_side/plot_side.jpg', new_image_point)
    return clear_image, matrix, new_matrix, list_of_grouping_four_point


def sort_dir(dirname):
    new = list()
    for file in os.listdir(dirname):
        if file.split('.')[0].isdigit():
            new.append(file)
    return sorted(new, key=lambda f: int(f.split('.')[0]))


def load_all_images(folder):
    images = []
    filenames = sort_dir(folder)
    # print('filenames', filenames)
    for filename in filenames:
        # print(filename)
        img = cv2.imread(os.path.join(folder, filename))
        if img is not None:
            images.append(img)
    return images


def checkList(list):
    first = list[0]
    for elem in list:
        if elem != first:
            return False
            break
    return True


def convert_to_fen(list_64str):
    if checkList(list_64str) == True and list_64str[0] == '.':
        return '8/8/8/8/8/8/8/8'

    # print('convert_to_fen')
    count = 0
    e = 0
    fen = ''
    for i in range(8):
        e = 0
        for j in range(8):
            # print(count)
            if list_64str[count] != '.':

                fen += list_64str[count]
            elif list_64str[count] == '.' and count+1 >= 64:
                e += 1
                break
            else:
                e += 1
                if list_64str[count+1] != '.':
                    fen += str(e)
                    e = 0
            count += 1
        if e != 0:
            fen += str(e)
        if i != 7:
            fen += '/'
    print(fen)
    return fen


def compare_move(old_board, new_board):
    change = []
    for index, (old, new) in enumerate(zip(old_board, new_board)):
        if old != new:
            # print(index, old,new)
            change.append([index, int(old), int(new)])
    return change


def crop_and_predict(modelE4):
    # crop
    print('crop')
    top_data.list_of_image_new = []
    side_data.list_of_image_new = []
    for group in range(len(top_data.new_matrix_to_crop)):

        crop_top = crop_perspective_for_dataset(
            top_data.new_matrix_to_crop[group], top_data.clear_image.copy())
        top_data.list_of_image_new.append(crop_top)

        crop_side = crop_for_dataset_piece(
            side_data.new_matrix_to_crop[group], side_data.clear_image.copy(), 60)
        side_data.list_of_image_new.append(crop_side)

    print('predict')
    ans = []
    for img in side_data.list_of_image_new:
        ans.append(modelE4.make_prediction(img))
        pred = tf.concat(ans, axis=0)
    mappings = {0: 'b', 1: '.', 2: 'k', 3: 'n', 4: 'p', 5: 'q', 6: 'r'}
    pred = np.array(pred)
    pred = [mappings[i] for i in pred]
    print('to str', pred)
    index_not_empty = []
    for index in range(len(pred)):
        if pred[index] != '.':
            index_not_empty.append(index)
    print('index_not_empty', len(index_not_empty), index_not_empty)

    # classify_color
    print('evaluate color')
    list_of_images_to_clssify = []
    for index in index_not_empty:
        list_of_images_to_clssify.append(top_data.list_of_image_new[index])
    list_of_color_classified = color_classify.kmeans_classify(
        list_of_images_to_clssify)

    black = 1
    for index_normal in range(len(index_not_empty)):
        if list_of_color_classified[index_normal] == black:
            pred[index_not_empty[index_normal]
                 ] = pred[index_not_empty[index_normal]].upper()
    print('have color', pred, len(pred))

    fen = convert_to_fen(pred)

    return fen


def crop_and_predict_empty(modelE4_top):
    print('crop')
    top_data.list_of_image_new = []
    for group in range(len(top_data.new_matrix_to_crop)):
        crop_top = crop_perspective_for_dataset(
            top_data.new_matrix_to_crop[group], top_data.clear_image.copy())
        top_data.list_of_image_new.append(crop_top)

    print('predict')
    ans = []
    for img in top_data.list_of_image_new:

        length = 3
        h1 = length
        h2 = img.shape[1]-length
        w1 = length
        w2 = img.shape[0]-length
        cropped_image = img[h1:h2, w1:w2]

        ans.append(modelE4_top.make_prediction(cropped_image))
        pred = tf.concat(ans, axis=0)
    return pred


def save_plot_point_image():
    image_point = df.color_points(
        top_data.clear_image.copy(), top_data.matrix.copy())
    cv2.imwrite('top_data.jpg', image_point)

    image_point = df.color_points(
        side_data.clear_image.copy(), side_data.matrix.copy())
    cv2.imwrite('side_data.jpg', image_point)

    image_point = df.color_points(
        top_data.clear_image.copy(), top_data.new_matrix.copy())
    cv2.imwrite('top_data2.jpg', image_point)

    image_point = df.color_points(
        side_data.clear_image.copy(), side_data.new_matrix.copy())
    cv2.imwrite('side_data2.jpg', image_point)


def save_plot_point_image_top():
    image_point = df.color_points(
        top_data.clear_image.copy(), top_data.matrix.copy())
    cv2.imwrite('top_data.jpg', image_point)

    image_point = df.color_points(
        top_data.clear_image.copy(), top_data.new_matrix.copy())
    cv2.imwrite('top_data2.jpg', image_point)


# new_detect==1 is use detection board
def main_chess_piece(frame_side, frame_top, new_detect, model):

    check_hand_mediaPipe = cap_top.check_hand(frame_top)
    print('detect', check_hand_mediaPipe)
    if check_hand_mediaPipe == 'Hand' or check_hand_mediaPipe == None:
        return None

    try:
        if new_detect == 1:
            top_data.clear_image, top_data.matrix, top_data.new_matrix, top_data.new_matrix_to_crop = finding_new_matrix(
                frame_top)
            side_data.clear_image, side_data.matrix, side_data.new_matrix, side_data.new_matrix_to_crop = finding_new_matrix(
                frame_side)

        # save_plot_point_image()

        top_data.list_of_image_old = copy.deepcopy(top_data.list_of_image_new)
        side_data.list_of_image_old = copy.deepcopy(
            side_data.list_of_image_new)

        return crop_and_predict(model)

    except:
        print('sad')
        return None


# def main_chess_piece_old_point(frame_side, frame_top):
#     check_hand_mediaPipe = cap_top.check_hand(frame_top)
#     print('detect', check_hand_mediaPipe)
#     if check_hand_mediaPipe == 'Hand' or check_hand_mediaPipe == None:
#         return None
#     try:
#         top_data.clear_image = copy.deepcopy(frame_top)
#         side_data.clear_image = copy.deepcopy(frame_side)

#         save_plot_point_image()
#         return crop_and_predict()

#     except:
#         print('sad too')
#         return None
# def convert_color(list_of_color):
#     if tb_top.color_threshold == 'H':
#         for i in range(len(list_of_color)):
#             if list_of_color[i] == 0:
#                 list_of_color[i] = 1
#             elif list_of_color[i] == 1:
#                 list_of_color[i] = 0


# def define_first_board_color():
#     print(len(top_data.list_of_image_new))
#     not_empty_image = []
#     # black=[]
#     # white=[]
#     for image in range(16):
#         # print(image)
#         # black.append(color_classify.avg(top_data.list_of_image_new[image]))
#         not_empty_image.append(top_data.list_of_image_new[image])
#     for image in range(48, 64):
#         # print(image)
#         # white.append(color_classify.avg(top_data.list_of_image_new[image]))
#         not_empty_image.append(top_data.list_of_image_new[image])
#     tb_top.centroid, labels = color_classify.kmeans_classify_track(
#         not_empty_image)
    # print(labels)
    # if labels[0] == 0:
    #     tb_top.color_threshold = 'H'  # Low is Black
    #     for i in range(len(labels)):
    #         if labels[i] == 0:
    #             labels[i] = 1
    #         else:
    #             labels[i] = 0
    # else:
    #     tb_top.color_threshold = 'L'
    # if min(black)> max(white):
    #     top_data.color_threshold='H'
    #     top_data.thresh= (min(black)+ max(white))/2
    # elif min(white)> max(black):
    #     top_data.color_threshold='L'
    #     top_data.thresh=(min(white)+ max(black))/2
    # return tb_top.thresh


def predict_color_board(index_not_empty):  # classify_color
    print('evaluate color')
    list_of_color = [-1, -1, -1, -1, -1, -1, -1, -1,
                     -1, -1, -1, -1, -1, -1, -1, -1,
                     -1, -1, -1, -1, -1, -1, -1, -1,
                     -1, -1, -1, -1, -1, -1, -1, -1,
                     -1, -1, -1, -1, -1, -1, -1, -1,
                     -1, -1, -1, -1, -1, -1, -1, -1,
                     -1, -1, -1, -1, -1, -1, -1, -1,
                     -1, -1, -1, -1, -1, -1, -1, -1]
    list_predict = []
    list_of_image_to_classify = []
    for index in index_not_empty:
        list_of_image_to_classify.append(top_data.list_of_image_new[index])
        # color=color_classify.avg(cropped_image)
        # if color > top_data.thresh: list_of_color[index]=0
        # else:list_of_color[index]=1

    list_predict = color_classify.kmeans_classify(list_of_image_to_classify)
    print('predict_color')
    print(list_predict)
    print(index_not_empty)
    count = 0
    for index in index_not_empty:
        list_of_color[index] = list_predict[count]
        count += 1
    if tb_top.count == 0:
        if tb_top.board_list_old[0] != tb_top.board_list_new[0]: #1,0
            tb_top.color_threshold=0
            for i in range(len(list_of_color)):
                if list_of_color[i] == 0:
                    list_of_color[i] = 1
                elif list_of_color[i] == 1:
                    list_of_color[i] = 0
        tb_top.count += 1
    elif tb_top.color_threshold==0:
        for i in range(len(list_of_color)):
                if list_of_color[i] == 0:
                    list_of_color[i] = 1
                elif list_of_color[i] == 1:
                    list_of_color[i] = 0

    tb_top.board_color_new = copy.deepcopy(list_of_color)

    # print('list_of_color',list_of_color)
    # color_classify.kmeans_track()
    return list_of_color


def get_fen_pieces(board):
    """
    Read board and return piece locations in fen format.
    """
    ret = None
    cnt = 0  # counter for successive empty cell along the row
    save = []  # temp container

    board = board[::-1]  # reverse first

    for i, v in enumerate(board):
        if v == '.':
            cnt += 1

            # sum up the successive empty cell and update save
            if cnt > 1:
                save[len(save)-1] = str(cnt)
            else:
                save.append(str(cnt))  # add
        else:
            save.append(v)  # add
            cnt = 0  # reset, there is no successive number

        if (i+1) % 8 == 0:  # end of row
            save.append('/')
            cnt = 0

    ret = ''.join(save)  # convert list to stringcolor_choose
    # print(ret)

    return ret


# def fen_to_list(fen):
#     fen_before
# def update_move():


# new_detect==1 is use detection board #color 1 is detect black
def use_trackback(frame_top, new_detect, fen_before, color_choose, model):

    print('start', tb_top.old_pred_empty)
    tb_top.board_list_old = list(
        str(chess.Board(fen_before)).replace(' ', '').replace('\n', ''))
    print('old board')

    for c in range(64):
        if tb_top.board_list_old[c] == '.':
            tb_top.board_color_old[c] = -1
            tb_top.old_pred_empty[c] = 0
        else:
            tb_top.old_pred_empty[c] = 1
            if tb_top.board_list_old[c].islower():
                tb_top.board_color_old[c] = 1
            if tb_top.board_list_old[c].isupper():
                tb_top.board_color_old[c] = 0
    print(np.reshape(tb_top.board_list_old, (8, 8)))
    print(np.reshape(tb_top.board_color_old, (8, 8)))
    print(np.reshape(tb_top.old_pred_empty, (8, 8)))
    check_hand_mediaPipe = cap_top.check_hand(frame_top)
    print('detect', check_hand_mediaPipe)
    if check_hand_mediaPipe == 'Hand' or check_hand_mediaPipe == None:
        return None

    if new_detect == 1:
        top_data.clear_image, top_data.matrix, top_data.new_matrix, top_data.new_matrix_to_crop = finding_new_matrix(
            frame_top)

    top_data.clear_image = copy.deepcopy(frame_top)

    tb_top.new_pred_empty = crop_and_predict_empty(model)
    # save_plot_point_image_top()

    print('empty')
    print(np.reshape(tb_top.new_pred_empty, (8, 8)))
    tb_top.fen_before = fen_before
    # print(np.reshape(tb_top.board_list_old,(8,8)))

    # if 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR' in fen_before and tb_top.count == 0:
    #     print('first time')
    #     # Find first Threshold
    #     define_first_board_color()
    #     tb_top.count += 1

    #     return 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR'
    top_data.index_not_empty = []
    for index in range(len(tb_top.new_pred_empty)):
        if tb_top.new_pred_empty[index] != 0:
            top_data.index_not_empty.append(index)
    # print(top_data.index_not_empty)

    predict_color_board(top_data.index_not_empty)

    print('predict_color_board\n', np.reshape(tb_top.board_color_new, (8, 8)))
    print('old_color_board\n', np.reshape(tb_top.board_color_old, (8, 8)))

    # print('old\n',np.reshape(tb_top.board_color_old,(8,8)))
    color_change = compare_move(tb_top.board_color_old, tb_top.board_color_new)
    move = compare_move(tb_top.old_pred_empty, tb_top.new_pred_empty)

    tb_top.board_list_new = copy.deepcopy(tb_top.board_list_old)
    print('compare')
    print('piece', move)
    print('color', color_change)
    if len(move) <= 3:
        for changes in color_change:
            if changes[2] == color_choose:
                print('new_pos')
                new_position = changes[0]
        for changes in move:
            if changes[1] == 1 and changes[2] == 0:
                piece_to_move = changes[0]
        print(new_position, piece_to_move)

        tb_top.board_list_new[new_position] = copy.deepcopy(
            tb_top.board_list_old[piece_to_move])
        tb_top.board_list_new[piece_to_move] = '.'

    elif len(move) >= 4:  # castling
        if color_change[0] == [60, 0, -1] and color_change[3] == [63, 0, -1]:
            tb_top.board_list_new[60] = '.'
            tb_top.board_list_new[61] = 'R'
            tb_top.board_list_new[62] = 'K'
            tb_top.board_list_new[63] = '.'

        elif color_change[0] == [56, 0, -1] and color_change[3] == [60, 0, -1]:
            tb_top.board_list_new[56] = '.'
            tb_top.board_list_new[58] = 'K'
            tb_top.board_list_new[59] = 'R'
            tb_top.board_list_new[60] = '.'

        elif color_change[0] == [4, 1, -1] and color_change[3] == [7, 1, -1]:
            tb_top.board_list_new[4] = '.'
            tb_top.board_list_new[5] = 'r'
            tb_top.board_list_new[6] = 'k'
            tb_top.board_list_new[7] = '.'

        elif color_change[0] == [0, 1, -1] and color_change[3] == [4, 1, -1]:
            tb_top.board_list_new[0] = '.'
            tb_top.board_list_new[1] = 'k'
            tb_top.board_list_new[2] = 'r'
            tb_top.board_list_new[4] = '.'
        else:
            return None
    else:
        return None
    print('Answer')
    print(np.reshape(tb_top.board_list_new, (8, 8)))

    tb_top.old_pred_empty = list(copy.deepcopy(tb_top.new_pred_empty))
    tb_top.board_list_old = copy.deepcopy(tb_top.board_list_new)
    tb_top.board_color_old = copy.deepcopy(tb_top.board_color_new)
    print(convert_to_fen(tb_top.board_list_new))
    return convert_to_fen(tb_top.board_list_new)

    # find_color=None
    # index_collect=None
    # index_to_change=None
    # print(move)
    # if len(move)<=3:
    #     for m in move:
    #         print(m)
    #         if m[2] == 0:
    #             print('index_to_change')
    #             index_to_change=m[0]

    #         if tb_top.board_color_new[m[0]] == color_choose:
    #             index_collect=m[0]
    # print('find_color',find_color,color_choose)
    # print('why',index_to_change,index_collect,color_choose)
    # print(tb_top.board_list_new[index_to_change])
    # print(tb_top.board_list_new[index_collect])
    # print(tb_top.board_list_old[index_to_change])
    # tb_top.board_list_new[index_collect]=tb_top.board_list_old[index_to_change]
    # tb_top.board_list_new[index_to_change]=tb_top.board_list_old[index_collect]

    # # print(tb_top.board_list_square_new)

    # # update_move()
    # # tb_top.board_list_new

    # for index in range(len(tb_top.new_pred)):
    #     if tb_top.new_pred[index] != '.':
    #         top_data.index_not_empty.append(index)

    # print(top_data.index_not_empty)

    # # print(define_color())

    # print('new')
    # print(tb_top.new_pred)
    # print('old')
    # print(tb_top.old_pred)
    # # tb_top.new_pred=[1, 1, 1, 1, 1, 1, 1, 1,
    # #                  1, 1, 1, 1, 1, 1, 1, 1,
    # #                  0, 0, 0, 0, 0, 0, 0, 0,
    # #                  0, 0, 0, 0, 0, 0, 0, 0,
    # #                  0, 0, 0, 0, 0, 1, 0, 0,
    # #                  0, 0, 0, 0, 0, 0, 0, 0,
    # #                  1, 1, 1, 1, 1, 1, 1, 1,
    # #                  1, 1, 1, 1, 1, 1, 1, 1]

    # # tb_top.old_pred =[1, 1, 0, 0, 1, 1, 1, 1,
    #                 #   1, 1, 1, 0, 1, 0, 0, 1,
    #                 #   0, 0, 1, 1, 1, 0, 1, 0,
    #                 #   0, 0, 0, 0, 0, 0, 0, 0,
    #                 #   0, 0, 0, 0, 1, 0, 0, 1,
    #                 #   0, 0, 0, 1, 0, 0, 1, 0,  compare_move
    #                 #   1, 1, 1, 0, 1, 1, 0, 0,
    #                 #   1, 1, 1, 1, 0, 1, 1, 1]

    # if tb_top.old_pred ==[]:
    #     print('No old data')
    #     return None
    # change = compare_move(tb_top.new_pred, tb_top.old_pred)
    # print(change)
    # update_board(change)
    # return tb_top.new_pred


# if __name__ == "__main__":
#     # file ='D:\Year4_2\FRAwebpro\module8-9\Detection/test_picture/top_for_p1.jpg'
#     file='D:\Year4_2\FRAwebpro\module8-9\Detection/test_picture\p1.jpg'
#     frame_top=cv2.imread(file)
#     fen_before='rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
#     use_trackback(frame_top,1,fen_before,0)

#     print('turn2')
#     file2='D:\Year4_2\FRAwebpro\module8-9\Detection/test_picture\p4.jpg'
#     frame_top2=cv2.imread(file2)
#     fen_before='rnbqkbnr/pp1ppppp/8/8/2p5/8/PPPPPPPP/RNBQKBNR b KQkq - 0 1'
#     use_trackback(frame_top2,0,fen_before,1)

    # print('turn2')
    # file2='D:\Year4_2\FRAwebpro\module8-9\Detection/test_picture\p2.jpg'
    # frame_top2=cv2.imread(file2)
    # # fen_before='rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
    # use_trackback(frame_top2,0,fen_before,0)

    # print('turn3')
    # file3='D:\Year4_2\FRAwebpro\module8-9\Detection/test_picture\p3.jpg'
    # frame_top3=cv2.imread(file3)
    # # fen_before='rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
    # use_trackback(frame_top3,0,fen_before,1)
