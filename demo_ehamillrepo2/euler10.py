# variables 
i = 1
x = 2000000
import math
primelist = []
# prime checker 
def is_prime(i):
    if i > 1:
        if i == 2:
            return True
        if i % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(i) + 1), 2):
            if i % current == 0: 
                return False
        return True
    return False
# runs prime checker for #'s 1 - 2 mil, appends primes to a list and prints the sum of the primes.
while i <= x:
    i += 1
    if is_prime(i) == True:
        primelist.append(i)
    
print(sum(primelist))
    
