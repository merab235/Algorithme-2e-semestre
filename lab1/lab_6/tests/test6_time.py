import time
import tracemalloc
from lab1.lab_6.src.task6 import max_prizes

def test_max_prizes():
    n = 10**9  # Nombre de bonbons

    # Début du suivi de la mémoire
    tracemalloc.start()

    # Début du chronomètre
    start_time = time.time()

    k, prizes = max_prizes(n)

    # Fin du chronomètre
    end_time = time.time()

    # Fin du suivi de la mémoire
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    # Affichage des résultats
    print(f"Temps d'exécution pour l'exercice 6 : {end_time - start_time:.6f} secondes")
    print(f"Utilisation maximale de la mémoire : {peak / 10**6} MB")

test_max_prizes()