students= [
    "Ade", "Bola", "Chinedu", "David", "Esther", "Faith", "Grace", "Henry", "Ibrahim", "John"
]
#To add a new student to the list
new_students = input("Enter new student: ")
students.append(new_students)

#To insert a student at a specific position
name = input("Enter student name to insert: ")
position = int(input("Enter position: "))
students.insert(position, name)

#To remove a student from the list
remove_student = input("Enter student name to remove: ")
if remove_student in students:
    students.remove(remove_student)
else:
    print("Student not found.")
    
#To display the list of students in alphabetical order
print("Students in alphabetical order:")
print(sorted(students))

#To display the list of students in reverse order
print("Students in reverse order:")
print(students[::-1])