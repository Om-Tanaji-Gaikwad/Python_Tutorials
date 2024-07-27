# Dictionary and its functions
d1={"Harry":"burger","Rohan":"Cake","Mohan":"ice cream"
    ,"Shubham":{"A":"Maggie","B":"Roti","C":"chapati"}}
print(type(d1))
print(d1)
print(d1["Shubham"])
print(d1["Shubham"]["B"])
d1["Ankit"]="Junk food"
del d1["Rohan"]
print(d1)
#if we do d2=d1 and make changes in d2 then value stored in d1 will also change
#therefore do this d2=d1.copy()
d1.update({"Leena":"Toffee"})
print(d1)
print(d1.keys())
print(d1.items())