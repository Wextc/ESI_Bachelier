
#code robuste
def char_to_int(liste):
    if not isinstance(liste, list):
        return False

    for i in range(len(liste)):
        # Vérifier que c'est un caractère minuscule non accentué
        if not isinstance(liste[i], str) or len(liste[i]) != 1:
            return False
        if not ('a' <= liste[i] <= 'z'):
            return False

        liste[i] = ord(liste[i]) - ord('a')

    return liste
