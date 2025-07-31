def convert_temp(temp):
    fahrenheit=(temp*9/5)+32
    return fahrenheit

temp=int(input("Enter Temperature in celsius"))

print(convert_temp(temp))

