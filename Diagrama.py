import networkx as nx
import matplotlib.pyplot as plt

# Crear un grafo dirigido
G = nx.DiGraph()

# Añadir los nodos
G.add_node("Estado 0")
G.add_node("Estado 1")

# Añadir las aristas con las probabilidades de transición
G.add_edge("Estado 0", "Estado 0", weight=1, label="1.0 (Mantenerse)")
G.add_edge("Estado 0", "Estado 1", weight=1, label="1.0 (Cambiar)")
G.add_edge("Estado 1", "Estado 0", weight=1, label="1.0 (Cambiar)")

# Posiciones de los nodos
pos = nx.spring_layout(G)

# Dibujar el grafo
nx.draw(G, pos, with_labels=True, node_size=2000, node_color="lightblue", font_size=15, font_weight="bold", arrowsize=20)
edge_labels = nx.get_edge_attributes(G, 'label')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=12)

plt.title("Diagrama de Transiciones de Probabilidades de la Cadena de Markov")
plt.show()
