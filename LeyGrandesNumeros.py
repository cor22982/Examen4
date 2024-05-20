import numpy as np

def monty_hall_law_of_large_numbers_10_doors(trials=10000):
    wins_change = 0
    wins_stay = 0
    
    for _ in range(trials):
        # 1. Colocar el premio detrás de una puerta al azar
        prize_door = np.random.randint(0, 10)
        
        # 2. Concursante elige una puerta al azar
        chosen_door = np.random.randint(0, 10)
        
        # 3. Monty abre 8 de las otras puertas que no tienen premio
        remaining_doors = [door for door in range(10) if door != chosen_door and door != prize_door]
        np.random.choice(remaining_doors, 8, replace=False)  # Monty opens 8 doors
        
        # 4. Concursante decide si quedarse o cambiar
        # Si se queda
        if chosen_door == prize_door:
            wins_stay += 1
        # Si cambia
        else:
            wins_change += 1
    
    return wins_stay, wins_change

trials = 1000000
wins_stay, wins_change = monty_hall_law_of_large_numbers_10_doors(trials)
print(f"Ganar sin cambiar: {wins_stay} ({(wins_stay / trials) * 100:.2f}%)")
print(f"Ganar cambiando: {wins_change} ({(wins_change / trials) * 100:.2f}%)")


