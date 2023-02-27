# Here we are learn the tuples methods in python


# Note: tuples are immutable hence if you want to add,remove or change the tuples items then first you want to convert the tuple into the lists




name=('prasanna','pratik','tejas','aniket')

temp=list(name)
print(temp)
# this is just the example 


# methods in the python

tuple1=(1,2,3,'prasanna',79,2)

result=tuple1.count(2)  # count give the repeted value in the tuple
print(result)

result=tuple1.index('prasanna')  # Here the index give the index number of the item in the tuple
print(result)

result=len(tuple1)  # here the length gives the total items present in the length

print(result)


