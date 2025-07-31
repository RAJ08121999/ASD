char=input("Enter a character")
vowel=['a','e','i','o','u','A','E','I','O','U']
digit=['1','2','3','4','5','6','7','8','9','0']
specialChar=['~','@','#','%','^','&','*','(',')','-','_','=','+',':',';','"',',','<','>','?','/','\\','|']

if char in vowel:
    print("It's a vowel letter")
elif char in digit:
    print("Its a digit")
elif char in specialChar:
    print("its a special character")
else:
    print("its a consonant letter")