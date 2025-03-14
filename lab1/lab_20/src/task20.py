def count_almost_palindromes(N, K, S):
    count = 0
    for i in range(N):
        for j in range(i + 1, N + 1):
            substring = S[i:j]
            changes_needed = 0
            left = 0
            right = len(substring) - 1
            while left < right:
                if substring[left] != substring[right]:
                    changes_needed += 1
                left += 1
                right -= 1
            if changes_needed <= K:
                count += 1
    return count

# Lecture du fichier input.txt
with open('../txtf/input.txt', 'r') as file:
    N, K = map(int, file.readline().split())
    S = file.readline().strip()

# Calcul du nombre de sous-chaînes presque palindromes
result = count_almost_palindromes(N, K, S)

# Écriture du résultat dans output.txt
with open('../txtf/output.txt', 'w') as file:
    file.write(f"{result}")