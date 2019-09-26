'''@package docstring
Documentation Exercice 1 : Average.
 
Learn algorithmie.
Use Dioxygen docs.
Use git and versionning.
'''

'''
What happens if Som initialization is forgotten ?
    An NameError occured and said that som is not defined.

What can you expect if all the values are below zero ?
    The averrage will be a division by 0 then it will display an error.

'''

''' Exercice 1 : Average '''
array=[1,5,8,7,0,-5,4-2,0,10,9,7]

import numpy as np

tab_zeros=np.zeros(12, dtype=np.int32)
tab_fromList=np.array(array)

def average_above_zero(array):
    '''Function that return average from array
    Arg:
        @param array: an array

    @return float
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

''' Exercice 2 : Table maximum value '''

def max_value(array):
    '''Function that find max value of an array and it index
        Arg:
            @param array : an array
        
        @return float, int
    '''
    max=0
    index=0
    for i in range(len(array)):
        if max < array[i]:
            max=array[i]
            index=i

    return max, index

array_max_one, index = max_value(array)
print('The max number of \'array\' is {0} at index {1}'.format(array_max_one, index))

array_max_two = max(array)
print('The max number of \'array\' is {0} (using existing method)'.format(array_max_two))

''' Exercice 3 : Reverse a table: '''

def reverse_array(array):
    '''Function reverse array
        Arg:
            @param array: an array
        
        @return array
    '''
    return array[::-1]

def reverse_table(table):
    count=len(table)
    for i in range(count):
        temp=table[count-1]
        table.pop()
        table.insert(i, temp)

    return table
         
reverse_array=reverse_table(array)
print("Original array : {0}".format(array))
print('Reversed array : {0}'.format(reverse_array))