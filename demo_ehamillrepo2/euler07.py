# variables
number = 1
counter = 0
primelist = []
# checks for primes
def prime(x):
    for number in range(2, int(x **0.5) +1):
        if x % number == 0:
            return False
    return True
# if prime adds one, when at 10002, thats the 10001st prime
def primecounter(x):
    if prime(x) == True:
        global counter
        counter += 1
        primelist.append(x)
    if counter == 10002:
            return True
    return False
# 
while primecounter(number) == False:
    number += 1
print(max(primelist))
