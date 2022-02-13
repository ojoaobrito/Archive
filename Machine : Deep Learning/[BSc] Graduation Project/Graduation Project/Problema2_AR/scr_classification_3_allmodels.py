########################################################################################################################
# CONVOLUTIONAL NEURAL NETWORKS
########################################################################################################################

import sys
import os
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
import cv2
from random import shuffle, sample
import pickle
import sklearn.metrics as mt
import math
import datetime
import natsort
from read_csv_data_file import read_csv_data_file
from read_batch import read_batch, get_input_pattern
from get_imdbs import *
import models_hugomcp as md
from PIL import Image

import tensorflow.contrib.slim as slim
from tensorflow.contrib.slim.nets import inception

from models.research.slim.nets.inception_resnet_v2 import inception_resnet_v2, inception_resnet_v2_arg_scope

# ##########################
# Configs

TYPE_NORMALIZATION = 3

STOP_CRITERIUM = [65] #[10, 0.05]  #1 value: TOT_epochs; 2 values: last N iterations minimum percentual improvement

LEARNING_BATCH_SIZE = 100
VALIDATION_BATCH_SIZE = 100
PROPORTION_VALIDATION = 0.15

learning_rate = 1e-3
lr_decay = 0.9
decay_epochs = 10

SHOW_WORST_CASES = 200


BALANCED_DATASET = 0
if len(sys.argv) > 1:
    BALANCED_DATASET = int(sys.argv[1])

DATA_AUGMENTATION = 1
if len(sys.argv) > 2:
    DATA_AUGMENTATION = int(sys.argv[2])

DROPOUT_PROB = 1
if len(sys.argv) > 3:
    DROPOUT_PROB = float(sys.argv[3])

TRAIT = 'Gender'
if len(sys.argv) > 4:
    TRAIT = sys.argv[4]

TYPE_DISJOINT = 2
if len(sys.argv) > 5:
    TYPE_DISJOINT = int(sys.argv[5])

ITERATION_DATASET = 1
if len(sys.argv) > 6:
    ITERATION_DATASET = int(sys.argv[6])

EXPERIMENT = '%s_Disjoint_%d_Iteration_%d' % (TRAIT, TYPE_DISJOINT, ITERATION_DATASET)

DATASET = os.path.join('data.csv')
INPUT_FOLDER = os.path.join('BIODI', 'Data_constant_proportion')

DEBUG_FOLDER = os.path.join('BIODI', TRAIT, 'Debug')
if not os.path.isdir(DEBUG_FOLDER):
    os.makedirs(DEBUG_FOLDER)
DEBUG_FOLDER = os.path.join('BIODI', TRAIT, 'Debug', EXPERIMENT)
if not os.path.isdir(DEBUG_FOLDER):
    os.makedirs(DEBUG_FOLDER)

now = datetime.datetime.now()
DATE_TIME_FOLDER = now.strftime("%Y_%m_%d_%H_%M_%S")
os.makedirs(os.path.join(DEBUG_FOLDER, DATE_TIME_FOLDER))

IMDB_FILE = os.path.join('BIODI', TRAIT, EXPERIMENT + '.dat')

learning_samples, validation_samples, test_samples, classes = read_csv_data_file(DATASET, INPUT_FOLDER)
TOT_CLASSES = len(classes)

INPUT_PATTERN = get_input_pattern(learning_samples[0])

HEIGHT_IMGS = INPUT_PATTERN[0][0]
WIDTH_IMGS = INPUT_PATTERN[0][1]
depths = [x[1] for x in INPUT_PATTERN[1:]]
DEPTH_IMGS = sum(depths)

############################
# AUXILIARY FUNCTIONS


def get_worst_cases(batch, responses, ground):
    w = []
    for i, r in enumerate(responses):
        md = r[np.argmax(r)]
        tr = r[ground[i]]
        err = np.max([md-tr, 0])
        w.append([batch + i, ground[i], np.argmax(r), err])
    return w


########################################################################################################################
# TensorFlow
########################################################################################################################

###############################
# Create Placeholders

x_input_shape = (None, HEIGHT_IMGS, WIDTH_IMGS, DEPTH_IMGS)
x_inputs = tf.placeholder(tf.float32, shape=x_input_shape)
y_targets = tf.placeholder(tf.int32, shape=None)
y_model = tf.placeholder(tf.float32, shape=(None, TOT_CLASSES))
dropout_prob = tf.placeholder(tf.float32)
generation_num = tf.Variable(0, trainable=False)


