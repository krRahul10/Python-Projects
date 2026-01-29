# same like array

# A built-in data type that stores set of values
# in can store element in different types(str,int,float etc)
# Imp : strings are immutable(change nhi ho sakti) in python and lists are mutable(change ho sakti hai) in python

marks = [50,54,30,80,90]
print(type(marks), len(marks))

# Slicing in List

# similar to string in slicing

# list_name = [staring index: ending index] ending index not includes



# List methods 

marks.append(66) # will add element in the last of this list mutations allow
print(marks)

# marks.sort()
# print(marks)
marks.reverse()
print(marks)
marks.sort(reverse=True)
print(marks)