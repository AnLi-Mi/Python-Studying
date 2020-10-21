student_attendence = {"Roy":"20h", "Jen": "88h", "Moss": "60h", "Anna": "70h", "Craig":"34h"}

print(f"Printing all the values: {student_attendence.values()}")
print(type(student_attendence.values()))
print(f"Printing all the keys: {student_attendence.keys()}")
print(type(student_attendence.keys()))
print(f"Printing all the elements: {student_attendence}")
print(type(student_attendence))
print(f"Printing all the elements: {student_attendence.items()}")
print(type(student_attendence.items()))

print(f"Printing each key - not whole element")
for name in student_attendence:
    print (name)


print(f"Printing each value - not whole element")
for name in student_attendence:
    print (student_attendence[name])


print(f"Printing each key + value")
for name in student_attendence:
    print (name, student_attendence[name])


print(f"Printing each key + value V2")
for name, hours in student_attendence.items():
    print (name, hours)


print(f"Printing each key + value reversed")
for name, hours in student_attendence.items():
    print (hours, name)


print(f"Printing each key + values - reverted variables names")
for hours, name in student_attendence.items():
    print (name, hours)

print(f"Printing each item")
for item in student_attendence.items():
    print (item)

print(f"Printing each elements of each item")
for name, hours in student_attendence.items():
    print (name, hours)

for item in student_attendence.items():
    print (item[0], item[1])


