total = 0
for number in range(1, 1001):
    if number % 3 == 0 or number % 5 == 0:
        total += number
print(total)
        
