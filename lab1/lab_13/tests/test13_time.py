import time
import tracemalloc
import resource
from lab1.lab_13.src.task13 import peut_diviser_en_trois

def test_time_and_memory():
    # Données d'entrée pour le test
    valeurs = [17, 59, 34, 57, 17, 23, 67, 1, 18, 2, 59]  # Exemple de valeurs

    # Début du suivi de la mémoire
    tracemalloc.start()

    # Début du chronomètre
    start_time = time.time()

    # Appel de la fonction
    result = peut_diviser_en_trois(valeurs)

    # Fin du chronomètre
    end_time = time.time()

    # Fin du suivi de la mémoire
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    # Mesure de l'utilisation des ressources système
    usage_after = resource.getrusage(resource.RUSAGE_SELF)
    cpu_time = usage_after.ru_utime  # Temps CPU utilisé
    memory_usage = usage_after.ru_maxrss  # Mémoire maximale utilisée (en Ko)

    # Affichage des résultats
    print(f"Résultat : {result}")
    print(f"Temps d'exécution : {end_time - start_time:.6f} secondes")
    print(f"Utilisation maximale de la mémoire : {peak / 10**6} MB")
    print(f"Temps CPU utilisé : {cpu_time:.6f} secondes")
    print(f"Mémoire max RSS : {memory_usage} Ko")

# Exécution du test
test_time_and_memory()