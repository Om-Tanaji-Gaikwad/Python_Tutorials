# If else
"""
a = 25
b = 56
c=int(input())

if c>a:
    print("Greater")
elif c==a:
    print("Equal")
else:
    print("Lesser")
"""
"""
list1 = [5,7,3]
print(5 in list1)
print(15 in list1)
if 5 in list1:
    print("It is in list")
if 15 not in list1 :
    print("It is not in list")
"""
# Quiz
print("Enter your age :")
age=int(input())
if 1<=age<=100:
    if age > 18:
        print("You can drive")
    elif age < 18:
        print("You cannot Drive")
    else:
        print("Come visit us we will test your skills")
else:
    print("You Entered a invalid age")
