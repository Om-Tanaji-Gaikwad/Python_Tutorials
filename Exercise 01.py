#Dictionary
"""
Q. Create a dictionary and take input from user and return the
meaning of the word from the dictionary
"""
d1={"set":"It is a collection of data","mutable":"It can be changed","immutable":"It can not be changed"
    ,"headphone":"It is device used for hearing"}
print("Enter a word : ")
word=input()
print("The Meaning of the given word :",end=" ")
print(d1[word])