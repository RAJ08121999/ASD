fruitsSet={"apple","banana","mango","litchi","apple"}

print(fruitsSet)
#{'litchi', 'mango', 'apple', 'banana'}
#here we can see that only unique values are printed and also it is unordered.


fruitsSet.add("chiku")

print(fruitsSet)
#{'chiku', 'litchi', 'apple', 'banana', 'mango'}
#using add function we can add only a single item at a time

#to add multiple items we use update method

fruitsSet.update(["orange","strawberry","etc"])
print(fruitsSet)
#{'banana', 'etc', 'chiku', 'mango', 'orange', 'apple', 'strawberry', 'litchi'}


fruitsSet.remove("apple")
print(fruitsSet)

#{'banana', 'orange', 'etc', 'chiku', 'strawberry', 'litchi', 'mango'} apple is removed from the fruitsSet
