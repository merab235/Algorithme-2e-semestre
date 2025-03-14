def matrix_chain_order(p):
    n = len(p) - 1
    m = [[0] * n for _ in range(n)]
    s = [[0] * n for _ in range(n)]

    for l in range(2, n + 1):  # l est la longueur de la chaîne
        for i in range(n - l + 1):
            j = i + l - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                cost = m[i][k] + m[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                if cost < m[i][j]:
                    m[i][j] = cost
                    s[i][j] = k

    return m, s


def print_optimal_parentheses(s, i, j):
    if i == j:
        return "A"
    else:
        return f"({print_optimal_parentheses(s, i, s[i][j])}{print_optimal_parentheses(s, s[i][j] + 1, j)})"


# Lecture du fichier input.txt
with open('input.txt', 'r') as file:
    n = int(file.readline())
    p = []
    for _ in range(n):
        a, b = map(int, file.readline().split())
        p.append(a)
    p.append(b)  # Ajouter le dernier nombre de colonnes

# Calcul de l'ordre optimal
m, s = matrix_chain_order(p)
optimal_parentheses = print_optimal_parentheses(s, 0, n - 1)

# Écriture du résultat dans output.txt
with open('output.txt', 'w') as file:
    file.write(optimal_parentheses)