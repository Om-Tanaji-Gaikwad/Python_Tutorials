# For loop
"""
list1=[["harry",4],["carry",2],["larry",6],["parry",250]]
dict1=dict(list1)
for item,lollypop in dict1.items():
    print(item,"has",lollypop,"lollypops")
for item in dict1:
    print(item)
"""
# Quiz
items=[int,float,"Harry",5,4,3,87,45,23,6]
for item in items:
    if str(item).isnumeric() and item>=6:
        print(item)