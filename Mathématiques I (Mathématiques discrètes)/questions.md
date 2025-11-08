🧩 CHAPITRE 1 — ALGÈBRE BOOLÉENNE
🔹 Q1. Qu’est-ce qu’une proposition ?

Réponse :
Une proposition est un énoncé qui possède une valeur de vérité : vraie (V) ou fausse (F).
Exemples :
✔️ « 2 est pair » → vraie  ✖️ « Va au marché ! » → pas une proposition.

🔹 Q2. Qu’est-ce qu’une tautologie ? une contradiction ?

Réponse :

Tautologie : proposition toujours vraie, quelle que soit la valeur des variables.
Ex :
𝑝
∨
¬
𝑝
p∨¬p.

Contradiction (antilogie) : toujours fausse.
Ex :
𝑝
∧
¬
𝑝
p∧¬p.

🔹 Q3. Donne la table de vérité de l’implication
𝑝
⇒
𝑞
p⇒q.
p q p⇒q
V V V
V F F
F V V
F F V

Astuce : seule la ligne (V,F) est fausse.

🔹 Q4. Quelle est la forme logique équivalente à une implication ?

Réponse :

𝑝
⇒
𝑞
≡
¬
𝑝
∨
𝑞
p⇒q≡¬p∨q.

🔹 Q5. Quelle est la contraposée et la réciproque de
𝑝
⇒
𝑞
p⇒q ?

Réponse :

Contraposée :
¬
𝑞
⇒
¬
𝑝
¬q⇒¬p (équivalente).

Réciproque :
𝑞
⇒
𝑝
q⇒p (non équivalente).

🔹 Q6. Applique la loi de De Morgan à ¬(p ∧ q).

Réponse :

¬
(
𝑝
∧
𝑞
)
≡
(
¬
𝑝
∨
¬
𝑞
)
¬(p∧q)≡(¬p∨¬q).

🔹 Q7. Simplifie : ¬(p⇒q).

Réponse :

¬
(
𝑝
⇒
𝑞
)
≡
𝑝
∧
¬
𝑞
¬(p⇒q)≡p∧¬q.
(Intuitivement : « p vrai et q faux » est le seul cas où l’implication est fausse.)

🔹 Q8. Quelle est la différence entre disjonction et disjonction exclusive ?

Réponse :

𝑝
∨
𝑞
p∨q : vraie si au moins un est vrai.

𝑝
⊕
𝑞
p⊕q : vraie si exactement un est vrai.

🔹 Q9. Vrai ou faux : ¬(p⇔q) ≡ (p⊕q).

✅ Vrai.

🔹 Q10. Ordonne les opérateurs par priorité.

Réponse :
¬ > ∧ > ∨ > ⇒ > ⇔

🧮 CHAPITRE 2 — THÉORIE DES ENSEMBLES
🔹 Q1. Qu’est-ce qu’un ensemble ?

Réponse :
Une collection d’éléments distincts.
Notation :
𝑥
∈
𝐴
x∈A (“x appartient à A”),
𝑥
∉
𝐴
x∈
/
A (“x n’appartient pas à A”).

🔹 Q2. Que signifie
𝐴
⊆
𝐵
A⊆B ? et
𝐴
⊂
𝐵
A⊂B ?

Réponse :

𝐴
⊆
𝐵
A⊆B : tout élément de A est dans B (inclusion large).

𝐴
⊂
𝐵
A⊂B : A est inclus strictement dans B (A ≠ B).

🔹 Q3. Qu’est-ce que le cardinal d’un ensemble ?

Réponse :

∣
𝐴
∣
∣A∣ = nombre d’éléments de A.
Ex :
∣
{
1
,
2
,
3
}
∣
=
3
∣{1,2,3}∣=3.

🔹 Q4. Qu’est-ce que l’ensemble vide ?

Réponse :

∅
∅ est l’ensemble sans élément, de cardinal 0.

🔹 Q5. Définis un ensemble en compréhension.

Réponse :
On le définit par une propriété commune :

# 𝐸

{
𝑥
∣
propri
e
ˊ
t
e
ˊ
sur
𝑥
}
E={x∣propri
e
ˊ
t
e
ˊ
sur x}.
Ex :
{
𝑥
∈
N
∣
𝑥
<
5
}
=
{
0
,
1
,
2
,
3
,
4
}
{x∈N∣x<5}={0,1,2,3,4}.

🔹 Q6. Qu’est-ce que 𝒫(A) ?

Réponse :

𝑃
(
𝐴
)
P(A) = ensemble de toutes les parties de A (sous-ensembles).
Si |A| = n, alors
∣
𝑃
(
𝐴
)
∣
=
2
𝑛
∣P(A)∣=2
n
.

🔹 Q7. Définis :

