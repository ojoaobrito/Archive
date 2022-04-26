import os, sys
from random import uniform

###############################################################
## GENETIC ALGORITHM TO SOLVE THE FOLLOWING SYSTEM OF EQUATIONS
###############################################################
# | 2x + y = 9
# | x*x - y = 2
# THE REAL SOLUTION IS (x = , y = )

NUM_INDIVIDUALS = 10
INIT_RANGE = (-20,20)
NUM_FEATURES = 2

class AG: # class to deal with cromossomes (genetic algorithm)

    def __init__(self,num_individuals,init_range,num_features): # class constructor
        
        # initialize the population
        self.individuals = [ [id+1] + [uniform(init_range[0],init_range[1]) for _ in range(num_features)] for id in range(num_individuals)]

    def fitness_function(self, cromossome): # fitness function that evaluates how good (or bad) a cromossome is

        first_equation_diff = (2*cromossome[0] + cromossome[1]) - 9
        second_equation_diff = (cromossome[0]**2 - cromossome[1]) - 2

        return(first_equation_diff + second_equation_diff)

    def sort_fitness_values(self, fitness_values):
        
        return(fitness_values.copy().sort(key = lambda x : x[1]))

    def proportional_selection(self):

        # compute the fitness function for every cromossome
        fitness_values = []
        for i in self.individuals:
            fitness_values.append(self.fitness_function(i[1:]))

        # compute the proportional probabilities of every cromossome
        probabilities = []
        denominator = sum(fitness_values)
        for i in range(self.individuals):
            probabilities.append(fitness_values[i]/denominator)

        # choose a cromossome (roulette algorithm)
        epsilon = uniform(0,1)
        i = 1
        s = probabilities[i-1]

        while(s<epsilon):
            i += 1
            s = s + probabilities[i-1]

        # save the best individual (the index, rather)
        self.best_individual_index = i-1

    def show_best_cromossome(self):

        print("Best cromossome: " + ",".join(self.individuals[self.best_individual_index][1:]))

    def show_all_cromossomes(self):

        for i in self.individuals:
            print("ID " + i[0] + ", cromossomes (" + i[1] + ", " + i[2] + ")")

if __name__ == "__main__":

    ag = AG(NUM_INDIVIDUALS,INIT_RANGE,NUM_FEATURES)