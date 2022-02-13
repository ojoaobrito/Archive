import os, sys, csv
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.lines as mlines
from pickle import load
from kmeans_pp import kmeans_pp

###################################
# HYPERPARAMETERSp
###################################
K_MAX = 8
NORMALIZED_DATA = False
PCA = 75 # 75; 90; 95 or None
ELBOW = False
SILHOUETTE = False
PLOT_3D = True

if(not NORMALIZED_DATA):
    ELBOW_DOT_SIZE = 10
    if(PCA==75): NUM_FEATURES = 3
    elif(PCA==90): NUM_FEATURES = 4
    elif(PCA==95): NUM_FEATURES = 5
    else: NUM_FEATURES = 17

else:
    ELBOW_DOT_SIZE = 70
    if(PCA==75): NUM_FEATURES = 3
    elif(PCA==90): NUM_FEATURES = 5
    elif(PCA==95): NUM_FEATURES = 7
    else: NUM_FEATURES = 17

SILHOUETTE_DOT_SIZE = 30

###############################################################################################################################################
# SILHOUETTE METHOD
###############################################################################################################################################
def silhouette_score(k, data, assignments): # auxiliary function, uses the silhouette method to find the optimal value for "k"

    silhouette_scores = {}
    silhouette_score = 0.0

    # retrieve the points in every cluster
    points_cluster = {}
    for i in range(k):
        points_cluster.update({i: list(map(lambda x : x[0],list(filter(lambda x : x[1]==i,assignments))))})

    for idx,i in enumerate(data):

        ##############################################################################################################################
        # COMPUTE "a(i)" (MEAN DISTANCE BETWEEN DATA POINT "i" ALL OTHER DATA POINTS IN THE SAME CLUSTER)
        ##############################################################################################################################
        # get "i"'s cluster
        for key,v in points_cluster.items():
            if(idx in v): 
                i_cluster = key
                break
    
        # get every data point that belongs to the same cluster as "i"
        points_same_cluster = points_cluster[i_cluster]
        
        if(len(points_same_cluster)==1): a_i = 0

        else:
            # compute the distances between "i" and the points in its cluster
            i_d_distances = sum([np.math.sqrt(sum([(i[j]-data[k][j])**2])) for k in points_same_cluster for j in range(NUM_FEATURES)])

            # compute "a(i)"
            a_i = i_d_distances/(len(points_same_cluster)-1)

        #######################################################################################################################################
        # COMPUTE "b(i)" (MINIMUM DISTANCE BETWEEN DATA POINT "i" AND ALL POINTS OF A CLUSTER TO WHICH "i" DOES NOT BELONG)
        #######################################################################################################################################
        # get the other clusters
        other_clusters = list(filter(lambda x : x!=i_cluster, [k for k in points_cluster.keys()]))
        
        # compute "b(i)"
        b_i = sys.maxsize
        for c in other_clusters:
            # get every data point that belongs to the cluster "c"
            points_cluster_c = points_cluster[c]
            
            # compute the distances between "i" and the points in the cluster "c"
            aux = sum([np.math.sqrt(sum([(i[j]-data[k][j])**2])) for k in points_cluster_c for j in range(NUM_FEATURES)])/len(points_cluster_c)

            if(aux<b_i): b_i = aux

        ###############################################################
        # FINALLY, COMPUTE "s(i)" (SILHOUETTE VALUE FOR DATA POINT "i")
        ###############################################################
        s_i = (b_i - a_i)/max(a_i,b_i)

        # update the silhouette score
        silhouette_score += s_i
    
    return(silhouette_score/len(data))

#############################################################################################################
# ELBOW METHOD
#############################################################################################################
def distortion(data, centroids, assignments): # loss function, computes either the distortion or inertia loss

    result = 0.0

    for i in assignments:
        result += sum([(data[i[0]][j]-centroids[i[1]][j])**2 for j in range(NUM_FEATURES)])

    return(result/len(data))

