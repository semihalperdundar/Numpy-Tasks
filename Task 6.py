# Write a function dot_product(a,b) that takes two matrices as input, 
# reshapes a as necessary, and returns the dot product of a and b as a numpy array (a.b not b.a).

# Depending on the shape of a and b, it may not be possible to compute the dot product of the two matrices 
# as is and it might be necessary to first reshape a such that the dot product can validly be computed.

# *Mathematically speaking, it isn't always possible to reshape a matrix in the right shape, 
# but for this question, you can assume that matrix a can be reshaped appropriately.
# Note: You may not use any loops (if,for, while, etc) to solve this question.


import numpy as np

def dot_product(a, b):
    
    if a.size == b.size:
        a_reshaped = np.reshape(a, b.shape)
        return np.dot(a_reshaped, b)
    else:
        print("The shapes of `a` and `b` are not compatible for reshaping and dot product.")

a = np.random.randint(0, 15, (7, 7))
b = np.random.randint(10, 20, (5, 7))
e=  np.random.randint(10, 20, (7,7))
print(dot_product(a, b))
print(dot_product(a, e))
