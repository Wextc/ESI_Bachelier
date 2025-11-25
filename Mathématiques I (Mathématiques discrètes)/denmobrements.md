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

<b> Type de
