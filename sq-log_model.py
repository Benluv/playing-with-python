# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np


##############--FUNCTION DECLARATIONS--################

# constructing a new array with all the values of y hat given the model
def calculate_y_hat(val, n) :
    y_hat_final = []
    while n >= 0:
        y_app = x1[4-n]*val[0] + x2[4-n]*val[1] + val[2]
        y_hat_final.append(y_app)
        n = n - 1
    return y_hat_final

# constructing a new array with all the values of y hat given the logarithmic
# model
def calculate_ln_y_hat(val, m) :
    y_hat_final_ln = []
    while m >= 0:
        y_app = np.log(x1[4-m]*val[0] + x2[4-m]*val[1] + val[2])
        y_hat_final_ln.append(y_app)
        m = m - 1
    return y_hat_final_ln

# adding some space, trying to save some time
def space() :
    print();print();print()
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
        print("This is " + name + " Log-Linear regression")
    print()
#######################################################


# we are provided two observations in our training set
x1 = np.array([12,14,16,20,24])
x2 = np.array([4,3,6,5,2])
# y is denoted as the label
y = np.array([50,53,67,70,63])

# Function for Model 1 y-hat
y_hat_1 = np.array([1.5, 5, 12])
# Function for Model 2 y-hat
y_hat_2 = np.array([2.0, 4, 10])

# Gets the size of the array (5)
c = x1.size - 1    

print("using sum of squared errors as the objective function")    

#model 1

intro("model 1", 1)

# makes all the calculations respectively for model 1 (refer to functions)
y_mod_1 = calculate_y_hat(y_hat_1, c)
error_mod_1 = error(y_mod_1, y)
sse4error_1 = error_mod_1**2
sse_1 = np.sum(sse4error_1)

# prints the data in an orderly fashion
print("the y hat of model 1 is :") 
print(y_mod_1)
print("and the error is: ")
print(str(error_mod_1) + " with standard error " + str(sse_1))
print("the standard deviation is :" + str(std(sse_1, c+1)))

#model 2

intro("model 2", 1)

# makes all the calculations respectively for model 2 (refer to functions)
y_mod_2 = calculate_y_hat(y_hat_2, c)
error_mod_2 = error(y_mod_2, y)
sse4error_2 = error_mod_2**2
sse_2 = np.sum(sse4error_2)

# prints the data in an orderly fashion
print("the y hat of model 1 is :") 
print(y_mod_2)
print("and the error is: ")
print(str(error_mod_2) + " with standard error " + str(sse_2))
print("the standard deviation is :" + str(std(sse_2, c+1)))

space()

print("using log likelihood as the objective function")

#model 1

intro("model 1", 2)

# makes all the calculations respectively for model 1 (refer to functions)
y_mod_1_ln = calculate_ln_y_hat(y_hat_1, c)
error_mod_1_ln = error(y_mod_1_ln, y)
sse4error_1_ln = error_mod_1_ln**2
sse_1_ln = np.sum(sse4error_1_ln)

# prints the data in an orderly fashion
print("the y hat of log  model 1 is :") 
print(y_mod_1_ln)
print("and the error is: ")
print(str(error_mod_1_ln) + " with standard error " + str(sse_1_ln))
print("the standard deviation is :" + str(std(sse_1_ln, c+1)))

intro("model 2", 100)

# makes all the calculations respectively for model 2 (refer to functions)
y_mod_2_ln = calculate_ln_y_hat(y_hat_2, c)
error_mod_2_ln = error(y_mod_2_ln, y)
sse4error_2_ln = error_mod_2_ln**2
sse_2_ln = np.sum(sse4error_2_ln)

# prints the data in an orderly fashion
print("the y hat of log  model 2 is :") 
print(y_mod_2_ln)
print("and the error is: ")
print(str(error_mod_2_ln) + " with standard error " + str(sse_2_ln))
print("the standard deviation is :" + str(std(sse_2_ln, c+1)))





