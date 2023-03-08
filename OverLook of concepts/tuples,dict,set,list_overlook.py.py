# --------------Lets OverLook Lists,Tuples,Dictionary and Sets

# here we are create the list methods
# for list we are create use the []

list1=['prasanna',56,True,'pratik']
print(list1)

print(type(list1))

list1.append('tejas')
print(list1)

list1.count(56)
print(list1)

list1.extend('prasanna')
print(list1)

print(list1.index(True))

list1.insert(3, 'shambho')
print(list1)

list1.pop(1)
print(list1)

list1.remove('prasanna')
print(list1)

list1.reverse()
print(list1)

list2=[1,55,9,3,65,999,4,4322]

list2.sort()
print(list2)

list1.append(list2)
print(list1)


#---------- here we are create the some tuples and its methods

# for tuple we use ()

tup1=(1,44,'prasanna','tejas',False)
print(tup1)
print(type(tup1))


print(tup1.count('prasanna'))


print(tup1.index('tejas'))


tup2=(7,9,55,'raju')

print(tup2)

tup1.__add__(tup2)
print(tup1)


# -------Here we are create the dictinary and its methods

#  for dictionary we use {} and i contains the key and value pair in the dictionary

dict1={'name':'prasanna',
       'age':20,
       'gender':'male',
       'occupation':'student'}

print(dict1)
print(type(dict1))


print(dict1.get('name'))

print(dict1.pop('gender'))

print(dict1.popitem())

dict2=dict1.copy()
print(dict2)

print(type(dict2))



#------ here we are learn the sets and its methods

#   for set we use {}

set1={1,44,'prasanna',10,55,'tejas'}

set2={'tejas','raju',100,55,10,66,52}

print(set1)
print(type(set1))
print(set2)
print(type(set2))


print(set1.intersection(set2))

print(set1.intersection_update(set2))


print(set1.issubset(set2))

print(set1.symmetric_difference(set2))

print(set1.union(set2))

print(set1.isdisjoint(set2))
print(set2.isdisjoint(set1))


