import sys
import os
import logging
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
import cv2
from random import shuffle, sample
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

## GERAR TESTES
##############################################################################################################################################################################################################################
# obter a imagem que não se conhece
if(len(sys.argv)>1):
    input_image = sys.argv[1]

else:
    for i in os.listdir("input"):
        if(i[0]!="."):
            input_image = i

individuos = []
individuos_index = []
base_dados = os.listdir("grupos_BD")
testes = []
num_testes = 1

for i in base_dados:
    if(i[0]!="."):
        if((input_image.split("-")[0])!=(i.split("-")[0])): continue # géneros diferentes
        individuos.append([i,0.0,0,[]]) # nome, classificação atual, número de testes feitos e histórico
        individuos_index.append(i)
        for j in range(num_testes):
            lista_aux = ["grupos_BD/" + i, "input/" + input_image]
            # shuffle(lista_aux)
            testes.append([lista_aux[0], lista_aux[1]])
 
ficheiro = open("base.csv","r")
base = ficheiro.read()
ficheiro.close()

with open("data.csv","w") as ficheiro:
    ficheiro.write(base)
    for i in testes:
        ficheiro.write(i[0] + "," + i[1] + ",0,2\n")
##############################################################################################################################################################################################################################

## CONFIGURAÇÕES
##############################################################################################################################################################################################################################
TYPE_NORMALIZATION = 3

BALANCED_DATASET = 0
DROPOUT_PROB = 1
VALIDATION_BATCH_SIZE = 100

DATASET = os.path.join('data.csv')

IMDB_FILE = os.path.join('IMDB.dat')

learning_samples, validation_samples, test_samples, classes = read_csv_data_file(DATASET, "")
TOT_CLASSES = 2

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

for index, elemento in enumerate(test_samples):
    if("grupos_BD" in elemento[0]):
        individuos[(individuos_index.index(elemento[0].split("/")[1]))][2] += 1
        individuos[(individuos_index.index(elemento[0].split("/")[1]))][3].append(int(predicted_test[index]))
        individuos[(individuos_index.index(elemento[0].split("/")[1]))][1] = float(sum(individuos[(individuos_index.index(elemento[0].split("/")[1]))][3]))/individuos[(individuos_index.index(elemento[0].split("/")[1]))][2] 
    else:
        individuos[(individuos_index.index(elemento[1].split("/")[1]))][2] += 1
        individuos[(individuos_index.index(elemento[1].split("/")[1]))][3].append(int(predicted_test[index]))
        individuos[(individuos_index.index(elemento[1].split("/")[1]))][1] = float(sum(individuos[(individuos_index.index(elemento[1].split("/")[1]))][3]))/individuos[(individuos_index.index(elemento[1].split("/")[1]))][2] 

individuos.sort(reverse=True,key=lambda x: x[1])
##############################################################################################################################################################################################################################

## PRODUZIR O OUTPUT
##############################################################################################################################################################################################################################
# imprimir o ranking
'''
print("- TOP -")
print("-------")
for i in range(len(individuos)):
    print(individuos[i][0] + " --- " + str(individuos[i][1]) + " --- " + str(individuos[i][2]))
'''
pontuacao = 0.0
# imprimir a posição da pessoa certa
for i in range(len(individuos)):
    if((input_image.split("-")[0] + input_image.split("-")[1])==(individuos[i][0].split("-")[0] + individuos[i][0].split("-")[1])):
        pos = i+1
        pontuacao = individuos[i][1]
        while(pos-2>=0 and individuos[pos-2][1]==individuos[pos-1][1]):
            pos-=1
        print("A pessoa certa ficou em " + str(pos) + "º lugar")

# contar as pessoas com igual pontuação à certa
iguais = 0
for i in range(len(individuos)):
    if(individuos[i][1]==pontuacao): iguais+=1

# guardar a posição num ficheiro específico
with open("face_match1_ranking.txt","a+") as ficheiro:
    ficheiro.write(str(pos) + " " + str(iguais-1) + "\n")

# guardar o ranking num ficheiro específico
with open("face_match1_top.txt","a+") as ficheiro:
    ficheiro.write("-------------------------\n")
    ficheiro.write("PESSOA CERTA: " + input_image + "\n")
    for i in range(len(individuos)):
        ficheiro.write(individuos[i][0] + " --- " + str(individuos[i][1]) + " --- " + str(individuos[i][2]) + "\n")
    ficheiro.write("-------------------------\n")
##############################################################################################################################################################################################################################
