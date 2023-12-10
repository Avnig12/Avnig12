str1=input("Enter a string:")
al=0
num=0
for i in str1:
    if(i.isalpha()==True):
        al=al+1
    elif(i.isnumeric()==True):
        num=num+1
print("Number of alphbets=",al)
print("Number of digits=",num)
