from Detection import DetectAllPoints as dtp
from Detection import DetectionFunctions as df
from Detection import color_classify
from Detection import variable
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

mp_hands = mp.solutions.hands


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


cap_top = MediaPipe_check_Hand()
# cap_side = MediaPipe_check_Hand(1)


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


modelE4 = EfficientNetModel(
    '.\Detection\checkpoint_hyper', (380, 380))
get_m = variable.get_matrix_variable
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


def convert_to_fen(list_64str):
    # print('convert_to_fen')
    count = 0
    e = 0
    fen = ''
    for i in range(8):
        e = 0
        for j in range(8):
            # print(count)
            if list_64str[count] != 'e':

                fen += list_64str[count]
            elif list_64str[count] == 'e' and count+1 >= 64:
                e += 1
                break
            else:
                e += 1
                if list_64str[count+1] != 'e':
                    fen += str(e)
                    e = 0
            count += 1
        if e != 0:
            fen += str(e)
        if i != 7:
            fen += '/'
    print(fen)
    return fen


def main_chess_piece(frame_side, frame_top):
    # cv2.imshow('top', frame_top)
    # cv2.imshow('side', frame_side)
    top_data = get_m()
    side_data = get_m()
    print('MediaPipe')
    print('test1', cap_top.check_hand(frame_top))
    # print('test2', cap_side.check_hand(frame_side))
    if cap_top.check_hand(frame_top) == 'Hand' or cap_top.check_hand(frame_top) == None:
        return None
    try:
        top_data.clear_image, top_data.matrix, top_data.new_matrix, top_data.new_matrix_to_crop = finding_new_matrix(
            frame_top)
        side_data.clear_image, side_data.matrix, side_data.new_matrix, side_data.new_matrix_to_crop = finding_new_matrix(
            frame_side)

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

        # group and crop
        print('crop')
        list_image_crop_top = []
        list_image_crop_side = []
        for group in range(len(top_data.new_matrix_to_crop)):
            crop_top = crop_perspective_for_dataset(
                top_data.new_matrix_to_crop[group], top_data.clear_image.copy())
            list_image_crop_top.append(crop_top)
            # cv2.imwrite(
            #     "D:\Bachelor\Y4/bhir_vision\Demo/top_crop" +
            #     str(group) + ".jpg",
            #     crop_top)
            crop_side = crop_for_dataset_piece(
                side_data.new_matrix_to_crop[group], side_data.clear_image.copy(), 60)
            # cv2.imwrite(
            #     "D:\Bachelor\Y4/bhir_vision\Demo\side_crop/" +
            #     str(group) + ".jpg",
            #     crop_side)
            list_image_crop_side.append(crop_side)
        print('predict')
        # file_crop_side='D:\Year4_2\module89\AI detection\Demo\side_crop/'
        ans = []
        for img in list_image_crop_side:
            ans.append(modelE4.make_prediction(img))
            pred = tf.concat(ans, axis=0)
        print('predict', pred)
        mappings = {0: 'b', 1: 'e', 2: 'k', 3: 'n', 4: 'p', 5: 'q', 6: 'r'}
        pred = np.array(pred)
        pred = [mappings[i] for i in pred]
        print('to str', pred)
        index_not_empty = []
        for index in range(len(pred)):
            if pred[index] != 'e':
                index_not_empty.append(index)
        print('index_not_empty', len(index_not_empty), index_not_empty)

        # classify_color
        print('evaluate color')
        list_of_images_to_clssify = []
        for index in index_not_empty:
            # print(index)
            list_of_images_to_clssify.append(list_image_crop_top[index])
        list_of_color_classified = color_classify.kmeans_classify(
            list_of_images_to_clssify)
        # # print('list_of_images_to_clssify', len(list_of_images_to_clssify))
        # thresh_top, list_of_avg_hue = color_classify.find_threshold_color_chess_piece(
        #     list_of_images_to_clssify)
        # # print('thresh', thresh_top, 'list_of_avg_hue', list_of_avg_hue)
        # list_of_color_classified = color_classify.clssify_color_by_threshold(
        #     thresh_top, list_of_avg_hue)
        # # print(list_of_color_classified)
        black = 1

        for index_normal in range(len(index_not_empty)):
            if list_of_color_classified[index_normal] == black:
                print(pred[index_not_empty[index_normal]],
                      type(pred[index_not_empty[index_normal]]))
                pred[index_not_empty[index_normal]
                     ] = pred[index_not_empty[index_normal]].upper()
        print('have color', pred, len(pred))
        fen = convert_to_fen(pred)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        return fen
    except:
        print('sad')
        return None


# if __name__ == "__main__":
#     print(main_chess_piece())
