
def addition(l1, valeur):
    # Vérifier que l1 est une liste
    if not isinstance(l1, list):
        raise TypeError("Le premier argument doit être une liste")

    # Vérifier que valeur est un nombre
    if not isinstance(valeur, (int, float)):
        raise TypeError("Le second argument doit être un nombre")

    for i in range(len(l1)):
        l1[i] = l1[i] + valeur

    return l1

print(addition([1,2,3], 2))