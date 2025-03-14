import time
import tracemalloc
from lab1.lab_19.src.task19 import matrix_chain_order, print_optimal_parentheses

def test_matrices_product():
    p = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]  # Dimensions des matrices

    # Début du suivi de la mémoire
    tracemalloc.start()

    # Début du chronomètre
    start_time = time.time()

    m, s = matrix_chain_order(p)
    result = print_optimal_parentheses(s, 0, len(p) - 2)

    # Fin du chronomètre
    end_time = time.time()

    # Fin du suivi de la mémoire
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    # Affichage des résultats
    print(f"Temps d'exécution pour l'exercice 19 : {end_time - start_time:.6f} secondes")
    print(f"Utilisation maximale de la mémoire : {peak / 10**6} MB")

test_matrices_product()