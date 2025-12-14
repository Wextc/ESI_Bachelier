 import carre

# Demande d’un nombre positif à l’utilisateur
x = float(input("Entrez la longueur du côté du carré (en cm) : "))

if x > 0:
    aire = carre.aire_carre(x)
    print(f"L’aire du carré de côté {x} cm est {aire} cm².")
else:
    print("Erreur : la valeur doit être un nombre positif.")