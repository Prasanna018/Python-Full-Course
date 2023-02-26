# Function are use to do the same work with limited code and use the function when necessary 

# There are built in and the user defined function in the python

def add(a,b):  # def is used to define any function in the python
    sum=a+b
    print("the sum of two values is :" ,sum)

add(50, 90)  # here we are execute the function



# ------functions using the user inputs:
value1=int(input("Enter the first value :"))
value2=int(input("Enter the second value :"))

def add1 (value1,value2):
    total=value1+value2
    print("The sum of two values is :" ,total)

add1(value1, value2)

def average (value1,value2):
    print("The average is : ",(value1+value2)/2)

average(value1, value2)
