numbers=[1,2,3,4,5,6,7]#this is a list of numbers

print(numbers)#[1, 2, 3, 4, 5, 6, 7]

numbers.append(8)

print(numbers)#[1, 2, 3, 4, 5, 6, 7, 8] append means adding an item in the last index

numbers.remove(4)
print(numbers)#[1, 2, 3, 5, 6, 7, 8] 4 is removed from the list

numbers.sort(reverse=True)
print(numbers)#it will first sort in ascending order then it will reverse the list to make it in descending order
#[8, 7, 6, 5, 3, 2, 1]

numbers.extend([4,9,10])#extend takes only one argument but i have to send multiple numbers so i made it a list then sending now python will consider it one argument as it is a single list 
numbers.sort()#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers)
#creating a list from 1 to 10 numbers

ans=0
for i in numbers:
    ans+=i #the sum from 1 to 10 will be stored in ans 
    avg=ans/len(numbers)#then avg will be calculated 
    
print(f'the average is {avg}')