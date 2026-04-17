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

### 10 - Trier un colonne:

sort -t ',' -k N → trier colonne N

-n → nombres

-g → notation scientifique

-r → inverse

-o → sauvegarder

cut -d ',' -f X → extraire colonnes

### Bash – Redirection

## 1 - Flux standard:

stdin (0) → clavier

stdout (1) → écran

stderr (2) → erreurs

<b>Commandes vues</b>

sort → trie

wc → compte

tr → remplace caractères

Astuce importante

sans fichier → lecture clavier

Ctrl + D → fin de saisie

### 2 - Redirection de l'entrée standard:

```
nano enum.txt

```

tr ',' '\n' < enum.txt

nano : créer/éditer le fichier

tr : remplacer les virgules par des retours à la ligne

< : faire lire le fichier à la commande

### 3 - Redirection de la sortie standard

'> → redirige (écrase)'

'>> → ajoute'

cat → concatène

echo → écrit du texte

tail -f → surveille un fichier en direct

### 4 - Redirection de la sortie d'erreur

" > "→ redirige sortie normale

" >> " → ajoute sortie normale

" 2> " → redirige erreurs

" 2>> " → ajoute erreurs

Astuce utile:

Pour tout mettre dans un seul fichier :

```
ls fichier-existant fichier-inexistant > tout.txt 2>&1

```

Explication:

2>&1 → redirige les erreurs vers la sortie normale

donc tout va dans tout.txt

### 5 - Composition de commandes:

| → enchaîne les commandes

sort → trie

head → extrait début

cut → extrait colonnes

<b>Astuce importante</b>

On peut faire des chaînes puissantes :

cat fichier | grep mot | sort | head
