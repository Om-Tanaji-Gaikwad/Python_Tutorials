# Faulty Calculator
"""
Q. Design a calculator which will correctly solve all the problems except the following ones:
45*3 = 555,56+9=77,56/6=4
Your program should take operator and the two numbers as input from user and then return the result
"""
# Answer

num1=int(input("Enter 1st number : "))
ope=input("Enter a operator : ")
num2=int(input("Enter 2nd number : "))

if ope=="+":
    if num1==56 and num2==9:
        print("77")
    elif num1==9 and num2==56:
        print("77")
    else:
        print(num1 + num2)
elif ope=="-":
    print(num1-num2)
elif ope=="*":
    if num1==45 and num2==3:
        print("555")
    elif num1==3 and num2==45:
        print("555")
    else:
        print(num1 * num2)
elif ope=="/":
    if num1==56 and num2==6:
        print("4")
    else:
        f=num1/num2
        print(f)
else:
    print("Invalid Operator")
