# Create an array containing the numbers 1 up to and including 100 (stepsize 1). 
# Assign the last 20 elements to a separate variable, then add 40 to each element in the new array. 
# Bonus: Solve the problem two ways, one that changes the values in place, and one that does not change the original values but creates a new array.

import numpy as np

a= np.arange(1,101)
b = a[-20:].copy()
b+=40
print(b)
print(a)