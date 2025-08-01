num1=int(input("Enter first number"))
num2=int(input("Enter second number"))


add=lambda x,y:num1+num2

print(f'The sum of {num1}+{num2} is {add(num1,num2)}')

#x and y are parameters and num1+num2 is the operation
#add is the function variable which will store the anonymous function defined using lambda
