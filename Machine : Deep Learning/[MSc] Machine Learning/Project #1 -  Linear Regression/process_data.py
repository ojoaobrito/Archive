import os, sys, csv
from datetime import datetime
import numpy as np
from sklearn import preprocessing, model_selection

MODE = "zero_one" # "zero_one" = [0,1]; "minus_one_one" = [-1,1]
NORMALIZE_OUTPUT = True

####################################################################################################################################################################
# READ AND PREPARE THE DATA
####################################################################################################################################################################
# read the original data
with open("nyse_prices.csv","r") as file:
    content = list(csv.reader(file,delimiter=","))

# take the first column (date) and turn it into a timestamp
content_aux = np.asarray(list(map(lambda x : datetime(int(x.split("-")[0]),int(x.split("-")[1]),int(x.split("-")[2])).timestamp(),list(np.asarray(content)[1:,0]))))

# output column ("close")
y = (np.asarray(content[1:])[:,3]).astype(float)

# input columns, already with the processed "date" column ("date", "open", "low", "high", "volume")
X = np.delete((np.delete(np.asarray(np.column_stack((content_aux,np.asarray(content)[1:,1:]))),3,1)),1,1).astype(float)

# divide in 3 subsets (training, validation and test)
X_train_aux, X_val, y_train_aux, y_val = model_selection.train_test_split(X, y, test_size=0.1, random_state=1)
X_train, X_test, y_train, y_test = model_selection.train_test_split(X_train_aux, y_train_aux, test_size=0.1111121263, random_state=1)

# write everything to the respective files
scaler = preprocessing.MinMaxScaler()
for i in [("training",X_train,y_train),("validation",X_val,y_val),("test",X_test,y_test)]:
    with open("nyse_prices_" + i[0] + ".csv","w") as file:

        # write the header
        file.write("Date,Open,Low,High,Volume,Close\n")

        # scale X
        scaler.fit(i[1])
        if(MODE=="zero_one"): new_X = scaler.transform(i[1])
        else: new_X = (2*(scaler.transform(i[1])))-1
        
        if(NORMALIZE_OUTPUT):
            # scale y
            scaler.fit(np.reshape(i[2],(-1,1)))
            if(MODE=="zero_one"): new_y = scaler.transform(np.reshape(i[2],(-1,1)))
            else: new_y = (2*(scaler.transform(np.reshape(i[2],(-1,1)))))-1

        else: new_y  = i[2]

        # save everything
        np.savetxt(file,np.column_stack((new_X,new_y)),delimiter=',', fmt='%f')