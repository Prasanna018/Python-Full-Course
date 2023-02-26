# Here we are learn diffrence methods of the lists in python


number=[1,2,3,4,5,8,4]
print(number)
number.append(55)
print(number)   # append will add the value in list at last

number.sort()
print(number) # it will makes list in accending order

number.sort (reverse=True)
print(number)    # it will sort the list in accending order and makes reverse

number.reverse()
print(number)   # it makes the list in reverse

number.index(3) 
print(number)    # it will print the value of given index

number.count(4)
print(number)  # it count the repeated values in the list

num=number.copy()
print(number) # it makes copy of list
print(num)

number.insert(2, 100)
print(number)      # insert will add value in given index

number.extend(num)
print(number)      # extend means it will add two lists