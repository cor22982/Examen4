from pydtmc import MarkovChain
import numpy as np

def simulate_monty_hall_markov(trials=10000):
    # Definición de la matriz de transición para el problema Monty Hall con 10 puertas
    # Estados: 0 - Inicial, 1 - Puerta con premio elegida, 2 - Puerta sin premio elegida
    p_matrix = [
        [0, 0.1, 0.9],  # Desde estado inicial, 10% de elegir la puerta con premio, 90% sin premio
        [0, 1, 0],       # Si inicialmente eligió la puerta con premio, se mantiene en ese estado
        [0, 1, 0]        # Si cambia después de elegir una puerta sin premio, va al estado de premio (cambio forzado al premio)
    ]

    # Creación de la cadena de Markov
    mc = MarkovChain(p_matrix, ['Inicial', 'Premio', 'No Premio'])

    # Simulación de resultados
    wins_change = 0
    wins_stay = 0

    for _ in range(trials):
        initial_state = 0  # Siempre empezamos en el estado inicial
        if np.random.rand() < 0.1:
            final_state = 1  # Se queda con la puerta original que tiene el premio
        else:
            final_state = 2  # Cambia a la única otra puerta no abierta que tiene el premio

        if final_state == 1:
            wins_stay += 1
        if final_state == 2:
            wins_change += 1

    return wins_stay, wins_change

# Número de simulaciones
trials = 1000000
wins_stay, wins_change = simulate_monty_hall_markov(trials)
print(f"Staying wins: {wins_stay} ({(wins_stay / trials) * 100:.2f}%)")
print(f"Changing wins: {wins_change} ({(wins_change / trials) * 100:.2f}%)")
