![permission_cat](https://github.com/Wextc/ESI_Bachelier/blob/main/1DEV1A_Développement_I/Laboratoire/TD13/img/exercice_01.png)

```
M1 = [[1,2,3],[4,5,6],[7,8,9]]
M2 = [[9,8,7],[6,5,4],[3,2,1]]

def add_matrices(M1, M2):
    length = len(M1)
    resultat = []
    for i in range(length):
        row = []
        for j in range(length):
            row.append(M1[i][j] + M2[i][j])
        resultat.append(row)
    return resultat


print(add_matrices(M1, M2))
```

Ensuite, on définit la fonction add_matrices(M1, M2), dont le rôle est d’additionner deux matrices de même taille. La variable length contient le nombre de lignes de la matrice, obtenu grâce à len(M1). On crée aussi une liste vide appelée resultat, qui servira à stocker la matrice finale.

La première boucle for i in range(length) parcourt les lignes des matrices. Pour chaque ligne, on crée une nouvelle liste row qui contiendra les valeurs de la ligne résultante. La seconde boucle for j in range(length) parcourt les colonnes. À chaque position (i, j), on additionne l’élément de M1 et celui de M2 situés au même endroit, puis on ajoute cette somme à la liste row.

Une fois toutes les colonnes traitées pour une ligne donnée, la liste row est ajoutée à la liste resultat. Lorsque toutes les lignes ont été parcourues, resultat contient la matrice somme complète, et la fonction la renvoie grâce à l’instruction return resultat.

Enfin, l’appel à print(add_matrices(M1, M2)) affiche le résultat de l’addition des deux matrices. Dans cet exemple, chaque élément de la matrice finale vaut 10, car chaque nombre de M1 est additionné à un nombre complémentaire de M2.

![permission_cat](https://github.com/Wextc/ESI_Bachelier/blob/main/1DEV1A_Développement_I/Laboratoire/TD13/img/exercice_02.png)
