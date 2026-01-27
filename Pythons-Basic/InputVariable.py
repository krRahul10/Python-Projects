val = input("enter some val :")
print(type(val), val) 

value = int(input("enter some val :"))
print(type(value), value) 



# Que

num1 = int(input("enter your first number :"))
num2 = int(input("enter your second number"))
sum = num2+ num1
print("this is your sum :", sum)

# WAP to input side of a square & print area

side = int(input("enter teh of the square :"))
print("area of square : ", side**2)

# write a programme input 2 floating point number & print their avg.

num1 = float(input("enter your first number :"))
num2 = float(input("enter your second number : "))
average = (num1+num2)/2
print(" this is your avg : ", average)


# write a programme to input 2 int numbers a, and b
# print True if a is greater than or equal to b. if not print False

num1 = int(input("enter your first number : "))
num2 = int(input("enter your second number : "))
print(num1 >= num2)
if (num1 >= num2):
    print("Num1 is greater than b or equal to Num2", True)
else:
    print("print false; ", False)
    
    