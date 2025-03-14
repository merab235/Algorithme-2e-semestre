def max_prizes(n):
    prizes = []
    k = 0
    total = 0
    while total + (k + 1) <= n:
        k += 1
        prizes.append(k)
        total += k
    if total < n:
        prizes[-1] += n - total
    return k, prizes

# Lecture du fichier input.txt
with open('input.txt', 'r') as file:
    n = int(file.readline())

# Calcul des prix
k, prizes = max_prizes(n)

# Écriture du résultat dans output.txt
with open('output.txt', 'w') as file:
    file.write(f"{k}\n")
    file.write(" ".join(map(str, prizes)))