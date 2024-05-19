import numpy as np

def monty_hall_markov(trials=10000):
    wins_change = 0
    wins_stay = 0
    for _ in range(trials):
        prize_door = np.random.randint(0, 10)
        chosen_door = np.random.randint(0, 10)
        if chosen_door == prize_door:
            wins_stay += 1
        else:
            wins_change += 1
    return wins_stay, wins_change

trials = 10000
wins_stay, wins_change = monty_hall_markov(trials)
print(f"Staying wins: {wins_stay} ({(wins_stay / trials) * 100:.2f}%)")
print(f"Changing wins: {wins_change} ({(wins_change / trials) * 100:.2f}%)")
