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
