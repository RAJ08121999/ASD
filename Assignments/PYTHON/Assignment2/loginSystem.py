userName='raj'
password=1234

UserName=input("Enter User Name")
Password=int(input("Enter Password"))

if(userName==UserName):
    if(password==Password):
        print("Login SuccessFull")
    else:
        print("Username/Password mismatch")
else:
    print("Username/Password mismatch")