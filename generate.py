import random 
import statistics

# flipping a coin
coin = random.choice(["heads", "tails"])


# schuffle cards
cards = ["jack", "queen", "king"]

random.shuffle(cards)

print(cards)


# find mean 
my_mean = statistics.mean([100, 96, 43])

print(my_mean)