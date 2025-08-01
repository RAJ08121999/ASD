students={
    "raj":98,
    "ramesh":89,
    "himesh":23,
    "roshni":54,
    "saran":89
}
print(students)
#{'raj': 98, 'ramesh': 89, 'himesh': 23, 'roshni': 54, 'saran': 89}

#created a dictionary of students where names are the keys and marks are their corresponding values


#adding a student in the dictionary

students["neha"]=80

print(students)
#{'raj': 98, 'ramesh': 89, 'himesh': 23, 'roshni': 54, 'saran': 89, 'neha': 80}

students["raj"]=100

print(students)
#{'raj': 100, 'ramesh': 89, 'himesh': 23, 'roshni': 54, 'saran': 89, 'neha': 80} 
#updated the marks of raj

del students["ramesh"]
print(students)
#{'raj': 100, 'himesh': 23, 'roshni': 54, 'saran': 89, 'neha': 80} ramesh has deleted from the dictionary

highest_student=max(students,key=students.get)
highestMarks=students[highest_student]

print(f"Topper is {highest_student} with {highestMarks} marks")

#Topper is raj with 100 marks