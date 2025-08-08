import re

with open("data.txt","r")as file:
    content=file.read()

pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

emails=re.findall(pattern,content)

unique_emais = sorted(set(emails))

print(f"Total unique emails found:{len(unique_emais)}")
print("\n Emails in alphabetical order:")

for email in unique_emais:
    print(email)