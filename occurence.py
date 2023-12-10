L1=[]
n=int(input("Enter the no. of characters in your list1:"))
for i in range (1,n+1):
    l=input("Enter the element:")
    L1.append(l)
print("List1=",L1)
x=input("Enter the element whose occurence is to be found:")
y=L1.count(x)
print("The no.of times it occurs=",y)
