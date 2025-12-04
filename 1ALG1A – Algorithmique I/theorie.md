## Chapitre 2

### Algorithmes séquentiels

- Algorithme séquentiel

Un algorithme séquentiel (ou linéaire) exécute une suite d’instructions dans l’ordre, une seule fois, sans alternatives ni boucles.

Données

Les algorithmes manipulent différents types de données selon le contexte (ingrédients, briques, rues…).
En informatique, les données de base sont :

Nombres

Booléens

Chaînes de caractères

- Variables

Les variables stockent des valeurs en mémoire et peuvent changer pendant l’exécution de l’algorithme.

Chaque variable a un type, qui détermine la nature des données qu’elle peut contenir.

- Types principaux

| Type    | Contenu possible | Remarques                           |
| ------- | ---------------- | ----------------------------------- |
| Entier  | 0, 5, 42, …      | Éléments de ℤ                       |
| Réel    | 2,5, 0,333…      | Peut aussi contenir des entiers     |
| Booléen | vrai / faux      | Deux seules valeurs possibles       |
| Chaîne  | "texte", "x", "" | Suite de caractères, peut être vide |

- Types et langages

Les types peuvent varier selon les langages (ex. Java : byte, short, int, long).

Les nombres réels sont souvent tronqués à cause de la capacité mémoire.

Certains langages (ex. Python) déterminent le type d’une variable automatiquement à partir de son contenu.

En algorithmique, on utilise des types simples et généraux pour la pédagogie, avant de les adapter dans un langage spécifique.

- Forme générale d’un algorithme

Forme générale d’un algorithme

Un algorithme suit généralement la structure suivante :

```
algorithme [nom]
    // déclaration des données
    // lecture des données
    // instructions agissant sur les données
    // écriture du résultat
fin
```

algorithme [nom] : ligne introductive (en-tête) qui donne un nom à l’algorithme.

Déclaration des données : section où l’on définit les variables qui seront utilisées.

Lecture des données : section où l’on récupère les valeurs fournies par l’utilisateur (Lire).

Instructions agissant sur les données : section où l’on effectue les calculs ou traitements nécessaires.

Écriture du résultat : section où l’on affiche les résultats (Écrire).

fin : ligne finale qui indique la fin de l’algorithme.

- Déclaration des données

La déclaration des données liste les variables utilisées dans l’algorithme.

Elle résulte de la compréhension du problème et de l’identification des données nécessaires pour obtenir le résultat attendu.

La forme générale d’une déclaration est :

nom_de_variable : type

Le nom de variable doit être clair et refléter son rôle.

Les noms peuvent être composés de plusieurs mots, mais sans espaces, par exemple :

nombreSpectateurs, prix_beurre, plaqueImmatriculation

Plusieurs variables peuvent être déclarées sur une seule ligne :

```
nombre1, nombre2, nombre3 : entier

```

Les noms peuvent contenir des chiffres, mais pas au début.

Il est conseillé d’éviter des variables différant uniquement par la casse (nombrePersonnes ≠ NombrePersonnes).

Bien que facultative dans certains langages (comme Python), la déclaration des données est utile à titre pédagogique pour structurer l’algorithme.

Exemples de types de variables :

quantité : entier

prix : réel

adresse : chaîne

exact : booléen
