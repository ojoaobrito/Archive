import tensorflow as tf
import os, sys, csv
import numpy as np
import matplotlib.pyplot as plt
from random import uniform
from sklearn.preprocessing import MinMaxScaler

TOT_ITERATIONS = 70000
LEARNING_RATE = 0.01
LAMBDA = 0.0
K = 5

def train(lr, tot_iter, training_file, fold):

    def h(X, thetas): # our first model (h_theta(x) = theta_1*x_1 + theta_2*x_2 + ... + theta_11)
        return(np.matmul(X, thetas))

    def f(x): # the chosen activation function (sigmoid)
        return(1.0 / (1.0 + np.exp(-x)))

    def J(f, y, thetas): # the cost function (cross entropy)
        return((-(np.matmul(np.transpose(y), np.log(f)) + np.matmul(np.transpose(1.0 - y), np.log(1.0 - f))) / len(y)) + LAMBDA * sum(thetas**2))

    def J_tf(predict, y): # tensorflow version of the cost function (cross entropy)
        return(-(tf.matmul(tf.transpose(tf.expand_dims(y, 1)), tf.log(predict))+ tf.matmul(tf.transpose(tf.expand_dims(1.0-y, 1)), tf.log(1.0 - predict))) / tf.cast(tf.size(y), tf.float64))

    #############################################################
    # READ AND PREPARE THE DATA
    #############################################################q
    with open(training_file,"r") as file:
        content = list(csv.reader(file, delimiter=","))[1:]
        X = []
        y = []
        for row in content:
            y.append(float(row[-1]))
            X.append([float(i) for i in row[:-1]])

    # convert to numpy arrays
    X = np.asarray(X)
    y = np.asarray(y)

    # add an extra 1 to every instance
    X = np.append(X, np.ones((X.shape[0],1), np.float64), axis=1)

    ##################################################################################################################
    # GRADIENT DESCENT METHOD
    ##################################################################################################################
    thetas_gd = np.random.uniform(-1.0,1.0, size=(len(X[0]),))
    thetas_gd_initial = thetas_gd
    Js_gd = []

    for i in range(tot_iter): # iterate over the training data

        # temporary variable for the updates
        temps = np.zeros(len(X[0]), dtype=np.float64)

        # the predictions of our model
        predictions = f(h(X, thetas_gd))

        # update each weight (theta)
        for j in range(len(X[0])):

            # get the derivative of J with respect to theta_j
            temps[j] = (np.matmul(np.transpose(X[:,j]), predictions - y) / len(y)) + 2 * LAMBDA * thetas_gd[j]

            # update theta_j
            thetas_gd[j] = thetas_gd[j] - lr * temps[j]

        if(((i+1)%1000)==0):
            # store the new loss value
            Js_gd.append(J(f(h(X,thetas_gd)),y,thetas_gd))

            # print the results
            print("(FOLD " + str(fold) + ") GRADIENT DESCENT METHOD: EPOCH " + str(i+1) + " - LOSS " + str(Js_gd[-1]))

    ############################################################################################################
    # TENSORFLOW
    ############################################################################################################
    sess = tf.Session()
    
    thetas_gd_initial = np.random.uniform(-1.0, 1.0, size=(len(X[0]),))

    # graph definition
    x_data = tf.placeholder(shape=[None, len(X[0])], dtype=tf.float64)
    y_target = tf.placeholder(shape=[None], dtype=tf.float64)
    thetas = tf.Variable(tf.convert_to_tensor(thetas_gd_initial))

    Js_tf = []

    # define the model
    with tf.variable_scope("model_definition") as scope:
        model_output = 1.0/(1.0 + tf.exp(- tf.matmul(x_data, tf.expand_dims(thetas,1))))
        scope.reuse_variables()

    # define the loss function
    loss = J_tf(model_output, y_target) + LAMBDA * tf.reduce_sum(tf.math.pow(thetas,2))

    # define the optimizer
    my_opt = tf.train.GradientDescentOptimizer(lr)
    train_step = my_opt.minimize(loss)

    # get everything ready
    init = tf.global_variables_initializer()
    sess.run(init)

    for i in range(tot_iter):

        # train the model
        sess.run(train_step, feed_dict={x_data: X, y_target: y})

        # get the loss value
        l = sess.run(loss, feed_dict={x_data: X, y_target: y})

        if(((i+1)%1000)==0):
            # store the new loss value
            Js_tf.append(l[0][0])

            # print the results
            print("(FOLD " + str(fold) + ") TENSORFLOW METHOD: EPOCH " + str(i+1) + " - LOSS " + str(Js_tf[-1]))

    ####################################################################################
    # SAVE THE LEARNED THETAS
    ####################################################################################
    if(not os.path.exists("learned_thetas.csv")): mode = "w"
    else: mode = "a"

    with open("learned_thetas.csv",mode) as file:
        file.write(",".join(list(map(lambda x : str(x),list(sess.run(thetas))))) + "\n")

    return(Js_gd,Js_tf)

