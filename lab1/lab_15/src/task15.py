# lecture.py
def lire_fichier(nom_fichier):
    """Lit le contenu du fichier et retourne la chaîne de caractères."""
    with open(nom_fichier, 'r') as f:
        return f.read().strip()

# traitement.py
def remove_invalid_brackets(s):
    """Supprime le nombre minimal de parenthèses pour obtenir une séquence correcte."""
    stack = []
    indices_to_remove = set()

    for i, char in enumerate(s):
        if char in "({[":
            stack.append((char, i))
        elif char in ")}]":
            if stack and ((stack[-1][0] == "(" and char == ")") or
                          (stack[-1][0] == "[" and char == "]") or
                          (stack[-1][0] == "{" and char == "}")):
                stack.pop()
            else:
                indices_to_remove.add(i)

    indices_to_remove.update({index for _, index in stack})

    return "".join([s[i] for i in range(len(s)) if i not in indices_to_remove])

# ecriture.py
def ecrire_fichier(nom_fichier, contenu):
    """Écrit le résultat dans un fichier."""
    with open(nom_fichier, 'w') as f:
        f.write(contenu)

# main.py
if __name__ == "__main__":
    input_file = "../txtf/input.txt"
    output_file = "../txtf/output.txt"

    texte = lire_fichier(input_file)
    resultat = remove_invalid_brackets(texte)
    ecrire_fichier(output_file, resultat)

    print("Résultat écrit dans", output_file)
