def fractional_knapsack(n, W, items):
    items.sort(key=lambda x: x[0]/x[1], reverse=True)
    total_value = 0.0
    for value, weight in items:
        if W == 0:
            break
        fraction = min(weight, W)
        total_value += fraction * (value / weight)
        W -= fraction
    return total_value

# Lecture du fichier input.txt
with open('input.txt', 'r') as file:
    n, W = map(int, file.readline().split())
    items = []
    for _ in range(n):
        value, weight = map(int, file.readline().split())
        items.append((value, weight))

# Calcul de la valeur maximale
max_value = fractional_knapsack(n, W, items)

# Écriture du résultat dans output.txt
with open('output.txt', 'w') as file:
    file.write(f"{max_value:.4f}")