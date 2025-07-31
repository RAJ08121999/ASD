ans=0


while(True):
    num=int(input("Enter a number:"))
    ans+=num
    print(f'the value of sum is ',ans)
    if(ans>=100):
        print(f'we have reached the maxlimit',ans)
        break
    