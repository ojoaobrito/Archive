import numpy as np
import cv2


def get_imdb_1(paths, input_pattern):
    # performs x_n = x/mu normalization
    depths = [x[1] for x in input_pattern[1:]]
    imdb = np.zeros((input_pattern[0][0], input_pattern[0][1], sum(depths),2), dtype=np.float32)
    img = np.zeros((input_pattern[0][0], input_pattern[0][1], sum(depths)), dtype=np.float32)
    for i, pt in enumerate(paths):
        print('IMDB /mean {}/{}'.format(i, len(paths)))
        cur_depth = 0
        for j in range(1, len(input_pattern)):
            if input_pattern[j][0] == 0:
                img[:, :, cur_depth:cur_depth + input_pattern[j][1]] = np.load(pt[j-1])
            else:
                img[:, :, cur_depth:cur_depth + input_pattern[j][1]] = cv2.imread(pt[j-1], cv2.IMREAD_COLOR)
            cur_depth += input_pattern[j][1]
        imdb[:, :, :, 0] = imdb[:, :, :, 0] + img
    imdb[:, :, :, 0] = imdb[:, :, :, 0] / len(paths)
    imdb[:, :, :, 1] = imdb[:, :, :, 0] > 1e-6
    return imdb


def get_imdb_2(paths, input_pattern):
    # performs x_n = (x- mu)/std normalization
    depths = [x[1] for x in input_pattern[1:]]
    imdb = np.zeros((input_pattern[0][0], input_pattern[0][1], sum(depths), 3), dtype=np.float32)
    img = np.zeros((input_pattern[0][0], input_pattern[0][1], sum(depths)), dtype=np.float32)

    for i, pt in enumerate(paths):
        print('IMDB_-mean/std 1/2: {}/{}'.format(i, len(paths)))
        cur_depth = 0
        for j in range(1, len(input_pattern)):
            if input_pattern[j][0] == 0:
                img[:, :, cur_depth:cur_depth + input_pattern[j][1]] = np.load(pt[j-1])
            else:
                img[:, :, cur_depth:cur_depth + input_pattern[j][1]] = cv2.imread(pt[j-1], cv2.IMREAD_COLOR)
            cur_depth += input_pattern[j][1]
        imdb[:, :, :, 0] = imdb[:, :, :, 0]+img
    imdb[:, :, :, 0] = imdb[:, :, :, 0]/len(paths)
    for i, pt in enumerate(paths):
        print('IMDB_-mean/std 2/2: {}/{}'.format(i, len(paths)))
        cur_depth = 0
        for j in range(1, len(input_pattern)):
            if input_pattern[j][0] == 0:
                img[:, :, cur_depth:cur_depth + input_pattern[j][1]] = np.load(pt[j-1])
            else:
                img[:, :, cur_depth:cur_depth + input_pattern[j][1]] = cv2.imread(pt[j-1], cv2.IMREAD_COLOR)
            cur_depth += input_pattern[j][1]
        imdb[:, :, :, 1] = imdb[:, :, :, 1]+(img - imdb[:, :, :, 0])**2
    imdb[:, :, :, 1] = np.sqrt(imdb[:, :, :, 1] / (len(paths)-1))
    imdb[:, :, :, 2] = np.abs(imdb[:, :, :, 1]) > 1e-6
    return imdb


def get_imdb_3(paths, input_pattern):
    # performs x_n = (x- mu)/std normalization
    depths = [x[1] for x in input_pattern[1:]]
    imdb = np.zeros((input_pattern[0][0], input_pattern[0][1], sum(depths), 3), dtype=np.float32)
    imdb[:, :, :, 0] = 257.0
    imdb[:, :, :, 1] = -1.0
    img = np.zeros((input_pattern[0][0], input_pattern[0][1], sum(depths)), dtype=np.float32)
    for i, pt in enumerate(paths):
        print('IMDB min-max: {}/{}'.format(i, len(paths)))
        cur_depth = 0
        for j in range(1, len(input_pattern)):
            if input_pattern[j][0] == 0:
                img[:, :, cur_depth:cur_depth + input_pattern[j][1]] = np.load(pt[j-1])
            else:
                img[:, :, cur_depth:cur_depth + input_pattern[j][1]] = cv2.imread(pt[j-1], cv2.IMREAD_COLOR)
            cur_depth += input_pattern[j][1]

        imdb[:, :, :, 0] = np.minimum(imdb[:, :, :, 0], img)
        imdb[:, :, :, 1] = np.maximum(imdb[:, :, :, 1], img)
        imdb[:, :, :, 2] = (imdb[:, :, :, 1] - imdb[:, :, :, 0]) > 1e-6
    return imdb

