with open ("data.txt","r") as file:
    cleaned_lines=[line for line in file if line.strip()!= ""]
    
with open ("cleaned_data.txt","w") as outfile:
    outfile.writelines(cleaned_lines)
    
print("Empty lines removed output saved to new file cleaned_Data.txt")