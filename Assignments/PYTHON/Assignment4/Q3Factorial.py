def fact(num):
    ans=1
    while(num>0):
        ans*=num
        num-=1
    return ans

num=int(input("Enter a number"))
ans=fact(num)

print(f"The factorial of {num} is {ans}")