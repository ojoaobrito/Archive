import os, sys, csv
import numpy as np
from sklearn.decomposition import PCA
from natsort import natsorted
np.set_printoptions(threshold=sys.maxsize)

def pca(file_name):

    ###################################################################################
    # READ THE DATA
    ###################################################################################
    # ---------------------------------------------------------------------------------
    # training file
    # ---------------------------------------------------------------------------------
    with open(file_name,"r") as file:
        content = list(csv.reader(file, delimiter=","))[1:]
        train_X = None
        train_y = None

        for row in content:
            if(train_X is None):
                train_X = np.asarray([float(i) for i in row[:-1]])
                train_y = np.asarray(float(row[-1]))

            else:
                train_X = np.vstack((train_X,np.asarray([float(i) for i in row[:-1]])))
                train_y = np.vstack((train_y,np.asarray(float(row[-1]))))

    # -------------------------------------------------------------------------------
    # test file
    # -------------------------------------------------------------------------------
    with open("data/voice_test_fold_" + file_name.split("_")[-1],"r") as file:
        content = list(csv.reader(file, delimiter=","))[1:]
        test_X = None
        test_y = None

        for row in content:
            if(test_X is None):
                test_X = np.asarray([float(i) for i in row[:-1]])
                test_y = np.asarray(float(row[-1]))

            else:
                test_X = np.vstack((test_X,np.asarray([float(i) for i in row[:-1]])))
                test_y = np.vstack((test_y,np.asarray(float(row[-1]))))

    ##########################################
    # APPLY THE PCA ALGORITHM
    ##########################################
    # make an instance of the Model
    pca = PCA(.95)

    # fit the PCA model with the training data
    pca.fit(train_X)

    # transform the data
    train_X = pca.transform(train_X)
    test_X = pca.transform(test_X)

    #######################################################################################################
    # SAVE THE NEW DATA
    #######################################################################################################
    # ----------------------------------------------------------------------------------------------------
    # training file
    # ----------------------------------------------------------------------------------------------------
    with open(file_name.split(".")[0] + "_pca.csv","w") as file:
        
        # write the new header
        new_header = ["Dimension" + str(i+1) for i in range(len(train_X[0]))]
        new_header.append("Label")
        file.write(",".join(new_header) + "\n")

        for idx,i in enumerate(train_X):
            file.write(",".join(list(map(lambda x : str(x),list(i)))) + "," + str(train_y[idx][0]) + "\n")
    
    os.remove(file_name)
    # -----------------------------------------------------------------------------------------------------
    # test file
    # -----------------------------------------------------------------------------------------------------
    with open("data/voice_test_fold_" + (file_name.split("_")[-1]).split(".")[0] + "_pca.csv","w") as file:
        
        # write the new header
        new_header = ["Dimension" + str(i+1) for i in range(len(test_X[0]))]
        new_header.append("Label")
        file.write(",".join(new_header) + "\n")

        for idx,i in enumerate(test_X):
            file.write(",".join(list(map(lambda x : str(x),list(i)))) + "," + str(test_y[idx][0]) + "\n")

    os.remove("data/voice_test_fold_" + file_name.split("_")[-1])

if __name__ == "__main__":

    # remove previous attempts
    for i in os.listdir("data"):
        if("pca" in i): os.remove("data/" + i)

    directory = natsorted([i for i in os.listdir("data") if ("training" in i and "pca" not in i)],reverse=False)

    count = 0
    for i in directory:
        count += 1
        print("PCA " + str(count) + "/" + str(len(directory)) + " - " + i)
        pca("data/" + i)