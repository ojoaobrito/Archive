import sys
import os
import logging
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
import cv2
from random import shuffle, sample, randint
import pickle
import sklearn.metrics as mt
import math
from read_csv_data_file import read_csv_data_file
from read_batch import read_batch, get_input_pattern
from get_imdbs import *
import models_hugomcp as md
from PIL import Image

import tensorflow.contrib.slim as slim
from tensorflow.contrib.slim.nets import inception

from inception_resnet_v2 import inception_resnet_v2, inception_resnet_v2_arg_scope

## IMPEDIR OUTPUTS DESNECESSÁRIOS
##############################################################################################################################################################################################################################
logging.getLogger("tensorflow").setLevel(logging.FATAL)
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
##############################################################################################################################################################################################################################

## OBTER O INPUT
##############################################################################################################################################################################################################################
diretoria = os.listdir("input")
teste = []

for i in diretoria:
    if(i[0]!="."):
        teste.append("input/" + i)

ficheiro = open("base.csv","r")
base = ficheiro.read()
ficheiro.close()

num_testes = 1
with open("data.csv","w") as ficheiro:
    ficheiro.write(base)
    for i in range(num_testes):
        #if(randint(0,1)==0): shuffle(teste_lista)
        ficheiro.write(",".join(teste) + ",0,2\n")
##############################################################################################################################################################################################################################

## CONFIGURAÇÕES
##############################################################################################################################################################################################################################
TYPE_NORMALIZATION = 3

BALANCED_DATASET = 0
DROPOUT_PROB = 1
VALIDATION_BATCH_SIZE = 1

DATASET = os.path.join('data.csv')

IMDB_FILE = os.path.join('IMDB.dat')

learning_samples, validation_samples, test_samples, classes = read_csv_data_file(DATASET, "")
TOT_CLASSES = len(classes)

INPUT_PATTERN = get_input_pattern(test_samples[0])

HEIGHT_IMGS = INPUT_PATTERN[0][0]
WIDTH_IMGS = INPUT_PATTERN[0][1]
depths = [x[1] for x in INPUT_PATTERN[1:]]
DEPTH_IMGS = sum(depths)

x_input_shape = (None, HEIGHT_IMGS, WIDTH_IMGS, DEPTH_IMGS)
x_inputs = tf.placeholder(tf.float32, shape=x_input_shape)
y_targets = tf.placeholder(tf.int32, shape=None)
y_model = tf.placeholder(tf.float32, shape=(None, TOT_CLASSES))
dropout_prob = tf.placeholder(tf.float32)

with tf.variable_scope('model_definition') as scope:
    # model_outputs = md.vgg(x_inputs, dropout_prob, TOT_CLASSES)
    model_outputs, _ = inception.inception_v2(x_inputs, TOT_CLASSES)
    # model_outputs, _ = inception_resnet_v2(x_inputs, TOT_CLASSES)

    scope.reuse_variables()

predictions_batch = tf.cast(tf.argmax(model_outputs, 1), tf.int32)

sess = tf.Session()
plt.ion()
saver = tf.train.Saver()

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
##############################################################################################################################################################################################################################
             
## AVALIAR OS INDIVÍDUOS
##############################################################################################################################################################################################################################
saver = tf.train.import_meta_graph('best_model.meta')
saver.restore(sess, tf.train.latest_checkpoint("./"))
i = 0
responses_test = []
while i < len(test_samples):
    idx = np.asarray(range(i, np.min([i+VALIDATION_BATCH_SIZE, len(test_samples)])))
    img, y = read_batch(test_samples, idx, imdb, 0, INPUT_PATTERN, TYPE_NORMALIZATION)

    temp_test_predictions = sess.run(predictions_batch, feed_dict={x_inputs: img, dropout_prob: DROPOUT_PROB})
    tmp_list = [temp_test_predictions, y]
    responses_test.append(tmp_list)
    i += VALIDATION_BATCH_SIZE

predicted_test = [item[0] for item in responses_test]
gt_test = [item[1] for item in responses_test]
predicted_test = [x for r in predicted_test for x in r]
gt_test = [x for r in gt_test for x in r]

contador_1 = 0
contador_0 = 0
# print(predicted_test)
for i in predicted_test:
    if(int(i)==1): contador_1 += 1
    else: contador_0 += 1

# print(contador_1)
# print(contador_0)
if(contador_1>contador_0): print("\nA sequência diz respeito ao mesmo indivíduo\n")
else: print("\nA sequência diz respeito a indivíduos diferentes\n")
##############################################################################################################################################################################################################################
