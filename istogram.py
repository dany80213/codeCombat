import matplotlib.pyplot as plt
import numpy as np

# Number of simulations
simulations = 10000


def roll_4d6():
    return np.sum(np.random.randint(1, 7, 4))


def roll_2d12():
    return np.sum(np.random.randint(1, 13, 2))

# Simulate the rolls
rolls_4d6 = [roll_4d6() for _ in range(simulations)]
rolls_2d12 = [roll_2d12() for _ in range(simulations)]
print(roll_4d6())
print(roll_2d12())

plt.figure(figsize=(10, 6))


plt.hist(rolls_4d6, bins=range(4, 25), alpha=0.6, label='4d6', color='blue', edgecolor='black')

# Plot 2d12 distribution
plt.hist(rolls_2d12, bins=range(2, 25), alpha=0.6, label='2d12', color='red', edgecolor='black')

plt.title('Comparison of Dice Rolls: 4d6 vs 2d12')
plt.xlabel('Sum of Rolls')
plt.ylabel('Frequency')
plt.legend()
plt.grid(True)
plt.show()
