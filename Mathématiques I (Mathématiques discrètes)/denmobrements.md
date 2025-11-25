# Chapitre 4 - Dénombrements

## Exercices

### Exercices 4.1

Imagine que tu dois poser les cartes l’une après l’autre :

Pour la première place : 52 choix

Pour la deuxième : tu as déjà utilisé une carte → 51 choix

Pour la troisième : 50 choix

ect ...

Dernière place : 1 choix

Tu multiplies tous les choix possibles → c’est exactement la définition de la factorielle.

Donc le nombre total de mélanges possibles est :

```
!
52×51×50×⋯×1=52!

52! ≈8.0658×1067

```

---

### Exercice 4.2

<b> Type de problème : </b>

- Combinaison sans répétition (on choisit des objets, l’ordre ne compte pas, sans doublons).

<b> Interprétation : </b>

- Tu choisis un ensemble de 6 numéros parmi 45, l’ordre n’a aucune importance.

Quelle est la situation ?

Il y a 45 numéros possibles : 1, 2, 3, …, 45

Sur ta grille, tu dois choisir 6 numéros.

On ne peut pas cocher deux fois le même numéro → pas de répétition.

L’ordre ne compte pas :

la grille 1, 2, 3, 4, 5, 6 est la même que 6, 5, 4, 3, 2, 1.

Au lotto, ce qui compte c’est l’ensemble des 6 numéros, pas dans quel ordre tu les as cochés.

Formule => C avec n=45 et k=6

La Réponse est

```
 C n=45 k=6 = (A n=45 et k=6) / 6! = (45 . 44 . 43 . 42 . 41 . 40) / (6 . 5 . 4 . 3 . 2 . 1) = 8 145 060


```

<b> Donc, il existe 8 145 060 façons différentes de remplir une grille de lotto (6 numéros parmi 45). </b>

---

### Exercice 4.3

<b> Type de problème: </b>

- Arrangement sans répétition
  (ordre important, objets tous différents, aucun doublon possible)

<b> Interprétation: </b>

- Tu dois choisir 3 chevaux parmi 20, et un cheval ne peut pas prendre deux places. L'ordre de selection des chevaux compte.

Comment compter ?

Tu choisis :

le 1ᵉ cheval : 20 possibilités

le 2ᵉ : 19 possibilités

le 3ᵉ : 18 possibilités

Donc :

```

A n=20 k=3 = 20 . 19 . 18 = 6840

```

<b> Il faut remplir 6 840 bulletins différents pour être certain de gagner le tiercé dans l’ordre.</b>

---

### Exercice 4.4

<b> Type de problème : </b>

- C’est un arrangement complet (tous les objets sont utilisés).

<b> Interprétations : </b>

Chaque personne reçoit exactement 1 chapeau - Aucun chapeau n’est donné deux fois → pas de répétition.

L’ordre compte parce que -> donner le chapeau A à Paul et B à Marie est différent de A à Marie et B à Paul.

Pour distribuer :

le 1ᵉ chapeau : 5 choix

le 2ᵉ : 4 choix

le 3ᵉ : 3 choix

le 4ᵉ : 2 choix

le 5ᵉ : 1 choix

Donc :

```
5! = 5 . 4 . 3 . 2 . 1 = 120

```

<b> Il existe 120 façons de distribuer 5 chapeaux différents à 5 personnes. </b>

---

### Exercice 4.5

<b> Type de problème : </b>

- Donc une arête est un choix de 2 sommets parmi 15,

  sans répétition,

  l’ordre n’a aucune importance.

<b> Interprétations : </b>

- Un graphe d’ordre 15 possède 15 sommets. On cherche le nombre maximal d’arêtes possible, donc le graphe est complet.

  Dans ce genre de graphe, chaque sommet est connecté à tous les autres.

  Donc, une arête correspond à un couple de sommets distincts, mais dans n’importe quel ordre (car ce n’est pas orienté).

  Ici, la manière dont on relie les sommets (ordres) n'est pas ordonnée, ainsi nous pouvons commencer par le sommet(ordre) de notre choix.

Nous avons une Combinaison sans répétition où n= 15 et k=2

<b> Un graphe d’ordre 15 peut contenir au maximum 105 arêtes. </b>

---

### Exercice 4.6

<b> Type de problème </b>

Dans les cas nous avons une combinaison sans répétition et l'ordre ne compte.

<b> Interprétations : </b>

1. Former une équipe de 10 personnes parmi 20

Il y a :

12 garçons

8 filles

total = 20 personnes

Une équipe de 10 personnes est un ensemble :

l’ordre ne compte pas (une équipe n’a pas d’ordre)

pas de répétition (une personne ne peut pas être choisie deux fois)

2. Former une équipe de 10 personnes avec 5 garçons et 5 filles

Ici, on impose :

choisir 5 garçons parmi 12

choisir 5 filles parmi 8

Les deux choix sont indépendants, donc on multiplie.

Les deux sont des combinaisons sans répétition, car :

on choisit un ensemble

l’ordre ne compte pas

pas de répétition

Réponse :

```
# Pour le cas 1:

C où n=20 et k=10


# Pour le cas 2:

(C où n=12 et k=5)* (C où n=8 et k=5)


```

<b>Dans le premier cas nous pouvons créer 184 756 équipes de 10 personnes possible. Dans le second cas, nous avons 44 352 équipes possibles constituées de 5 garçons et de 5 filles.</b>

Remarque ici nous multiplions nous voulons des équipes constituer de 5 garçon ET 5 filles. Si nous voulions des équipes constituer de garçon OU de filles il aurait fallut additions.

```
Example:

(C où n=12 et k=5) + (C où n=8 et k=5)

```

---

### Exercice 4.7

<b> Type de problème </b>

C’est un cas de produit avec répétitions possibles.

<b> Interprétations : </b>

On veut compter toutes les possibilités, donc :

l’ordre compte (changer l’ordre donne une plaque différente)

répétition autorisée (ex : 442 peut exister)

indépendance entre cases

- C’est un cas de produit avec répétitions possibles.
- On utilise le principe fondamental du dénombrement.

<b> Nombre de possibilités pour chaque position</b>

1 chiffre – 3 lettres – 3 chiffres

C−LLL−CCC

- 1er caractère : un chiffre

  10 possibilités (0–9)

- 2e, 3e, 4e caractères : des lettres

  26 possibilités chacune (A–Z)

- 5e, 6e, 7e caractères : des chiffres

  10 possibilités chacune (0–9)

Calcul total:

```
10×26×26×26×10×10×10 = 17576×10000 = 175760000

```

<b>Il existe 175 760 000 plaques d’immatriculation possibles.</b>

---

### Exercice 4.8

1
<b>Type de problèmes</b>

Arrangement avec répétition (ordre important, répétitions autorisées)

<b>Interprétation : </b>

Pour chaque position nous avons 10 possibilités. Les chiffres vont de 0 à 9.

. . . . . => Pour chaque point, il y a 10 possibilités.

Donc, le résultat est

```
10 . 10 . 10 . 10 = $$10^4$$

```
