import os, sys, csv
import numpy as np
from random import sample
from sklearn.model_selection import KFold
from shutil import rmtree

K = 5

def k_fold(file_name,K_in):

    ################################################################################################################################
    # INITIAL SETUP
    ################################################################################################################################
    # header
    header = ["Meanfreq","Sd","Median","Q25","Q75","IQR","Skew","Kurt","Sp_ent","Sfm","Mode","Centroid","Meanfun","Minfun","Maxfun",
            "Meandom","Mindom","Maxdom","Dfrange","Modindx","Label"]

    with open(file_name,"r") as file:
        content = list(csv.reader(file,delimiter=","))[1:]

    # make sure that our dataset is divisible by "K"
    if((len(content)%K_in)!=0):
        with open(file_name,"w") as file:
            
            # compute the desired size
            size = (len(content)//K_in)*K_in

            file.write(",".join(header) + "\n")
            content = sample(content, size)
            for row in content:
                file.write(",".join(row) + "\n")

    kfold = KFold(n_splits = K_in)
    fold = 1
    for train_index, test_index in kfold.split(content):

        ####################################################################################################################
        # SAVE EVERYTHING IN A CSV FILE
        ####################################################################################################################
        # ------------------------------------------------------------------------------------------------------------------
        # training file
        # ------------------------------------------------------------------------------------------------------------------
        with open("data/voice_training_fold_" + str(fold) +  ".csv", "w") as file:

            # write the header
            file.write(",".join(header) + "\n")
            
            # write the data
            for row in train_index:
                file.write(",".join(content[row]) + "\n")

        # ------------------------------------------------------------------------------------------------------------------
        # test file
        # ------------------------------------------------------------------------------------------------------------------
        with open("data/voice_test_fold_" + str(fold) +  ".csv", "w") as file:

            # write the header
            file.write(",".join(header) + "\n")
            
            # write the data
            for row in test_index:
                file.write(",".join(content[row]) + "\n")
        
        fold += 1

if __name__ == "__main__":

    if(os.path.exists("data")):
        rmtree("data")
    os.makedirs("data")

    k_fold("voice_shuffled.csv",K)