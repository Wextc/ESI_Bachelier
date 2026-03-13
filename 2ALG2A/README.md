## Chapitre 0 Pseudo code

# Chapitre 0 — Notre pseudo-code (ALG2)

| Concept / Mot-clé                            | Pseudo-code ALG2                        |
| -------------------------------------------- | --------------------------------------- |
| Déclaration d'une variable entière           | `int age`                               |
| Déclaration d'un réel                        | `float prix`                            |
| Déclaration d'une chaîne                     | `String nom`                            |
| Déclaration d'un booléen                     | `Boolean ok`                            |
| Assignation d'une valeur                     | `age = 20`                              |
| Assignation d'une chaîne                     | `nom = "Dimitri"`                       |
| Test d'égalité                               | `ok = age == 20`                        |
| Lire une valeur                              | `read mot`                              |
| Afficher un texte                            | `print "coucou"`                        |
| Déclarer une fonction avec retour            | `float moyenne2Entiers(int nb1, nb2)`   |
| Retourner une valeur                         | `return (nb1 + nb2) / 2`                |
| Procédure (sans valeur de retour)            | `void afficher(String mot)`             |
| Afficher une variable                        | `print mot`                             |
| Déclaration d'une méthode                    | `method T get(int pos)`                 |
| Retourner un élément d'un tableau            | `return tab[pos]`                       |
| Déclaration et initialisation d'un tableau   | `int[] tab = {1,2,3,4,5}`               |
| Déclaration d'un tableau de taille fixe      | `int[10] compteurs`                     |
| Déclaration d'un tableau sans initialisation | `int[] resultat`                        |
| Paramètre tableau dans une fonction          | `void afficher(int[n] tab)`             |
| Taille d'un tableau                          | `tab.length`                            |
| Boucle pour parcourir un tableau             | `for i from 0 to n-1`                   |
| Affectation dans un tableau                  | `tab[i] = valeur`                       |
| Initialiser un tableau                       | `void initialiser(int[n] tab, int val)` |
| Parcourir pour initialiser                   | `for i from 0 to n-1`                   |
| Affecter une valeur dans chaque case         | `tab[i] = val`                          |

### 2.2 Instructions élémentaire

Le point 2.2 – Instructions élémentaires explique comment mesurer le travail qu’un algorithme réalise. L’idée est de compter les actions simples qu’un programme exécute pour résoudre un problème. Ces actions simples sont appelées instructions élémentaires. Par exemple, créer une variable, faire une assignation comme x = 5, comparer deux valeurs ou modifier une variable sont considérés comme des instructions élémentaires.

Pour analyser un algorithme, on regarde combien de ces instructions sont exécutées. Dans un programme très simple, le nombre d’instructions est fixe. Par exemple, si un algorithme crée un tableau et assigne quatre valeurs dans ce tableau, il exécutera toujours le même nombre d’instructions, peu importe la situation.

Dans d’autres cas, le nombre d’instructions dépend de la taille des données utilisées. Par exemple, si un algorithme parcourt un tableau avec une boucle pour initialiser chaque case, le nombre d’instructions dépend du nombre d’éléments du tableau. Si le tableau contient n éléments, la boucle sera exécutée n fois, donc le nombre d’instructions augmente avec n.

Il peut aussi arriver que le nombre d’instructions dépende des valeurs reçues en paramètre. Par exemple, dans un algorithme avec une condition if, certaines instructions ne seront exécutées que si la condition est vraie. Dans ce cas, l’algorithme peut parfois exécuter très peu d’instructions, et parfois beaucoup plus.

En résumé, cette section explique que pour analyser l’efficacité d’un algorithme, on peut compter le nombre d’instructions élémentaires qu’il exécute. Cela permet de comprendre combien de travail l’algorithme doit faire et de comparer différents algorithmes entre eux.

**A retenir:**

Une instruction élémentaire est une action très simple que l’ordinateur fait.

Par exemple :

créer une variable

faire une assignation (x = 5)

comparer deux valeurs

ajouter 1 à une variable

Chaque petite action = 1 instruction.

Exemple 1 (très simple)

Algorithme :

```
vecteur[0] = "Un"
vecteur[1] = "Deux"
vecteur[2] = "Trois"
vecteur[3] = "Quatre"

```

Ici il y a :

4 assignations

Donc :

4 instructions élémentaires

Dans le syllabus ils comptent aussi la création du tableau, donc :

5 instructions au total.

Pour savoir si un algorithme est rapide ou lent, on compte le nombre d’actions simples qu’il exécute (instructions élémentaires).

### 2.3 Complexité dans le pire des cas

Pour simplifier l’analyse d'un alg, on choisit généralement d’étudier la situation la plus défavorable, c’est-à-dire celle où l’algorithme exécute le plus d’instructions. On appelle cela le pire des cas.

Par exemple, un algorithme peut contenir une condition if. Si la condition est fausse, l’algorithme peut ne faire qu’une seule instruction. Mais si la condition est vraie, il peut devoir exécuter beaucoup d’autres instructions, par exemple parcourir tout un tableau avec une boucle. Dans ce cas, pour analyser la complexité, on considère la situation où la condition est vraie et où toutes les instructions supplémentaires sont exécutées.

