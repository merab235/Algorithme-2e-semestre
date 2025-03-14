import time
import tracemalloc
from lab1.lab_15.src.task15 import remove_invalid_brackets

def test_remove_parentheses():
    s = "({[]})" * 1000  # Chaîne de 6000 caractères

    # Début du suivi de la mémoire
    tracemalloc.start()

    # Début du chronomètre
    start_time = time.time()

    result = remove_invalid_brackets(s)

    # Fin du chronomètre
    end_time = time.time()

    # Fin du suivi de la mémoire
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    # Affichage des résultats
    print(f"Temps d'exécution pour l'exercice 15 : {end_time - start_time:.6f} secondes")
    print(f"Utilisation maximale de la mémoire : {peak / 10**6} MB")

test_remove_parentheses()