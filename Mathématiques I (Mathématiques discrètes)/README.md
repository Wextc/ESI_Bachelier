# Synthèse complète des 5 premiers chapitres et utile pour les exercices

## Chapitre 1 – Algèbre booléenne

Résumé ultra-court:
traduction logique + tables de vérité + simplifications + rigueur

### 1. Propositions logiques

Une proposition logique est une phrase qui admet une valeur de vérité unique :

vrai

faux

Exemples :

```
1 + 1 = 2 → vrai

3 < 2 → faux

```

Les propositions sont notées en général : p, q, r, …

### 2. Connecteurs logiques

| Connecteur  | Symbole | Lecture                | Valeur vraie si…                                |
| ----------- | ------- | ---------------------- | ----------------------------------------------- |
| Négation    | ¬p      | non p                  | p est faux                                      |
| Conjonction | p ∧ q   | p et q                 | p et q sont vrais                               |
| Disjonction | p ∨ q   | p ou q                 | au moins un des deux est vrai                   |
| Implication | p → q   | si p alors q           | faux **uniquement** si p est vrai et q est faux |
| Équivalence | p ↔ q   | p si et seulement si q | p et q ont la même valeur                       |

⚠️ Remarques importantes :

le ou logique est inclusif

une implication avec une hypothèse fausse est toujours vraie

### 3. Tables de vérité

Les tables de vérité servent à :

calculer la valeur d’une formule logique

vérifier si une proposition est une tautologie, contradiction ou contingente

Exemple : table de vérité de p → q

| p   | q   | p → q |
| --- | --- | ----- |
| V   | V   | V     |
| V   | F   | F     |
| F   | V   | V     |
| F   | F   | V     |

Nombre de lignes d’une table :

```
2^n   (n = nombre de propositions)

```

### 4. Lois fondamentales de l’algèbre booléenne

| Expression | Résultat |
| ---------- | -------- |
| p ∧ faux   | faux     |
| p ∨ vrai   | vrai     |
| p ∧ vrai   | p        |
| p ∨ faux   | p        |
| p ∧ p      | p        |
| p ∨ p      | p        |
| p ∧ ¬p     | faux     |
| p ∨ ¬p     | vrai     |

👉 Ces lois servent à simplifier les expressions (exercices 1.3, 1.8, 1.9)

### 5. Traduction langage courant ↔ logique

| Phrase en français     | Traduction logique |
| ---------------------- | ------------------ |
| p et q                 | p ∧ q              |
| p ou q                 | p ∨ q              |
| non p                  | ¬p                 |
| si p alors q           | p → q              |
| p seulement si q       | p → q              |
| p si et seulement si q | p ↔ q              |

⚠️ Attention aux mots piégeux :

« sauf si »

« uniquement si »

doubles négations

### 6. Négation d’une proposition (Lois de De Morgan)

| Proposition | Négation |
| ----------- | -------- |
| ¬(p ∧ q)    | ¬p ∨ ¬q  |
| ¬(p ∨ q)    | ¬p ∧ ¬q  |
| ¬(p → q)    | p ∧ ¬q   |

👉 Indispensable pour les exercices de négation (exercice 1.5)

### 7. Implication : contraposée et réciproque

Pour une implication p → q :

| Forme       | Expression | Équivalence     |
| ----------- | ---------- | --------------- |
| Implication | p → q      | —               |
| Contraposée | ¬q → ¬p    | **équivalente** |
| Réciproque  | q → p      | pas équivalente |

📌 Les exercices 1.10 et 1.11 portent directement là-dessus.

### 8. Tautologie, contradiction, contingence

| Type          | Définition                    |
| ------------- | ----------------------------- |
| Tautologie    | toujours vraie                |
| Contradiction | toujours fausse               |
| Contingente   | parfois vraie, parfois fausse |

Méthodes pour vérifier :

    table de vérité

    simplification logique

### 9. Conditions logiques dans les algorithmes

Une condition est une proposition dépendant de variables (souvent entières).

Méthode générale :

comprendre quand la boucle s’arrête

déterminer ce qui est forcément vrai

déterminer ce qui est peut-être vrai

éliminer ce qui est forcément faux

