# Here we are learn about the if-else statements

a=60
b=50
# here wea are use only one condition 
if a > b:
    print(f"{a} is greater than {b}")
else:
    print(f"{a} is smaller than {b}")

    
# for more conditions we are use nested if-elif-else statements

number=int(input("enter the number here:"))

if number < 10:
    print(f"the number is one digit {number} ")
elif number < 100:
    print(f"the number is two digit {number}")

elif number < 1000:
    print(f"the number is three digit {number}")

else:
    print(f"unknown number found {number}")
    
# note: practise more about this conditional statements
    