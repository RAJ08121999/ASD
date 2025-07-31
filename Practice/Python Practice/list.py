myList=["raj",2334,True,"asif"]

print(myList)

print(type(myList))

myList2=list(#creating a list using list constructor
    {"C","c++",123,True}
)

print(type(myList2))

print(myList2[3])#accessing the list using indices,,indexing starts with 0
print(myList2[-4])#accessing the list using negative indices,,indexing starts with -1 at rightmost index


#python lists are mutable that means we can change its values

myList2[2]="raj",

print(myList2)