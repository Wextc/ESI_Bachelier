## Exercice Avant blocus

### Exercice 1:

Écrire un algorithme qui reçoit deux tableaux d’entiers non triés de taille logique nReg et mReg.

Créer un tableau de taille physique nReg + mReg tel que :

Les éléments du deuxième tableau soient insérés en premier.

Ensuite on ajoute les éléments du premier tableau dont l’indice est pair.

Retourner la référence vers ce nouveau tableau.

Exemple

Tableau 1 (nReg = 5)

```
[3, 7, 4, 9, 2]
 0  1  2  3  4

```

Tableau 2 (mReg = 3)

```
[5, 8, 1]
 0  1  2

```

Résultat attendu :

```
[5, 8, 1, 3, 4, 2, ? , ?]

```

```

int[n] createNewArray(int[n] tabA, int[n]tabB, int nReg, mReg)
    int i
    int j = 0
    int[n] res = new int[nReg + mReg]

    for int i = 0 to nReg-1 by 2
        res[j] = tabA[i]
        j = j + 1
    end for
    for int i = 0 to mReg-1
        res[j] = tabB[i]
        j = j + 1
    end for

    return res

```

---

### Exercice 2:

Écrire un algorithme qui reçoit deux tableaux A et B de taille logique nReg et mReg.

Créer un tableau de taille physique nReg + mReg.

Dans ce tableau :

Insérer les éléments de A dans l’ordre inverse

Ajouter les éléments de B dont la valeur est paire

Retourner le tableau.

Exemple

A (nReg = 4)

```
[2, 5, 7, 9]

```

B (mReg = 4)

```
[3, 8, 6, 1]

```

Résultat :

```
[9, 7, 5, 2, 8, 6, ?, ?]

```

```
int[n] createArray(int[n]tabA, int[n] tabB, int nReg, int mReg)

    int i
    int j = 0
    int [n] res = new int[tabA + tabB]

    for i = 0 to mReg - 1
        res[j] = tabA[i]
        j = j+1
    end for

    for i = 0 to nReg - 1 by 2
        res[j] = tabB[i]
        j= j+1
    end for

    return res

```

### Exercice 3 (très classique examen)

Écrire un algorithme qui reçoit deux tableaux T1 et T2.

Créer un tableau de taille physique nReg + mReg.

On insère :

les éléments d’indice impair de T1

puis les éléments d’indice pair de T2

Retourner le tableau.

Exemple

T1 (nReg = 6)

```
[4, 1, 7, 3, 8, 2]
0 1 2 3 4 5

```

T2 (mReg = 5)

```
[9, 5, 6, 4, 1]
0 1 2 3 4
```

Résultat :

```
[1, 3, 2, 9, 6, 1, ?, ?, ?, ?]

```

```
int [n] createArray(int[n]T1, int[n] T2, int nReg, int mReg)
    int i
    int j = 0
    int[n] res = int new[ nReg + mReg]
    for i = 1 to nReg -1 by 2
        res[j] = T1[i]
        j = j + 1
    end for
    for i = 1 to mRed - 1 by 2
        res[j] = T2[i]
        j = j+1
    end for
    return res

```

### Algorithme dichotomique

### Exercice 1

Écrire une méthode en Java (ici en pseudo code car on est algo) qui recherche une valeur entière dans un tableau d’entiers trié par ordre croissant.

La méthode doit utiliser l’algorithme de recherche dichotomique (binary search).

Signature de la méthode

La méthode reçoit :

un tableau d’entiers myArray

une valeur entière value à rechercher

Comportement attendu

si la valeur est présente dans le tableau, la méthode retourne l’indice de cette valeur

si la valeur n’est pas présente, la méthode retourne -1

Exemple

Tableau :

```
[2, 5, 8, 12, 16, 23, 38]
0 1 2 3 4 5 6

```

Recherche de 12

Résultat :

```
3

```

Recherche de 7

Résultat :

```
-1
```

```
int giveValue(int[n] myArray, int value)

    int right = myArray.length - 1
    int left = 0
    int medianIndex  //Resultatde(left + right)//2.
    int candidat
    boolean isFound = False
    int value

    while NOT isFound AND left <= right
        medianIndex = (left + right) / 2
        candidat = myArray[medianIndex]
        if value == candidat
            isFound = True
         else if value < candidat
            right = medianIndex - 1
         else
            left = medianIndex + 1
    if isFound
        return medianIndex
    else
        return -1

```

---

## Exercice blocus

Écrire un algorithme qui reçoit deux tableaux d’entiers non triés de taille logique nReg et mReg.

Créer un tableau de taille physique nReg + mReg tel que :

Les éléments du deuxième tableau soient insérés en premier.

Ensuite on ajoute les éléments du premier tableau dont l’indice est pair.

Retourner la référence vers ce nouveau tableau.

Exemple

Tableau 1 (nReg = 5)

```
[3, 7, 4, 9, 2]
 0  1  2  3  4

```

Tableau 2 (mReg = 3)

```
[5, 8, 1]
 0  1  2
```

Résultat attendu :

```
[5, 8, 1, 3, 4, 2, ? , ?]

```

---

### Exercice 1

Écrire un algorithme qui reçoit deux tableaux d’entiers non triés de tailles logiques nReg et mReg et qui crée un nouveau tableau de taille physique nReg + mReg.

Les éléments du premier tableau seront copiés en premier dans le nouveau tableau. Ensuite, on ajoutera uniquement les éléments du deuxième tableau dont la valeur est strictement positive.

En fin d’algorithme, la référence vers le nouveau tableau sera retournée.

Exemple

Soit le premier tableau de taille logique nReg = 4 :

```
index : 0 1 2 3 4 5
tab1 : 7 0 -2 5 ? ?

```

Soit le deuxième tableau de taille logique mReg = 5 :

```
index : 0 1 2 3 4 5 6
tab2 : -1 4 0 9 -3 ? ?

```

Le résultat sera :

```
[7, 0, -2, 5, 4, 9]

```

### Exercice 2

Écrire un algorithme qui reçoit un tableau d’entiers non trié de taille logique nReg et qui crée un nouveau tableau contenant uniquement les éléments situés à des indices pairs du tableau initial.

Le nouveau tableau aura pour taille physique nReg.

En fin d’algorithme, la référence vers le nouveau tableau sera retournée.

Exemple

Soit le tableau de taille logique nReg = 6 :

```
index : 0 1 2 3 4 5 6 7
tab : 12 5 8 1 3 9 ? ?

```

Le résultat sera :

[12, 8, 3]

car on garde les éléments d’indices 0, 2 et 4.

### Exercice 3

Écrire un algorithme qui reçoit deux tableaux d’entiers non triés de tailles logiques nReg et mReg et qui crée un nouveau tableau de taille physique nReg + mReg.

On commencera par copier dans le nouveau tableau les éléments du premier tableau dont la valeur est paire, puis les éléments du deuxième tableau dont la valeur est impaire.

En fin d’algorithme, la référence vers ce nouveau tableau sera retournée.

Exemple

Soit le premier tableau de taille logique nReg = 5 :

```
index : 0 1 2 3 4 5 6
tab1 : 6 3 8 1 4 ? ?

```

Soit le deuxième tableau de taille logique mReg = 4 :

```
index : 0 1 2 3 4 5
tab2 : 7 2 5 8 ? ?

```

Le résultat sera :

```
[6, 8, 4, 7, 5]

```
