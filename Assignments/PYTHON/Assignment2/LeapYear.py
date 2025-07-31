year=int(input("Enter the Year:"))

if(year%4==0):
    if(year%100==0):
        if(year%400==0):
            print("its a leap year")
        else:
            print("its not a leap year")
    else:
        print("its a leap year")
else:
    print("its not a leap year")
    
    
# agar koi year 4 se fully divisible hai to leap year hone k chances hai then check karna hoga ki kya ye ek century year hai matlab jo 100 se fully divisible ho agar hai to ye 400 se v fully divisible hona hi chahiye nahi to leap year nahi hoga

# conclusion agar koi year 4 ya 400 se divisible hai to leap year hoga