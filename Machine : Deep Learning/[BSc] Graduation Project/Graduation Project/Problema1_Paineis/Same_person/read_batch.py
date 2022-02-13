
import numpy as np
from imgaug import augmenters as iaa
import cv2


def read_batch(paths, rand_idx, imd, data_augment, input_pattern, type_normalization):
    cls = np.zeros(len(rand_idx), dtype=np.int32)
    seq = iaa.SomeOf((0, None), [iaa.GaussianBlur(sigma=(0.0, 3.0)), iaa.ContrastNormalization((0.75, 1.5)),
                                 iaa.Multiply((0.7, 1.3), per_channel=0.2), iaa.Fliplr(1)], random_order=True)
    depths = [x[1] for x in input_pattern[1:]]
    imgs = np.zeros((len(rand_idx), input_pattern[0][0], input_pattern[0][1], sum(depths)), dtype=np.float32)
    for i, idx in enumerate(rand_idx):
        cur_depth = 0
        for j in range(1, len(input_pattern)):
            if input_pattern[j][0] == 0:
                imgs[i, :, :, cur_depth:cur_depth+input_pattern[j][1]] = np.load(paths[idx][j-1])
            else:
                imgs[i, :, :, cur_depth:cur_depth+input_pattern[j][1]] = cv2.imread(paths[idx][j-1], cv2.IMREAD_COLOR)
            cur_depth += input_pattern[j][1]
        cls[i] = paths[idx][-1]
    if data_augment:
        imgs = seq.augment_images(imgs)

    flags = imd[:, :, :, -1]
    if type_normalization == 1:
        mean_values = imd[:, :, :, 0]
        for i, _ in enumerate(rand_idx):
            tmp = imgs[i, :, :, :]
            tmp[flags > 0] = np.divide(tmp[flags > 0], mean_values[flags > 0])
            tmp[flags == 0] = 0
            imgs[i, :, :, :] = tmp

    if type_normalization == 2:
        mean_values = imd[:, :, :, 0]
        std_values = imd[:, :, :, 1]
        for i, _ in enumerate(rand_idx):
            tmp = imgs[i, :, :, :] - mean_values
            tmp[flags > 0] = np.divide(tmp[flags > 0], std_values[flags > 0])
            imgs[i, :, :, :] = tmp

    if type_normalization == 3:
        min_values = imd[:, :, :, 0]
        max_values = imd[:, :, :, 1]
        for i, _ in enumerate(rand_idx):
            tmp = 2 * (imgs[i, :, :, :] - min_values)
            tmp[flags > 0] = tmp[flags > 0] / (max_values[flags > 0]-min_values[flags > 0]) - 1
            imgs[i, :, :, :] = tmp
    return imgs, cls


def get_input_pattern(line):
    # returns array with: HEIGHT, WIDTH; TYPE_0, DEPTH_0, ...
    pattern = []
    for i in range(len(line)-1):
        if '.npy' in line[i]:
            inp = np.load(line[i])
            if i == 0:
                pattern.append([inp.shape[0], inp.shape[1]])
            pattern.append([0, inp.shape[2]])
        else:
            inp = cv2.imread(line[0], cv2.IMREAD_COLOR)
            if i == 0:
                pattern.append([np.size(inp, 0), np.size(inp, 1)])
            pattern.append([1, np.size(inp, 2)])
    return pattern


