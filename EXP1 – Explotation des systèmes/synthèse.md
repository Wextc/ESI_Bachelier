## Bash – Manipuler des fichiers textes:

### Obtenir quelques statistiques:

wc -l → lignes seulement

wc -L → plus longue ligne

uniq → supprime doublons

uniq -c → compte les occurrences

sort | uniq → pour vrais doublons non triés

---

## Manipuler des fichiers textes

### 3 - Numéroter des lignes && 4 - Afficher les premières ou dernières lignes

nl fichier → numéroter les lignes

head -n K → K premières lignes

head -n -K → tout sauf les K dernières

tail -n K → K dernières lignes

tail -n +K → à partir de la ligne K

---

### 4 - Afficher les premières ou dernières lignes

head -n K → premières K lignes

head -n -K → tout sauf les K dernières

tail -n K → dernières K lignes

tail -n +K → à partir de la ligne K

### 5 - Concaténer des fichiers && 6 - Trier des lignes

cat → fusionner fichiers

sort → trier

sort -r → inverse

sort -u → sans doublons

cut -c → extraire colonnes/positions

paste → coller ligne par ligne

### 8 - Extraire des lignes:

grep -e mot → chercher un mot

-e mot1 -e mot2 → OU

-F → texte exact (pas regex)

-n → numéros de ligne

-v → exclure

-r → dossier entier

### 9 - Remplacer des occurrences:

sed 's/a/b/' → remplace 1 fois par ligne

sed 's/a/b/g' → remplace partout

\. → point réel

\& → caractère &

<b>Trier un CSV par colonne (continent):</b>

```
sort elevation-extremes.csv -t ',' -k 1

```

Explication:

- " -t " ',' → séparateur = virgule (CSV)

- " -k " 1 → trie selon la colonne 1 (continent)

<b>Trier un TSV avec tabulation:</b>

```
sort cities/eu.be.tsv -t $'\t' -k 2

```

Explication:

- " $'\t' " → tabulation

- " -k " 2 → colonne 2 (ex : provinces)

<b>Trier planets.csv par gravité (sans option):</b>

```
sort planets.csv -t ',' -k 4

```

Résultat:

Mauvais tri → tri alphabétique (ex : 10 < 2)

Trier correctement par gravité (numérique)

```
sort planets.csv -t ',' -k 4 -n

```

Explication:

" -n " → tri numérique

<b>Trier par volume (notation scientifique):</b>

```
sort planets.csv -t ',' -k 2 -g

```

Explication:

- " -g " → gère les nombres comme 6e10

<b>Trier par nombre de lunes (du plus grand au plus petit):</b>

```
sort planets.csv -t ',' -k 6 -n -r

```

Explication:

- " -n "→ numérique

- " -r " → ordre inverse (descendant)

<b>Trier earthquakes par magnitude:</b>

```
sort earthquakes.dsv -t ',' -k 2 -n

```

(adapter la colonne selon le fichier)

<b>Trier et enregistrer dans un fichier:</b>

```
sort mots.txt -o mots-trie.txt

```

Explication:

- " -o " → sauvegarde le résultat

Exemple complet:

Créer un fichier :

```
cat > mots.txt
chat
chien
abeille
zebre
lion
Ctrl + D

```

Puis trier :

```
sort mots.txt -o mots-trie.txt

```

<b>Extraire des colonnes avec cut:</b>

Commande demandée

```
cut planets.csv -d ',' -f 1,6,5

```

Explication

- " -d " ',' → séparateur CSV

- " -f " → colonnes :

- " 1 " → nom planète

- " 6 " → nombre de satellites

- " 5 " → anneaux

### 10 - Trier un colonne:

sort -t ',' -k N → trier colonne N

-n → nombres

-g → notation scientifique

-r → inverse

-o → sauvegarder

cut -d ',' -f X → extraire colonnes
