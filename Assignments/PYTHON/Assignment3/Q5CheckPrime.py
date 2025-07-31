num=int(input("Enter a number"))
flag=True

if(num==1):
    print("Its not a prime number")

for i in range(2,int(num**0.5),+1):
    if(num%i==0):
        flag=False
    else:
        flag=True
else:
    print("program run successfully")

if flag==True:
    print("Its  a prime number")
else:
    print("Its not a prime number")