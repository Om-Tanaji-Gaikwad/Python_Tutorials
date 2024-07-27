# Break and continue statements in Python
"""
i=0
while(True):
    if(i+1<5):
        i=i+1
        continue

    print(i+1,end=" ")
    if(i==44):
        break
    i=i+1
"""
# Quiz
while(1):
    num = int(input("Enter a number : \n"))
    if num > 100:
        print("Congratulations you entered a number greater than 100\n")
        break
    else:
        print("Try again!")
        continue
