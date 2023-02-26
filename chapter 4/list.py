# Now we are startfor learing for the lists in python---

l=[1,2,3,'prasanna','b',99]
print(l)
print(type(l))  

# List is maintain the order
# List can changed
# List consists string,boolean,integer.

list1=[1,2,'tejas',True]
print(list1)

# List Indexing------

k=[1,2,3,4,5,6,7,8,9]
 #  positive  indexing
print(k[0:6])  
print(k[:5])
print(k[2:])

m=[1,2,3,4,5,6,7,8,9,10]
# negative indexing

print(m[-7:-2]) 

print(m[0:len(m)-4])



# Item checking in the list


name=['prasanna','tejas','ram','kishor']
if 'tejas' in name:
    print("Tejas is present ",name)
    
num_list=[1,22,33,4,5,66]
if 23 in num_list:
    print("23 is present")
else:
    print("23 is not present in this list")
    

# List comprehension

p=[i for i in range(5)]
print(p)

q=[i*i for i in range(10)]
print(q)

v=[i*i for i in range(10) if i%2 ==0]
print(v)

