# In python we can use if-else statement for the conditions

# 1. if-else

a=50
b=55


# In the python there is comparison operators-
# <,>,<=,>=,==

if a < b :
    print("a is small") 
else:
    print(" a is big")
    
    
# taking user input for if-else statement

number=int(input("Enter the digit : "))

if number > 50:
    print("the nmmber is greater than 50 :",number)
else:
    print("the number is less than 50 :", number)
    
    
    
# Nested and use of if-elif-else statement

# Nested means one statement with more conditions makes nested

grade=int(input("Enter the marks obtained out of 100 :"))  # taking the user input for grade

if grade >= 90:
    print("You got 'A' grade :" ,grade )

# ----here we are use elif for more condition of one statement
elif grade >= 80 :                     
    print("You got 'B' grade :" ,grade)  

elif grade >= 70:
    print("You got 'C' grade :" ,grade)

else:
    print("You are Not Qualified for the Exam :" ,grade)



