# Here we are learn the about how to use the break and contiune in the conditional statements


# ---------Break

for i in range(11):
    if i == 5:
        break  # here the break will stop the loop after the condition 
    print(i)
else:
    print("this is our break function")
    
    
for i in range(1,50):
    if i == 25:
        break
    print(i)
    
    
# -----------Continue


for id in range(20):
    if id == 15:
        continue   # the condition were true the continue will iterate the value in range and continue to forward.
    print(id)
    

list1=[1,2,3,4,5,6,7,8,9]
for i in list1:
    if i == 5:
        continue
    print(i)