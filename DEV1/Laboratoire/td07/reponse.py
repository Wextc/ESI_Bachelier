"""
TD 07 – Boucles while (solutions commentées)
HE2B ESI — 1DEV1A / 1DEVL1A (2025–2026)

⚠️ Note : chaque exercice est écrit sous forme de fonction afin de
respecter la séparation « module / programme principal ». Le bloc
`if __name__ == "__main__":` au bas du fichier contient un petit menu
permettant de lancer un exercice précis. Vous pouvez aussi importer ce
fichier et appeler directement les fonctions voulues pour vos tests
unitaires.

Toutes les explications sont données en commentaires au-dessus ou
à l'intérieur du code.
"""

from __future__ import annotations
import math
import random

# ===============================================================
# Exercice 1 — Boucles while
# ---------------------------------------------------------------
# Objectif : demander un entier n (avec n >= 1) puis afficher les
# entiers de 1 à n au moyen d'une boucle while.
#
# Idée clé :
#  - initialiser un compteur à 1
#  - tant que compteur <= n, afficher puis incrémenter
#  - cela illustre la mécanique « initialisation → condition → mise à jour »
# ===============================================================

def ex1_afficher_1_a_n() -> None:
    n = int(input("Entrez un entier n (n >= 1) : "))
    # Sécurité minimale pour rester dans l'esprit de l'exercice.
    while n < 1:
        n = int(input("n doit être >= 1. Réessayez : "))

    compteur = 1
    while compteur <= n:  # la condition de boucle
        print(compteur)
        compteur = compteur + 1  # mise à jour indispensable sinon boucle infinie


# ===============================================================
# Exercice 2 — Boucles while dans une fonction
# ---------------------------------------------------------------
# Demander un entier (fonction 1) et afficher 1..n (fonction 2),
# puis relier les deux comme indiqué.
# ===============================================================

def demander_entier() -> int:
    """Demande un entier >= 1 à l'utilisateur et le renvoie.
    On boucle tant que la saisie ne respecte pas la contrainte.
    """
    n = int(input("Entrez un entier (>= 1) : "))
    while n < 1:
        n = int(input("Erreur : l'entier doit être >= 1. Réessayez : "))
    return n


def afficher_premiers_entiers(n: int) -> None:
    """Affiche les entiers de 1 à n (inclus)."""
    i = 1
    while i <= n:
        print(i)
        i += 1


def ex2_demo() -> None:
    afficher_premiers_entiers(demander_entier())


# ===============================================================
# Exercice 3 — Suites d'entiers
# ---------------------------------------------------------------
# Demander n et afficher :
#  - les nombres pairs entre 1 et n
#  - les nombres de -n à n
#  - les multiples de 5 entre 1 et n
#  - les multiples de n entre 1 et 100
# 
# Astuces :
#  - utiliser un compteur, tester la parité ou le modulo
#  - pour -n..n, partir de -n et incrémenter
# ===============================================================

def ex3_suites() -> None:
    n = int(input("Entrez un entier n (>= 1) : "))
    while n < 1:
        n = int(input("Erreur : n doit être >= 1. Réessayez : "))

    # 1) pairs entre 1 et n
    print("Pairs entre 1 et", n, ":", end=" ")
    i = 1
    while i <= n:
        if i % 2 == 0:  # i pair si le reste de la division par 2 vaut 0
            print(i, end=" ")
        i += 1
    print()

    # 2) de -n à n
    print("De -%d à %d :" % (n, n), end=" ")
    i = -n
    while i <= n:
        print(i, end=" ")
        i += 1
    print()

    # 3) multiples de 5 entre 1 et n
    print("Multiples de 5 entre 1 et", n, ":", end=" ")
    i = 1
    while i <= n:
        if i % 5 == 0:
            print(i, end=" ")
        i += 1
    print()

    # 4) multiples de n entre 1 et 100
    print("Multiples de", n, "entre 1 et 100 :", end=" ")
    i = 1
    while i <= 100:
        if i % n == 0:
            print(i, end=" ")
        i += 1
    print()


