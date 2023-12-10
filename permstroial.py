n=int(input("Enter a no."))
q=n//10
y=n%10
z=q//10
x=q%10
if(y==z):
    print("The no. is Palindrome")
else:
    print("The no. is not Palindrome")
if(x**3+y**3+z**3==n):
    print("The no. is Armstrong")
else:
    print("The no. is not Armstrong")
sum=0
i=2
while(i<=n):
    x=n//i
    if(n%i==0):
        sum=sum+x
    i=i+1
if(sum==n):
    print("The no.is perfect")
else:
    print("The no. is not perfect")