Union :
𝐴
∪
𝐵
=
{
𝑥
∣
𝑥
∈
𝐴
∨
𝑥
∈
𝐵
}
A∪B={x∣x∈A∨x∈B}

Intersection :
𝐴
∩
𝐵
=
{
𝑥
∣
𝑥
∈
𝐴
∧
𝑥
∈
𝐵
}
A∩B={x∣x∈A∧x∈B}

Différence :
𝐴
∖
𝐵
=
{
𝑥
∈
𝐴
∣
𝑥
∉
𝐵
}
A∖B={x∈A∣x∈
/
B}

Complémentaire :
𝐴
𝑐
=
𝑈
∖
𝐴
A
c
=U∖A (dans U).

Différence symétrique :
𝐴
△
𝐵
=
(
𝐴
∪
𝐵
)
∖
(
𝐴
∩
𝐵
)
A△B=(A∪B)∖(A∩B).

Produit cartésien :
𝐴
×
𝐵
=
{
(
𝑎
,
𝑏
)
∣
𝑎
∈
𝐴
,
𝑏
∈
𝐵
}
A×B={(a,b)∣a∈A,b∈B}.

🔹 Q8. Si A={1,2,3} et B={2,3,4}, calcule :

a) A∪B b) A∩B c) A\B
Réponse :
a) {1,2,3,4} b) {2,3} c) {1}.

🔹 Q9. Vrai ou faux :
(
𝐴
∩
𝐵
)
𝑐
=
𝐴
𝑐
∪
𝐵
𝑐
(A∩B)
c
=A
c
∪B
c
.

✅ Vrai (loi de De Morgan pour ensembles).

🔹 Q10. Si |A|=3 et |B|=2, quel est |A×B| ?

Réponse :
|A×B| = 3×2 = 6 couples.

🔵 CHAPITRE 3 — THÉORIE DES GRAPHES
🔹 Q1. Qu’est-ce qu’un graphe non orienté ?

Réponse :
Un couple
𝐺
=
(
𝑉
,
𝐸
)
G=(V,E) avec

V : sommets,

E : paires non ordonnées de sommets (les arêtes).

🔹 Q2. Quelle est la différence entre ordre et taille d’un graphe ?

Réponse :

Ordre = |V| (nombre de sommets).

Taille = |E| (nombre d’arêtes).

🔹 Q3. Définis : degré, voisinage, adjacence.

Réponse :

Adjacents : sommets reliés par une arête.

Voisinage :
𝑁
(
𝑣
)
=
{
𝑢
∣
{
𝑢
,
𝑣
}
∈
𝐸
}
N(v)={u∣{u,v}∈E}.

Degré :
𝑑
(
𝑣
)
=
∣
𝑁
(
𝑣
)
∣
d(v)=∣N(v)∣ (nombre d’arêtes incidentes).

🔹 Q4. Quelle relation relie la somme des degrés et le nombre d’arêtes ?

Réponse :

∑
𝑣
∈
𝑉
𝑑
(
𝑣
)
=
2
∣
𝐸
∣
v∈V
∑
​

d(v)=2∣E∣.

🔹 Q5. Qu’est-ce qu’un graphe connexe ?

Réponse :
G est connexe s’il existe un chemin entre chaque paire de sommets.

🔹 Q6. Qu’est-ce qu’un cycle ?

Réponse :
Un chemin fermé dont le premier et le dernier sommet sont les mêmes.

🔹 Q7. Qu’est-ce qu’un arbre ?

Réponse :
Graphe connexe et acyclique (sans cycles).
Un arbre à n sommets a n − 1 arêtes.

🔹 Q8. Quelles sont les conditions d’existence :

Cycle eulérien : tous les sommets de degré pair.

Chemin eulérien : 0 ou 2 sommets de degré impair.

🔹 Q9. Qu’est-ce qu’un chemin ou cycle hamiltonien ?

Réponse :
Chemin (ou cycle) qui passe exactement une fois par chaque sommet.

🔹 Q10. Qu’est-ce que le diamètre d’un graphe ?

Réponse :
La plus grande distance (plus court chemin minimal) entre deux sommets du graphe.

🔹 Q11. Qu’est-ce qu’une coloration de graphe ?

Réponse :
Attribuer une couleur à chaque sommet de sorte que deux sommets adjacents n’aient jamais la même couleur.

🔹 Q12. Qu’est-ce que le nombre chromatique χ(G) ?

Réponse :
Le nombre minimum de couleurs nécessaires pour une coloration valide.

🔹 Q13. Énonce le théorème des 4 couleurs.

Réponse :
Tout graphe planaire peut être colorié avec au plus 4 couleurs.

🔹 Q14. Donne un exemple concret.

Réponse :
Colorier les pays d’une carte sans deux pays voisins de même couleur : 4 couleurs suffisent.
