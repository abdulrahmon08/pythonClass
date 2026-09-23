students = [
    "Ade", "Bola", "Chinedu", "David", "Esther",
    "Faith", "Grace", "Henry", "Ibrahim", "John"
]

while True:
    print("\n1. Add Student")
    print("2. Insert Student")
    print("3. Remove Student")
    print("4. Display Alphabetically")
    print("5. Display Reverse Order")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        students.append(name)

    elif choice == "2":
        name = input("Enter student name: ")
        position = int(input("Enter position: "))
        students.insert(position, name)

    elif choice == "3":
        name = input("Enter student name to remove: ")
        if name in students:
            students.remove(name)
        else:
            print("Student not found.")

    elif choice == "4":
        print(sorted(students))

    elif choice == "5":
        print(sorted(students, reverse=True))

    elif choice == "6":
        break

    else:
        print("Invalid choice")