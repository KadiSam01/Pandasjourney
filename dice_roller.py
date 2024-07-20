import random
import matplotlib.pyplot as plt

rolls = []
for times in range(1000000):
    roll = random.randint(1,6)+random.randint(1,6)
    rolls.append(roll)
    #number = myList.randint(2,12) #random.randint(1,5)

   # print(len(rolls))
    #print(rolls)
counts = []
for sum_ in range(2,13):
    counts += [rolls.count(sum_)]
plt.bar(range(2,13), counts)
plt.show()