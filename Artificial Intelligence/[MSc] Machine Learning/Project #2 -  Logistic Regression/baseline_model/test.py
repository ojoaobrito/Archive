import seaborn as sn
import pandas as pd
import tensorflow as tf
import os, sys, csv
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc
from natsort import natsorted
from math import sqrt
from scipy import interp
np.set_printoptions(threshold=sys.maxsize)
np.set_printoptions(suppress=True)

NUM_CLASSES = 2
PLOT = True
K = 5
NUM_SAMPLES = 0
mean_confusion_matrix = [0,0,0,0]

def confusion_matrix(data): # auxiliary function to get a confusion matrix

    df_cm = pd.DataFrame(data, range(2), range(2))

    sn.set(font_scale=1.0) # for label size

    # create the confusion matrix
    ax = sn.heatmap(df_cm, annot=True, annot_kws={"size": 10}, cmap="Blues",fmt='d', xticklabels=["Positive\n(TP + FP)","Negative\n(FN + TN)"],
                    yticklabels=["Positive\n(TP + FN)","Negative\n(FP + TN)"])
    ax.axes.set_title("Confusion Matrix (n = " + str(NUM_SAMPLES) + ")" ,fontsize=18)

    # add some additional items
    plt.yticks(rotation=0)
    plt.xlabel("Predicted Label")
    plt.ylabel("Ground Truth")
    plt.tight_layout()

    # save the final figure
    plt.savefig("confusion_matrix.png")

def compute_positives_and_negatives(y, predictions, decision_boundary): # auxiliary function to compute the true positives, false positives, true negatives and false negatives

    global mean_confusion_matrix
    TP = FP = TN = FN = 0

    # calculate the true positives, false positives, true negatives and false negatives
    for i in range(len(predictions)):

        predicted = [0,0]

        # get the prediction based on the best decision boundary
        if(predictions[i][1]>=decision_boundary): predicted = [0,1]
        else: predicted = [1,0]

        if(np.array_equal(y[i],[1,0]) and np.array_equal(predicted,[1,0])):
            TN += 1
            continue
        
        if(np.array_equal(y[i],[1,0]) and np.array_equal(predicted,[0,1])):
            FP += 1
            continue

        if(np.array_equal(y[i],[0,1]) and np.array_equal(predicted,[0,1])):
            TP += 1
            continue

        if(np.array_equal(y[i],[0,1]) and np.array_equal(predicted,[1,0])):
            FN += 1
            continue

    # update the mean values
    mean_confusion_matrix[0] += TP
    mean_confusion_matrix[1] += FN
    mean_confusion_matrix[2] += FP
    mean_confusion_matrix[3] += TN

    return(TP, FN, FP, TN)

def test(thetas, test_file): # main function to perform some testing and retrieve performance metrics

    global NUM_SAMPLES

    def h_1(X, thetas): # our first model (h_theta(x) = theta_1*x_1 + theta_2*x_2 + ... + theta_11)
        return(np.matmul(X, thetas))

    def f_1(x): # the chosen activation function (sigmoid)
        return(1.0 / (1.0 + np.exp(-x)))

    ###########################################################
    # READ AND PREPARE THE DATA
    ###########################################################
    with open(test_file,"r") as csv_file:
        content = list(csv.reader(csv_file, delimiter=','))[1:]
        NUM_SAMPLES = len(content)
        X = []
        y = []
        for row in content:
            y.append(float(row[-1]))
            X.append([float(i) for i in row[:-1]])
        
    # convert to numpy arrays
    X = np.asarray(X)
    y = np.asarray(y)

    # add the an extra 1 to every instance
    X = np.append(X, np.ones((X.shape[0],1), np.float64), axis=1)

    # the predictions of our model
    predictions = f_1(h_1(X, thetas))

    ############################################################################
    # COMPUTE ROC CURVES AND AUC VALUES
    ############################################################################
    # reshape our predictions
    predictions = np.column_stack((1-predictions,np.expand_dims(predictions,1)))
    y = np.asarray([[1,0] if i==0.0 else [0,1] for i in y])

    fpr = dict()
    tpr = dict()
    roc_auc = dict()
    best_values = (0,0)
    best_decision_boundary = 0.0
    best_distance = 50.0
    for i in range(NUM_CLASSES):
        fpr[i], tpr[i], thresholds = roc_curve(y[:, i], predictions[:, i])

        # get the best decision boundary
        if(i==1):
            for jdx,j in enumerate(fpr[i]):
                distance_aux = np.sqrt((0-j)**2 + (1-tpr[i][jdx])**2)
                if(distance_aux<best_distance):
                    best_distance = distance_aux
                    best_values = (j,tpr[i][jdx])
                    best_decision_boundary = thresholds[jdx]

        roc_auc[i] = auc(fpr[i], tpr[i])

    ######################################################################################
    # COMPUTE PRECISION, RECALL AND ACCURACY METRICS
    ######################################################################################
    TP, FN, FP, TN = compute_positives_and_negatives(y,predictions,best_decision_boundary)

    # compute some performance metrics
    accuracy = (TP + TN) / (TP + TN + FP + FN) # ideally would be 1.0
    precision = TP / (TP + FP) # ideally would be 1.0
    recall = TP / (TP + FN) # ideally would be 1.0

    return(fpr[1],tpr[1],(roc_auc[1],accuracy,precision,recall))

