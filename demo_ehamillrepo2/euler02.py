total = 0
x = 0
y = 1
while x <= 4000000:
    y = x + y
    x = y - x
    if y % 2 == 0:
        total += y
print(total)


#fib formula, while loop = if statemeant loop, equations on different lines
    
    
    
    
