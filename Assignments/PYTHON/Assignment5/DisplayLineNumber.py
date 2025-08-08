with open("data.txt","r") as file:
    for line_number,line in enumerate (file,start=1):
        print(f"{line_number}:{line.strip()}")

# 1:hello it is a sample file handling operation
# 2:hello it is a sample file handling operation
# 3:hello it is a sample file handling operation
# 4:hello it is a sample file handling operation
# 5:hello it is a sample file handling operation

# line_number is holding the current line_number and line is holding the text in each corresponding line_number.