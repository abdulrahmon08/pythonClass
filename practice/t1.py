#Check student grade based on score
score = int(input("Input the student score: "))
if score >= 70 and score <= 100:
    grade = "A"
elif score >= 60 and score <= 69:
    grade = "B"
elif score >= 50 and score <= 59:
    grade = "C"
elif score >= 45 and score <= 49:
    grade = "D"
elif score >= 0 and score <= 44:
    grade = "F"
else:
    grade = "Invalid Score"
print("Grade:", grade)