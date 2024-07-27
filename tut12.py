# Sets in Python
"""
s=set()
print(type(s))
s_from_list = set([1,2,3,4])
print(s_from_list)

"""
"""
l= [1,2,3,4]
s_from_list = set(l)
print(s_from_list)
print(type(s_from_list))
"""
s = set()
s.add(1)
s.add(2)
s.remove(2)
s.add(1)
s1 = s.union({1,2,3})
s2 = s.intersection({1,2,3})
print(s,s1,s2)
