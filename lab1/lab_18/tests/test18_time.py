import time
import tracemalloc
from lab1.lab_18.src.task18 import min_cost_lunches

def test_cafe_coupons():
    n = 100  # Nombre de jours
    costs = [i * 3 for i in range(1, n + 1)]  # Coûts linéaires

    # Début du suivi de la mémoire
    tracemalloc.start()

    # Début du chronomètre
    start_time = time.time()

    result = min_cost_lunches(n, costs)

    # Fin du chronomètre
    end_time = time.time()

    # Fin du suivi de la mémoire
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    # Affichage des résultats
    print(f"Temps d'exécution pour l'exercice 18 : {end_time - start_time:.6f} secondes")
    print(f"Utilisation maximale de la mémoire : {peak / 10**6} MB")

test_cafe_coupons()