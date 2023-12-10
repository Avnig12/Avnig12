n=int(input("Enter a no:"))
i=2
f=1
while(i<n):
    if(n%i==0):
        f=0
        i=i+1
if(f==0):
    print("Composite")
else:
    print("Prime")
