# Write a function called generate_tvt_sets that takes three inputs:

#     a two-dimensional numpy array of float numbers (named x)
#     and two integers (named training_count and test_count)

# The function should write the following 3 files.

#     write the first training_count rows  of x to a CSV file named q1_training_data.csv.
#     write the final test_count rows of x to a CSV file named q1_test_data.csv.
#     write all other rows x (not in the training or test set) to a CSV file named q1_validate_data.csv.
#     Note: You may not use any loops (for, while, etc) to solve this question.

import numpy as np

def generate_tvt_sets(x: float, training_count: int, test_count: int):
    training_data = x[:training_count].copy()
    np.savetxt('q1_training_data.csv', training_data, fmt='%f', delimiter=',')
    

    validation_data = x[training_count:-test_count].copy()
    np.savetxt('q1_validate_data.csv', validation_data, fmt='%f', delimiter=',')
    
    test_data = x[-test_count:].copy()
    np.savetxt('q1_test_data.csv', test_data, fmt='%f', delimiter=',')
    
    return training_data, validation_data, test_data

x= np.arange(0,101)
train, validate, test = generate_tvt_sets(x, 71, 15)



