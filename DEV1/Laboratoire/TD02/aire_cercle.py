# Programme : cercle.py
# Objectif : calculer l’aire et le périmètre d’un cercle à partir du rayon lu au clavier.

import math  # On importe le module math pour utiliser la constante π

# Lecture du rayon
rayon = float(input("Entrez le rayon du cercle : "))

# Calculs
aire = math.pi * rayon ** 2
perimetre = 2 * math.pi * rayon

# Affichage des résultats
print("L’aire du cercle est :", aire)
print("Le périmètre du cercle est :", perimetre)