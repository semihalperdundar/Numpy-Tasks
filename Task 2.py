# Create a function that takes as input an integer. 
# The function should create an array of random values between 0 and 1 the size of the input parameter, 
# and return the number of entries with a value lower than 0.025 or higher than 0.975.



import numpy
def veryimportantexercise(a):
    values = numpy.random.random(a)
    low_values = values < 0.025
    high_values = values > 0.975
    extreme_values = low_values | high_values
    return numpy.sum(extreme_values), extreme_values
print(veryimportantexercise(35))
