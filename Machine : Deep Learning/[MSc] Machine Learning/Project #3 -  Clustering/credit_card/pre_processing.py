import os, sys, csv
from random import sample, shuffle
from sklearn.preprocessing import MinMaxScaler
from shutil import rmtree
import numpy as np

NORMALIZE_DATA = False

###########################################################################
# CHECK FOR MISSING VALUES AND SHUFFLE THE INSTANCES
###########################################################################
with open("credit_card_data.csv","r") as file:
    content = list(csv.reader(file,delimiter=","))
    HEADER = content[0]
    content = content[1:]
    instances = []

    # check for missing values
    for idx,i in enumerate(content):
        if("" not in i): instances.append(list(map(lambda x : float(x),i)))

shuffle(instances)
    
###########################################
# IF NEEDED, NORMALIZE THE DATA
###########################################
if(NORMALIZE_DATA):
    scaler = MinMaxScaler()
    
    # normalize the data
    scaler.fit(instances)
    instances = scaler.transform(instances)

###################################################################################
# DUMP THE DATA INTO THE FINAL FILE
###################################################################################
with open("credit_card_data_processed.csv","w") as file:

    # write the header
    file.write(",".join(HEADER) + "\n")

    # populate the file
    for instance in instances:
        file.write(",".join(list(map(lambda x : str(round(x,3)),instance))) + "\n")