👉 Très important pour les exercices 1.12 à 1.19

### 10. Classe de vérité

La classe de vérité d’une condition est :

l’ensemble des valeurs qui rendent la condition vraie

Utilisée pour :

analyser des boucles tant que

raisonner sur les valeurs possibles en sortie de programme

### 11. Méthode générale pour réussir les exercices

Checklist systématique :

identifier les propositions de base

traduire correctement en logique

utiliser une table de vérité si nécessaire

simplifier avec les lois

analyser soigneusement les implications

toujours justifier (calculs ou explication claire)

---

## Chapitre 2 – Théorie des ensembles

Résumé ultra-court:
écriture des ensembles + opérations + cardinaux + rigueur logique

### 1. Notions de base sur les ensembles

Définitions fondamentales

| Notation | Signification                      |     |                                   |
| -------- | ---------------------------------- | --- | --------------------------------- |
| `x ∈ A`  | x est un élément de A              |     |                                   |
| `x ∉ A`  | x n’est pas un élément de A        |     |                                   |
| `A ⊆ B`  | A est un sous-ensemble de B        |     |                                   |
| `A ⊂ B`  | A est un sous-ensemble strict de B |     |                                   |
| `∅`      | ensemble vide                      |     |                                   |
| `        | A                                  | `   | cardinal (nombre d’éléments) de A |

### 2. Écriture des ensembles

### 1. Notions de base sur les ensembles

Définitions fondamentales

| Notation | Signification                      |     |                                   |
| -------- | ---------------------------------- | --- | --------------------------------- |
| `x ∈ A`  | x est un élément de A              |     |                                   |
| `x ∉ A`  | x n’est pas un élément de A        |     |                                   |
| `A ⊆ B`  | A est un sous-ensemble de B        |     |                                   |
| `A ⊂ B`  | A est un sous-ensemble strict de B |     |                                   |
| `∅`      | ensemble vide                      |     |                                   |
| `        | A                                  | `   | cardinal (nombre d’éléments) de A |

### 2. Écriture des ensembles

a) En extension

On liste tous les éléments.

Exemple :

```
A = {1, 3, 5, 7}

```

b) En compréhension

On décrit les éléments par une propriété logique.

Exemple :

```
A = { x ∈ ℕ | x est impair et x < 10 }

```

Correspondance extension ↔ compréhension

| Extension   | Compréhension |                         |
| ----------- | ------------- | ----------------------- |
| `{2, 4, 6}` | `{ x ∈ ℕ      | x est pair et x ≤ 6 }`  |
| `{1, 4, 9}` | `{ x ∈ ℕ      | x = n², n ∈ ℕ, n ≤ 3 }` |

👉 Exercices concernés : 2.1, 2.2, 2.5

### 3. Ensembles de nombres usuels

| Symbole | Ensemble         |
| ------- | ---------------- |
| `ℕ`     | nombres naturels |
| `ℤ`     | entiers relatifs |
| `ℚ`     | rationnels       |
| `ℝ`     | réels            |

### 4. Opérations sur les ensembles

| Opération             | Notation | Définition                             |
| --------------------- | -------- | -------------------------------------- |
| Intersection          | `A ∩ B`  | éléments communs à A et B              |
| Union                 | `A ∪ B`  | éléments dans A ou B                   |
| Différence            | `A \ B`  | éléments dans A mais pas dans B        |
| Différence symétrique | `A Δ B`  | éléments dans A ou B mais pas les deux |

Tableau logique des opérations

| x ∈ A | x ∈ B | x ∈ A ∩ B | x ∈ A ∪ B | x ∈ A \ B | x ∈ A Δ B |
| ----- | ----- | --------- | --------- | --------- | --------- |
| V     | V     | V         | V         | F         | F         |
| V     | F     | F         | V         | V         | V         |
| F     | V     | F         | V         | F         | V         |
| F     | F     | F         | F         | F         | F         |

👉 Très utilisé dans les exercices 2.3, 2.4, 2.9, 2.10

### 5. Cardinal d’un ensemble

Définition

```
|A| = nombre d’éléments distincts de A

```

Propriétés importantes

