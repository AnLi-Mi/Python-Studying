# creating new list with the dubled elements form the given list


my_list = [1,2,3,4,5,6,7,8,9,10,11]

doubled = []

# solution with a for loop

for num in my_list:
    num=2*num
    doubled.append(num)

print (doubled)

# colution with comprehension

doubled = [num*2 for num in my_list]

print (doubled)
