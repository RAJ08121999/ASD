user_input = int(input("Enter a number between 1 and 20: "))

print("Numbers from 1 to 20 excluding", user_input, ":")

for i in range(1, 21):
    if i == user_input:
        continue
    print(i)
