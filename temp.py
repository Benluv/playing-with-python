# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np

# 5obser
x1 = [12,14,16,20,24]
x2 = [4,3,6,5,2]
y = [50,53,67,70,63]
np_x1 = np.array(x1)
np_x2 = np.array(x2)
np_y = np.array(y)

# y(hat) = 1.5x1 + 5x2 + 12
np_y_hat_mod_1 = np.array([1.5, 5, 12])

y_hat_final = []
i = 1
count = np_x1.size
#model1
while (count < 9):
   print ('The count is:'), count
   count = count + 1

print ("Good bye!")
print("more changes here")

