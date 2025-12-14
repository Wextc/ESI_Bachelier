# Demande des quatre nombres
a = float(input("Entrez le numérateur a : "))
b = float(input("Entrez le dénominateur b : "))
c = float(input("Entrez le numérateur c : "))
d = float(input("Entrez le dénominateur d : "))

# Vérifie que les dénominateurs ne sont pas nuls
if b == 0 or d == 0:
    print("Erreur : les dénominateurs ne peuvent pas être nuls.")
else:
    # Compare les fractions sans division (évite erreurs d'arrondi)
    if a * d == b * c:
        print(True)
    else:
        print(False)