Cette méthode permet d’avoir une estimation sûre du temps que peut prendre l’algorithme. Même si certaines situations sont plus rapides, l’analyse du pire des cas garantit que l’algorithme ne prendra jamais plus de temps que ce que l’on a estimé. Cela permet aussi de comparer différents algorithmes de manière plus simple et plus fiable.

**A retenir:**

L’analyse du pire des cas consiste à étudier la situation où l’algorithme exécute le plus grand nombre d’instructions possible.

### 2.4 Grand O

La complexité d’un algorithme est une mesure qui permet d’estimer le nombre d’instructions qu’un algorithme exécute en fonction de la taille des données en entrée, afin de comparer l’efficacité des algorithmes.
Complexité O(1) (temps constant)

L’algorithme fait toujours le même nombre d’instructions, peu importe la taille des données.

Pseudo-code :

```
int premierElement(int[n] tab)
return tab[0]

```

✔ Peu importe la taille du tableau, on lit une seule case.

➡ Complexité : O(1)

2️⃣ Complexité O(n) (linéaire)

L’algorithme parcourt tout le tableau.

Pseudo-code :

```
int somme(int[n] tab)
int somme = 0

for i from 0 to n-1
    somme = somme + tab[i]
```

return somme

✔ Si le tableau a n éléments, la boucle tourne n fois.

➡ Complexité : O(n)

3️⃣ Complexité O(n²)

Il y a deux boucles imbriquées.

Pseudo-code :

```
void afficherPairs(int[n] tab)

for i from 0 to n-1
for j from 0 to n-1
print tab[i], tab[j]

```

✔ Si n = 10 → 100 opérations
✔ Si n = 100 → 10000 opérations

➡ Complexité : O(n²)

4️⃣ Complexité O(log n) (recherche dichotomique)

On divise le problème par 2 à chaque étape.

Pseudo-code :

int rechercheDicho(int[n] tab, int value)

```
left = 0
right = n-1


while left <= right
mid = (left + right) / 2

    if tab[mid] == value
        return mid
    else if value < tab[mid]
        right = mid - 1
    else
        left = mid + 1

return -1

```

✔ À chaque étape on élimine la moitié du tableau.

➡ Complexité : O(log n)

### 2.5 L’arithmétique des grands O

L’arithmétique des grands O explique comment déterminer la complexité d’un algorithme à partir de la complexité des différentes parties qui le composent. Lorsqu’un algorithme est constitué de plusieurs blocs d’instructions (par exemple plusieurs appels de méthodes, des conditions ou des boucles), on peut utiliser quelques règles simples pour calculer sa complexité globale.

D’abord, lorsqu’un algorithme exécute deux parties l’une après l’autre, la complexité totale correspond à la somme des complexités de ces deux parties. Cependant, en pratique, on garde surtout la partie qui grandit le plus vite lorsque la taille des données augmente. Par exemple, si une partie est en O(n) et l’autre en O(n²), la complexité globale sera considérée comme O(n²).

Ensuite, lorsqu’un algorithme contient une condition (un if/else), la complexité dépend du bloc qui demande le plus de travail. Pour analyser le pire des cas, on retient donc la complexité la plus grande entre les différentes branches possibles.

Dans le cas d’une boucle, la complexité dépend du nombre de fois que la boucle est exécutée et de la complexité des instructions qui se trouvent à l’intérieur. Si une boucle s’exécute n fois et que le code à l’intérieur est en O(n), la complexité totale devient O(n²).

Enfin, le cours montre aussi que certaines complexités augmentent beaucoup plus vite que d’autres lorsque la taille des données grandit. Par exemple, un algorithme en O(log n) reste très efficace même pour de grandes valeurs de n, tandis qu’un algorithme en O(n²) ou en O(2ⁿ) devient très lent lorsque la taille des données augmente fortement. C’est pour cette raison que l’analyse de la complexité est importante pour choisir le meilleur algorithme.

| Structure dans l’algorithme | Règle de complexité                      | Exemple                            |
| --------------------------- | ---------------------------------------- | ---------------------------------- |
| **Instruction simple**      | O(1)                                     | `x = a + b`                        |
| **Suite d’instructions**    | O(f(n) + g(n)) → on garde la plus grande | O(n) + O(n²) = **O(n²)**           |
| **Condition (if / else)**   | O(max(f(n), g(n)))                       | if O(n) else O(n²) → **O(n²)**     |
| **Boucle simple**           | O(n × complexité du corps)               | boucle n fois avec O(1) → **O(n)** |
| **Boucles imbriquées**      | on multiplie les complexités             | n × n → **O(n²)**                  |
| **Appel de fonction**       | on prend la complexité de la fonction    | appel de `search()` en O(n)        |
| **Recherche dichotomique**  | O(log n)                                 | division du problème par 2         |

## 3.5

https://www.youtube.com/watch?v=bRPHvWgc6YM