| Situation       | Formule             |     |     |     |     |       |     |
| --------------- | ------------------- | --- | --- | --- | --- | ----- | --- |
| Ensembles finis | on compte           |     |     |     |     |       |     |
| A ∪ B           | `                   | A   | +   | B   | −   | A ∩ B | `   |
| Trois ensembles | inclusion–exclusion |     |     |     |     |       |     |

👉 Exercices : 2.1, 2.4, 2.6, 2.7, 2.8

### 6. Diagrammes de Venn

Ils servent à :

visualiser les unions, intersections, différences

résoudre des problèmes de comptage

Méthode générale

dessiner les ensembles

remplir les intersections d’abord

compléter les parties restantes

### 7. Intervalles réels

Notation des intervalles

| Intervalle | Signification |
| ---------- | ------------- |
| `[a, b]`   | a ≤ x ≤ b     |
| `]a, b[`   | a < x < b     |
| `[a, b[`   | a ≤ x < b     |
| `]a, b]`   | a < x ≤ b     |

👉 Exercices : 2.11, 2.12, 2.16, 2.17

### 8. Inclusion, appartenance : ne pas confondre ⚠️

| Expression | Sens                       |
| ---------- | -------------------------- |
| `2 ∈ A`    | 2 est un élément           |
| `{2} ∈ A`  | `{2}` est un élément       |
| `{2} ⊆ A`  | `{2}` est un sous-ensemble |

👉 Exercices pièges : 2.13, 2.14

### 9. Complémentaire (ensemble de référence S)

Si S est l’univers :

| Notation        | Définition                           |
| --------------- | ------------------------------------ |
| `Aᶜ` ou `S \ A` | éléments de S qui ne sont pas dans A |

### 10. Traduction logique ↔ ensembles

| Logique         | Ensembles   |
| --------------- | ----------- |
| `x ∈ A ∧ x ∈ B` | `x ∈ A ∩ B` |
| `x ∈ A ∨ x ∈ B` | `x ∈ A ∪ B` |
| `x ∈ A ∧ x ∉ B` | `x ∈ A \ B` |
| `x ∈ A ⊕ x ∈ B` | `x ∈ A Δ B` |
| `x ∈ A → x ∈ B` | `A ⊆ B`     |

👉 Très important pour les exercices 2.16 et 2.17

### 11. Méthode générale pour les exercices du chapitre 2

Checklist :

identifier l’univers (ℕ, ℤ, ℝ…)

traduire correctement les conditions

écrire proprement les ensembles

utiliser les opérations adaptées

vérifier inclusion / appartenance

justifier clairement chaque réponse

---

## Chapitre 3 – Théorie des graphes

Résumé ultra-court:
structure + degrés + connexité + Euler / Hamilton + modélisation

### 1. Définition d’un graphe

Un graphe non orienté est un couple :

G = (V, E)

```
G = (V, E)

```

Exemple :

```
V = {a, b, c}
E = {{a,b}, {b,c}}

```

### 2. Ordre et taille d’un graphe

| Notion | Définition            |     |     |
| ------ | --------------------- | --- | --- |
| Ordre  | nombre de sommets = ` | V   | `   |
| Taille | nombre d’arêtes = `   | E   | `   |

| Notion | Définition            |     |     |
| ------ | --------------------- | --- | --- |
| Ordre  | nombre de sommets = ` | V   | `   |
| Taille | nombre d’arêtes = `   | E   | `   |

### 3. Degré d’un sommet

Définition

Le degré d’un sommet = nombre d’arêtes qui y sont incidentes.

| Cas particulier | Contribution |
| --------------- | ------------ |
| arête classique | +1           |
| boucle          | +2           |

### Propriété fondamentale (à connaître par cœur)

Somme des degrés = 2 × nombre d’arêtes

👉 Utilisée dans les exercices 3.2, 3.6, 3.7

### 4. Graphe connexe

| Terme              | Signification                                     |
| ------------------ | ------------------------------------------------- |
| Graphe connexe     | il existe un chemin entre chaque paire de sommets |
| Graphe non connexe | au moins deux sommets non reliés                  |

### 5. Chemins, distances, diamètre

Définitions

