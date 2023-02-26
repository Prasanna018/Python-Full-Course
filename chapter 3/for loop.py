#  For loop can iterate over a sequence of iterable in python

name='tejas'
for i in name:
    print(i)

color=['red','pink','black','yellow']
for i in color:
    print(i)
    
# using range

for i in range(5):
    print(i)
    
    
a=50
for i in range(a):
    print(i)
    i=i+1
    
    
    
# Using range printing pattern

for i in range(5):
    for j in range(1+i):
        print(j ,end=" ")
    print()
    
pattern=int(input("Enter the number for pattern :"))
for i in range(pattern):
    for j in range(1+i):
        print(j ,end=" ")
    print()