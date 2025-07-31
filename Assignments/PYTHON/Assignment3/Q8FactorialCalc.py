num=int(input("Enter a positive integer"))
orginalNum=num

ans=1
while(num):
    ans*=num
    num-=1

print(f'factorial of {orginalNum} is {ans} ')