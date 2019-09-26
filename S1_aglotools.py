'''@package docstring
Documentation Exercice 1 : Average.
 
Learn algorithmie.
Use Dyoxigen docs.
Use git and versionning.
'''

'''
What happens if Som initialization is forgotten ?
    An NameError occured and said that som is not defined.

What can you expect if all the values are below zero ?
    The averrage will be a division by 0 then it will display an error.

'''
array=[1,5,8,7,0,-5,4-2,0,9,10,7]

import numpy as np

tab_zeros=np.zeros(12, dtype=np.int32)
tab_fromList=np.array(array)

def average_above_zero(array):
    '''
    Function that return average from array
    Args:
        array: an array
    Return the average of positive number above zero
    '''

    som=0
    n=0
    for i in range(len(array)):
        if array[i] > 0:
            som += int(array[i])
            n += 1

    try:
        average=som/n

        return average
    except Exception as e:
 
        return e.args


average_one = average_above_zero(array)
print("The fisrt average is {0}".format(average_one))

average_two = average_above_zero(tab_zeros)
print("The second average is {0} (An error)".format(average_two))

average_three = average_above_zero(tab_fromList)
print("The third average is {0} (same as first)".format(average_three))