| Notion            | Définition                           |
| ----------------- | ------------------------------------ |
| Chemin            | suite de sommets adjacents           |
| Distance `d(u,v)` | longueur du plus court chemin        |
| Diamètre          | distance maximale entre deux sommets |

👉 Exercices : 3.1, 3.5, 3.7

### 6. Matrice d’adjacence

Pour un graphe d’ordre n, matrice n × n :

| Valeur | Signification      |
| ------ | ------------------ |
| 1      | arête entre i et j |
| 0      | pas d’arête        |

Propriétés :

    diagonale nulle (sans boucle)

    matrice symétrique (graphe non orienté)

### 7. Graphe eulérien

Définitions

| Terme           | Condition                                 |
| --------------- | ----------------------------------------- |
| Chemin eulérien | traverse chaque arête exactement une fois |
| Graphe eulérien | possède un cycle eulérien                 |

Critère fondamental

| Graphe connexe | Sommets de degré impair | Conclusion            |
| -------------- | ----------------------- | --------------------- |
| oui            | 0                       | graphe eulérien       |
| oui            | 2                       | chemin eulérien       |
| oui            | > 2                     | ni eulérien ni chemin |
| non            | —                       | impossible            |

👉 Exercices : 3.2, 3.5, 3.6, 3.7

### 8. Graphe hamiltonien

Définition

| Terme              | Signification                    |
| ------------------ | -------------------------------- |
| Chemin hamiltonien | passe une fois par chaque sommet |
| Cycle hamiltonien  | revient au sommet de départ      |

⚠️ Contrairement à Euler :

pas de critère simple

on raisonne par construction ou intuition

👉 Exercices : 3.5, 3.10, 3.11

### 9. Arbre

Définition équivalente (très importante)

Un arbre est un graphe :

    connexe

    sans cycle

Propriétés fondamentales:

| Propriété | Valeur                    |
| --------- | ------------------------- |
| ordre     | n                         |
| taille    | n − 1                     |
| chemins   | unique entre deux sommets |

👉 Exercices : 3.1, 3.2

### 10. Nombre chromatique (coloration)

Définition

Nombre minimum de couleurs pour colorier les sommets sans conflit.

| Graphe              | Nombre chromatique |
| ------------------- | ------------------ |
| graphe biparti      | 2                  |
| graphe complet `Kₙ` | n                  |
| arbre               | 2 (si n ≥ 2)       |

👉 Exercices : 3.1, 3.5, 3.8, 3.9

### 11. Graphe complet

Définition

Tous les sommets sont reliés deux à deux.

| Notation               | Propriété                  |
| ---------------------- | -------------------------- |
| `Kₙ`                   | graphe complet à n sommets |
| taille                 | `n(n−1)/2`                 |
| degré de chaque sommet | `n−1`                      |

### 12. Modélisation par graphes

| Situation        | Sommets  | Arêtes           |
| ---------------- | -------- | ---------------- |
| incompatibilités | objets   | conflits         |
| antennes         | antennes | interférences    |
| wagons           | plantes  | incompatibilités |

👉 Exercices : 3.8, 3.9

### 13. Méthode générale pour réussir les exercices

Checklist :

identifier sommets et arêtes

déterminer ordre et taille

calculer les degrés

vérifier connexité

appliquer critères eulériens

raisonner pour Hamilton

justifier clairement

---

## Chapitre 4 – Dénombrement

Résumé ultra-court:

ordre / répétition / contraintes / méthode

### 1. Principe fondamental du dénombrement

Principe multiplicatif

Si une action se fait en plusieurs étapes indépendantes :

```
nombre total = produit des possibilités de chaque étape

```

Exemple :

3 choix pour A

5 choix pour B

→ 3 × 5 = 15 possibilités

👉 Base de presque tous les exercices

### 2. Factorielle

Définition

```
n! = n × (n−1) × … × 2 × 1

```

| n   | n!  |
| --- | --- |
| 0   | 1   |
| 1   | 1   |
| 2   | 2   |
| 3   | 6   |
| 4   | 24  |
| 5   | 120 |

### 3. Permutations (ordre important)

a) Tous les éléments sont distincts

