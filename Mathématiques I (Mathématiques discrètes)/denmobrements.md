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

Donc :

pas de répétition

ordre non important

C’est exactement ce qu’on appelle une :

Combinaison sans répétition ou n = 45 et k=6

Formule => C ac n=45 et k=6

La Réponse est

```
 (A n=45 et k=6) / 6! = (45 . 44 . 43 . 42 . 41 . 40) / (6 . 5 . 4 . 3 . 2 . 1) = 8 145 060


```

Donc, il existe 8 145 060 façons différentes de remplir une grille de lotto (6 numéros parmi 45).

---
