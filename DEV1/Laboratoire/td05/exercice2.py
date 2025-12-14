import math
def perimetre_cercle(rayon):
    perim_c = 2*rayon*math.pi
    print(perim_c)
    
permimetre_cercle(-6)
perimetre_cercle("bonjour")
"""
Correction
import math

def perimetre_cercle(rayon):
    """Calcule le périmètre d’un cercle si le rayon est valide."""
    # Vérifie que le rayon est un nombre
    if not isinstance(rayon, (int, float)):
        print("Erreur : le rayon doit être un nombre.")
        return
    
    # Vérifie que le rayon est positif
    if rayon < 0:
        print("Erreur : le rayon ne peut pas être négatif.")
        return
    
    # Calcul du périmètre
    perim_c = 2 * math.pi * rayon
    print(f"Le périmètre du cercle est : {perim_c:.2f}")

# Appels de test
perimetre_cercle(-6)
perimetre_cercle("bonjour !")


"""