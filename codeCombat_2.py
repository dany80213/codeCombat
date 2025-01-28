from random import randint
from statistics import mean



def res_dice(string):
    """
    Roll multiple dice and return results, sum, and maximum.

    :param string: String of dice to roll
    :return: A integer containing:
             - The sum of all rolls
    """
    n,m = map(int,string.split("d"))
    somma = sum(randint(1,m) for i in range(n))
    return somma
win_1 = 0
win_2 = 0
turns_list = []

#Simulate 1000 games and count wins for each player
for i in range(1000):
    hp_1 = randint(80,100) # hp player 1
    hp_2 = randint(80,100) # hp player 2
    shield_1 = randint(5,10) #shield player 1
    shield_2 = randint(5,10) #shield player 2
    roll_1 = "4d6"
    roll_2 = "4d6"
    #roll_1 = "4d6"
    #roll_2 = "2d12"
    turns = 0

    #print(f"Player1 starting health: {hp_1}")
    #print(f"Player1  shield: {shield_1}")
    #print(f"Player2 starting health: {hp_2}")
    #print(f"Player2  shield: {shield_2}")
    while hp_1 > 0 and hp_2 > 0:
        turns += 1
        #print(f"Turns {turns}")
        damage_1 = max(res_dice(roll_1)- shield_2,0)
        damage_2 = max(res_dice(roll_2) - shield_1,0)
        hp_1 -= damage_2
        hp_2 -= damage_1
        #print(f"[Player1] Damage: {damage_1}")
        #print(f"[Player2] Health: {hp_2}")
        #print("-----")
        #print(f"[Player2] Damage: {damage_2}")
        #print(f"[Player1] Health: {hp_1}")

    #print(f"Game ended. Turns played: {turns}")

    if hp_2 <= 0 and hp_1 <= 0:
        pass
        #print("Draw. Both players are defeated.")
    elif hp_1 <= 0:
        #print("Player 2 wins!")
        win_2 += 1
    else:
        #print("Player 1 wins!")
        win_1 += 1

    turns_list.append(turns)

if win_1 > win_2:
    print(f"Player 1 wins {win_1} out of 1000 games.")
    print(f"Average turns per game: {mean(turns_list):.0f}")
else:
    print(f"Player 2 wins {win_2} out of 1000 games.")
    print(f"Average turns per game: {mean(turns_list):.0f}")