```
n objets distincts → n!

```

Exemples :

mélanger 52 cartes → 52!

arranger des personnes en ligne

👉 Exercices : 4.1, 4.4, 4.12, 4.23

b) Avec répétitions (objets identiques)

```
n objets dont :

- a identiques

- b identiques

→ n! / (a! b!)

```

### 4. Arrangements (ordre important, choix partiel)

```
A(n,k) = n × (n−1) × … × (n−k+1)

```

👉 Utilisé quand :

on choisit k éléments

l’ordre compte

sans répétition

👉 Exercices : 4.3, 4.20, 4.26

### 5. Combinaisons (ordre non important)

```
C(n,k) = nombre de sous-ensembles de k éléments

```

👉 Utilisé quand :

l’ordre ne compte pas

sans répétition

Exemples :

équipes

choix de menus

loto

👉 Exercices : 4.2, 4.6, 4.13, 4.21

### 6. Avec ou sans répétition

Tableau décisionnel clé

| Situation                     | Répétition | Ordre | Méthode                      |
| ----------------------------- | ---------- | ----- | ---------------------------- |
| mots, codes                   | oui        | oui   | principe multiplicatif       |
| mots avec lettres différentes | non        | oui   | arrangements                 |
| équipes                       | non        | non   | combinaisons                 |
| choix illimité                | oui        | non   | combinaisons avec répétition |

### 7. Codes, chiffres, mots

Codes de chiffres

| Cas                      | Méthode                |
| ------------------------ | ---------------------- |
| chiffres autorisés       | principe multiplicatif |
| chiffres différents      | arrangements           |
| contraintes (début, fin) | découper en cas        |

👉 Exercices : 4.7, 4.8, 4.9, 4.15, 4.16, 4.17, 4.25

### 8. Méthode par cas (ou complémentaire)

Très fréquente 🔥

Exemple

```
nombre total − cas interdits

```

👉 Exercices :

“ne contient pas”

“au moins”

“exactement”

### 9. Problèmes de type « au moins / exactement »

| Formulation  | Méthode             |
| ------------ | ------------------- |
| exactement k | compter directement |
| au moins k   | total − moins de k  |
| au plus k    | somme des cas       |

### 10. Problèmes de poignées de mains

    Formule clé

    n personnes → n(n−1)/2 poignées

👉 Exercices : 4.12

### 11. Problèmes de répartition

Cas typique

répartir des objets identiques

ordre sans importance

👉 Exercices : 4.14

### 12. Inclusion–exclusion (liens avec chap. 2)

Deux ensembles

```
|A ∪ B| = |A| + |B| − |A ∩ B|

```

Trois ensembles

```
|A ∪ B ∪ C|
= |A| + |B| + |C|
− |A ∩ B| − |A ∩ C| − |B ∩ C|
+ |A ∩ B ∩ C|

```

👉 Exercices : 4.27

### 13. Problèmes de placement (tables, rangées)

| Cas                 | Attention                       |
| ------------------- | ------------------------------- |
| table ronde         | rotations équivalentes          |
| table rectangulaire | positions distinctes            |
| contraintes         | placer d’abord ce qui contraint |

👉 Exercices : 4.23, 4.24

### 14. Méthode générale pour réussir les exercices

Checklist universelle :

ordre important ou non ?

répétition autorisée ou non ?

contraintes ?

découper en cas si nécessaire

utiliser le complément si plus simple

ne jamais écrire de formules non développées (exigence du syllabus)

## Chapitre 5 – Principe de récurrence

### 1. Définitions récursives

Une définition récursive décrit un objet :

à partir de cas de base

et d’une relation de récurrence

Structure générale

```
f(0) = valeur initiale
f(n) = expression utilisant f(n−1), f(n−2), …
```

Exemple

```
f(0) = 1
f(n) = 2f(n−1)
```

👉 Exercices : 5.1, 5.2, 5.3, 5.4

### 2. Calcul de termes d’une suite récursive

Méthode systématique

partir du cas de base

calculer les valeurs une à une

ne jamais sauter d’étape

Exemple

```
f(0) = 1
f(n) = f(n−1) + 2
```

