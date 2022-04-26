import os,sys
import numpy as np
import csv
import matplotlib.pyplot as plt
import math

LEARNING_RATE = 0.005 # 0.005 for "exemplo1.dat"; 0.05 for "exemplo1N.dat"
BIAS_LEARNING_RATE = 0.005 # 0.005 for "exemplo1.dat"; 0.05 for "exemplo1N.dat"
NUM_EPOCHS = 1500000 # 1500000 for "exemplo1.dat"; 35000 for "exemplo1N.dat"
SIGMOID_LAMBDA = 1

# SIMPLE NEURON CLASS
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class Neuron():

    def __init__(self, num_inputs, seed, act_fun_in, loss_fun_in): # class constructor

        # initialize the random generator
        np.random.seed(seed)

        # main variables
        self.weights = np.random.uniform(low=-0.1, high=0.1, size=num_inputs+1)
        self.act_fun_aux = act_fun_in
        self.loss_fun_aux = loss_fun_in
        self.in_product = 0.0

        # plot variables
        self.line1 = None
        self.line2 = None
        self.line3 = None
        self.axes = None
    
    def act_fun(self, in_product): # call the chosen activation function (applied on the internal product)

        if(self.act_fun_aux=="sigmoid"):
            return(1/(1+(np.exp(-SIGMOID_LAMBDA*in_product))))

        elif(self.act_fun_aux=="tanh"):
            return(np.exp(in_product)-np.exp(-in_product))/(np.exp(in_product)+np.exp(-in_product))
        
        elif(self.act_fun_aux=="linear"):
            return(in_product)
        
        elif(self.act_fun_aux=="relu"):
            return(max(0,in_product))

        elif(self.act_fun_aux=="step"):
            if(in_product<0): return(-1)
            else: return(1)
        
        elif(self.act_fun_aux=="ramp"):
            if(in_product<-0.5): return(-1)
            elif(in_product>0.5): return(1)
            else: return(in_product)

    def calculate(self, inputs): # activate the neuron (according to the chosen activation function)
        
        self.in_product = self.weights[0]
        for i,x in enumerate(inputs): self.in_product += self.weights[i+1]*x
        return(self.act_fun(self.in_product))

    def loss(self, samples): # compute the loss (on the given samples)

        loss_aux = 0.0

        for sample in samples:

            predicted = self.calculate(sample[:-1])

            if(self.loss_fun_aux=="mse"):
                loss_aux += (sample[-1] - predicted)**2
            elif(self.loss_fun_aux=="cross-entropy"):
                loss_aux += (-sample[-1] * math.log10(predicted)) - ((1-sample[-1]) * math.log10(1 - predicted))

        return(loss_aux/len(samples))

    def act_fun_derivative(self, in_product): # return the derivative of the chosen activation function

        if(self.act_fun_aux=="sigmoid"):
            return(self.act_fun(in_product) * (1 - self.act_fun(in_product)))

        elif(self.act_fun_aux=="tanh"):
            return(1 - (self.act_fun(in_product)**2))
        
        elif(self.act_fun_aux=="linear"):
            return(1)
        
        elif(self.act_fun_aux=="relu"):
            if(in_product>0): return(1)
            else: return(0)

        elif(self.act_fun_aux=="step"):
            return(0)
        
        elif(self.act_fun_aux=="ramp"):
            if(in_product<-0.5 or in_product>0.5): return(0)
            else: return(1)

    def loss_fun_derivative(self, real, predicted): # return the derivative of the chosen loss function

        if(self.loss_fun_aux=="mse"):
            return(-2 * (real - predicted))
        
        elif(self.loss_fun_aux=="cross-entropy"):
            return((-real * (1/predicted)) - ((1-real) * (1/(1 - predicted))))

    def fit(self, samples, mode): # train the neuron
        
        if(mode=="stochastic"): # stochastic mode

            for sample in samples:
                for i in range(len(self.weights)):
                    if(i==0):
                        error_variation = (self.loss_fun_derivative(sample[-1], self.calculate(sample[:-1])) * self.act_fun_derivative(self.in_product) * 1)
                        self.weights[i] = self.weights[i] - (BIAS_LEARNING_RATE * error_variation)
                    else:
                        error_variation = (self.loss_fun_derivative(sample[-1], self.calculate(sample[:-1])) * self.act_fun_derivative(self.in_product) * sample[i-1])
                        self.weights[i] = self.weights[i] - (LEARNING_RATE * error_variation)
        
        elif(mode=="batch"): # batch mode

            error_variations = [0.0 for _ in range(len(self.weights))]

            # get the error variation per weight across every sample
            for sample in samples:
                for i in range(len(self.weights)):
                    if(i==0):
                        error_variations[i] += (self.loss_fun_derivative(sample[-1], self.calculate(sample[:-1])) * self.act_fun_derivative(self.in_product) * 1)
                    else:
                        error_variations[i] += (self.loss_fun_derivative(sample[-1], self.calculate(sample[:-1])) * self.act_fun_derivative(self.in_product) * sample[i-1])

            # update the weights
            for i in range(len(self.weights)):
                if(i==0):
                    self.weights[i] = self.weights[i] - (BIAS_LEARNING_RATE * (error_variations[i]/len(samples)))
                else:
                    self.weights[i] = self.weights[i] - (LEARNING_RATE * (error_variations[i]/len(samples)))

    def show_weights(self): # display the current weights

        print(self.weights)

    def read_weights(self, file_name): # import weights from a file

        with open(file_name,"r") as file:
            reader = list(csv.reader(file,delimiter=" "))
            reader = list(map(lambda x : float(x),reader[0]))
            self.weights = np.asarray(reader)

    def write_weights(self, file_name): # write the weights to a file

        with open(file_name,"w") as file:
            for i in range(len(self.weights)):
                if(i==(len(self.weights)-1)): file.write(str(self.weights[i]))
                else: file.write(str(self.weights[i]) + " ")

    def show_plot(self, samples, update): # show the plot with the proposed decision boundary

        if(update): # update the line

            self.line3[0].remove()

            # plot the line
            x = np.linspace(-3.5,3.5,100)
            y = (-(self.weights[0]/self.weights[2]) / (self.weights[0]/self.weights[1])) * x + (-(self.weights[0]/self.weights[2]))
            self.line3 = self.axes.plot(x, y, 'g')
            plt.draw()
            plt.pause(1e-17)

        else:

            x_class1 = []
            y_class1 = []

            x_class2 = []
            y_class2 = []

            for sample in samples:
                if(sample[-1]==0):
                    x_class1.append(sample[0])
                    y_class1.append(sample[1])
                else:
                    x_class2.append(sample[0])
                    y_class2.append(sample[1])

            plt.show()
 
            self.axes = plt.gca()

            # for "exemplo1.dat"
            self.axes.set_xlim(1, 2)
            self.axes.set_ylim(-5, 70)

            # for "exemplo1N.dat"
            # self.axes.set_xlim(-1.5, 1.5)
            # self.axes.set_ylim(-1.5, 1.5)

            self.line1 = self.axes.scatter(x_class1, y_class1, c='b')
            self.line2 = self.axes.scatter(x_class2, y_class2, c='r')

            # plot the line
            x = np.linspace(-3.5,3.5,100)
            y = (-(self.weights[0]/self.weights[2]) / (self.weights[0]/self.weights[1])) * x + (-(self.weights[0]/self.weights[2]))
            self.line3 = self.axes.plot(x, y, c='g')
            self.axes.grid()
            plt.title('Perceptron Training')
            plt.xlabel('Feature 1')
            plt.ylabel('Feature 2')

    def keep_plot(self): # keep the plot on the screen

        plt.show()
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":

    with open("exemplo1.dat","r") as file:

        reader = list(csv.reader(file,delimiter=" "))
        neuron = Neuron(2,53217,"sigmoid","mse") # neuron = Neuron(2,53217,"sigmoid","mse") for "exemplo1.dat"; neuron = Neuron(2,10,"sigmoid","mse") for "exemplo1N.dat" 

        initial_weights = np.copy(neuron.weights)

        # READ THE TRAINING DATA
        # -------------------------------------------------------
        samples = []
        for i in reader:
            samples.append(list(map(lambda x : float(x),i[:-1])))
            samples[-1].append(int(i[-1]))
        # -------------------------------------------------------

        neuron.show_plot(samples,False)

        # TRAIN THE MODEL
        # --------------------------------------------------------------------------------------------------------
        for epoch in range(NUM_EPOCHS): # train (show the progress every 1000 epochs)

            if((epoch%1000)==0):
                print("EPOCH: " + str(epoch+1) + "/" + str(NUM_EPOCHS) +  " - LOSS: " + str(neuron.loss(samples)))
                
            neuron.fit(samples,"stochastic")
            
            if((epoch%1000)==0):
                neuron.show_plot(samples,True)
        # --------------------------------------------------------------------------------------------------------

        # MAKE PREDICTIONS
        # ---------------------------------------------------------------------------------------------------------------------
        for i in reader:
            print("PREDICTED: " + str(neuron.calculate(list(map(lambda x : float(x),i[:-1])))) + " - REAL: " + str(int(i[-1])))
        # ---------------------------------------------------------------------------------------------------------------------
        
        # FINAL TOUCHES
        # --------------------------------
        print("\n> Initial weights")
        print(initial_weights)
        print("\n --- \n")
        print("\n> Final weights")
        neuron.show_weights()
        neuron.show_plot(samples,"update")
        neuron.keep_plot()
        # --------------------------------