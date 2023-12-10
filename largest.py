x=int(input("Enter 1st no."))
y=int(input("Enter 2nd no."))
z=int(input("Enter 3rd no."))
if(x>y and x>z):
    print(x,"is the largest no.")
elif(y>x and y>z):
    print(y,"is the largest no.")
else:
    print(z,"is the largest no.")
if(x<y and x<z):
    print(x,"is the smallest no.")
elif(y<x and y<z):
    print(y,"is the smallest no.")
else:
    print(z,"is the smallest no.")
