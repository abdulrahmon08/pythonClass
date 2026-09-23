score = int(input("Enter student's score: "))

if 70 <= score <= 100:
    grade = "A"
elif 60 <= score <= 69:
    grade = "B"
elif 50 <= score <= 59:
    grade = "C"
elif 45 <= score <= 49:
    grade = "D"
elif 0 <= score <= 44:
    grade = "F"
else:
    grade = "Invalid Score"

print("Grade:", grade)