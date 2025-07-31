unit=int(input("Enter the Unit of Electricity You Used:"))

if(unit<=100):
    print(f" Pay Rs. {unit} X {5} = ",unit*5)
elif(unit>100 and unit<200):
    print(f" Pay Rs. {unit} X {8} = ",unit*8)
else:
    print(f" Pay Rs. {unit} X {10} = ",unit*10)