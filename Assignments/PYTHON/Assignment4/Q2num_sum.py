def number_sum(num):
    ans=0
    while(num>0):
        ans+=num%10
        num//=10
    return ans

num=int(input("Enter a number"))

ans = number_sum(num)

print(f'the sum of the digits is {ans}')