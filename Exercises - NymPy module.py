import numpy as np

print(f'Version: {np.__version__}')

print('-------------------Q1----------------------')
#Question 1: Create a 4X2 integer array and
#Prints its attributes: the shape, dimensions,each element of the array in bytes 
#The element must be a type of unsigned int16. 


arr = np.empty([4,2], dtype=np.uint16)

# print array
print('The 4x2 array: ')
print(arr)
# print number of dimensions
print(f'\n The array has {arr.ndim} dimensions')
#print shape of the array
print(f'\n The array has {arr.shape} shape')
# print length of each element of the array in bytes
print(f'\n The length of each element is {arr.itemsize} bytes')

print('-------------------Q2----------------------')
# Question 2: Create a 5X2 integer array from a range between 100 to 200
#such that the difference between each element is 10

#creating a 1D array using np.arrange:
arr1 = np.arange(100,200,10, dtype=None)
##print(arr1)

#breaking the 1D array into 2D array using reshape
arr2 = arr1.copy()
arr3 = arr2.reshape(5,2)
print(arr3)

print('-------------------Q3----------------------')
#Question 3: Following is the provided numPy array.
#return array of items in the third column from all rows

sampleArray = np.array([[11 ,22, 33], [44, 55, 66], [77, 88, 99]])

new_array = sampleArray[...,2]
print(new_array)
print(type(new_array))

print('-------------------Q4----------------------')
# Question 4: Following is the given numpy array return array of odd rows
#and even columns

sampleArray = np.array([[3 ,6, 9, 12], [15 ,18, 21, 24], 
[27 ,30, 33, 36], [39 ,42, 45, 48], [51 ,54, 57, 60]])


# chosing starting row/column, double colon (skipping last row/column), choosing 'step'
newArray = sampleArray[0::2,1::2]
print(newArray)

print('-------------------Q5----------------------')
# Question 5: Add the following two NumPy arrays and
# Modify a result array by calculating the square of each element

arrayOne = np.array([[5, 6, 9], [21 ,18, 27]])
arrayTwo = np.array([[15 ,33, 24], [4 ,7, 1]])

# using ufuncs add()func

added_array = np.add(arrayOne,arrayTwo)
print(added_array)

# using ufuncs power()func

powered_array = np.power(added_array, 2)
print(powered_array)


print('-------------------Q6----------------------')

# Question 6: Split the array into four equal-sized sub-arrays
# Note: Create an 8X3 integer array from a range between 10 to 34 such that
# the difference between each element is 1 and
# then Split the array into four equal-sized sub-arrays.

# creating an array

arr = np.arange(10,34,1, dtype=int)
print(arr)

# spliting into a 8x3 array

new_arr = arr.reshape(8,3)
print(new_arr)

#spliting 4 sub-arrays 2x3
new_arr = np.split(new_arr, 4)

for x in new_arr:
    print('\n', x,'\n')

print('-------------------Q7.1----------------------')

#Question 7.1; Sort following NumPy array by the second row 

sampleArray = np.array([[34,43,73],[82,22,12],[53,94,66]])

sort_row = sampleArray[:,sampleArray[1,:].argsort()]
print(sort_row)



print('-------------------Q7.2----------------------')

#Question 7.2; Sort following NumPy array by the second column

sampleArray = np.array([[34,43,73],[82,22,12],[53,94,66]])