def elbow_method(losses): # auxiliary function, uses the elbow method to find the optimal value for "k"

    # parameters for the imaginary line
    p1 = (1,losses[0])
    p2 = (K_MAX,losses[K_MAX-1])
    p2_p1_distance = ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

    best_k = [0,0.0]
    distances = []
    projected_points = []

    for idx,l in enumerate(losses):
        p3 = (idx+1,l)

        # project the point onto the imaginary line
        u = ((p3[0] - p1[0])*(p2[0] - p1[0]) + (p3[1] - p1[1])*(p2[1] - p1[1]))/p2_p1_distance
        projected_point = (p1[0] + u * (p2[0] - p1[0]),p1[1] + u * (p2[1] - p1[1]))

        # calculate the distance of this loss point to the projected one
        current_distance = np.math.sqrt((p3[0]-projected_point[0])**2 + (p3[1]-projected_point[1])**2)

        # save the best (most distant) point
        if(current_distance>best_k[1]):
            best_k = [idx+1,current_distance]

        distances.append(current_distance)
        projected_points.append(projected_point)

    return(best_k, distances, projected_points)

if __name__ == "__main__":

    if(PCA is None): file_name = "credit_card_data_processed.csv"
    else: file_name = "pca/credit_card_data_pca_.csv".replace(".csv",str(PCA) + ".csv")

    # load the data
    with open(file_name,"r") as file:
        data = list(map(lambda x : list(map(lambda y : float(y),x)),list(csv.reader(file,delimiter=","))[1:]))

    # load the results from the K-Means algorithm
    with open("centroids_and_assignments.pkl","rb") as file:
        centroids_and_assignments = load(file)

    ########################################################################################################################################
    # COMPUTE AND PLOT THE ELBOW METHOD SCORES
    ########################################################################################################################################
    if(ELBOW):
    
        elbow_losses = []

        # compute the distortion loss for every value of "k" tested
        for i in centroids_and_assignments.values():
            if(not NORMALIZED_DATA): elbow_losses.append(distortion(data,i[0],i[1])/10000000)
            else: elbow_losses.append(distortion(data,i[0],i[1]))

        # display the distortion values
        print("Distortion:")
        for idx,i in enumerate(elbow_losses):
            print("K=" + str(idx+1) + ": " + str(round(i,2)))
        
        # call the elbow method
        elbow_best_k, distances, projected_points = elbow_method(elbow_losses)
            
        plt.rcParams['axes.axisbelow'] = True
        
        # plot an imaginary line
        p1 = (1,elbow_losses[0])
        p2 = (K_MAX,elbow_losses[K_MAX-1])
        plt.plot([p1[0],p2[0]],[p1[1],p2[1]],"--",color="royalblue",zorder=2)

        # scatter the points
        first = True
        for idx,l in enumerate(elbow_losses):

            original_point = (idx+1,l)
            projected_point = projected_points[idx]

            # plot the loss points
            if((idx+1)==elbow_best_k[0]): 
                # plot a line between this loss point and the projected one on the imaginary line
                plt.plot([original_point[0],projected_point[0]],[original_point[1],projected_point[1]],"--",color="royalblue",zorder=1)
                
                plt.scatter(idx+1,l,color="g",marker="o",s=distances[idx]*ELBOW_DOT_SIZE,zorder=4)
            else: 
                # plot a line between this loss point and the projected one on the imaginary line
                plt.plot([original_point[0],projected_point[0]],[original_point[1],projected_point[1]],"--",color="lightsteelblue",zorder=1)
                
                plt.scatter(idx+1,l,color="r",marker="o",s=distances[idx]*ELBOW_DOT_SIZE,zorder=4)
            
            # add some informative text
            if(idx==0 or idx==(K_MAX-1)): continue
            plt.annotate(str(round(distances[idx],3)),(idx+1,l),size=6)

        # plot a line to join the points
        plt.plot([k for k in range(1,K_MAX+1)],elbow_losses,color="grey",zorder=3)

        title = "Elbow method for K-Means++ - " + str(NUM_FEATURES) + " Features"

        if(NORMALIZED_DATA): title += " - Norm."
        if(not PCA is None): title += " - PCA " + str(PCA) + "%"
            
        plt.title(title)
        plt.xlabel("Number of clusters (K)")
        if(not NORMALIZED_DATA): plt.ylabel("Distortion value (J) * 1e-7")
        else: plt.ylabel("Distortion value (J)")
        
        # create custom handles for the legend
        optimal_k = mlines.Line2D([], [], color='green', marker='o', linestyle='None', markersize=5, label="Optimal K")
        suboptimal_k = mlines.Line2D([], [], color='red', marker='o', linestyle='None', markersize=5, label="Suboptimal K")

        plt.legend(handles=[optimal_k,suboptimal_k], loc="best")
        plt.grid()
        #plt.axis("equal")
        plt.show()
    
    #######################################################################################################################
    # COMPUTE AND PLOT THE SILHOUETTE METHOD SCORES
    #######################################################################################################################
    if(SILHOUETTE):
        silhouette = []

        for k,v in centroids_and_assignments.items():
            if(k==1): continue
            print("SILHOUETTE SCORE (K=" + str(k) + ")")
            silhouette.append(silhouette_score(k,data,v[1]))

        silhouette_best_k = silhouette.index(max(silhouette))+2

        # display the silhouette values
        print("Silhouette:")
        for idx,i in enumerate(silhouette):
            print("K=" + str(idx+2) + ": " + str(round(i,2)))

        plt.rcParams['axes.axisbelow'] = True
        
        for idx,i in enumerate(silhouette):
            if((idx+2)==silhouette_best_k): plt.scatter(idx+2,i,color="g",marker="o",s=i*SILHOUETTE_DOT_SIZE,zorder=2)
            else: plt.scatter(idx+2,i,color="r",marker="o",s=i*SILHOUETTE_DOT_SIZE,zorder=2)

        # plot a line to join the points
        plt.plot([k for k in range(2,K_MAX+1)],silhouette,color="grey",zorder=1)

        plt.title("Silhouette method for K-Means - " + str(NUM_FEATURES) + " Features")
        plt.xlabel("Number of clusters (K)")
        plt.ylabel("Silhouette score (S)")

        # create custom handles for the legend
        optimal_k = mlines.Line2D([], [], color='green', marker='o', linestyle='None', markersize=5, label="Optimal K")
        suboptimal_k = mlines.Line2D([], [], color='red', marker='o', linestyle='None', markersize=5, label="Suboptimal K")

        plt.legend(handles=[optimal_k,suboptimal_k], loc="best")
        plt.grid()
        #plt.axis("equal")
        plt.show()

    #########################################################################################################################################
    # VISUALIZE THE DATA POINTS AND THE CLUSTERS
    #########################################################################################################################################
    if(PLOT_3D):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        with open("pca/credit_card_data_pca_75.csv","r") as file:
            content = list(map(lambda x : x,list(map(lambda x : list(map(lambda y : float(y),x)),list(csv.reader(file,delimiter=","))[1:]))))
            
            # run the KMeans algorithm again, but know knowing the optimal number of clusters
            centroids, assignments = kmeans_pp(content,elbow_best_k[0])

            colors = ["red","cornflowerblue","green","yellow","magenta","aqua","chocolate","purple","blue"]
            
            # scatter the centroids
            for idx,c in enumerate(centroids):
                ax.scatter(c[0],c[1],c[2],marker="o",color="black",s=30)

            # scatter and color the data points
            for idx,value in enumerate(content):
                #if(idx%10!=0): continue
                color = colors[list(filter(lambda x : x[0]==idx,assignments))[0][1]]
                ax.scatter(value[0], value[1], value[2], marker="o", color=color)

        ax.set_title("3D visualization of K-Means - " + str(NUM_FEATURES) + " Features")
        ax.set_xlabel("Dimension 1")
        ax.set_ylabel("Dimension 2")
        ax.set_zlabel("Dimension 3")

        plt.show()