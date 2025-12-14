cote_1 = float(input("Entrez la longueur du premier côté : "))
cote_2 = float(input("Entrez la longueur du deuxième côté : "))
cote_3 = float(input("Entrez la longueur du troisième côté : "))

# Vérifie d'abord si les côtés peuvent former un triangle (inégalité triangulaire)
if cote_1 + cote_2 <= cote_3 or cote_1 + cote_3 <= cote_2 or cote_2 + cote_3 <= cote_1:
    print("Ces longueurs ne peuvent pas former un triangle.")
else:
    # Vérifie le type du triangle
    if cote_1 == cote_2 == cote_3:
        print("Le triangle est équilatéral.")
    elif cote_1 == cote_2 or cote_2 == cote_3 or cote_1 == cote_3:
        print("Le triangle est isocèle.")
    else:
        print("Le triangle est quelconque.")