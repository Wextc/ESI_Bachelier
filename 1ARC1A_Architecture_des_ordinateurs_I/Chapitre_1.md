# Chapitre 1

## Représentation des nombres

### 1. CALCUL BINAIRE ET ENTIERS POSITIFS

<b>Calcul dans une base quelconque</b>

Un calcul dans une base quelconque consiste à représenter et manipuler des nombres dans un système de numération dont la base

n’est pas forcément 10 (le système décimal habituel). La base, notée B, indique le nombre de symboles différents utilisés

pour écrire les nombres et la valeur par laquelle chaque position est pondérée.

Dans une base B, les chiffres possibles vont de 0 à B−1. La valeur d’un chiffre dépend donc à la fois de sa valeur propre et

de sa position dans le nombre. Chaque position correspond à une puissance de la base.

![permission_cat](https://github.com/Wextc/ESI_Bachelier/blob/main/1ARC1A_Architecture_des_ordinateurs_I/img/chapitre_1_form_general.png)
![permission_cat](https://github.com/Wextc/ESI_Bachelier/blob/main/1ARC1A_Architecture_des_ordinateurs_I/img/chapitre_1_exemple.png)

<b> Remarque </b>

l’écriture d’un nombre peut être ambiguë si la base n’est pas précisée. En effet, une même suite de chiffres peut représenter

des valeurs très différentes selon le système de numération utilisé.

Prenons l’exemple de l’écriture 101. Si on la lit en base 10 (système décimal), elle représente simplement le nombre cent un.

En revanche, si on interprète cette même écriture en base 6, sa valeur change : le chiffre 1 de gauche correspond à

6², le 0 à 6¹ et le 1 de droite 6⁰. On obtient alors 1×62+0×6+1=36+1=37. Enfin, en base 2 (binaire), l’écriture 101

correspond à 1×22+0×2+1=4+1=5.

Ainsi, sans indication de la base, il est impossible de connaître la valeur exacte du nombre. Pour lever toute ambiguïté, on précise généralement la base en l’indiquant en indice. On écrit par exemple

![permission_cat](https://github.com/Wextc/ESI_Bachelier/blob/main/1ARC1A_Architecture_des_ordinateurs_I/img/Ch_1_10.png)

pour le décimal,

![permission_cat](https://github.com/Wextc/ESI_Bachelier/blob/main/1ARC1A_Architecture_des_ordinateurs_I/img/Ch_1_06.png)

pour la base 6 ou

​![permission_cat](https://github.com/Wextc/ESI_Bachelier/blob/main/1ARC1A_Architecture_des_ordinateurs_I/img/Ch_1_02.png)

pour le binaire. Cette notation permet de savoir immédiatement dans quel système de numération le nombre est exprimé et

d’éviter toute confusion.

### 1.1 Calcul dans une base quelconque

<b> Calcul binaire :</b>

Le calcul binaire est un mode de calcul fondé sur le système de numération en base 2. Dans ce système, seuls deux chiffres

sont utilisés : 0 et 1. Toutes les opérations numériques, comme l’addition, la soustraction ou la multiplication, reposent

sur des combinaisons de ces deux valeurs. Le calcul binaire est au cœur du fonctionnement des ordinateurs, car les circuits

électroniques peuvent facilement représenter deux états distincts, par exemple allumé ou éteint.

<b>Base 2 : </b>

La base 2, <b> aussi appelée système binaire </b>, est un système de numération dans lequel les nombres sont écrits en

utilisant uniquement deux chiffres : 0 et 1. La base 2 indique que chaque position dans un nombre représente une puissance de

2.

Dans ce système, la valeur d’un chiffre dépend de sa position : en partant de la droite, les positions correspondent à 2⁰,

2¹, 2², 2³, et ainsi de suite. Un chiffre égal à 1 signifie que la puissance de 2 correspondante est prise en compte, tandis

qu’un chiffre égal à 0 signifie qu’elle ne l’est pas.

La base 2 est fondamentale en informatique, car elle correspond directement au fonctionnement des composants électroniques,

qui peuvent représenter deux états distincts, comme ouvert ou fermé, vrai ou faux.

<b> Nombre binaire: </b>

Un nombre binaire est un nombre écrit dans ce système en base 2. Il est constitué uniquement de chiffres binaires, appelés

bits, qui sont 0 et 1. Comme dans le système décimal, la valeur d’un chiffre dépend de sa position dans le nombre : chaque

position correspond à une puissance de 2. Ainsi, un nombre binaire représente une quantité en combinant des puissances de 2

pondérées par des 0 ou des 1.

<b> Octet :</b>

Un octet est un regroupement de huit chiffres binaires, c’est-à-dire de huit bits. Il constitue une unité fondamentale de

l’informatique, notamment pour représenter des données comme des caractères, des nombres ou des instructions. Un octet peut

représenter 256 valeurs différentes, ce qui permet par exemple de coder une lettre, un symbole ou une petite valeur numérique.

<b> Pourquoi utiliser le système binaire? </b>

Par souci de simplicité.

Il est en effet simple de distinguer deux valeurs de tension sur un fil.

Si l’on avait souhaité reproduire directement le calcul décimal, dix valeurs différentes de la tension auraienté été

nécessaires, ce qui aurait rendu les circuits beaucoup plus complexes.

<b> Quelle technique à-t-on trouvé pour rendre l'écriture binaire le plus compacte possible?</b>

Le calcul binaire, fondé sur la base 2 et utilisant uniquement les chiffres 0 et 1, est essentiel en informatique car il

correspond au fonctionnement des circuits électroniques. Un nombre binaire est donc une suite de bits, et huit bits forment

un octet, unité fondamentale pour représenter les données.

Cependant, l’écriture binaire présente un inconvénient majeur : elle est peu compacte. Pour un même nombre, la représentation

binaire nécessite environ trois fois plus de symboles que la représentation décimale. Cette différence s’explique par le fait

que le nombre de chiffres nécessaires dépend du logarithme du nombre dans la base choisie.

Pour pallier ce problème de longueur, d’autres bases ont été utilisées en informatique, notamment la base 8 (octale) et la

base 16 (hexadécimale). Ces systèmes offrent une écriture plus courte et plus lisible que le binaire, tout en restant

étroitement liés à celui-ci. Ils constituent ainsi un compromis pratique entre la simplicité du binaire pour les machines et

la lisibilité pour les humains.

<b> Atttention : </b>

La base 8 n'est plus utilisée contrairement à la base 16.

<b>Qu'est ce qui détermine le poids des bits? </b>

​![permission_cat](https://github.com/Wextc/ESI_Bachelier/blob/main/1ARC1A_Architecture_des_ordinateurs_I/img/Ch_1_10_poids.png)

Dans un nombre binaire ou dans une donnée composée de plusieurs octets, l’octet de poids fort est celui qui se situe le plus

à gauche. C’est lui qui représente la valeur la plus élevée, car il est associé aux puissances de 2 les plus grandes. À

l’inverse, l’octet de poids faible se trouve le plus à droite et correspond aux plus petites puissances de 2.

De manière générale, le poids d’un bit ou d’un octet dépend de sa position dans l’écriture du nombre. Lorsqu’on se déplace

vers la gauche, le poids augmente : chaque déplacement vers la gauche multiplie la valeur par 2. À l’inverse, lorsqu’on se

déplace vers la droite, le poids diminue : chaque déplacement divise la valeur par 2.

Il est souvent utile de pouvoir désigner la partie la plus ou la moins importante d’un nombre, c’est-à-dire celle qui pèse le

plus ou le moins dans le calcul de sa valeur. Cela correspond aux symboles placés le plus à gauche ou le plus à droite dans

l’écriture du nombre, quelle que soit la base utilisée. On parle ainsi du bit de poids fort et du bit de poids faible pour un

nombre binaire, du chiffre de poids fort ou de poids faible pour un nombre décimal, ou encore du symbole hexadécimal de poids

fort ou faible.

Par extension, lorsqu’un nombre binaire est écrit sur plusieurs octets, on appelle octet de poids fort l’ensemble des huit

bits situés le plus à gauche dans l’écriture binaire de ce nombre, et octet de poids faible l’ensemble des huit bits situés

le plus à droite. Ainsi, la position détermine directement l’importance d’un bit ou d’un octet dans la valeur totale du

nombre, ce qui justifie les notions de poids fort et de poids faible.
