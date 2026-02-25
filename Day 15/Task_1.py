import itertools

actions = ["Click", "Scroll", "Exit"]

# Generate all possible pairs (2 consecutive actions)
sample_space = list(itertools.product(actions, repeat=2))

print("Sample Space:")
print(sample_space)

print("Total Outcomes:", len(sample_space))

# Count outcomes with at least one "Click"
favorable = [outcome for outcome in sample_space if "Click" in outcome]

print("Favorable Outcomes:")
print(favorable)

probability = len(favorable) / len(sample_space)

print("Probability of at least one Click:", probability)

import random

trials = 1000
count_sum_7 = 0

for _ in range(trials):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    
    if dice1 + dice2 == 7:
        count_sum_7 += 1

experimental_probability = count_sum_7 / trials

print("Experimental Probability of sum = 7:", experimental_probability)
