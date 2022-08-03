# filter primes
# filter largest
x = 600851475143
primelist = []
# prime checker 
def factor(x):
    for i in range(2, x - 1):
        if x % i == 0:
            return False
    return True
# calls fucntion runs through #2-x, checks if its a factor and a prime then prints i
for i in range(2, x - 1):
    if x % i == 0 and factor(i) == True:
        print(i)
        primelist.append(i)

print(max(primelist))
            
    
