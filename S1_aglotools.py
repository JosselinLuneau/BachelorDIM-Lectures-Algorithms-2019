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

tab_fromList=np.array(array)

def average_above_zero(array):
    '''Function that return average from array
    Arg:
        @param array: an array

    @return float

    Raises ValueError if input param is not a list and if is empty
    '''
    if not(isinstance(array, list) or isinstance(array, np.ndarray)):
        raise ValueError('average_above_zero, expected a list as input')
    if len(array)==0:
        raise ValueError('average_above_zero, expect a non empty array')

    som=0
    n=0
    for i in range(len(array)):
        if array[i] > 0:
            som += int(array[i])
            n += 1
        
    if som==0 or n==0 :
        raise ValueError('average_above_zero, no positive element found')
    
    average=som/n
    
    return average

        



average_one = average_above_zero(array)
print("The fisrt average is {0}".format(average_one))

average_three = average_above_zero(tab_fromList)
print("The third average is {0} (same as first)".format(average_three))

''' Exercice 2 : Table maximum value '''

def max_value(array):
    '''Function that find max value of an array and it index
        Arg:
            @param array : an array
        
        @return float, int
        Raises ValueError if input param is not a list and if is empty
    '''
    if not(isinstance(array, list) or isinstance(array, np.ndarray)):
        raise ValueError('average_above_zero, expected a list as input')
    if len(array)==0:
        raise ValueError('average_above_zero, expect a non empty array')

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
        Raises ValueError if input param is not a list and if is empty
    '''
    if not(isinstance(array, list) or isinstance(array, np.ndarray)):
        raise ValueError('average_above_zero, expected a list as input')
    if len(array)==0:
        raise ValueError('average_above_zero, expect a non empty array')

    return array[::-1]

def reverse_table(table):
    '''Function reverse array
        Arg:
            @param table: an array
        
        @return array
       Raises ValueError if input param is not a list and if is empty
    '''
    if not(isinstance(array, list) or isinstance(array, np.ndarray)):
        raise ValueError('average_above_zero, expected a list as input')
    if len(array)==0:
        raise ValueError('average_above_zero, expect a non empty array')

    buffer=len(table)
    iteration=int(buffer/2)
    max_index=buffer-1
    for i in range(iteration):
        diffId=max_index-i
        temp=table[i]
        table[i]=table[diffId]
        table[diffId]=temp

    return table

print("Original array : {0}".format(array))
reverse_array=reverse_table(array)  
print('Reversed array : {0}'.format(reverse_array))

''' Exercice 4 : Bounding box '''

# Créer sa matrice
#matrix=np.zeros((10,10), dtype=np.int32)
# matrix.shape = (3,4)
#matrix[3:4, 4:8]=np.ones((3,4), dtype=np.int32)
#print(matrix)

import cv2
img=cv2.imread('img.png', 0)
# cv2.imshow('Show image', img)
# cv2.waitKey() # attend que l'image soit fermée

def roi_bbox(input_image, color_search=0):
    '''Function that compute the bounding box coordinates of the object
        Arg:
            @param input_image: an array
        
        @return np.array
        Raises ValueError if input param is not a list and if is empty
    '''
    if not(isinstance(input_image, list) or isinstance(input_image, np.ndarray)):
        raise ValueError('roi_bbox, expected a list as input')
    if len(input_image)==0:
        raise ValueError('roi_bbox, expect a non empty array')
    
    height, weight=input_image.shape # image size
    image_spot_index=np.argwhere(input_image==color_search) # get pixel index of color search
    buffer_col=len(image_spot_index)
    
    max_row_index=0
    min_row_index=height
    max_col_index=0
    min_col_index=weight

    for i_row in range(buffer_col): # browse index table
        if min_row_index > image_spot_index[i_row][0]: # get min row index
            min_row_index = image_spot_index[i_row][0]
        if max_row_index < image_spot_index[i_row][0]: # get max row index
            max_row_index = image_spot_index[i_row][0]

        if min_col_index > image_spot_index[i_row][1]: # get min col index
            min_col_index = image_spot_index[i_row][1]
        if max_col_index < image_spot_index[i_row][1]: # get max col index
            max_col_index = image_spot_index[i_row][1]
        
    return [
            [min_col_index, min_row_index], 
            [min_col_index, max_col_index], 
            [min_row_index, max_row_index], 
            [max_col_index, max_row_index]
        ]

bbox=roi_bbox(img)
print("Boudind box {0}".format(bbox))

