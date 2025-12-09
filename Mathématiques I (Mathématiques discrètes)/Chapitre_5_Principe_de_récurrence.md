## Chapitre 5

# Chapitre 4 - Dénombrements

## Vidéos qui explique

https://www.youtube.com/watch?v=udGGlHdSAgc

https://www.youtube.com/watch?v=LXSJB0BnPD4

### Exercice 5.1:

<b>Calculer f(1)</b>

En utilisant la formule de récurrence

```
f(n+1) = -2f(n) avec n = 0 et f(0) = 1

    f(1) = -2 f(0) = -2 * 1 = -2

```

<b>Calculer f(2)</b>

En utilisant la formule de récurrence

```
f(n+1) = -2f(n) avec n = 1 et f(1) = -2

    f(1) = -2 f(1) = -2 * (-2) = 4

```

<b>Calculer f(3)</b>

En utilisant la formule de récurrence

```
f(n+1) = -2f(n) avec n = 2 et f(2) = 4

    f(3) = -2 f(3) = -2 * 4 = -8

```

<b>Calculer f(4)</b>

En utilisant la formule de récurrence

```
f(n+1) = -2f(n) avec n = 3 et f(3) = -8

    f(4) = -2 f(3) = -2 * (-8) = 16

```

### Exercice 5.2:

<b>Calculer f(1)</b>

En utilisant la formule de récurrence

f(n) = 3 \* (n + 1) + 1 avec n = 1 et la condition initiale f(0) = 1, on obtient:

```
f(1) = 3 * f(1-1) + 1 = 3 * f(0) + 1 = 4

```

<b>Calculer f(2)</b>

En utilisant la formule de récurrence

```
f(2) = 3 * f(2-1) + 1 = 3 * f(1) + 1 =  12 + 1 = 13

```

<b>Calculer f(3)</b>

En utilisant la formule de récurrence

```
f(3) = 3 * f(3-1) + 1 = 3 * 13 + 1 = 39 + 1 = 40

```

<b>Calculer f(4)</b>

En utilisant la formule de récurrence

```
f(4) = 3 * f(4-1) + 1 =  3 * 40 + 1 = 121

```

Pour <b> f(n) = (f(n-1))² + 1 avec f(0) = 1</b>

Etape de départ : le valeur initiale

On te donne :

```
 f(0) = 1

```

C'est la valeur de départ (comme un point de départ pour la suite).

<b> Calcul de f(1) </b>

Pour avoir f(1), on remplace n par 1:

```
f(1) = (f(1-1)²) + 1 = (f(0)²) + 1 = (1²) + 1 = 2

```

<b> Calcul de f(2) </b>

Pour avoir f(2), on remplace n par 2:

```
f(2) = (f(2-1)²) + 1 = (f(1)²) + 1 = (2²) + 1 = 5

```

<b> Calcul de f(3) </b>

Pour avoir f(3), on remplace n par 3:

```
f(3) = (f(3-1)²) + 1 = (f(2)²) + 1 = (5²) + 1 = 26

```

<b> Calcul de f(4) </b>

Pour avoir f(4), on remplace n par 4:

```
f(4) = (f(4-1)²) + 1 = (f(3)²) + 1 = (26²) + 1 = 676 + 1 = 676

```
