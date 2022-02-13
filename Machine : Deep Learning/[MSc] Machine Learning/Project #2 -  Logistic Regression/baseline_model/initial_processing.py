import os, sys, csv
import pandas
import random
import math

####################################################################################################################################
# INITIAL SETUP
####################################################################################################################################
SHUFFLE = True # if "True", the instances will be pseudo-randomly shuffled
new_header = ["Meanfreq","Sd","Median","Q25","Q75","IQR","Skew","Kurt","Sp_ent","Sfm","Mode","Centroid","Meanfun","Minfun","Maxfun",
        "Meandom","Mindom","Maxdom","Dfrange","Modindx","Label"]

def initial_processing(file_name):

    #################################################################
    # SHUFFLE THE INSTANCES
    #################################################################
    with open("voice.csv","r") as file:
        content = list(csv.reader(file,delimiter=","))[1:]

    if(SHUFFLE): random.shuffle(content)

    with open(file_name.split(".")[0] + "_shuffled.csv","w") as file:

        # write the header
        file.write(",".join(new_header) + "\n")

        # write the data
        for row in content:
            if(row[-1]=="male"):
                file.write(",".join(row[:-1]) + ",1\n")
            else:
                file.write(",".join(row[:-1]) + ",0\n")

if __name__ == "__main__":

    initial_processing("voice.csv")