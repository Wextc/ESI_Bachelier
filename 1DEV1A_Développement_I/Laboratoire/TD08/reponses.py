"""
TD 08 – Boucles for (solutions commentées)
HE2B ESI — 1DEV1A / 1DEVL1A (2025–2026)

⚠️ Note : chaque exercice est écrit sous forme de fonction pour garder la
séparation « module / programme principal ». Un petit menu en bas du
fichier vous permet de lancer chaque exercice rapidement.

Toutes les explications sont données en commentaires au-dessus ou à
l'intérieur du code.
"""

from __future__ import annotations
import unicodedata

# ---------------------------------------------------------------
# Utilitaires
# ---------------------------------------------------------------

def _strip_accents(s: str) -> str:
    """Retourne s en supprimant les accents (ex. 'é' -> 'e').
    Utile pour traiter les voyelles de manière simple.
    """
    return ''.join(
        c for c in unicodedata.normalize('NFD', s)
        if unicodedata.category(c) != 'Mn'
    )


# ===============================================================
# Exercice 1 — Boucles for avec une liste
# ---------------------------------------------------------------
# Dans le sujet, on part d'une boucle sur une liste littérale.
# Ici, on montre directement les 3 variantes demandées.
# ===============================================================

def ex1_listes() -> None:
    # 1) entiers impairs de 1 à 9
    print("Impairs de 1 à 9 :", end=" ")
    for i in [1, 3, 5, 7, 9]:  # on place explicitement les impairs
        print(i, end=" ")
    print()

    # 2) nombres 0, 0.25, 0.5, 0.75 et 1
    print("Quarts de 0 à 1 :", end=" ")
    for x in [0, 0.25, 0.5, 0.75, 1]:
        print(x, end=" ")
    print()

    # 3) les mots « une », « boucle », « for »
    for mot in ["une", "boucle", "for"]:
        print(mot)


# ===============================================================
# Exercice 2 — Boucle for avec range
# ---------------------------------------------------------------
# Rappels range(a, b) -> a, a+1, ..., b-1 ; range(stop) -> 0..stop-1 ;
# range(a, b, pas). On exploite range pour éviter d'énumérer les valeurs
# à la main.
# ===============================================================

def ex2_range() -> None:
    n = int(input("Entrez un entier n : "))

    # a) tous les entiers entre 1 et n (inclus)
    print("1..n :", end=" ")
    for i in range(1, n + 1):  # on va jusqu'à n inclus → n+1 en borne sup
        print(i, end=" ")
    print()

    # b) tous les entiers impairs entre 1 et n, sans 'if' (utiliser le pas)
    print("Impairs 1..n :", end=" ")
    for i in range(1, n + 1, 2):  # on saute de 2 en 2 → 1,3,5,...
        print(i, end=" ")
    print()

    # c) tous les entiers entre -n et n
    print("-n..n :", end=" ")
    for i in range(-n, n + 1):
        print(i, end=" ")
    print()


# ===============================================================
# Exercice 3 — Boucle for avec du texte
# ---------------------------------------------------------------
# Pour 'for c in mot:', la variable de boucle prend chaque caractère.
# ===============================================================

def ex3_texte() -> None:
    mot = input("Entrez un mot : ")
    for c in mot:
        print(c)


# ===============================================================
# Exercice 4 — Compteur d'itérations sans enumerate
# ---------------------------------------------------------------
# On affiche la position (1..len) et la lettre correspondante.
# ===============================================================

def ex4_compteur_sans_enumerate() -> None:
    mot = input("Entrez un mot : ")
    position = 1
    for c in mot:
        print(f"La lettre {position} est un {c}")
        position += 1  # on incrémente explicitement le compteur


# ===============================================================
# Exercice 5 — enumerate
# ---------------------------------------------------------------
# enumerate(sequence) renvoie des couples (indice, valeur). Par défaut,
# l'indice commence à 0 ; ici on ajoute 1 pour correspondre à l'énoncé.
# ===============================================================

def ex5_enumerate_puissances() -> None:
    valeurs = [76, 23, 18, 6, 5, 2]
    for i, val in enumerate(valeurs, start=1):  # start=1 → indices 1..n
        # On calcule val**i (puissance égale à la place dans la liste)
        print(f"{val}^{i} = {val ** i}")


