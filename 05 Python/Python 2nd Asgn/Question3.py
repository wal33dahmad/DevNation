import random

times = int(input("How many times would you like to roll the dice? "))
luckyTime = 0

for i in range(times):
    no1 = random.randint(1,6)
    no2 = random.randint(1,6)
    if (no1 + no2) == 7:
        luckyTime = luckyTime + 1
    print("(", no1, ",", no2, ")")
    print("Dice roll ", i+1 ," sum: ", no1+no2)

print("You Rolled Lucky Seven '", luckyTime, "' time(s)")