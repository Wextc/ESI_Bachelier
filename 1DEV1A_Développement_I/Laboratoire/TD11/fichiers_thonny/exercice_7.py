def moyenne(ma_liste):
    # Vérifier que c'est une liste
    if not isinstance(ma_liste, list):
        return False
    # Vérifier que la liste n'est pas vide
    if len(ma_liste) == 0:
        return False
    total = 0
    for i in range(len(ma_liste)):
        # Vérifier que chaque élément est un nombre
        if not isinstance(ma_liste[i], (int, float)):
            return False
        total += ma_liste[i]
    return total / len(ma_liste)

print(moyenne([1,2]))