# ===============================================================
# Exercice 6 — Somme des carrés des 100 premiers entiers
# ---------------------------------------------------------------
# On additionne i*i pour i allant de 1 à 100 inclus.
# ===============================================================

def ex6_somme_carres_100() -> None:
    total = 0
    for i in range(1, 101):
        total += i * i
    print("Somme des carrés de 1 à 100 :", total)


# ===============================================================
# Exercice 7 — Consonne ou voyelle
# ---------------------------------------------------------------
# On parcourt chaque lettre du mot et on indique si c'est une voyelle.
# On normalise les accents pour que 'é' soit traité comme 'e'.
# ===============================================================

def ex7_consonne_ou_voyelle() -> None:
    mot = input("Entrez un mot : ")
    voyelles = set("aeiouy")
    for c in mot:
        c_norm = _strip_accents(c.lower())
        if not c.isalpha():
            print(f"'{c}' n'est pas une lettre (ignoré)")
            continue
        if c_norm in voyelles:
            print(f"{c} → voyelle")
        else:
            print(f"{c} → consonne")


# ===============================================================
# Exercice 8 — Bagages dans l'avion
# ---------------------------------------------------------------
# On lit un nombre de passagers (1..10). Pour chacun : nom et poids de
# valise. Si poids > 10 kg, on signale un supplément. On calcule aussi le
# poids total.
# ===============================================================

def ex8_bagages() -> None:
    n = int(input("Nombre de passagers (1..10) : "))
    while n < 1 or n > 10:  # petite validation d'entrée
        n = int(input("Erreur : entrez un entier entre 1 et 10 : "))

    noms: list[str] = []
    for i in range(n):
        noms.append(input(f"Nom du passager {i+1} : "))

    total = 0.0
    for nom in noms:
        poids = float(input(f"Poids de la valise de {nom} (kg) : "))
        total += poids
        if poids > 10.0:
            print(f"{nom} : valise trop lourde (>10 kg) → supplément à payer")

    print(f"Poids total des valises : {total} kg")


# ===============================================================
# Exercice 9 — Palindrome
# ---------------------------------------------------------------
# On vérifie d'abord que l'entrée est un « mot » (que des lettres).
# Puis on compare les paires (1ère vs dernière, etc.), et on conclut.
# ===============================================================

def ex9_palindrome() -> None:
    mot = input("Entrez un mot : ")
    # Validation simple : uniquement des lettres (pas d'espace, pas de tiret)
    if not mot.isalpha():
        print("Erreur : veuillez entrer un mot composé uniquement de lettres.")
        return

    txt = _strip_accents(mot.lower())  # on baisse la casse et retire les accents
    txt_inverse = txt[::-1]

    # Comparaison paire par paire, en affichant le détail
    for i in range(len(txt)):
        gauche = txt[i]
        droite = txt_inverse[i]
        # droite correspond à txt[len-1-i]
        print(f"Lettre {i+1} : {gauche} vs {droite} → {'OK' if gauche == droite else '≠'}")

    if txt == txt_inverse:
        print(f"→ '{mot}' est un palindrome.")
    else:
        print(f"→ '{mot}' n'est pas un palindrome.")


# ===============================================================
# Petit menu pour exécuter facilement un exercice depuis ce script.
# ===============================================================

if __name__ == "__main__":
    print("TD08 — Boucles for : choisissez un exercice à lancer")
    print("1: ex1_listes")
    print("2: ex2_range")
    print("3: ex3_texte")
    print("4: ex4_compteur_sans_enumerate")
    print("5: ex5_enumerate_puissances")
    print("6: ex6_somme_carres_100")
    print("7: ex7_consonne_ou_voyelle")
    print("8: ex8_bagages")
    print("9: ex9_palindrome")

    choix = input("Votre choix (1-9) ou ENTER pour quitter : ")
    actions = {
        "1": ex1_listes,
        "2": ex2_range,
        "3": ex3_texte,
        "4": ex4_compteur_sans_enumerate,
        "5": ex5_enumerate_puissances,
        "6": ex6_somme_carres_100,
        "7": ex7_consonne_ou_voyelle,
        "8": ex8_bagages,
        "9": ex9_palindrome,
    }
    action = actions.get(choix)
    if action is not None:
        action()
    else:
        print("Au revoir !")
