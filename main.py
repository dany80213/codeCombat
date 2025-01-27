from random import randint
hp = 30
turns = 0

print(f"Initial health points:{hp}")
while hp > 0:
    turns += 1
    roll = randint(1,6)
    print(f"Damage taken: {roll}")
    hp -= roll
    print(f"Remaining health is {hp if hp > 0 else 0}")

print(f"The character has been defeated.\n{turns} turns were played.")