| n   | f(n) |
| --- | ---- |
| 0   | 1    |
| 1   | 3    |
| 2   | 5    |
| 3   | 7    |

### 3. Définition récursive valide ou non

Pour être valide, une définition récursive doit :

| Condition       | Explication                    |
| --------------- | ------------------------------ |
| Cas de base     | valeur définie explicitement   |
| Progression     | dépend de valeurs plus petites |
| Pas d’ambiguïté | une seule valeur possible      |

👉 Exercices : 5.4

### 4. Définir une suite récursive à partir d’une formule

On transforme une formule explicite en définition récursive.

Exemple

```
aₙ = 4n − 2

```

Définition récursive :

```
a₀ = −2
aₙ = aₙ₋₁ + 4

```

👉 Exercices : 5.5, 5.16

### 5. Principe de récurrence (preuve par récurrence)

Schéma fondamental

Pour prouver :

```
∀ n ∈ ℕ, P(n)
```

Étapes obligatoires (TOUJOURS)

| Étape                   | Contenu              |
| ----------------------- | -------------------- |
| Initialisation          | prouver P(0) ou P(1) |
| Hypothèse de récurrence | supposer P(n) vraie  |
| Hérédité                | prouver P(n+1)       |
| Conclusion              | donc P(n) vraie ∀ n  |

⚠️ Ne jamais oublier une étape → points perdus à l’examen

### 6. Hypothèse de récurrence : bien l’utiliser

Exemple

À prouver :

```
∑ᵢ₌₁ⁿ i = n(n+1)/2

```

Hypothèse :

```
∑ᵢ₌₁ⁿ i = n(n+1)/2

```

Hérédité :

```
∑ᵢ₌₁ⁿ⁺¹ i = (∑ᵢ₌₁ⁿ i) + (n+1)

```

👉 Exercices : 5.10, 5.11

### 7. Types de preuves par récurrence

a) Récurrence simple

| Dépend de | Exemple           |
| --------- | ----------------- |
| P(n)      | sommes classiques |

b) Récurrence double

| Dépend de      | Exemple                  |
| -------------- | ------------------------ |
| P(n−1), P(n−2) | suites de type Fibonacci |

👉 Exercices : 5.3

### 8. Récurrence et inégalités

Très fréquent ⚠️

Méthode type

supposer l’inégalité vraie à l’ordre n

majorer ou minorer proprement

conclure pour n+1

👉 Exercices : 5.12, 5.13

### 9. Récurrence et divisibilité

Objectif

Montrer que :

```
f(n) est divisible par k

```

Méthode

écrire f(n+1)

factoriser

faire apparaître le facteur k

👉 Exercices : 5.17, 5.18

### 10. Récurrence avec sommes et produits

Sommes

| Forme | Technique                |
| ----- | ------------------------ |
| ∑ aᵢ  | séparer le dernier terme |

Produits

| Forme | Technique                 |
| ----- | ------------------------- |
| ∏ aᵢ  | isoler le dernier facteur |

👉 Exercices : 5.14, 5.15

### 11. Récurrence sur des ensembles

Exemple

```
⋂ᵢ₌₁ⁿ Sᵢ ∪ T = ⋂ᵢ₌₁ⁿ (Sᵢ ∪ T)

```

Méthode :

initialisation n = 1

utiliser propriétés des ensembles

👉 Exercices : 5.19, 5.20

### 12. Récurrence sur des graphes

on construit Gₙ à partir de Gₙ₋₁

on prouve une propriété structurelle

👉 Exercices : 5.21, 5.24

### 13. Coefficients binomiaux (récursifs)

Définition récursive

```
C(n,0) = 1
C(n,n) = 1
C(n,k) = C(n−1,k−1) + C(n−1,k)
```

👉 Exercices : 5.23

### 14. Récurrence et algorithmes

On prouve une propriété :

ligne par ligne

nombre d’itérations

👉 Exercice : 5.25

### 15. Méthode générale pour réussir les exercices

Checklist finale :

identifier la propriété P(n)

vérifier le bon point de départ

écrire clairement l’hypothèse

utiliser l’hypothèse (pas juste la recopier)

conclure explicitement
