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

Pour <b>f(n) = (3 \* f(n-1)) mod 7</b>

Etape de départ : le valeur initiale

On te donne :

```
 f(0) = 1

```

C'est la valeur de départ (comme un point de départ pour la suite).

<b> Calcul de f(1) </b>

Pour avoir f(1), on remplace n par 1:

```
f(1) = (3 * f(1-1)) mod 7 = (3 * f(0)) mod7 = (3 * 1) mod 7 = 3

```

<b> Calcul de f(2) </b>

Pour avoir f(2), on remplace n par 2:

```
f(2) = (3 * f(2-1)) mod 7 = (3 * f(1)) mod7 = (3 * 3) mod 7 = 2

```

<b> Calcul de f(3) </b>

Pour avoir f(3), on remplace n par 3:

```
f(3) = (3 * f(3-1)) mod 7 = (3 * f(2)) mod7 = (2 * 3) mod 7 = 6

```

<b> Calcul de f(4) </b>

Pour avoir f(4), on remplace n par 4:

```
f(4) = (3 * f(4-1)) mod 7 = (3 * f(3)) mod7 = (2 * 6) mod 7 = 4

```

### Exercice 5.3:

<b>f(n + 1) = f(n)- f(n-1)</b>

<b>f(1)</b>

n = 1 ou f(0) = -1 et f(1) = 2

```
f(1+1) = f(1) - f(0) = 2  -(-1) 2 + 1 = 3

f(2) = 3

```

<b>f(2)</b>

```
f(2+1) = f(2) - f(1) = 3 - 1 = 1
f(3) = 1
```

<b>f(3)</b>

```
f(3+1) = f(3) − f(2) = 1 − 3 = −2
f(4) = -2
```

<b>f(4)</b>

```
f(4+1) = f(4) − f(3) = − 2 − 1 = − 3
f(5) = -3

```

<b>f(n + 1) = (f(n))² + f(n - 1)</b>

<b>f(1)</b>

n = 1

```
f(1 +1) = (f(1))² + f(1 - 1)
f(2) = (2)² + f(0) = 4 + (-1) = 3

```

<b>f(2)</b>

n = 2

```
f(2 +1) = (f(2))² + f(2 - 1)
f(3) = (3)² + f(1) = 9 + 2 = 11

```

<b>f(3)</b>

n = 3

```
f(3 +1) = (f(3))² + f(3 - 1)
f(4) = (11)² + f(2) = 121 + 3 = 124

```

<b>f(4)</b>

n = 4

```
f(4 +1) = (f(4))² + f(4 - 1)
f(5) = (124)² + f(3) =  124² + 11 = 15 376 + 11 = 15 387

```

<b>f(n+1) = f(n) \* f(n - 1)</b>

<b>f(1)</b>

n = 1

```
f(1 +1) = (f(1))² + f(1 - 1)
f(2) = (2)² + f(0) = 4 + (-1) = 3

```
