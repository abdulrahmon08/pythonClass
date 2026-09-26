even_numbers = []
odd_numbers = []

for i in range (1, 101):
    if i % 2 == 0:
        even_numbers.append(i)
    else:
        odd_numbers.append(i)
    sum_even = sum(even_numbers)
    sum_odd = sum(odd_numbers)
print("Even Numbers:", even_numbers)
print("Odd Numbers:", odd_numbers)
print("Sum of Even Numbers:", sum_even)
print("Sum of Odd Numbers:", sum_odd)
