# Here we are get more expertie in the python programming with more practsice 

# Various Data Types 

# 1. Tuple


tup1=(1,2,33,'prasanna','p',33)

print(type(tup1))
print(tup1)

print(tup1.count(33))
print(tup1.index('prasanna'))

# Practice more about the tuples using the documentation of official python site @python.org

# 2. List

list1=[1,33,8,'prasanna',98,]
print(type(list1))
print(list1)

list1.append(66)
print(list1)

print(list1.pop(3))

print(list1.reverse())
print(list1.remove(98))

print(list1.sort())
print(list1.insert(3, 'ANIKET'))

# 3.Dictionary

dict1={'name':'prasanna',
       'age': 50,
       'profesion':'worker',
       'hobby':'reading'
       
       }

print(type(dict1))
print(dict1)

print(dict1.get('name'))
print(dict1.fromkeys('age'))
print(dict1.keys())

# 4. Sets

set1={1,2,3,88,90,'prasanna','tejas'}
set2={2,5,66,88,'raju','mohit'}
print(type(set1))
print(set1)
print(set2)

print(set1.issubset(set2))

print(set1.intersection(set2))
print(set2.isdisjoint(set1))

print(set1.issuperset(set2))
print(set1.symmetric_difference(set2))
print(set1.pop())


# Here are some datatypes of the python learn more about its methods and all to be handy.




