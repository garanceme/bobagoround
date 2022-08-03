
import random

difficulty = input("what difficulty do you want (easy, medium, hard)? ")

if difficulty == 'easy':
    with open('easylist.txt' , 'r') as file:
        rlist = []
        for line in file:
            linefromog = line.strip()
            lineinlist = linefromog.split()
            rlist.append(lineinlist)
            randomeasylist = random.choice(rlist)
        print(randomeasylist)

elif difficulty == 'medium':
    with open('mediumlist.txt' , 'r') as file:
        rlist = []
        for line in file:
            linefromog = line.strip()
            lineinlist = linefromog.split()
            rlist.append(lineinlist)
            randommediumlist = random.choice(rlist)
        print(randommediumlist)

elif difficulty == 'hard':
    with open('hardlist.txt' , 'r') as file:
        rlist = []
        for line in file:
            linefromog = line.strip()
            lineinlist = linefromog.split()
            rlist.append(lineinlist)
            randomhardlist = random.choice(rlist)
        print(randomhardlist)


#data = file.readlines()
#randomhardlist = random.randint(0 , len data)
#print

