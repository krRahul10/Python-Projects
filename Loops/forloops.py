'''list = [2,3,4,57,5,3,23,4,5,6]
veggies = ["potato","tomato","ladyfinger"]
for val in veggies:
    print(val)
else :
    print("end")
    '''
    
    
'''str = "masaischool"
for i in str:
    if (i == 'o'):
        print("o found at :", i)
        break
    print(i)
else: print("Not found")'''

# Questions

# print the element of the following list
list = [1,2,3,4,5,6,7,3,10,2,3]
x = 3
idx =0 
for i in list:
    print(i)
    if (x==i):
        idx+=1
        print("we have found at idex : ",idx )
        break
else: print("Not found")