# string formatting - f-string {  }
# String Foramtting used for the insert the variable in the print function

name='prasanna'
country="India"

print(f"Hey my name is {name}, And I am from {country} ")
# here the f is used for string formatting before the qoutes and then insear the varibale in the curly brackets

price=49.1900

txt=f"for only {price :.2f} dollars!!"  # Here the .2f used to print only two digits after the decimal like 49.19
print(txt)



# Doc string

# python docstring are the string iterals that apper right after the definaition of the function,methods.class or module

def square (n):
    ''' takes in a number n,returns the square of n ''' # note that this is not the comment
    print(n**2)
square(5)
print(square.__doc__)


def add (a,b):
    ''' this def function will add the two number in the a,b and give the result  '''
    sum=a+b
    print(sum)
add(50, 40)
print(add.__doc__)