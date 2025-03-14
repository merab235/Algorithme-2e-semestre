def lire_fichier(nom_fichier):
    """Lit le fichier et retourne les valeurs sous forme de liste d'entiers."""
    with open(nom_fichier, 'r') as f:
        lignes = f.readlines()
    n = int(lignes[0].strip())  # Nombre d'éléments
    valeurs = list(map(int, lignes[1].strip().split()))  # Liste des valeurs
    return n, valeurs

def peut_diviser_en_trois(valeurs):
    """Vérifie si on peut diviser les valeurs en trois sous-ensembles de même somme."""
    total = sum(valeurs)

    # Si la somme totale n'est pas divisible par 3, c'est impossible
    if total % 3 != 0:
        return 0

    cible = total // 3  # Chaque sous-ensemble doit avoir cette somme
    n = len(valeurs)

    # Tableau DP pour voir si on peut former 3 sous-ensembles de somme `cible`
    dp = [[[False] * (cible + 1) for _ in range(cible + 1)] for _ in range(n + 1)]
    dp[0][0][0] = True

    for i in range(1, n + 1):
        val = valeurs[i - 1]
        for j in range(cible, -1, -1):
            for k in range(cible, -1, -1):
                dp[i][j][k] = dp[i - 1][j][k]
                if j >= valeurs[i - 1]:
                    dp[i][j][k] = dp[i][j][k] or dp[i - 1][j - valeurs[i - 1]][k]
                if k >= valeurs[i - 1]:
                    dp[i][j][k] = dp[i][j][k] or dp[i - 1][j][k - valeurs[i - 1]]

    return 1 if dp[n][cible][cible] else 0

def ecrire_fichier(nom_fichier, contenu):
    """Écrit le résultat dans un fichier."""
    with open(nom_fichier, 'w') as f:
        f.write(str(contenu))

# Programme principal
if __name__ == "__main__":
    input_file = "input.txt"
    output_file = "output.txt"

    _, valeurs = lire_fichier(input_file)
    resultat = peut_diviser_en_trois(valeurs)
    ecrire_fichier(output_file, resultat)

    print("Résultat écrit dans", output_file)
