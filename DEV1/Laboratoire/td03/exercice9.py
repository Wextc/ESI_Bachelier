montant = float(input("Entrez le montant à placer (€) : "))
annees = int(input("Entrez le nombre d'années : "))

# Taux d'intérêt de 2 %
taux = 0.02

# Calcul des intérêts après le nombre d'années (intérêts simples)
interets = montant * taux * annees

# Affichage des résultats
print("Les intérêts après", annees, "an(s) seront de :", interets, "€")
print("Le montant total après", annees, "an(s) sera de :", montant + interets, "€")