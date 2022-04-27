# # import cv2


# # # capture from camera at location 0
# # cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# # # set the width and height, and UNSUCCESSFULLY set the exposure time
# # # cap.set(3, 1280)
# # # cap.set(4, 1024)

# # while True:
# #     ret, img = cap.read()
# #     cv2.imshow("input", img)
# #     #cv2.imshow("thresholded", imgray*thresh2)

# #     key = cv2.waitKey(10)
# #     if key == 27:
# #         break


# # cv2.destroyAllWindows()
# # cv2.VideoCapture(2).release()

# points = [0.1, 0.31,  0.32, 0.45, 0.35, 0.40, 0.5]


# def clustering_2group(points):
#     clusters = []
#     eps = 0.2
#     points_sorted = sorted(points)
#     curr_point = points_sorted[0]
#     curr_cluster = [curr_point]
#     for point in points_sorted[1:]:
#         if point <= curr_point + eps:
#             curr_cluster.append(point)
#         else:
#             clusters.append(curr_cluster)
#             curr_cluster = [point]
#         curr_point = point
#     clusters.append(curr_cluster)
#     if min(clusters[0]) > max(clusters[1]):
#         thresh = (min(clusters[0]) + max(clusters[1]))/2
#     else:
#         thresh = (min(clusters[1]) + max(clusters[0]))/2
#     print('threshold', thresh, clusters)
#     return thresh

def convert_to_fen(list_64str):
    print('convert_to_fen')
    count = 0
    e = 0
    fen = ''
    for i in range(8):
        e = 0
        for j in range(8):
            print(count)
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


# clustering_2group(points)
list_fen = ['R', 'b', 'e', 'e', 'e', 'e', 'q', 'R', 'e', 'e', 'n', 'k', 'e', 'e', 'q', 'n', 'p', 'p', 'e', 'e', 'e', 'e', 'p', 'n', 'e', 'e', 'q', 'p', 'e', 'e', 'e',
            'e', 'e', 'e', 'e', 'e', 'e', 'P', 'e', 'e', 'P', 'e', 'e', 'e', 'e', 'e', 'e', 'P', 'e', 'e', 'P', 'e', 'P', 'e', 'e', 'P', 'e', 'R', 'e', 'Q', 'e', 'e', 'e', 'e']
convert_to_fen(list_fen)
