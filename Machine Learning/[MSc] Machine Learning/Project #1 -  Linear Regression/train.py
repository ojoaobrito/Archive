import tensorflow as tf
import os, sys, csv
import numpy as np
import matplotlib.pyplot as plt
from random import uniform

LEARNING_RATE = 0.000001
NUM_EPOCHS = 200
NUM_EPOCHS_TF = 200

def J(X, y, thetas): # loss function (MSE)

    error = 0.0

    for idx,i in enumerate(X):
        error += (np.dot(i,thetas) - y[idx])**2
    
    return(error/(len(X)*2))

##################################################################
# READ THE DATA
##################################################################
with open('nyse_prices_training.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader) # to skip the header file
    X = []
    y = []
    for row in csv_reader:
        X.append(list(map(lambda x : float(x), row[:-1])) + [1.0])
        y.append(float(row[-1]))

X = np.asarray(X)
y = np.asarray(y)
##################################################################

#####################################################################################################
# CLOSED-FORM METHOD
#####################################################################################################
theta_direct = np.matmul(np.matmul(np.linalg.inv(np.matmul(np.transpose(X), X)), np.transpose(X)), y)

print("Solution Closed-Form:")
print("J = {:.7f}".format(J(X,y, theta_direct)))
print("Thetas = " + ", ".join(list(map(lambda x : str(x),list(theta_direct)))))
#####################################################################################################

##################################################################################################################################################################
# GRADIENT DESCENT METHOD
##################################################################################################################################################################
theta_gd = [uniform(-8.5e-06, -10e-06), uniform(-0.40, -0.7), uniform(0.5,0.8), uniform(0.6,1.0), uniform(-8.1e-05,-9e-05),uniform(4.5e-05,5.5e-05)]

for i in range(NUM_EPOCHS):
    print("EPOCH (" + str(i+1) + "/" + str(NUM_EPOCHS) + ")")
    aux = [0.0 for _ in range(6)]
    for j in range(len(y)):

        # calculate the gradients
        for k in range(5): # the first 5 thetas (the last theta is special)
            aux[k] += (theta_gd[0]*X[j][0] + theta_gd[1]*X[j][1] + theta_gd[2]*X[j][2] + theta_gd[3]*X[j][3] + theta_gd[4]*X[j][4] + theta_gd[5] - y[j]) * X[j][k]
        
        aux[5] += (theta_gd[0]*X[j][0] + theta_gd[1]*X[j][1] + theta_gd[2]*X[j][2] + theta_gd[3]*X[j][3] + theta_gd[4]*X[j][4] + theta_gd[5] - y[j])

    aux = list(map(lambda x : x/len(y),aux))

    # update the weights
    for k in range(6):
        theta_gd[k] = theta_gd[k] - LEARNING_RATE * aux[k]

print("Solution Gradient Descent:")
print("J = {:.7f}".format(J(X,y, theta_gd)))
print("Thetas = " + ", ".join(list(map(lambda x : str(x),list(theta_gd)))))
##################################################################################################################################################################

########################################################################################################
# TENSORFLOW VERSION OF GRADIENT DESCENT
########################################################################################################
sess = tf.compat.v1.Session()

# graph definition
x_data = tf.compat.v1.placeholder(shape=[None, 6], dtype=tf.float32)
y_target = tf.compat.v1.placeholder(shape=[None], dtype=tf.float32)
weight_0 = tf.compat.v1.Variable(tf.random.uniform(shape=[1, 1], minval=-8.5e-06, maxval=-10e-06))
weight_1 = tf.compat.v1.Variable(tf.random.uniform(shape=[1, 1], minval=-0.40, maxval=-0.7))
weight_2 = tf.compat.v1.Variable(tf.random.uniform(shape=[1, 1], minval=0.5, maxval=0.8))
weight_3 = tf.compat.v1.Variable(tf.random.uniform(shape=[1, 1], minval=0.6, maxval=1.0))
weight_4 = tf.compat.v1.Variable(tf.random.uniform(shape=[1, 1], minval=-8.1e-05, maxval=-9e-05))
weight_5 = tf.compat.v1.Variable(tf.random.uniform(shape=[1, 1], minval=4.5e-05, maxval=5.5e-05))
weights = tf.compat.v1.concat([weight_0, weight_1, weight_2, weight_3, weight_4, weight_5], 0)

# define the model
with tf.compat.v1.variable_scope('model_definition') as scope:
    model_output = tf.compat.v1.matmul(x_data, weights)
    scope.reuse_variables()

def loss_l2(predict, gt):

    predict = tf.compat.v1.squeeze(predict)
    resid = predict - gt
    ret = tf.compat.v1.sqrt(tf.compat.v1.reduce_sum(tf.compat.v1.pow(resid, tf.compat.v1.constant(2.))))
    return ret

loss = loss_l2(model_output, y_target)
my_opt = tf.compat.v1.train.GradientDescentOptimizer(LEARNING_RATE)
train_step = my_opt.minimize(loss)

# graph execution
init = tf.compat.v1.global_variables_initializer()
sess.run(init)

for i in range(NUM_EPOCHS_TF):
    sess.run(train_step, feed_dict={x_data: X, y_target: y})

theta_tf = sess.run(weights)
cur_loss = J(X,y, theta_tf)

print("Solution Tensorflow:")
print("J = {:.7f}".format(J(X,y, theta_tf)[0]))
print("Thetas = " + ", ".join(list(map(lambda x : str(x),list(theta_tf)))))
########################################################################################################