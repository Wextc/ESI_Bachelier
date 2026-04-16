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
