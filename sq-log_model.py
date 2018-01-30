# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
from scipy.stats import norm

##############--FUNCTION DECLARATIONS--################

# constructing a new array with all the values of y hat given the model
def calculate_y_hat(val, n) :
    y_hat_final = []
    while n >= 0:
        y_app = x1[4-n]*val[0] + x2[4-n]*val[1] + val[2]
        y_hat_final.append(y_app)
        n = n - 1
    return y_hat_final

# calculating the log-likelihood of the models
def Log_Likelihood(val, std) :
    L = []
    for x in val :
        error = norm.pdf(x, 0, std)
        ln_error = np.log(error)
        L = np.append(L, ln_error)
    return (np.sum(L))

# adding some space, trying to save some time
def space() :
    print(" ");print(" ");print(' ')
    return

# calculating the standard error of every single observation
def error(y_hat, y) :
    error = y - y_hat
    return error    

# standard deviation assuming the errors are normally distributed with a mean 
# of '0'
def std(sse, n) :
    s = (sse/(n-1))**(1/2)
    return s

# introduction for the model number and the type of regression
def intro(name, val) :
    print()
    if val == 1 :
        print("This is " + name + " linear regression")
    else :
        print("This is " + name + " Log likelihood regression")
    print()
#######################################################


# we are provided two observations in our training set
x1 = np.array([12,14,16,20,24])
x2 = np.array([4,3,6,5,2])
# y is denoted as the label
y = np.array([50,53,67,70,63])

# Function for Model 1 y-hat
y_beta_1 = np.array([1.5, 5, 12])
# Function for Model 2 y-hat
y_beta_2 = np.array([2.0, 4, 10])

# Gets the size of the array (5)
c = x1.size - 1    
print(" ")
print("We calculate the y hat of each model and the standard error.")
print("We follow by calculating the sum of squared errors, the standard "
      "deviation and the log likelihood. ")    

#model 1

intro("model 1", 1)

# makes all the calculations respectively for model 1 (refer to functions)
y_mod_1 = calculate_y_hat(y_beta_1, c)
error_mod_1 = error(y_mod_1, y)
sse_1 = np.sum(error_mod_1**2)
std_1 = std(sse_1, c+1)

# prints the data in an orderly fashion
print("the y hat of model 1 is :") 
print(y_mod_1)
print("and the error is: ")
print(str(error_mod_1) + " with the sum of squared errors: " + str(sse_1))
print("the standard deviation is :" + str(std_1))
print("the log likelihood is: " + str(Log_Likelihood(error_mod_1, std_1)))

#model 2

intro("model 2", 1)

# makes all the calculations respectively for model 2 (refer to functions)
y_mod_2 = calculate_y_hat(y_beta_2, c)
error_mod_2 = error(y_mod_2, y)
sse_2 = np.sum(error_mod_2**2)
std_2 = std(sse_2, c+1)

# prints the data in an orderly fashion
print("the y hat of model 1 is :") 
print(y_mod_2)
print("and the error is: ")
print(str(error_mod_2) + " with the sum of squared errors: " + str(sse_2))
print("the standard deviation is :" + str(std_2))
print("the log likelihood is: " + str(Log_Likelihood(error_mod_2, std_2)))

space()

print("It can be observed that the first model describes the data more"
      " accurate than model 2. ")
print ("This can be seen by comparing the sum of the"
      " the squared errors and comparing the log likelihood of the two mode"
      "ls. ")




