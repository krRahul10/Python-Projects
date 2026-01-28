# RedLight Example

'''light = input("light :")
if(light == 'red'):
    print('STop')
elif(light == 'green'):
    print('Goo!')
elif(light == 'yellow'):
    print("Look")
else:
    print('Light broken')'''

# School Grade system

'''marks = int(input("Enter your marks"))
if (marks >= 90):
    print("A+ Grade")
elif(marks >= 80 and marks <=90):
    print('B+ Grade')
elif(marks >= 50 and marks <=80 ):
    print("C+ grade")
else:
    print('only Pass')'''
    

# Single Line Condition statement (Ternary Operator)

# food = input("Food : ")
# eat = "Yes" if food == "cake" else 'no'
# print(eat)

# food = input ("food : ")
# print("SWeet") if food == "Cake" or food == "Jalebi" else print("No sweet")


# age = int(input("Age : "))
# vote = ("Yes", "No") [age >= 18]
# print(vote)

# sal = int(input("Salary : "))
# tax = sal*(0.1, 0.3) [sal >= 50000]
# print(tax)

# Assignment operator

# num = 10
# num = num 
# num= num**5
# print(num)

# Nesting condition

# age = int(input("Enter your age :"))

# if (age >= 18):
#     # print(" You can drive")
#     if(age >=80):
#         print("You can not drive bhude ghar ja")
#     else:(print("Can drive"))
# else:
#     print("app abi bache ho")
    
    
# write a programme check if a number entered by user is odd or even

# number = int(input("Enter your number to check odd or even :"))

# if(number%2==0):
#     print("even")
# else:
#     print("odd")    
    
# write a programme to check if a number is multiple by 7 or not

# number = int(input("Enter your number to check odd or even :"))

# if(number%7==0):
#     print("Can multiple by 7")
# else:
#     print("can't multiple by 7")  
    
# write programme to find the greatest number enter by user   

number1 = int(input("Enter your number1 :"))
number2 = int(input("Enter your number2 :"))
number3 = int(input("Enter your number3 :"))

if (number1 > number2 and number1 > number3):
    print("A is greater than B and C ", number1)
elif(number2 > number3):
    print("B is greater than C and A", number2)
else: print("C is greater than A and B",number3)

