# Tuple built-in data type in python that lets us create immutable sequence value. 
# tup = (80,90,30,59,68)
# print(type(tup))
# tup[0]=40 #not allowed in tuple 

# slicing is possible in tuple 
# write programme to ask the user to enter their of their 3 favorite move name and store in list 

# list = []
# list.append(input("enter your first movie name : "))
# list.append(input("enter your second movie name "))
# list.append(input("enter third movie name"))
# print(list)

# palindrome list

# [1,2,3,2,1]

list1 = [1,2,3,2,5]
copy_list1 = list1.copy()
copy_list1.reverse()
print(copy_list1)
print(list1)

if(list1 == copy_list1):
    print("Palindrome")
else: print("Not palindrome")

print(list1.count(2))

