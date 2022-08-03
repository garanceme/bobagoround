# variables
sosq = []
sqos = []
a = 0
b = 0

# creates 1-100 list
def squareofsums(x):
    global a 
    for i in range (1, 101):
        sqos.append(i)
        a += 1
        if a == 100:
            return True
    return False

# creates list of 1 - 100 individually squared
def sumofsquares(x):
    global b
    for i in range (1, 101):
        sosq.append(i **2)
        i **2
        b += 1
        if b == 100:
            return True
    return False

# calls both functions, performs necessary math, subtracts them, then prints answer 
for i in range (1, 101):
    if squareofsums(i) == True and sumofsquares(i) == True:
        print((sum(sqos)**2)-(sum(sosq)))