if __name__ == "__main__":

    if(os.path.exists("learned_thetas.csv")):
        os.remove("learned_thetas.csv")

    Js_gd = []
    Js_tf = []
    for i in range(K):

        #################################################################################################
        # TRAIN SEVERAL TIMES ON THE PREVIOUSLY DEFINED FOLDS
        #################################################################################################
        print("TRAINING ON FOLD " + str(i+1))
        results = train(LEARNING_RATE,TOT_ITERATIONS,"data/voice_training_fold_" + str(i+1) + ".csv",i+1)
        Js_gd.append(results[0])
        Js_tf.append(results[1])

    #########################################################################################################################################
    # RESULTS VISUALIZATION
    #########################################################################################################################################
    colors = ["r","g","b","y","c"]
    fig, ax = plt.subplots()
    
    # ---------------------------------------------------------------------------------------------------------------------------------------
    # GRADIENT DESCENT LOSS PLOT
    # ---------------------------------------------------------------------------------------------------------------------------------------
    plt.subplot(1, 2, 1)
    best = []

    # prepare the plot
    for idx,i in enumerate(Js_gd):
        plt.plot(range(TOT_ITERATIONS//1000), i, ("-" + colors[idx]), label=("Fold " + str(idx+1) + " (J={:.4f}".format(float(i[-1])) + ")"))
        best.append(i[-1])

    plt.xlabel("Iterations")
    plt.ylabel("Loss")
    plt.legend(loc="upper right")
    
    # compute the mean loss and standard deviation
    mean = (sum(best)/len(best))
    standard_deviation = float(np.std(np.asarray(best)))

    plt.title("Gradient Descent Loss ({:.4f} ± {:.4f}".format(mean,standard_deviation) + ")")
    plt.grid()

    # ---------------------------------------------------------------------------------------------------------------------------------------
    # TENSORFLOW LOSS PLOT
    # ---------------------------------------------------------------------------------------------------------------------------------------
    plt.subplot(1, 2, 2)
    best = []

    # prepare the plot
    for idx,i in enumerate(Js_tf):
        plt.plot(range(TOT_ITERATIONS//1000), i, ("-" + colors[idx]), label=("Fold " + str(idx+1) + " (J={:.4f}".format(float(i[-1])) + ")"))
        best.append(i[-1])
    
    plt.xlabel("Iterations")
    plt.ylabel("Loss")
    plt.legend(loc="upper right")

    # compute the mean loss and standard deviation
    mean = (sum(best)/len(best))
    standard_deviation = float(np.std(np.asarray(best)))

    plt.title("Tensorflow Loss ({:.4f} ± {:.4f}".format(mean,standard_deviation) + ")")
    plt.grid()
    
    # show the final plot
    plt.tight_layout()
    plt.show()