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
