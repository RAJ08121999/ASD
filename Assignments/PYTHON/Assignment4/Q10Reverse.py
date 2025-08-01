num=int(input("Enter a number")) #1234

rev=0

while(num>0):#1234 is greater than 0 true   ,123>0      ,12>0       2>0     ,0>0->false ,out from loop
    digit=num%10        #1234%10=4  ,123%10=3       ,12%10=2        1%10=1
    rev=rev*10+digit    #0*10+4=4   ,4*10+3=43      ,43*10+2=432    432*10+1=4321
    num=num//10         #1234//10=123   ,123//10=12     ,12//10=1       ,2//10=0

print(rev)#printing rev value

