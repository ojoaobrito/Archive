import os, sys, csv
from shutil import rmtree
import numpy as np
from sklearn.decomposition import PCA

def pca(data):

    for i in [.75,.90,.95]:

        # build an instance of the PCA model
        pca = PCA(i)

        # fit the PCA model with the training data
        pca.fit(data)

        # transform the data
        new_data = pca.transform(data)

        with open("pca/credit_card_data_pca_" + str(int(i*100)) + ".csv","w") as file:

            # write the header
            file.write(",".join(["dimension_" + str(j) for j in range(len(new_data[0]))]) + "\n")

            for j in new_data:
                file.write(",".join(list(map(lambda x : str(x),j))) + "\n")

if __name__ == "__main__":

    if(os.path.exists("pca")): rmtree("pca")
    os.makedirs("pca")

    with open("credit_card_data_processed.csv", "r") as file:
        data = list(map(lambda x : list(map(lambda y : float(y),x)),list(csv.reader(file,delimiter=","))[1:]))
        pca(data)