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
print(sampleArray)

# defining a new order of columns based on the sorted 2nd row (index 1)
new_order_c = sampleArray[1,:].argsort()
print(new_order_c)

# creating new array based on smapleArray with not changed order inside columns,
#but reorganised order of columns according to 'new_order_c'

new_arr_c = sampleArray[:,new_order_c]
print (new_arr_c)
    
print('-------------------Q7.2----------------------')

#Question 7.2; Sort following NumPy array by the third column

sampleArray = np.array([[34,43,73],[82,22,12],[53,94,66]])
print(sampleArray)


# defining a new order of the rows based on the sorted 3nd column (index 2)
new_order_r = sampleArray[:,2].argsort()
print(new_order_r)

# creating new array based on smapleArray with not changed order inside the rows,
#but reorganised order of rows according to 'new_order_r'

new_arr_r = sampleArray[new_order_r,:]
print (new_arr_r)

print('-------------------Q8----------------------')

#Question 8: Following is the 2-D array.
#Print max from axis 0 and min from axis 1

sampleArray = np.array([[34,43,73],[82,22,12],[53,94,66]])

print(sampleArray)

# creating an empty list to populate it with the min elemets of each row (axis 1)
min_row=[]

# looping through all rows and extracting the lowest element
for row in sampleArray:
    min_row.append(np.min(row))

print (f' the lowest elements of the rows are: {min_row}')

# creating an empty list to populate it with the max elemets of each column (axis 0)
max_col=[]

# looping through all columns (turned into arrays) and extracting the highest element
for i in range (0,3):
    max_col.append(np.max(sampleArray[:,i]))
       
print (f' the highest elements of the columns are: {max_col}')

# --------------------other solution--------------------------

#solution using the np.amin/max function

sampleArray = np.array([[34,43,73],[82,22,12],[53,94,66]])

min_row2=np.amin(sampleArray, axis=1)

print (f' the lowest elements of the rows are: {min_row2}')

max_col2=np.amax(sampleArray, axis=0)
print (f' the highest elements of the columns are: {max_col2}')

print('-------------------Q9----------------------')

# Question 9: Following is the input NumPy array delete column two and
#insert following new column in its place.

sampleArray = np.array([[34,43,73],[82,22,12],[53,94,66]])
print(sampleArray)

newColumn = np.array([[10,10,10]])

#selecting an element with index 1 from ewach arrey and replacing it with the given array
sampleArray[:,1]=newColumn
print(sampleArray)

# --------------------other solution--------------------------

#solution using deleting and inserting function
arr= np.array([[10,10,10]])

col_delete = np.delete(sampleArray, 1, axis= 1)
print(col_delete)

col_insert = np.insert(col_delete, 1, arr, axis= 1)
print(col_insert)
