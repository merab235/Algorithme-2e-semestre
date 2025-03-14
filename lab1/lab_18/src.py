def min_cost_lunches(n, costs):
    # dp[i][j] : coût minimal pour les i premiers jours avec j coupons restants
    dp = [[float('inf')] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 0  # Coût initial avec 0 coupons

    for i in range(n):
        for j in range(n):
            if dp[i][j] != float('inf'):
                # Cas 1 : Ne pas utiliser de coupon
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + costs[i])
                # Cas 2 : Utiliser un coupon si disponible
                if j > 0:
                    dp[i + 1][j - 1] = min(dp[i + 1][j - 1], dp[i][j])
                # Cas 3 : Obtenir un nouveau coupon si le coût est > 100
                if costs[i] > 100:
                    dp[i + 1][j + 1] = min(dp[i + 1][j + 1], dp[i][j] + costs[i])

    # Trouver le coût minimal avec 0 coupons restants
    result = min(dp[n][j] for j in range(n + 1))
    return result


# Lecture du fichier input.txt
with open('input.txt', 'r') as file:
    n = int(file.readline())
    costs = [int(file.readline()) for _ in range(n)]

# Calcul du coût minimal
result = min_cost_lunches(n, costs)

# Écriture du résultat dans output.txt
with open('output.txt', 'w') as file:
    file.write(f"{result}")