# ===============================================================
# Exercice 4 — Le nom du mois
# ---------------------------------------------------------------
# Entrer un entier entre 1 et 12 et afficher le nom du mois.
# Boucler tant que la valeur n'est pas dans l'intervalle.
# ===============================================================

def ex4_mois() -> None:
    mois_noms = [
        "Janvier", "Février", "Mars", "Avril", "Mai", "Juin",
        "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"
    ]
    x = int(input("Entrez un nombre de mois (1-12) : "))
    while x < 1 or x > 12:  # condition de validation
        x = int(input("Erreur : entrez un entier entre 1 et 12 : "))
    # Indices de liste en Python démarrent à 0, donc on soustrait 1
    print(mois_noms[x - 1])


# ===============================================================
# Exercice 5 — Le nombre secret (aléatoire)
# ---------------------------------------------------------------
# L'ordinateur choisit un nombre au hasard entre 1 et 10.
# On boucle tant que l'utilisateur ne l'a pas trouvé.
# ===============================================================

def ex5_nombre_secret() -> None:
    secret = random.randint(1, 10)  # borne inclusive
    print("L'ordinateur a choisi un nombre entre 1 et 10...")
    print("Vous allez devoir le deviner !")
    guess = int(input("Entrez un nombre : "))
    while guess != secret:
        guess = int(input("Raté ! Essayez encore : "))
    print("Bravo !")


# ===============================================================
# Exercice 6 — Nombre secret avec compteur d'essais
# ---------------------------------------------------------------
# Même principe que l'ex. 5 mais on compte le nombre d'essais.
# ===============================================================

def ex6_nombre_secret_compte() -> None:
    secret = random.randint(1, 10)
    print("L'ordinateur a choisi un nombre entre 1 et 10...")
    print("Vous allez devoir le deviner !")
    essais = 1  # on compte déjà la première saisie
    guess = int(input("Entrez un nombre : "))
    while guess != secret:
        essais += 1
        guess = int(input("Raté ! Essayez encore : "))
    print(f"Bravo ! Vous avez trouvé le nombre secret en {essais} essais.")


# ===============================================================
# Exercice 7 — Valeur sentinelle : somme jusqu'à -1
# ---------------------------------------------------------------
# On lit des entiers tant qu'ils sont >= 0 (i.e. > -1). Le -1 termine
# la saisie et on affiche la somme.
# ===============================================================

def ex7_somme() -> None:
    somme = 0
    val = int(input("Entrez une suite d'entiers positifs, terminez par -1 : "))
    while val > -1:  # tant qu'on ne voit pas la sentinelle
        somme += val
        val = int(input("Entrez une autre valeur (ou -1 pour terminer) : "))
    print("La somme vaut", somme)


# ===============================================================
# Exercice 8 — Moyenne avec sentinelle et cas vide
# ---------------------------------------------------------------
# Même lecture qu'en ex. 7 mais on calcule la moyenne. Si aucun
# nombre positif n'est donné, on signale l'erreur (division par zéro).
# ===============================================================

def ex8_moyenne() -> None:
    total = 0
    nb = 0
    val = int(input("Entrez une suite d'entiers positifs, terminez par -1 : "))
    while val > -1:
        total += val
        nb += 1
        val = int(input("Entrez une autre valeur (ou -1 pour terminer) : "))

    if nb == 0:
        print("Erreur : aucune valeur positive fournie, moyenne impossible.")
    else:
        print("La moyenne vaut", total / nb)


# ===============================================================
# Exercice 9 — Nombres carrés <= n
# ---------------------------------------------------------------
# Afficher tous les carrés parfaits <= n.
# Astuce : on peut incrémenter i et afficher i*i tant que i*i <= n.
# ===============================================================

def ex9_carres() -> None:
    n = int(input("Entrez un entier positif n : "))
    while n < 0:
        n = int(input("n doit être >= 0. Réessayez : "))

    i = 1
    # on évite de calculer sqrt(n) pour rester dans l'esprit des boucles
    while i * i <= n:
        print(i * i, end=" ")
        i += 1
    print()


