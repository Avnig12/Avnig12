L1=[]
n=int(input("Enter the no. the elements in the list:"))
for i in range(1,n+1):
    L=input("Enter the Element:")
    L1.append(L)
print("YOUR LIST IS=",L1)
L2=L1
L2.reverse()
print("Reversed list= ",L2)
