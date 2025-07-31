side1=int(input("Enter the First side of the Trinagle"))
side2=int(input("Enter the Second side of the Trinagle"))
side3=int(input("Enter the Third side of the Trinagle"))

if(side1==side2 and side1==side3):
    print("its a equilateral triangle")
elif(side1==side2 or side1==side3 or side2==side3):
    print("its a isosceles triangle")
else:
    print("its a scalene triangle")