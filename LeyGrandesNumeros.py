import numpy as np

def monty_hall_law_of_large_numbers(trials=10000):
    wins_change = 0
    wins_stay = 0
    
    for _ in range(trials):
        prize_door = np.random.randint(0, 10)  # Premio detrás de una de las 3 puertas
        chosen_door = np.random.randint(0, 10)  # Puerta elegida por el participante
        
        # Monty abre una de las puertas que no tiene premio y que no es la elegida
        remaining_doors = [door for door in range(10) if door != chosen_door and door != prize_door]
        monty_opens = np.random.choice(remaining_doors)
        
        # Si el participante decide cambiar, cambia a la puerta restante
        if chosen_door == prize_door:
            wins_stay += 1
        else:
            wins_change += 1
    
    return wins_stay, wins_change

trials = 10000
wins_stay, wins_change = monty_hall_law_of_large_numbers(trials)
print(f"Ganadas sin cambiar: {wins_stay} ({(wins_stay / trials) * 100:.2f}%)")
print(f"Ganadas cambiando: {wins_change} ({(wins_change / trials) * 100:.2f}%)")
