import numpy as np

def monty_hall_markov(trials=10000):
    # Estados: 0 - Puerta con premio, 1-9 Puertas sin premio
    wins_change = 0
    wins_stay = 0
    transition_matrix = np.array([[0, 1], [1, 0]])  # Cambiar o quedarse

    for _ in range(trials):
        prize_door = np.random.randint(0, 10)
        chosen_door = np.random.randint(0, 10)
        
        if chosen_door == prize_door:
            state = 0  # Estado ganador
        else:
            state = 1  # Estado perdedor

        final_state = np.random.choice([0, 1], p=transition_matrix[state])
        if final_state == 0:
            wins_change += 1
        else:
            wins_stay += 1
            
    return wins_stay, wins_change
trials = 1000000
wins_stay, wins_change = monty_hall_markov(trials)
print(f"Staying wins: {wins_stay} ({(wins_stay / trials) * 100:.2f}%)")
print(f"Changing wins: {wins_change} ({(wins_change / trials) * 100:.2f}%)")
