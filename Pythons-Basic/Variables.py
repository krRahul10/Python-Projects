name = "Rahul Kumar" #string
age = 31 # Number or integer
Company = "PwC" # String
Salary = 45.90


print(name);

print("My name is :", name)
print("My age is :", age)

# Rule of Identifiers
# 1. Identifiers can be combinations of uppercase and lowercase letter, digits or an underscore(_). so many myVariables, variables_1 all are valid identifiers
# 2. an identifier can not start with digit. so while var1 is valid and 1var is not valid.
# we can't use special symbol like !@#$%%^ etc in our identifier.
#  Identifier can be of any length.

print(type(age))
print(type(name))
print(type(Salary))

#  Data Type 
# Integer: 29,4,80,-30
# String : "sk", "David,
# Float : 60.0, 9.8
# Boolean: True and False only capital value 
# None : 

oldold = False;
abc = None;
 
print(type(oldold))
print(type(abc))

# IMP: Python is case sensitive language and also implicit type of language not explicit type like Java, c++ etc

# Type of Tokens
# Punctuators : Punctuators  are symbols to organize sentence structure in programming.
# EX: (), {}, @, [] etc


A,B =2,3
Txt="@"
print(2*Txt*3);

C,D="2",3;
Ext="@";
print((C+Ext)*D);