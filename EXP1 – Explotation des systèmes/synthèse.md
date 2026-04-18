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

### 6 - Tubes:

| → relie les commandes

chaque commande → filtre

permet de faire des traitements complexes

<b>Astuce clé:</b>

Penser en étapes :

filtrer (grep)

transformer (cut)

trier (sort)

compter (uniq, wc)

limiter (head)

### 7 - Résultat intermédiaire:

tee fichier → copie vers fichier + écran

tee -a → ajoute

utile dans les pipelines

Exemple utile

grep error apache.log | tee errors.txt | wc -l

Résultat :

sauvegarde erreurs dans errors.txt

affiche le nombre d’erreurs

### TD6 - Linux et variables d’environnement

echo VAR affiche "VAR"

$VAR=12 erreur

VAR=$VAR garde valeur

echo $VAR + 30 affiche "12 + 30"

VAR=$VAR+30 texte "12+30"

VAR="$VAR + 30" "12 + 30"

VAR=VAR valeur = "VAR"

---

" pwd " → où je suis

" ls "→ voir fichiers

" cat "→ lire fichier

" cp " → copier

" ~ " → home

" $VAR "→ valeur variable

PATH → où chercher les commandes

which → chemin d’une commande

### TD07 - Permissions et groupes

ls -l : voir propriétaire, groupe, permissions

groups : voir les groupes d’un utilisateur

chmod 644 fichier : changer les permissions en nombres

chmod g+w fichier : ajouter l’écriture au groupe

chgrp etudiants fichier : changer le groupe

umask : voir le masque par défaut

sur un dossier :

r = voir la liste

w = modifier le contenu

x = entrer/traverser

### TD08 - Administration et scripts

sudo : exécuter comme administrateur

apt update : mettre à jour la liste des paquets

apt install : installer un logiciel

mount / umount : monter / démonter une partition

chmod : changer les permissions

source : exécuter un script dans le shell courant

export PATH=... : modifier le chemin des exécutables

```
$1, $2, $# : paramètres d’un script

if ... then ... else ... fi : condition


$(commande) : récupérer la sortie d’une commande

tar -czf : créer une archive compressée


```

### TD08 - Administration et scripts:

Ctrl + Z → suspendre un processus

jobs → voir les jobs du shell

jobs -l → voir jobs + PID

fg %n → reprendre au premier plan

bg %n → reprendre en arrière-plan

commande & → lancer directement en arrière-plan

kill -SIGKILL PID → tuer un processus

top → voir tous les processus

/proc/PID/status → infos sur un processus

/proc/PID/fd → fichiers/descripteurs ouverts

Si tu veux, je peux aussi te faire une fiche ultra simple “jobs / fg / bg / kill / top”.
