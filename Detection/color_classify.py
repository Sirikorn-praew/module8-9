import cv2
import numpy as np
import math
import statistics

import matplotlib.pyplot as plt
import colorsys
import sys


import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


def kmeans_test(x):

    kmeans = KMeans(n_clusters=2)
    a = kmeans.fit(np.reshape(x, (len(x), 1)))
    centroids = kmeans.cluster_centers_

    labels = kmeans.labels_

    # print(centroids)
    # print(labels)
    return labels
# kmeans_test(x)


def clustering_2group(points):
    clusters = []
    eps = 0.2
    points_sorted = sorted(points)
    curr_point = points_sorted[0]
    curr_cluster = [curr_point]
    for point in points_sorted[1:]:
        if point <= curr_point + eps:
            curr_cluster.append(point)
        else:
            clusters.append(curr_cluster)
            curr_cluster = [point]
        curr_point = point
    clusters.append(curr_cluster)
    if min(clusters[0]) > max(clusters[1]):
        thresh = (min(clusters[0]) + max(clusters[1]))/2
    else:
        thresh = (min(clusters[1]) + max(clusters[0]))/2
    # print('threshold', thresh, clusters)
    return thresh


def avg(img):
    # print('go')
    # img = cv2.imread(
    #     'D:\Year4_2\module89\AI detection\Detect_chessBoard\chessApp\chess_piece/top_view_70.jpg')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # cv2.imshow('img', img)
    hue = img[:, :, 0]
    # print(hue)
    avg_hue = np.mean(hue)
    # print('H average=', avg_hue)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    return avg_hue


def kmeans_classify(list_of_image):
    # all_image, filename_all = load_all_images(file)
    list_of_avg_hue = []
    for image in range(len(list_of_image)):
        # draw_image = list_of_image[image].copy()
        resized = cv2.resize(list_of_image[image], (85, 85),
                             interpolation=cv2.INTER_AREA)
        length = 20
        h1 = length
        h2 = resized.shape[1]-length
        w1 = length
        w2 = resized.shape[0]-length
        contrast = cv2.convertScaleAbs(resized, alpha=1, beta=0)
        cropped_image = contrast[h1:h2, w1:w2]
        # print(image)
        list_of_avg_hue.append(int(avg(cropped_image)))
    # print('kmean')
    return kmeans_test(list_of_avg_hue)


def find_threshold_color_chess_piece(list_of_image):
    # all_image, filename_all = load_all_images(file)
    list_of_avg_hue = []
    for image in range(len(list_of_image)):
        # draw_image = list_of_image[image].copy()
        resized = cv2.resize(list_of_image[image], (85, 85),
                             interpolation=cv2.INTER_AREA)
        length = 20
        h1 = length
        h2 = resized.shape[1]-length
        w1 = length
        w2 = resized.shape[0]-length
        contrast = cv2.convertScaleAbs(resized, alpha=1, beta=0)
        cropped_image = contrast[h1:h2, w1:w2]
        # print(image)
        list_of_avg_hue.append(int(avg(cropped_image)))
    print('kmean')
    kmeans_test(list_of_avg_hue)
    # print('list_of_avg_hue', clustering_2group(
    #     sorted(list_of_avg_hue)), list_of_avg_hue)
    # for i in list_of_avg_hue:
    #     print(i)
    return clustering_2group(sorted(list_of_avg_hue)), list_of_avg_hue


def clssify_color_by_threshold(threshold, list_of_avg_hue):
    list_of_color = []
    for hue in range(len(list_of_avg_hue)):
        color = 0
        if list_of_avg_hue[hue] < threshold:
            color = 1
        list_of_color.append(color)

    return list_of_color
