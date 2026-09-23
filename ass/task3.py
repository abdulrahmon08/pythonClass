numbers = []

for i in range(10):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)

total = sum(numbers)
average = total / len(numbers)
highest = max(numbers)
lowest = min(numbers)

numbers.sort()

print("Total:", total)
print("Average:", average)
print("Highest Number:", highest)
print("Lowest Number:", lowest)
print("Ascending Order:", numbers)