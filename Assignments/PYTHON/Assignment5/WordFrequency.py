import string

word_count={}

with open("data.txt","r") as file:
    for line in file:
        line=line.lower()
        line=line.translate(str.maketrans("","",string.punctuation))
        words=line.split()
        for word in words:
            word_count[word]=word_count.get(word,0)+1

for word,count in word_count.items():
    print(f"{word}:{count}")
    

# hello:5
# it:5
# is:5
# a:5
# sample:5
# file:5
# handling:5
# operation:5