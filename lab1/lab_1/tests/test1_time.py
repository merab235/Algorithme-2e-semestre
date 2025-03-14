import time
import tracemalloc
from lab1.lab_1.src.task1 import fractional_knapsack

def test_fractional_knapsack():
    n = 1000  # Nombre d'objets
    W = 2000000  # Capacité du sac à dos
    items = [(i, i) for i in range(1, n + 1)]  # Objets avec poids et valeur égaux

    # Début du suivi de la mémoire
    tracemalloc.start()

    # Début du chronomètre
    start_time = time.time()

    result = fractional_knapsack(n, W, items)

    # Fin du chronomètre
    end_time = time.time()

    # Fin du suivi de la mémoire
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    # Affichage des résultats
    print(f"Temps d'exécution pour l'exercice 1 : {end_time - start_time:.6f} secondes")
    print(f"Utilisation maximale de la mémoire : {peak / 10**6} MB")

test_fractional_knapsack()