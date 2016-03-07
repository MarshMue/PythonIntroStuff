import random

samples = 100000


list = [t*.01 for t in range(1, 100)]
list2 = [t*.01 for t in range(1, 100)]
for x in list2:
    wins = 0
    losses = 0
    for m in list:
        for n in range(samples):
            choice = random.random()
            opponent = random.random()
            # if choice is above threshold, compare to opponent
            if choice <= x:
                choice = random.random()
            if opponent <= m:
                opponent = random.random()
            if choice > opponent:
                wins += 1.0
            else:
                losses += 1.0

    winrat = wins / losses
    print "lim: " + str(x) + " wins/losses: " + str(winrat)
