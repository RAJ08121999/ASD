initialBalane=5000

withdrawlAmout=int(input("Enter Amount to WithDrawl"))

if(withdrawlAmout<=initialBalane):
    initialBalane-=withdrawlAmout
    print("Withdrawl Successfull \n New Balance is:",initialBalane)
else:
    print("Insufficient balance")