import time
import tracemalloc
from lab1.lab_20.src.task20 import count_almost_palindromes

def test_almost_palindrome():
    N = 5000  # Longueur du mot
    K = 1000  # Nombre maximal de changements
    S = "a" * N  # Mot composé de 'a'

    # Début du suivi de la mémoire
    tracemalloc.start()

    # Début du chronomètre
    start_time = time.time()

    result = count_almost_palindromes(N, K, S)

    # Fin du chronomètre
    end_time = time.time()

    # Fin du suivi de la mémoire
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    # Affichage des résultats
    print(f"Temps d'exécution pour l'exercice 20 : {end_time - start_time:.6f} secondes")
    print(f"Utilisation maximale de la mémoire : {peak / 10**6} MB")

test_almost_palindrome()