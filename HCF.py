n=int(input("Enter a no.="))
m=int(input("Enter a no.="))
i=1
while(i<n):
    if(n%i==0 and m%i==0):
        HCF=i
    i=i+1
print("HCF=",HCF)
x=n*m
LCM=x/HCF
print("LCM=",LCM)
