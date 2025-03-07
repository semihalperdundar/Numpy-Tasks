# write a function convert_and_check() that 
# takes as input a one-dimensional numpy array of strings named initial_input and returns two outputs:
# (a) a one-dimensional numpy array with the same number of elements as initial_input but with the type set to an eight (8) character string.
# (b) a boolean value indicating if all characters from initial_input are preserved in the output array.
# See the instructions in Week1_sample_exam_question.ipynb Download Week1_sample_exam_question.ipynbfor more details. 
# You can use week1_sample_exam_question_template.py 
# Download week1_sample_exam_question_template.pyas a template for your solution.
# After submitting your solution you can see the correct solution.



import numpy
def convert_and_check (initial_input):
    output = numpy.array(initial_input, dtype='<U8')
    match = numpy.array_equal(initial_input,output)
    return output, match, output.dtype

initial_input= numpy.array(['gg','aaa','llll','a','ttttt','ss','rrrrr','yyyyyyyyy'])
print(convert_and_check(initial_input))
print(initial_input.dtype)



    