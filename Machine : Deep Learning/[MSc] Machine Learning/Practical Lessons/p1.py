import os, sys
import numpy as np
import matplotlib.pyplot as plt
import math

# QUESTION 1
# -----------------------------------
def basic_ops(a,b):

    # addition
    print(a+b)

    # subtraction
    print(a-b)

    # division
    if(b!=0): print(a/b)
    else: print("Can't divide by 0!")

    # multiplication
    print(a*b)

    # exponentiation
    print(a**b)
# -----------------------------------

# QUESTION 2
# ----------------------------------------
def matrix_sum(matrix, dimension):

    return(np.sum(matrix, axis=dimension))
# ----------------------------------------

# QUESTION 3
# ------------------------------------------------------------------
def count_elements(a, interval):

    return(np.count_nonzero( (a > interval[0]) & (a<=interval[1]) ))
# ------------------------------------------------------------------

# QUESTION 4
# ---------------------------------------
def plot_interval(a,b):

    def f(x): return(((x*x)*np.cos(2*x)))

    x = np.arange(a,b,0.01)
    line, = plt.plot(x, f(x), lw=2)
    plt.show()
# ---------------------------------------

# QUESTION 5
# -------------------------------
def solve_system(a,b):

    return(np.linalg.solve(a, b))
# -------------------------------

# QUESTION 6
# -----------------------------------------------------------
def fill_matrix():

    array = []
    while(True):
        
        try: # to stop, insert anything other than a number

            number = float(input("> "))
            array.append(number)
        
        except: break

    array_np = np.asarray(array).reshape((2,(len(array)//2)))
    return(np.asmatrix(array_np))
# -----------------------------------------------------------

# QUESTION 7
# ---------------------------------------------------------
def random_matrix(a,b):

    print(np.random.uniform(low=0.0, high=1.0, size=(a,b)))
# ---------------------------------------------------------

# QUESTION 8
# ---------------------------------
def matrix_symmetry(matrix):

    print((matrix==matrix.T).all())
# ---------------------------------

# QUESTION 9
# --------------------------
def matrix_trace(matrix):

    return(np.trace(matrix))
# --------------------------

# QUESTION 10
# -------------------------------
def invert_matrix(matrix):

    return(np.linalg.inv(matrix))
# -------------------------------

# QUESTION 11
# ---------------------------------
def inner_product(array1,array2):

    return(np.inner(array1,array2))
# ---------------------------------

# QUESTION 12
# ---------------------------------
def outer_product(array1,array2):

    return(np.outer(array1,array2))
# ---------------------------------

if __name__ == "__main__":

    # VARIABLE DECLARATION
    # -----------------------------
    matrix = [[1,2,3,4,5],
              [8,7,0,2,5],
              [9,3,2,3,3]]

    symmetric = np.array([[1,7,3],
                         [7,4,-5],
                         [3,-5,6]])
    # -----------------------------

    # SOLVE THE QUESTIONS
    # -------------------------------------------------------
    # question 1
    basic_ops(2,3)

    # question 2
    matrix_np = np.asarray(matrix)
    print(matrix_sum(matrix_np,1))

    # question 3
    print(count_elements(matrix_np,(1,5)))

    # question 4
    # plot_interval(0,100)

    # question 5
    a = np.array([[4,-5], [-2,3]])
    b = np.array([-13,9])
    print(solve_system(a,b))

    # question 6
    # print(fill_matrix())

    # question 7
    random_matrix(3,3)

    # question 8
    matrix_symmetry(symmetric)

    # question 9
    print(matrix_trace(symmetric))

    # question 10
    print(invert_matrix(symmetric))

    # question 11
    print(inner_product(np.array([1,2,3]),np.array([0,1,0])))

    # question 12
    print(outer_product(np.array([1,2,3]),np.array([0,1,0])))
    # -------------------------------------------------------