if __name__ == "__main__":

    #####################################################################################
    # LOAD THE LEARNED THETAS
    #####################################################################################
    with open("learned_thetas.csv","r") as file:
        content = list(csv.reader(file,delimiter=","))
        thetas = []
        for row in content:
            thetas.append(np.asarray(list(map(lambda x : float(x),row))))

    directory = natsorted([i for i in os.listdir("data") if ("test" in i)],reverse=False)
    
    #########################################################################
    # EVALUATE PERFORMANCE ON THE TEST SETS
    #########################################################################
    count = 0
    results = []

    # auxiliary variables for the plot
    tprs = []
    base_fpr = np.linspace(0, 1, 101)

    for i in directory:
        count += 1
        print("TEST - " + str(count) + "/" + str(len(directory)) + " - " + i)

        # perform the test
        fpr, tpr, metrics = test(thetas[count-1],"data/" + i)
        print(fpr)
        print(tpr)
        sys.exit()

        # save the results
        results.append(metrics)

        # save data for the plot
        tpr = interp(base_fpr, fpr, tpr)
        tpr[0] = 0.0
        tprs.append(tpr)
    
    ################################################################################
    # COMPUTE THE MEAN AND STANDARD DEVIATION OF OUR RESULTS
    ################################################################################
    # means
    means = [0.0 for i in range(4)]
    for i in range(4):
        means[i] = sum([j[i] for j in results])/count

    # standard deviations
    deviations = [0.0 for i in range(4)]
    for i in range(4):
        deviations[i] = sqrt(sum([(j[i] - means[i])**2 for j in results])/(count-1))

    ##################################################################
    # PRINT SOME PERFORMANCE METRICS
    ##################################################################
    print("\nMEAN PERFORMANCE METRICS")
    print("--------------------------")
    print("AUC: {:.2f} ± {:.2f}".format(means[0],deviations[0]))
    print("ACCURACY: {:.2f} ± {:.2f}".format(means[1],deviations[1]))
    print("PRECISION: {:.2f} ± {:.2f}".format(means[2],deviations[2]))
    print("RECALL: {:.2f} ± {:.2f}".format(means[3],deviations[3]))

    ###########################################################################################################################
    # PLOT THE MEAN ROC CURVE
    ###########################################################################################################################
    if(PLOT):
        tprs = np.array(tprs)
        mean_tprs = tprs.mean(axis=0)
        std = tprs.std(axis=0)

        tprs_upper = np.minimum(mean_tprs + std, 1)
        tprs_lower = mean_tprs - std

        plt.plot(base_fpr, mean_tprs, 'b', label="ROC curve (area = " + "{:.2f} ± {:.2f}".format(means[0],deviations[0]) + ")")
        plt.fill_between(base_fpr, tprs_lower, tprs_upper, color='grey', alpha=0.4)

        plt.plot([0, 1], [0, 1],'r--')
        plt.xlim([-0.01, 1.01])
        plt.ylim([-0.01, 1.01])
        plt.legend(loc="lower right")
        plt.title("Mean ROC curve (over " + str(K) + " folds)")
        plt.ylabel('True Positive Rate (TPR)')
        plt.xlabel('False Positive Rate (FPR)')
        plt.savefig("roc_curve_baseline.png")
        plt.clf()

    ############################################################################################
    # SAVE THE CONFUSION MATRIX
    ############################################################################################
    # average out every value
    mean_confusion_matrix = (np.reshape(np.asarray(mean_confusion_matrix)/count,(2,2))).tolist()
    mean_confusion_matrix = [list(map(lambda x : int(round(x,0)),i)) for i in mean_confusion_matrix]

    # save the confusion matrix
    confusion_matrix(mean_confusion_matrix)