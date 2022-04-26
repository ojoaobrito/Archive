import os, sys, csv
import numpy as np
import matplotlib.pyplot as plt

NUM_CLUSTERS = 2
LEARNING_RATE =  0.01
INITIAL_LEARNING_RATE = LEARNING_RATE
NEIGHBOURHOOD_RADIUS = 0.01
NUM_EPOCHS =  10
T_2 = 2

class Neuron():

    def __init__(self,initialize):

        self.weights = np.asarray([initialize[0],initialize[1]])

    def update(self, sample):

        for i in range(len(self.weights)):
            self.weights[i] += LEARNING_RATE * (sample[i] - self.weights[i])

class LVQ():

    def __init__(self,initialize): # class constructor
        
        self.neurons = [Neuron(initialize[i]) for i in range(NUM_CLUSTERS)]
        
    def euclidian_distance(self,sample,neuron):

        aux = 0.0

        for i in range(len(sample)):
            aux += (sample[i] - neuron.weights[i])**2

        return(np.math.sqrt(aux))

    def fit(self,samples,num_epoch):

        global LEARNING_RATE

        winner = 0
        best_distance =  1000000000.0
        neuron_idx = 0
        loss_aux = 0.0

        for sample in samples:

            # select the winner
            for i in range(NUM_CLUSTERS):
                distance =  self.euclidian_distance(sample,self.neurons[neuron_idx])
                if(distance<best_distance):
                    winner = neuron_idx
                    best_distance = distance
                
                neuron_idx += 1

            # update the winner
            self.neurons[winner].update(sample)

            # update the loss auxiliary variable
            loss_aux += best_distance**2
            
            # reset the variables
            winner = 0
            best_distance =  1000000000.0
            neuron_idx = 0
            LEARNING_RATE -= INITIAL_LEARNING_RATE * np.math.exp(num_epoch/T_2)
        sys.exit()
        return(loss_aux/len(samples))
        
if __name__ == "__main__":

    x_values = []
    y_values = []

    with open("exemplo2.dat","r") as file:

        reader = list(csv.reader(file,delimiter=" "))

        # READ THE TRAINING DATA
        # -------------------------------------------------------
        samples = []
        for i in reader:
            samples.append(list(map(lambda x : float(x),i[:-1])))
            # samples[-1].append(int(i[-1]))
            x_values.append(float(i[0]))
            y_values.append(float(i[1]))
        # -------------------------------------------------------

        lvq =  LVQ(samples[:NUM_CLUSTERS])

        # TRAIN THE MODEL
        # --------------------------------------------------------------------------------------------------------
        for epoch in range(NUM_EPOCHS): # train (show the progress every 1000 epochs)

            loss = lvq.fit(samples,epoch)

            print("EPOCH: " + str(epoch+1) + "/" + str(NUM_EPOCHS) +  " - LOSS: " + str(loss))
        # --------------------------------------------------------------------------------------------------------

        # show the graph
        plt.scatter(x_values,y_values,c='r')
        for i in range(NUM_CLUSTERS):
            plt.scatter(lvq.neurons[i].weights[0],lvq.neurons[i].weights[1],c='b')
        plt.title("Graph")
        plt.xlabel("Feature 1")
        plt.ylabel("Feature 2")
        plt.xlim(-1.8,1.8)
        plt.ylim(-1.8,1.8)
        plt.show()
        print(list(map(lambda x:x.weights,lvq.neurons)))