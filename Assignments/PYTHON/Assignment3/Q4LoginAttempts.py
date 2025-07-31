correctPassword='python123'

count=0

while(True):
    password=input("Enter the Password")
    if password!=correctPassword:
        count+=1
        if count>2:
            print("Account Locked")
            break
    elif password==correctPassword:
        print("Login Successfull")
        break
