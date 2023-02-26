# Here we are learn the advanced string.

# 1. String Slicing
# Using the indexing we can do the strings slicing

Fruit="Mango,Banana"
print(len(Fruit))

print(Fruit[0:5])

print(Fruit[:7])

# looking for the negative strings slicing

name="pratik,aniket"
print(len(name))

print(name[0:-5])

name1='prasanna'
print(len(name1))

print(name1[-2:-1])     # length of the name1 variable is '8' so it will 8-2=6 and 8-1=7 so, print(name1[6:7])




# String Methods

country="india!!"

print(len(country))  # here this is length method to find out the length of the string

print(country.upper())  # upper method will create the uppercase of string

print(country.lower())   # lower method will create the lowercase of string

print(country.rstrip('!!')) # rstrip will remove the the content in the string

print(country.replace('india', 'hindustan')) # replace method will replace the old string into the new

blog="welcome to the blog "

print(blog.title()) # title method will use to make capital the first letter of the string




                




