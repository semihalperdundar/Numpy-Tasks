# Create two 4x4, 2-dimensional arrays: one containing only zeros, the other containing only ones.
#Stack them using a vertical stack, then reshape the stacked array into a 3-dimensional array. 
# Now, use array indexing to retrieve only ones from the stacked array.
# Now reshape the stacked array into a 3-dimensional array in such a way that the first 
# (the leftmost) dimension consists of only ones or zeros, but not both. Again, use array indexing to retrieve only ones from the reshaped 3D array.

import numpy as np

a= np.zeros([4,4])
b= np.ones([4,4])

print(a)
print(b)

print("Vertical stack: ")
c = np.vstack([a,b])
print(c)
print(c.shape)


d= c.reshape(2,4,4)
print(d)
print(d.shape)

e= c[4:]
f= e.reshape(2,2,4)
print(f)
print(f.shape)