import numpy as np

# Partie A : Les données
#print("Partie A:\n")
observations = [
    [("B", "T", "G"), ("B", "T", "G"), ("B", "T", "P")],
    [("D", "T", "G"), ("D", "T", "G"), ("B", "T", "P")],
    [("D", "T", "G"), ("D", "T", "G"), ("B", "T", "P")],
    [("D", "T", "G"), ("D", "T", "G"), ("D", "T", "P")],
    [("B", "T", "G"), ("B", "T", "G"), ("D", "T", "P")],
    [("B", "S", "G"), ("B", "S", "G"), ("D", "S", "P")],
    [("B", "S", "G"), ("B", "S", "G"), ("B", "S", "P")],
    [("D", "S", "G"), ("D", "S", "G"), ("D", "S", "P")]
]
#print(observations)

def generate_alea(n):
    print("\n")
    table = []
    for _ in range(n):
        ligne = []
        for _ in range(3):
            x1 = np.random.choice(['B', 'D'])
            x2 = np.random.choice(['T', 'S'])
            x3 = np.random.choice(['G', 'P'])
            ligne.append((x1,x2,x3))
        table.append(ligne)
    
    return table
#print(generate_alea(3))

#print("\nPartie B:\n")

def generate_DTG(n):
    table = []
    choix = ['D','T','G']
    for _ in range(n):
        triplet = np.random.choice(choix, size=3, replace=False)
        triplet_liste = list(triplet)
        table.append(triplet_liste)
    return table

print(generate_DTG(10))

