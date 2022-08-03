
i = 2520 
def div20(i):
    counter = 0
    for n in range (11, 20):
        if i % n == 0:
            counter += 1
        if counter == 9:
            return True
    return False             
        
while True:
    if div20(i) == True:
        print(i)
        break
    i += 2520
