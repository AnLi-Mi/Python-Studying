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
