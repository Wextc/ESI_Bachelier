# Chapitre 1 — Algèbre booléenne

## 1.1 Propositions et opérateurs logiques

Définition — Proposition

Une proposition est une phrase qui a une valeur de vérité, vraie (V) ou fausse (F) (pas les deux, pas “ça dépend”).

Exemples :

« La carotte est un légume » (V) ;

« La carotte est un moyen de locomotion » (F) ;

« Arrache cette carotte ! » n’est pas une proposition (c’est un ordre, pas un énoncé vrai/faux).

Définition — Tautologie / Antilogie (contradiction)

Tautologie : toujours vraie, quelles que soient les valeurs des sous-propositions (dernière colonne remplie de V).

Antilogie (contradiction) : toujours fausse (dernière colonne remplie de F).

Intérêt : les tautologies servent de règles de raisonnement sûres.

Opérateurs logiques (avec intuition rapide)

Négation (¬p) : “non p”. Inverse V/F.

Table : p | ¬p → V|F, F|V. Exemple : « au moins 8 GB » → négation : « moins de 8 GB ».

Conjonction (p ∧ q) : “p ET q”. Vraie seulement si p et q sont vraies.

Intuition : les deux feux doivent être au vert pour passer.

Disjonction (p ∨ q) (ou inclusif) : “p OU q (ou les deux)”. Vraie si au moins un des deux est vrai.

Piège courant : “ou” mathématique est inclusif, pas exclusif.

Disjonction exclusive (p ⊕ q) : “soit p, soit q (mais pas les deux)”.

Lien utile : p⊕q≡¬(p⇔q).

Équivalence (p ⇔ q) : “p ssi q”. Vraie quand p et q ont la même valeur.

Astuce : c’est « égalité de bits ».

Implication (p ⇒ q) : “si p alors q”.

Seul cas faux : p est vrai et q est faux.

Lecture correcte : “p suffit pour q” (et pas “p cause q”).

Forme utile : p⇒q≡¬p∨q ; aussi p⇒q≡¬(p∧¬q).

Contraposée : ¬q⇒¬p. Équivalente à p⇒q (même table de vérité).

Réciproque : q⇒p. Non équivalente en général (peut être fausse quand p⇒q est vraie).

## 1.2 Calcul propositionnel et priorités

Priorité des opérateurs (du plus fort au plus faible) :

¬ → ∧ → ∨ → ⇒ → ⇔.

Réflexe : mettre des parenthèses si doute.

Lois importantes (à connaître + à savoir utiliser) :

De Morgan :

¬(p∧q)≡(¬p∨¬q) ;

¬(p∨q)≡(¬p∧¬q).

(Très pratique pour “faire sortir” une négation.)

Négation de l’implication : ¬(p⇒q)≡(p∧¬q).

(Directement la « seule ligne » où p⇒q est fausse.)

Lien équivalence / XOR : ¬(p⇔q)≡(p⊕q).

# Chapitre 2 — Théorie des ensembles

## 2.1 Concepts de base

Définition — Ensemble

Un ensemble est une collection d’objets distincts (ses éléments).

Notations : x∈S (x appartient), x∈/S (x n’appartient pas).

Égalité d’ensembles

S1​=S2​ ssi ils ont exactement les mêmes éléments (l’ordre/les noms n’ont pas d’importance).

Sous-ensemble

A⊆B ssi tout élément de A est dans B. A⊂B = inclusion stricte. (Rappel de langage courant en suite du chapitre.)

Cardinal

∣S∣ = nombre d’éléments si S est fini (les subtilités infinis arrivent plus tard).

Ensemble vide

∅ : unique ensemble sans élément ; ∅⊆S pour tout S.

## 2.2 Définition en compréhension

On définit un ensemble en donnant une propriété :

sur S={x∣proprieˊteˊ sur x}.

Exemples : P={2k∣k∈Z} (pairs).

Avantage : pratique pour grands/infinis ensembles.

## 2.3 Opérations ensemblistes (pont logique ↔ ensembles)

Parties

P(S)={A∣A⊆S}. Si S est fini : ∣P(S)∣=2∣S∣.

Ex. pour S={a,b,c}, P(S) a 8 ensembles.

Complémentaire

Dans un univers U (important de le fixer) : Ac=U∖A={x∈U∣x∈/A}.

Intuition : “tout ce qui n’est pas dans A”.

Union

A∪B={x∣x∈A ∨ x∈B}. (OU logique.)

Intersection

A∩B={x∣x∈A ∧ x∈B}. (ET logique.)

Différence

A∖B={x∈A∣x∈/B}. (A sans B.)

Différence symétrique

A△B=(A∪B)∖(A∩B) = “dans l’un ou l’autre, mais pas les deux” (c’est le XOR des ensembles).

Produit cartésien

A×B={(a,b)∣a∈A, b∈B} — base des relations/fonctions.

# Chapitre 3 — Théorie des graphes

## 3.1 Concepts de base

Graphe non orienté

Un graphe G=(V,E) avec V = sommets et E = paires non ordonnées de sommets (arêtes). (Déf. de base du chapitre.)

Adjacence : u et v sont adjacents si {u,v}∈E.

Voisinage : N(v)={u∣{u,v}∈E}.

Degré : d(v)=∣N(v)∣.

Somme des degrés = 2∣E∣. (Formule « chaque arête compte pour 2 ».)

## 3.2 Chemins et connexité

Chemin

Suite de sommets v1​−v2​−⋯−vk​ avec une arête entre chaque voisins de la suite. (Longueur = nombre d’arêtes.)

Connexe

Un graphe est connexe si toute paire de sommets est reliée par un chemin. (Sinon : plusieurs composantes.)

Cycle

Chemin fermé v1​=vk+1​ (avec sommets distincts pour “élémentaire”). Acyclique = sans cycle.

Arbre

Graphe connexe et acyclique. Faits équivalents (classiques) : un arbre à n sommets a n−1 arêtes ; il existe un unique chemin entre deux sommets. (Section “Arbres” du chapitre.)
3.3 Distances
Distance
∣u,v∣G​ = longueur du plus court chemin entre u et v.
Matrice des distances : tableau des ∣u,v∣G​.
Diamètre
D(G)=maxu,v∈V​∣u,v∣G​ (la plus grande de ces distances). (Défs groupées dans la section distance/diamètre.)
3.4 Coloration
Coloration
Attribuer des couleurs aux sommets pour que deux adjacents n’aient pas la même couleur.
Nombre chromatique
χ(G) = nombre minimal de couleurs pour une coloration valide.
(Rappel classique : les graphes planaires sont colorables en ≤ 4 couleurs — théorème cité dans le chapitre.)

Mini-pense-bête (utilisation)
• Transformer p⇒q en ¬p∨q simplifie souvent les tables de vérité et les preuves par équivalences.
• Pour dé-négativer une formule : appliquer De Morgan jusqu’au bout.
• En ensembles, pensez OU ↔ ∪, ET ↔ ∩, NON ↔ complémentaire.
• En graphes, vérifier la connexité avant de parler de distances/diamètre ; la somme des degrés donne vite ∣E∣.
