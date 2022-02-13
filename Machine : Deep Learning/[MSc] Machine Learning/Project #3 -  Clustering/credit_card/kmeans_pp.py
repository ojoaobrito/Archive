import os, sys, csv
import numpy as np
from random import uniform, choice
from pickle import dump

###################################
# HYPERPARAMETERS
###################################
K_MAX = 8
STOP_CRITERIUM = 0.1
NORMALIZED_DATA = False
PCA = 75 # 75; 90; 95 or None

if(not NORMALIZED_DATA):
    if(PCA==75): NUM_FEATURES = 3
    elif(PCA==90): NUM_FEATURES = 4
    elif(PCA==95): NUM_FEATURES = 5
    else: NUM_FEATURES = 17

else:
    if(PCA==75): NUM_FEATURES = 3
    elif(PCA==90): NUM_FEATURES = 5
    elif(PCA==95): NUM_FEATURES = 7
    else: NUM_FEATURES = 17

def centroid_initialization(data, k): # auxiliary function, provides a smarter way of initializing "k" centroids

    centroids = []

    # choose the first centroid uniformly at random from the data points
    centroids.append(choice(data))

    # if needed, choose the remaining "k"-1 centroids
    while(len(centroids)!=k):
        next_centroid = [[],0.0]
        for i in data:

            # data point "i" is already a centroid, let's ignore it
            if(i in centroids): continue

            # find the closest centroid
            best_centroid_distance = sys.maxsize
            for j in centroids:

                # NOTE: there is no need for the square root (the distance will be squared in the next step)
                i_j_distance = sum([(i[k]-j[k])**2 for k in range(NUM_FEATURES)])

                if(i_j_distance<best_centroid_distance): best_centroid_distance = i_j_distance

            # check if it is (so far) the point with the biggest squared distance to its nearest centroid
            if(best_centroid_distance**2>next_centroid[1]): next_centroid = [i,best_centroid_distance**2]
                
        centroids.append(next_centroid[0])

    return(centroids)

def kmeans_pp(data, k): # main function, applies the K-Means++ algorithm on "data" with "k" clusters

    total_position_changes = -1.0
    control = True

    # initialize "k" centroids
    centroids = centroid_initialization(data,k)

    while(control or total_position_changes>STOP_CRITERIUM):

        assignments = []
        control = False
        total_position_changes = 0.0
        most_distant_point = [0,0.0]

        #######################################################################################################
        # CLUSTER ASSIGNMENT
        #######################################################################################################
        for point_idx,point in enumerate(data):
            best_centroid = [0,-1]
            for centroid_idx,centroid in enumerate(centroids):
                
                # compute the euclidian distance of this centroid and the data point
                centroid_distance = np.math.sqrt(sum([(centroid[i]-point[i])**2 for i in range(NUM_FEATURES)]))
                
                # if better, save the centroid
                if(best_centroid[1]==-1 or centroid_distance<best_centroid[1]):

                    # see it it is the furthest point from its centroid (so far)
                    if(centroid_distance>most_distant_point[1]):
                        most_distant_point = [point_idx,centroid_distance]

                    best_centroid = [centroid_idx,centroid_distance]

            # save the assignment
            assignments.append([point_idx,best_centroid[0]])

        ###############################################################################################################
        # CENTROID UPDATE
        ###############################################################################################################
        for centroid_idx,centroid in enumerate(centroids):
            new_position = []

            # get the points assigned to this centroid
            assigned_points = list(map(lambda x : data[x[0]],list(filter(lambda x : x[1]==centroid_idx, assignments))))

            if(len(assigned_points)==0):
                # assign the most distant point (relative to its current centroid) to this centroid
                assigned_points = [data[most_distant_point[0]]]

            # average the assigned points and get the new position for this centroid
            for i in range(NUM_FEATURES):
                new_position.append(sum(list(map(lambda x : x[i],assigned_points)))/len(assigned_points))

            total_position_changes += sum([abs(new_position[i]-centroid[i]) for i in range(NUM_FEATURES)])
            
            # move the centroid
            centroids[centroid_idx] = new_position

    return(centroids,assignments)

if __name__ == "__main__":

    centroids_and_assignments = {}

    ##########################################################################################################
    # APPLY THE K-MEANS++ ALGORITHM
    ##########################################################################################################
    if(PCA is None): file_name = "credit_card_data_processed.csv"
    else: file_name = "pca/credit_card_data_pca_.csv".replace(".csv",str(PCA) + ".csv")

    with open(file_name,"r") as file:
        data = list(map(lambda x : list(map(lambda y : float(y),x)),list(csv.reader(file,delimiter=","))[1:]))

        for k in range(1,K_MAX+1):
            print("KMEANS (K=" + str(k) + ")")
            centroids, assignments = kmeans_pp(data,k)
            centroids_and_assignments.update({k: [centroids,assignments]})
        
    ######################################################################################################
    # DUMP THE CENTROIDS AND ASSIGNMENTS TO A FILE
    ######################################################################################################
    with open("centroids_and_assignments.pkl","wb") as file:
        dump(centroids_and_assignments,file)