l2 = [5, 6, 7, 8, 9]
l1 = [5, 6, 7, 8,19]

def liste_elements_communs(l1, l2):
    res =[]
    for i in l1:
        if i in l2 and i not in res:
            res.append(i)
    return res
print(liste_elements_communs(l1, l2))



"""
Le code suivant est un manière propre de faire.

def liste_elements_communs(l1, l2):
    return list(set(l1) & set(l2))


"""