def loss_gtsrb(logits, targets):
    targets = tf.squeeze(tf.cast(targets, tf.int32))
    cross_entropy = tf.nn.sparse_softmax_cross_entropy_with_logits(logits=logits, labels=targets, name='xentropy')
    cross_entropy_mean = tf.reduce_mean(cross_entropy)
    return cross_entropy_mean


def train_step(loss_value, gn):

    #gn = tf.Print(gn, ["GN: ", gn])

    model_learning_rate = tf.train.exponential_decay(learning_rate, gn, decay_epochs, lr_decay, staircase=True)
    #model_learning_rate = tf.Print(model_learning_rate, ["LR: ", model_learning_rate])

    # Create optimizer
    my_optimizer = tf.train.GradientDescentOptimizer(model_learning_rate)
    # Initialize train step
    train_step = my_optimizer.minimize(loss_value)

    return train_step


def accuracy_of_batch(logits, targets):
    targets = tf.squeeze(tf.cast(targets, tf.int32))

    #logits = tf.Print(logits, ["LOGITS: ", logits, tf.shape(logits)], summarize=50)

    batch_predictions = tf.cast(tf.argmax(logits, 1), tf.int32)

    #targets = tf.Print(targets, ["TRUE: ", targets, tf.shape(targets)], summarize=50)
    #batch_predictions = tf.Print(batch_predictions, ["PRED: ", batch_predictions, tf.shape(batch_predictions)], summarize=50)
    predicted_correctly = tf.equal(batch_predictions, targets)
    accuracy = tf.reduce_mean(tf.cast(predicted_correctly, tf.float32))
    return accuracy


with tf.variable_scope('model_definition') as scope:
    #model_outputs = md.vgg(x_inputs, dropout_prob, TOT_CLASSES)
    model_outputs, _ = inception.inception_v2(x_inputs, TOT_CLASSES)
    #model_outputs, _ = inception_resnet_v2(x_inputs, TOT_CLASSES)

    scope.reuse_variables()

loss = loss_gtsrb(model_outputs, y_targets)

train_op = train_step(loss, generation_num)
predictions_batch = tf.cast(tf.argmax(model_outputs, 1), tf.int32)
accuracy = accuracy_of_batch(y_model, y_targets)

sess = tf.Session()
plt.ion()
saver = tf.train.Saver()

########################################################################################################################
# LEARNING MAIN ()
########################################################################################################################


init = tf.global_variables_initializer()
sess.run(init)

shuffle(learning_samples)
shuffle(validation_samples)
shuffle(test_samples)


if BALANCED_DATASET:
    classes_learning_set = [int(x[1]) for x in learning_samples]
    tot_samples_per_class = []
    for i in classes:
        tot_samples_per_class.append(classes_learning_set.count(int(i)))
    max_samples = max(tot_samples_per_class)
    for i, c in enumerate(classes):
        draw = np.random.randint(0, tot_samples_per_class[i], max_samples - tot_samples_per_class[i])
        e = [idx for idx, value in enumerate(classes_learning_set) if value == int(c)]
        for idx in draw:
            learning_samples.append(learning_samples[e[idx]])
    shuffle(learning_samples)


if not os.path.isfile(IMDB_FILE):
    if  TYPE_NORMALIZATION == 1:
        imdb=get_imdb_1(learning_samples, INPUT_PATTERN)
    if TYPE_NORMALIZATION == 2:
        imdb = get_imdb_2(learning_samples, INPUT_PATTERN)
    if  TYPE_NORMALIZATION == 3:
        imdb=get_imdb_3(learning_samples, INPUT_PATTERN)
    with open(IMDB_FILE, 'wb') as f:
        pickle.dump(imdb, f)
else:
    with open(IMDB_FILE, 'rb') as f:
        imdb = pickle.load(f)

train_loss = []
train_accuracy = []
validation_accuracy = []


# del learning_samples[100:]
# del validation_samples[100:]
# del test_samples[100:]

