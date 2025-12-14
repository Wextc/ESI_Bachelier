import math

# Demande des coefficients à l'utilisateur
a = float(input("Entrez le coefficient a : "))
b = float(input("Entrez le coefficient b : "))
c = float(input("Entrez le coefficient c : "))

# Cas 1 : a = 0 → ce n’est pas une équation du 2nd degré
if a == 0:
    if b == 0:
        if c == 0:
            print("L’équation est vraie pour tout x (identité).")
        else:
            print("Pas de solution (équation impossible).")
    else:
        # Équation du 1er degré : bx + c = 0 → x = -c / b
        x = -c / b
        print(f"C’est une équation du premier degré.")
        print(f"La solution est : x = {x:.2f}")

# Cas 2 : a ≠ 0 → équation du second degré
else:
    delta = b**2 - 4*a*c  # Calcul du discriminant

    if delta > 0:
        x1 = (-b - math.sqrt(delta)) / (2*a)
        x2 = (-b + math.sqrt(delta)) / (2*a)
        print("Deux racines réelles distinctes :")
        print(f"x1 = {x1:.2f}, x2 = {x2:.2f}")

    elif delta == 0:
        x0 = -b / (2*a)
        print("Une racine réelle double :")
        print(f"x = {x0:.2f}")

    else:
        print("Pas de racine réelle (Δ < 0).")
