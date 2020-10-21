# Exercise 1 - creating new list with the dubled elements form the given list


my_list = [1,2,3,4,5,6,7,8,9,10,11]

doubled = []

# solution with a for loop

for num in my_list:
    num=2*num
    doubled.append(num)

print (doubled)

# solution with comprehension

doubled = [num*2 for num in my_list]

print (doubled)


# Exercise 2 - creating a new list only with elements starting with "S" from the given list

my_friends = ["Sara", "Klara", "Sylwia", "Henryk", "Tomek", "Sebastian"]
name_s =[]

# solution with a for loop and if cluse

for friend in my_friends:
    if friend.startswith('S'):
        name_s.append(friend)

print (name_s)

# solution with comprehension

name_s = [friend for friend in my_friends if friend.startswith('S')]

print (name_s)