# ===============================================================
# Exercice 10 — Le mot (sans espace)
# ---------------------------------------------------------------
# Demander un « mot » : une chaîne ne contenant aucun espace.
# On boucle tant que la chaîne contient un espace.
# ===============================================================

def ex10_mot_sans_espace() -> None:
    mot = input("Entrez un mot (sans espace) : ")
    # L'opérateur 'in' teste la présence d'un caractère dans la chaîne
    while " " in mot:
        mot = input("Erreur : le mot ne peut pas contenir d'espace. Réessayez : ")
    print("Merci, mot accepté :", mot)


# ===============================================================
# Exercice 11 — Nombre secret avec indication (trop petit/grand)
# ---------------------------------------------------------------
# Fournir une aide à l'utilisateur après chaque essai.
# ===============================================================

def ex11_nombre_secret_aide() -> None:
    secret = random.randint(1, 10)
    print("L'ordinateur a choisi un nombre entre 1 et 10...")
    print("Vous allez devoir le deviner !")
    essais = 1
    guess = int(input("Entrez un nombre : "))

    while guess != secret:
        essais += 1
        if guess < secret:
            guess = int(input("Trop petit ! Essayez encore : "))
        else:
            guess = int(input("Trop grand ! Essayez encore : "))

    print(f"Bravo ! Vous avez trouvé le nombre secret en {essais} essais.")


# ===============================================================
# Exercice 12 — Maximum et minimum avec sentinelle
# ---------------------------------------------------------------
# Lire des entiers >= 0 jusqu'à -1. Afficher le min et le max.
# Gérer le cas où aucune valeur positive n'est fournie.
# ===============================================================

def ex12_min_max() -> None:
    # On utilise deux variables initialisées à None pour savoir si on a
    # déjà reçu au moins une valeur valide.
    minimum = None
    maximum = None

    val = int(input("Entrez une suite d'entiers positifs, terminez par -1 : "))
    while val > -1:
        # Si c'est la première valeur, elle initialise min et max
        if minimum is None or val < minimum:
            minimum = val
        if maximum is None or val > maximum:
            maximum = val
        val = int(input("Entrez une autre valeur (ou -1 pour terminer) : "))

    if minimum is None:  # donc aucune valeur >= 0 saisie
        print("Erreur : aucune valeur positive fournie.")
    else:
        print("maximum :", maximum)
        print("minimum :", minimum)


# ===============================================================
# Petit menu pour lancer rapidement un exercice depuis ce script.
# Vous pouvez commenter/retirer cette partie si vous n'en avez pas
# besoin.
# ===============================================================

if __name__ == "__main__":
    print("TD07 — Boucles while : choisissez un exercice à lancer")
    print("1: ex1_afficher_1_a_n")
    print("2: ex2_demo (demander_entier + afficher_premiers_entiers)")
    print("3: ex3_suites")
    print("4: ex4_mois")
    print("5: ex5_nombre_secret")
    print("6: ex6_nombre_secret_compte")
    print("7: ex7_somme")
    print("8: ex8_moyenne")
    print("9: ex9_carres")
    print("10: ex10_mot_sans_espace")
    print("11: ex11_nombre_secret_aide")
    print("12: ex12_min_max")

    choix = input("Votre choix (1-12) ou ENTER pour quitter : ")
    if choix == "1":
        ex1_afficher_1_a_n()
    elif choix == "2":
        ex2_demo()
    elif choix == "3":
        ex3_suites()
    elif choix == "4":
        ex4_mois()
    elif choix == "5":
        ex5_nombre_secret()
    elif choix == "6":
        ex6_nombre_secret_compte()
    elif choix == "7":
        ex7_somme()
    elif choix == "8":
        ex8_moyenne()
    elif choix == "9":
        ex9_carres()
    elif choix == "10":
        ex10_mot_sans_espace()
    elif choix == "11":
        ex11_nombre_secret_aide()
    elif choix == "12":
        ex12_min_max()
    else:
        print("Au revoir !")