ep = 0
while True:
    i = 0
    sess.run(generation_num.assign(ep))
    epoch_loss = 0
    epoch_acc = 0
    while i < len(learning_samples):

        rand_idx = sample(range(len(learning_samples)), LEARNING_BATCH_SIZE)
        #rand_idx = range(i, np.min([i+LEARNING_BATCH_SIZE, len(learning_samples)]))

        rand_imgs, rand_y = read_batch(learning_samples, rand_idx, imdb, DATA_AUGMENTATION, INPUT_PATTERN, TYPE_NORMALIZATION)

        # #Test data augmentation
        # for ij, j in enumerate(rand_idx):
        #     img_original = cv2.imread(learning_samples[j][0], cv2.IMREAD_COLOR)
        #     name_img = "%s" % (learning_samples[j][0][learning_samples[j][0].rfind(os.sep)+1:])
        #     img_augmented = np.uint8(np.multiply(rand_imgs[ij, :, :, :], imdb[:, :, :, 1])+imdb[:, :, :, 0])
        #     both_imgs = np.concatenate((img_original, img_augmented), axis=1)
        #     cv2.imwrite(os.path.join(DEBUG_FOLDER, DATE_TIME_FOLDER, name_img), both_imgs)

        sess.run(train_op, feed_dict={x_inputs: rand_imgs, y_targets: rand_y, dropout_prob: DROPOUT_PROB})
        [t_loss, y_out] = sess.run([loss, model_outputs], feed_dict={x_inputs: rand_imgs, y_targets: rand_y, dropout_prob: DROPOUT_PROB})

        t_acc = sess.run(accuracy, feed_dict={y_model: y_out, y_targets: rand_y})

        print('Learning\tEpoch\t{}\tBatch {}/{}\tLoss={:.5f}\tAcc={:.2f}'.format(ep+1,
             (i + 1)//LEARNING_BATCH_SIZE+1, math.ceil(len(learning_samples) / LEARNING_BATCH_SIZE),
                                                                                     t_loss, t_acc*100))
        i += LEARNING_BATCH_SIZE
        epoch_loss += t_loss*len(rand_idx)
        epoch_acc += t_acc * len(rand_idx)

    epoch_loss /= len(learning_samples)
    epoch_acc /= len(learning_samples)
    train_loss.append(epoch_loss)
    train_accuracy.append(epoch_acc)

    i = 0
    epoch_acc = 0
    while i < len(validation_samples):
        rand_idx = range(i, np.min([i + VALIDATION_BATCH_SIZE, len(validation_samples)]))
        rand_imgs, rand_y = read_batch(validation_samples, rand_idx, imdb, DATA_AUGMENTATION, INPUT_PATTERN, TYPE_NORMALIZATION)

        temp_validation_y = sess.run(model_outputs, feed_dict={x_inputs: rand_imgs, dropout_prob: DROPOUT_PROB})
        t_acc = sess.run(accuracy, feed_dict={y_model: temp_validation_y, y_targets: rand_y})

        print('Validation\tEpoch\t{}\tBatch\t{}/{}\tAcc={:.2f}'.format(ep+1,
            (i + 1)//VALIDATION_BATCH_SIZE+1, math.ceil(len(validation_samples) / VALIDATION_BATCH_SIZE), t_acc*100))
        i += VALIDATION_BATCH_SIZE
        epoch_acc += t_acc * len(rand_idx)

    epoch_acc /= len(validation_samples)
    validation_accuracy.append(epoch_acc)

    if epoch_acc == max(validation_accuracy):
        saver.save(sess, os.path.join(DEBUG_FOLDER, DATE_TIME_FOLDER, 'best_model'))

    eval_indices = range(1, ep+2)
    plt.clf()
    plt.subplot(211)
    plt.plot(eval_indices, train_loss, 'g-x', label='Loss')
    plt.legend(loc='upper right')
    plt.xlabel('Generation')
    plt.ylabel('Loss')
    plt.grid(which='major', axis='both')

    plt.subplot(212)
    plt.plot(eval_indices, train_accuracy, 'g-x', label='Train Set Accuracy')
    plt.plot(eval_indices, validation_accuracy, 'r-x', label='Validation Set Accuracy')
    plt.plot(eval_indices, np.ones(len(eval_indices))/TOT_CLASSES, 'k--')
    plt.xlabel('Generation')
    plt.ylabel('Accuracy')
    plt.ylim(0, 1)
    plt.grid(which='both', axis='y')

    plt.show()
    plt.pause(0.01)

    ep += 1
    if np.size(STOP_CRITERIUM) == 1:
        if ep >= STOP_CRITERIUM[0]:
            break
    else:
        if ep > STOP_CRITERIUM[0]:
            if 1 - validation_accuracy[-1]/np.mean(validation_accuracy[len(validation_accuracy) -
                                                STOP_CRITERIUM[0]-1:len(validation_accuracy)]) < STOP_CRITERIUM[1]:
                break
plt.savefig(os.path.join(DEBUG_FOLDER, DATE_TIME_FOLDER, 'Learning.png'))
# Get test set performance
saver = tf.train.import_meta_graph(os.path.join(DEBUG_FOLDER, DATE_TIME_FOLDER, 'best_model.meta'))
saver.restore(sess, tf.train.latest_checkpoint(os.path.join(DEBUG_FOLDER, DATE_TIME_FOLDER)))
i = 0
responses_test = []
worst_cases = []
while i < len(test_samples):
    idx = np.asarray(range(i, np.min([i+VALIDATION_BATCH_SIZE, len(test_samples)])))
    img, y = read_batch(test_samples, idx, imdb, 0, INPUT_PATTERN, TYPE_NORMALIZATION)

    if np.size(SHOW_WORST_CASES) > 0:
        test_scores = sess.run(model_outputs, feed_dict={x_inputs: img, dropout_prob: DROPOUT_PROB})
        tmp_worst_cases = get_worst_cases(i, test_scores, y)
        worst_cases.extend(tmp_worst_cases)
        worst_cases.sort(key=lambda x: x[3], reverse=True)
        worst_cases = worst_cases[0: SHOW_WORST_CASES]

    temp_test_predictions = sess.run(predictions_batch, feed_dict={x_inputs: img, dropout_prob: DROPOUT_PROB})
    tmp_list = [temp_test_predictions, y]
    responses_test.append(tmp_list)
    i += VALIDATION_BATCH_SIZE

predicted_test = [item[0] for item in responses_test]
gt_test = [item[1] for item in responses_test]
predicted_test = [x for r in predicted_test for x in r]
gt_test = [x for r in gt_test for x in r]
accuracy = mt.accuracy_score(gt_test, predicted_test)
print('>>>Final>>>\n\tTest Accuracy: {:.3f}%'.format(accuracy*100))
file_out = open(os.path.join(DEBUG_FOLDER, DATE_TIME_FOLDER, 'results.txt'), "a+")
file_out.write("%d\t%d\t%.2f\t%f\n" % (BALANCED_DATASET, DATA_AUGMENTATION, DROPOUT_PROB, accuracy*100))
file_out.close()
file_out = open(os.path.join(DEBUG_FOLDER, DATE_TIME_FOLDER, 'scores_test.txt'), "a+")
for i, ts in enumerate(test_samples):
    file_out.write("%s,%d,%d\n" % (ts[0], gt_test[i], predicted_test[i]))
file_out.close()

conf_matrix = mt.confusion_matrix(gt_test, predicted_test)
plt.figure(2)
plt.imshow(conf_matrix, cmap='binary', interpolation='none')
plt.show()
plt.savefig(os.path.join(DEBUG_FOLDER, DATE_TIME_FOLDER, 'CM.png'))

if np.size(SHOW_WORST_CASES) > 0:
    for i in range(SHOW_WORST_CASES):
        print('Worst {}: Ground {}: Model={}: Error={:.4f}'.format(i, worst_cases[i][1], worst_cases[i][2],
                                                                   worst_cases[i][3]))
        img = cv2.imread(test_samples[worst_cases[i][0]][0], cv2.IMREAD_COLOR)
        name_img = "%d_%s_Ground_%d_Model_%d_Error_%d.jpg" % (i, test_samples[worst_cases[i][0]][0][test_samples[worst_cases[i][0]][0].rfind(os.sep)+1:-3], worst_cases[i][1], worst_cases[i][2], worst_cases[i][3])
        
        nome_individuo = test_samples[worst_cases[i][0]][0][test_samples[worst_cases[i][0]][0].rfind(os.sep)+1:-3]
        diretoria_nome = nome_individuo.split(")")[0]

        # montar a imagem final
        diretoria = os.listdir("grupos_errados/teste/" + diretoria_nome)
        diretoria = natsort.natsorted(diretoria,reverse=False)

        imagens = []
        for i in diretoria:
            if(i!="1escolha.txt"): imagens.append(i)
        
        for i in range(len(imagens)): imagens[i] = "grupos_errados/teste/" + diretoria_nome + "/" + imagens[i]

        images = [Image.open(i) for i in imagens]
        widths, heights = zip(*(i.size for i in images))

        total_width = sum(widths)
        max_height = max(heights)

        imagem_final = Image.new('RGB', (total_width, max_height))

        x_offset = 0
        for im in images:
            imagem_final.paste(im, (x_offset,0))
            x_offset += im.size[0]

        imagem_final.save(os.path.join(DEBUG_FOLDER, DATE_TIME_FOLDER, name_img))