import os, sys
import numpy as np
from sklearn import model_selection, preprocessing
from sklearn.preprocessing import StandardScaler
import pandas   

def normalize_data(file_name):

    ################################################################################################################################
    # INITIAL SETUP
    ################################################################################################################################
    MODE = "standard" # "zero_one" = [0,1]; "minus_one_one" = [-1,1]; "standard" = mean 0 and variance 1
    header = ["Meanfreq","Sd","Median","Q25","Q75","IQR","Skew","Kurt","Sp_ent","Sfm","Mode","Centroid","Meanfun","Minfun","Maxfun",
            "Meandom","Mindom","Maxdom","Dfrange","Modindx","Label"]

    #################################################################################################################################
    # READ THE ORIGINAL DATA
    #################################################################################################################################
    # read the training file
    data = pandas.read_csv(file_name, names=header)
    data_aux = [data.Meanfreq.tolist()[1:],data.Sd.tolist()[1:],data.Median.tolist()[1:],data.Q25.tolist()[1:],data.Q75.tolist()[1:],
                data.IQR.tolist()[1:],data.Skew.tolist()[1:],data.Kurt.tolist()[1:],data.Sp_ent.tolist()[1:], data.Sfm.tolist()[1:],
                data.Mode.tolist()[1:],data.Centroid.tolist()[1:],data.Meanfun.tolist()[1:],data.Minfun.tolist()[1:],
                data.Maxfun.tolist()[1:],data.Meandom.tolist()[1:],data.Mindom.tolist()[1:], data.Maxdom.tolist()[1:],
                data.Dfrange.tolist()[1:],data.Modindx.tolist()[1:],data.Label.tolist()[1:]]

    final_data = []

    #########################################################################################################
    # NORMALIZE THE TRAINING DATA 
    #########################################################################################################
    scaler = preprocessing.MinMaxScaler()
    for i in range(len(data_aux)):

        i_np = np.asarray(list(map(lambda x : float(x),data_aux[i])))

        # scale feature "X_i"
        if(i<20):
            scaler.fit(np.reshape(i_np,(-1,1)))
            if(MODE=="zero_one"): final_data.append(scaler.transform(np.reshape(i_np,(-1,1))))
            elif(MODE=="minus_one_one"): final_data.append((2*(scaler.transform(np.reshape(i_np,(-1,1)))))-1)
            else: final_data.append(StandardScaler().fit_transform(np.reshape(i_np,(-1,1))))

        # simply save the output variable "y"
        else:
            final_data.append(i_np)

        final_data[i] = np.reshape(final_data[i],(-1,))

    with open(file_name,"w") as file:

        ####################################################################################################################
        # SAVE EVERYTHING IN THE SOURCE CSV FILE
        ####################################################################################################################
        final_data = list(zip(*final_data))
        
        # write the header
        file.write(",".join(header) + "\n")

        # write the data
        for row in final_data:
            file.write(",".join(list(map(lambda x : str(round(x,2)),row))) + "\n")

if __name__ == "__main__":

    directory = os.listdir("data")
    count = 1
    for i in directory:
        if(i[0]!="."):
            print("NORMALIZE - " + str(count) + "/" + str(len(directory)) + " - " + i)
            normalize_data("data/" + i)
            count += 1