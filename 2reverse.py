L1=[]
L2=[]
n=int(input("Enter the no. of characters in your list1:"))
for i in range (1,n+1):
    l=input("Enter the element:")
    L1.append(l)
print("List1=",L1)
m=int(input("Enter the no. of characters in your list2:"))
for j in range (1,m+1):
    L=input("Enter the element:")
    L2.append(L)
print("List2=",L2)
L3=L1+L2
print("Combined List=",L3
L4=L3
L4.reverse()
print("Reversed List=",L4)
    
