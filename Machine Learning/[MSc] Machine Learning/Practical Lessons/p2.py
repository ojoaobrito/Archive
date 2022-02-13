import os, sys
import csv
import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import inv

x_values = []
y_values = []
NUM_HYPOTHESIS = 100000

def loss_function(model, x, y):

    loss = 0.0

    for i in range(len(x)):
        loss += ((model[0] * x[i] + model[1]) - y[i])**2

    return(loss/len(x))

def brute_force():

    best_model = []
    best_loss = 1000000.0

    x_plot = []
    y_plot = []

    for i in range(NUM_HYPOTHESIS):

        x_plot.append(i+1)

        model_aux = [np.random.uniform(0.0,1.0),np.random.uniform(300,500)]
        loss = loss_function(model_aux,x_values,y_values)
        if(loss<best_loss):
            best_model = model_aux
            best_loss = loss
        
        if(i%1000):
            print(best_model)
            print(best_loss)

        y_plot.append(best_loss)

    return(x_plot,y_plot,best_loss,best_model)

def closed_form():

    new_x = [[i,1] for i in x_values]

    X = np.asarray(new_x).reshape((len(new_x),2))
    y = np.asarray(y_values).reshape((len(y_values),1))
    
    return(np.matmul(np.matmul(inv(np.matmul(X.transpose(),X)), X.transpose()),y))


def gradient_descent():

    def gradient(thetas,theta):
        
        value = 0.0

        if(theta==0):
    
            for i in range(len(x_values)):
                value += ((thetas[0] * x_values[i]) + thetas[1] - y_values[i]) * x_values[i]

            return(value/len(x_values))

        elif(theta==1):

            for i in range(len(x_values)):
                value += ((thetas[0] * x_values[i]) + thetas[1] - y_values[i])

            return(value/len(x_values))

    thetas = [np.random.uniform(0.0,1.0),np.random.uniform(300,500)]
    num_epochs = 1000000
    learning_rate = 0.0000001

    for i in range(num_epochs):

        for j in range(len(thetas)):
            thetas[j] -= learning_rate * gradient(thetas,j)

        print(loss_function(thetas,x_values,y_values))

    return(thetas)

# read the data
with open("pizza.csv", "r") as file:
    content = list(csv.reader(file,delimiter=","))
    for i in range(1,len(content)):
        x_values.append(float(content[i][0]))
        y_values.append(float(content[i][1]))

# x_plot,y_plot,brute_force_loss,brute_force_model = brute_force()
#plt.plot(x_plot,y_plot)
#plt.show()
'''
print("\nBRUTE FORCE")
print(brute_force_model)'''

print("\nCLOSED FORM")
print(closed_form())
'''
print("\nGRADIENT DESCENT")
print(gradient_descent())'''