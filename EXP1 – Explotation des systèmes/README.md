## Bash – Modifier le système de fichiers

### 1 - Créer un répertoire:

Créer un répertoire my-dir sur le bureau:

```
mkdir ~/Bureau/my-dir

```

"~/Bureau" correspond au dossier Bureau (Desktop) en français (sur certains systèmes ce sera ~/Desktop).

---

Essayer de recréer my-dir.

```
mkdir ~/Bureau/my-dir

```

Résultat :

Bash affiche une erreur du type :

```
mkdir: cannot create directory ‘my-dir’: File exists

```

Explication :

Le dossier existe déjà, donc mkdir refuse de le recréer.

---

Créer la hiérarchie avec -p

Structure demandée :

```
my-documents
└── photos
    └── personal

```

Commande :

```
mkdir -p my-documents/photos/personal

```

-p permet :

- de créer tous les dossiers en une fois

- d’éviter les erreurs si certains existent déjà

---

Créer toute la hiérarchie en une seule commande avec expansion d’accolades

Structure demandée :

```
my-documents
├── photos
│   ├── personal
│   └── work
└── videos
    ├── personal
    └── work
```

Commande :

```
mkdir -p my-documents/{photos,videos}/{personal,work}

```

Explication rapide de l’expansion

```
{photos,videos}

```

devient :

photos videos

```
{personal,work}

```

devient :

personal work

Donc Bash génère automatiquement :

```
my-documents/photos/personal

my-documents/photos/work

my-documents/videos/personal

my-documents/videos/work

```

<b>Remarque:</b>

Avec la commande tree (le plus clair)

```
tree my-documents

```

Cela donne:

```
my-documents
├── photos
│   ├── personal
│   └── work
└── videos
    ├── personal
    └── work

```

C’est la meilleure commande pour visualiser une arborescence.

### 2 - Éditeur de texte:

<b>Création de fichier avec nano:</b>

```
cd ~/Bureau/my-dir

```

Ecrit nano:

```
nano

```

Écris quelques lignes, puis :

```
Ctrl + S → sauvegarder
tape : my-file.txt
Entrée
Ctrl + X → quitter

```

---

<b>Modifier un fichier existant: </b>

```
nano my-file.txt

```

Modifie le texte.

Tu verras "Modified" en haut si tu changes quelque chose

Ensuite :

```
Ctrl + S pour sauvegarder
Ctrl + X pour quitter
Aide de nano

```

---

<b>Utiliser des options de nano:</b>

Afficher les numéros de ligne:

```
nano -l my-file.txt

```

Affiche les numéros de ligne à gauche du texte.

Utile pour :

- se repérer dans un fichier

- coder ou corriger des erreurs

Activer la souris:

```
nano -m my-file.txt

```

Tu peux utiliser la souris pour:

- placer le curseur

- sélectionner du texte

- faire défiler

Utile si tu n’aimes pas tout faire au clavier.

Mode lecture seule (view):

```
nano -v my-file.txt

```

Effet :

ouvre le fichier sans possibilité de modifier

Tu peux :

- lire le fichier

- naviguer

Tu ne peux pas :

- modifier

- sauvegarder

---

<b>Vérifier les dates avec stat:</b>

Commande :

```
stat my-file.txt

```

Tu verras plusieurs dates :

- Access (accès)

- Modify (modification du contenu)

- Change (changement des métadonnées)

Après modification avec nano :

- seule la date Modify change

- les autres restent généralement identiques

### 3 - Créer un fichier vide:

<b> Création d'un fichier vide :</b>

```
touch fichier-vide.txt

```

- La commande "touch" crée le fichier s’il n’existe pas.

- Si le fichier existe déjà, touch met à jour sa date de modification.

---

<b> Vérifier avec ls que le fichier existe et qu’il est vide:</b>

```
ls -l fichier-vide.txt

```

- "ls" liste les fichiers.

- "-l" affiche les détails.

- Si le fichier est vide, sa taille affichée sera 0.

Exemple de résultat :

```
-rw-r--r-- 1 user user 0 avril 16 10:20 fichier-vide.txt

```

Ici, le 0 signifie que le fichier est vide.

Tu peux aussi vérifier le contenu :

```
cat fichier-vide.txt

```

Comme le fichier est vide, rien ne s’affiche.

---

<b>Créer toute la hiérarchie demandée avec un minimum de commandes:</b>

Structure voulue :

```
my-documents
|-- exercises
| |-- part1.md
| |-- part2.md
| |-- part3.md
| `-- part4.md
`-- solutions
|-- part1.md
|-- part2.md
|-- part3.md
`-- part4.md

```

Commande en une seule ligne

```
mkdir -p my-documents/{exercises,solutions} && touch my-documents/{exercises,solutions}/part{1..4}.md

```

Explication de la commande:

Partie 1 : créer les dossiers.

```
mkdir -p my-documents/{exercises,solutions}

```

mkdir crée des répertoires.

-p crée aussi les parents si nécessaire, sans erreur s’ils existent déjà.

{exercises,solutions} est une expansion d’accolades.

Bash développe cela en :

```
my-documents/exercises

my-documents/solutions

```

Partie 2 : créer les fichiers:

```
touch my-documents/{exercises,solutions}/part{1..4}.md

```

touch crée des fichiers vides.

{exercises,solutions} donne les deux dossiers.

{1..4} donne 1 2 3 4.

Bash développe donc en :

```
touch my-documents/exercises/part1.md
touch my-documents/exercises/part2.md
touch my-documents/exercises/part3.md
touch my-documents/exercises/part4.md
touch my-documents/solutions/part1.md
touch my-documents/solutions/part2.md
touch my-documents/solutions/part3.md
touch my-documents/solutions/part4.md

```

---

<b> Vérifier la structure créée: </b>

Avec tree :

```
tree my-documents

```

Ou sans tree :

```
ls -R my-documents

```

Résumé des commandes:

```
touch fichier-vide.txt
ls -l fichier-vide.txt
mkdir -p my-documents/{exercises,solutions} && touch my-documents/{exercises,solutions}/part{1..4}.md
ls -R my-documents

```

### 4 - Télécharger un fichier:

<b>Télécharger le fichier texte:</b>

```
curl https://www.rfc-editor.org/rfc/rfc791.txt --output downloaded-file.txt

```

Explication:

```
curl → télécharge depuis Internet

```

--output → nom du fichier local

Télécharger une image:

```
curl https://curl.se/logo/curl-logo.svg --output downloaded-image.svg

```

### 5 - Supprimer un fichier:

Supprimer downloaded-file.txt:

```
rm downloaded-file.txt

```

Explication:

```
rm → supprime définitivement (pas de corbeile)

```

---

<b>Supprimer tous les .tmp:</b>

```
rm *.tmp

```

Explication:

- → tous les fichiers

- .tmp → tous les fichiers finissant par .tmp

Mode sécurisé:

```
rm -i fichier.txt

```

demande confirmation avant suppression

Danger de cette commande

```
rm -ri ~/ pictures/ blurry.jpg

```

---

<b>Supprime :</b>

- tout le dossier ~ (home !)

- le dossier pictures/

- le fichier blurry.jpg

/!\ tu peux supprimer énormément de données sans le vouloir.

### 6 - Supprimer un répertoire:

<b> Créer puis supprimer:

```
mkdir test-dir
rmdir test-dir

```

"rmdir" fonctionne seulement si le dossier est vide

---

<b>Supprimer un dossier avec contenu:</b>

```
mkdir -p new-dir/dir1/dir2
rm -r new-dir

```

Explication:

- "-r" → suppression récursive (tout le contenu)

---

<b>Supprimer my-dir avec fichier:</b>

```
rm -r my-dir

```

### 7 - Créer un raccourci (lien):

Créer le dossier et fichiers:

```
mkdir books
nano books/my-life.txt
nano books/tales.txt

```

Créer un lien (hard link):

```
ln books/my-life.txt books/favorite

```

Ouvrir avec less:

```
less books/favorite

```

Créer avec extension:

```
ln books/my-life.txt books/favorite.txt

```

---

<b>Observer les liens:</b>

```
ls -l books

```

colonne 2 = nombre de liens

Supprimer un lien:

```
rm books/favorite

```

Le nombre de liens diminue.

Afficher les identifiants (inode):

```
ls -i books

```

- mêmes numéros = même fichier (hard link)

Supprimer fichier original:

```
rm books/my-life.txt

```

- favorite.txt fonctionne encore (car les données existent toujours via le lien)

Vérifier avec stat:

```
stat books/favorite.txt

```

- seule la date Change est modifiée, car les métadonnées (liens) changent

### 8 - Copier avec cp:

<b>Copier un fichier:</b>

```
cp readme.txt texts/general-readme.txt

```

- Cas d’erreurs.

```
cp long-text.txt long-text.txt

```

- erreur (même fichier)

```
cp long-text.txt dossier-inexistant/

```

- erreur (dossier absent)

---

<b>Copier avec nouveau nom:</b>

```
cp long-text.txt long-text-copy.txt

```

---

<b>Empêcher écrasement:</b>

```
cp -n fichier.txt dossier/

```

Cas de cp license folder

- si folder est un fichier → écrasé

- si folder est un dossier → copie dedans

- si n’existe pas → créé comme fichier

---

<b>Copier un dossier:</b>

```
cp -r originals originals-save
```

Cas cp -r photos backup:

- backup fichier → erreur

- backup dossier → copie dedans

- inexistant → créé comme copie

### 9 - Renommer:

Renommer avec mv:

```
mv ancien.txt nouveau.txt

```

Explication:

- mv = move (déplacer)

Mais si tu restes dans le même dossier → ça devient un renommage.

Exemple :

```
mv fichier.txt notes.txt

```

Le fichier change juste de nom.

Renommer plusieurs fichiers avec rename.

Contrairement à mv, rename peut modifier plusieurs fichiers en une fois.

Exemple simple:

```
rename 's/.txt/.md/' _.txt

```

Explication:

```
_.txt → tous les fichiers .txt

```

- 's/.txt/.md/' → remplace .txt par .md

Résultat :

```
file1.txt → file1.md
file2.txt → file2.md
```

Attention importante:

```

rename

```

- n’est pas toujours installé

- peut avoir plusieurs versions différentes

  Exemple :

- sur certains systèmes → syntaxe avec 's/.../.../' (Perl)

- sur d’autres → syntaxe différente

## Bash – Manipuler des fichiers textes:

### 1 - Obtenir quelques statistiques:

Compter lignes, mots et octets avec wc.

<b>Voir lignes + mots + octets:</b>

```
wc dudh.txt

```

Explication:

- wc = word count.

Affiche :

- nombre de lignes

- nombre de mots

- nombre d’octets

Exemple de sortie :

```
120 450 3000 dudh.txt

```

120 lignes, 450 mots, 3000 octets

---

<b>Afficher uniquement le nombre de lignes:</b>

```
wc -l apache.log

```

Explication:

- "-l" → affiche seulement les lignes

Exemple :

```
250 apache.log

```

---

<b>Vérifier avec un éditeur:</b>

```
nano apache.log

```

En bas de nano → numéro de ligne total visible.

---

<b>Longueur de la plus longue ligne:</b>

```
wc -L apache.log

```

Explication:

-L → longueur (en caractères) de la ligne la plus longue

---

### 2 - Supprimer les doublons avec "uniq":

Afficher sans doublons + nombre d’occurrences

```
uniq -c apache.log

```

Explication:

- uniq → supprime les doublons consécutifs

- "-c" → affiche combien de fois chaque ligne apparaît

Exemple :

```
3 GET /index.html
1 POST /login

```

Important:

- "uniq" fonctionne seulement si

- les lignes identiques sont à la suite

Donc souvent on fait :

```
sort apache.log | uniq -c

```

---

<b> Vérifier que le fichier n’est pas modifié:</b>

```
cat apache.log

```

Le contenu original est inchangé.

Explication :

- "uniq" affiche le résultat

- mais ne modifie pas le fichier

---

### 3 - Numéroter des lignes:

<b>Numéroter les lignes avec nl:</b>

```
nl apache.log
```

Explication:

- nl = number lines

- affiche le fichier avec numéros de ligne

- ne numérote que les lignes non vides

Exemple :

```
1  GET /index.html
2  POST /login

```

---

<b>Afficher les premières lignes avec head:</b>

Afficher les 5 premières lignes.

```
head -n 5 elevation-extremes.csv

```

Explication:

- "head" → affiche le début du fichier

- "-n" 5 → limite à 5 lignes

---

<b>Afficher toutes sauf la dernière:</b>

```
head -n -1 elevation-extremes.csv

```

Explication:

- "-n -1" → enlève la dernière ligne

- donc affiche tout sauf la dernière

---

<b>Afficher les dernières lignes avec tail:</b>

Afficher les 5 dernières lignes.

```
tail -n 5 elevation-extremes.csv

```

Explication:

- "tail" → affiche la fin du fichier

- "-n 5" → 5 dernières lignes

---

<b>Afficher toutes sauf la première</b>

```
tail -n +2 elevation-extremes.csv

```

Explication:

- "+2" → commence à la ligne 2

- donc ignore la première ligne

---

<b>Afficher les dernières lignes avec tail:</b>

Afficher les 5 dernières lignes

```
tail -n 5 elevation-extremes.csv

```

Explication:

- tail → affiche la fin du fichier

- "-n 5" → 5 dernières lignes

<b>Afficher toutes sauf la première:</b>

```
tail -n +2 elevation-extremes.csv

```

Explication:

- "+2" → commence à la ligne 2

- donc ignore la première ligne

### 4 - Afficher les 5 premières lignes:

```
head -n 5 elevation-extremes.csv

```

Explication:

- head → affiche le début du fichier

- "-n 5" → limite à 5 lignes

---

<b>Afficher toutes les lignes sauf la dernière:</b>

```
head -n -1 elevation-extremes.csv

```

Explication:

- "-n -1" → enlève 1 ligne à la fin

- donc affiche tout sauf la dernière

<b>Afficher les 5 dernières lignes:</b>

```
tail -n 5 elevation-extremes.csv

```

Explication:

- "tail" → affiche la fin du fichier

- "-n 5" → les 5 dernières lignes

<b>Afficher toutes les lignes sauf la première:</b>

```
tail -n +2 elevation-extremes.csv

```

Explication:

- "+2 "→ commence à la ligne 2

- donc ignore la première ligne

### 5 - Concaténer des fichiers avec cat

Afficher 2 fichiers.

```
cat cities/eu.be.tsv cities/eu.nl.tsv

```

Explication:

- cat = concaténer

- affiche les fichiers l’un à la suite de l’autre

---

<b>Afficher tous les fichiers des villes d’Europe</b>

```
cat cities/eu.\*.tsv

```

Explication:

- = tous les fichiers correspondants

- eu.\*.tsv → tous les fichiers Europe

---

<b>Trier des lignes avec sort:</b>

Trier un fichier

```
sort unordered.txt

```

Explication:

- trie les lignes par ordre alphabétique

- Trier en ordre inverse

```
sort -r unordered.txt

```

Explication:

- "-r" → inverse l’ordre (Z → A)

<b>Trier sans doublons:</b>

```
sort -u unordered.txt

```

Explication:

- "-u" → supprime les doublons après tri

<b>Extraire des caractères avec cut:</b>

Extraire uniquement les dates (exemple).

```
cut -c 1-10 apache.log

```

Explication:

- "-c "→ sélection des caractères

- "1-10" → du caractère 1 à 10 (souvent les dates sont au début des logs)

---

### 6 - Extraire des caractères avec cut:

```
cut -c 12- apache.log

```

Explication:

- "12-" → du caractère 12 jusqu’à la fin

- donc on enlève la date au début

Exemple général:

```
cut -c 5-20 fichier.txt

```

extrait les caractères 5 à 20

---

<b>Concaténer ligne par ligne avec paste:</b>

Exemple:

paste file1.txt file2.txt

Explication:

- combine les lignes en parallèle

Exemple :

```
file1: A file2: 1
file1: B file2: 2

```

Résultat :

```
A 1
B 2
```

### 8 - Extraire les lignes contenant "jk":

```
grep -e 'jk' apache.log

```

Explication:

- "grep" → cherche dans un fichier

- "-e 'jk'" → lignes contenant "jk"

<b>Chercher dans plusieurs fichiers (quote)</b>:

```
grep -e 'it' quote*

```

Explication:

- "quote\*" → tous les fichiers commençant par quote

- chaque ligne affichée sera précédée du nom du fichier

Exemple :

```
quote1.txt:It is good
quote2.txt:Try it now

```

<b>Chercher plusieurs mots (jk OU in):</b>

```
grep -e 'jk' -e 'in' apache.log

```

Explication:

- plusieurs -e → OU logique

- ligne affichée si elle contient jk ou in

---

<b>Chercher un symbole spécial $:</b>

```
grep -F -e '$' iso-4217.csv

```

Explication:

- $ est un caractère spécial en regex

- "-F" → le traite comme texte normal

---

<b>Ajouter les numéros de ligne:</b>

```
grep -n -e 'jk' apache.log

```

Explication:

- "-n" → affiche le numéro de ligne

Exemple :

15:GET /jk/test

Lignes SANS "jk"

```
grep -v -n -e 'jk' apache.log

```

Explication:

- "-v "→ inverse → lignes ne contenant pas "jk"

- "-n" → ajoute les numéros

---

<b>Comprendre cette commande:</b>

```
grep -v -e 'hello' -e 'world' fichier.txt

```

Résultat:

Affiche les lignes qui :

ne contiennent ni "hello" ni "world"

car :

- "-e" = OU

- "-v"= inverse → exclut tout ce qui correspond

---

<b>Recherche dans un dossier (récursive):</b>

```
grep -r -e 'are' -e 'but' exercises/

```

Explication:

- "-r "→ cherche dans tous les fichiers du dossier

- affiche les lignes contenant "are" ou "but"

### 9 - Remplacer des occurrences:

<b>Remplacer “de l'homme” par “humains”</b>

```
sed "s/de l'homme/humains/g" dudh.txt

```

Explication:

- "sed" → éditeur de texte en ligne de commande

- s/.../.../ → substitution

- g → remplace toutes les occurrences

- guillemets " utilisés ici à cause de ' dans l'homme

Résultat : affiche le texte modifié (sans modifier le fichier)

---

<b>Remplacer les points . par !</b>

```
sed 's/\./!/g' quote*

```

Explication:

- " . "est un caractère spécial (regex = “n’importe quel caractère”)

- " \. " → signifie un vrai point

- " g "→ remplace tous les points

---

<b>Remplacer les virgules par &:</b>

```
sed 's/,/\&/g' quote5.txt

```

Explication:

- " , "→ virgule

- " \& " → caractère & (doit être échappé)

- sinon & signifie “le texte trouvé”

Points importants à retenir:

- Caractères spéciaux (à échapper dans le motif)

```
  . \* [ ] ^ $ \

```

Exemple :

" \. "

Caractères spéciaux dans le remplacement

" & " → correspond au texte trouvé

" \ " → caractère d’échappement

donc :

" \& "

### 9 - Remplacer des occurrences:

sed 's/a/b/' → remplace 1 fois par ligne

sed 's/a/b/g' → remplace partout

\. → point réel

\& → caractère &

---

<b>Trier un CSV par colonne (continent):</b>

```
sort elevation-extremes.csv -t ',' -k 1

```

Explication:

- " -t " ',' → séparateur = virgule (CSV)

- " -k " 1 → trie selon la colonne 1 (continent)

---

<b>Trier un TSV avec tabulation:</b>

```
sort cities/eu.be.tsv -t $'\t' -k 2

```

Explication:

- " $'\t' " → tabulation

- " -k " 2 → colonne 2 (ex : provinces)

---

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

---

<b>Trier par volume (notation scientifique):</b>

```
sort planets.csv -t ',' -k 2 -g

```

Explication:

- " -g " → gère les nombres comme 6e10

---

<b>Trier par nombre de lunes (du plus grand au plus petit):</b>

```
sort planets.csv -t ',' -k 6 -n -r

```

Explication:

- " -n "→ numérique

- " -r " → ordre inverse (descendant)

---

<b>Trier earthquakes par magnitude:</b>

```
sort earthquakes.dsv -t ',' -k 2 -n

```

(adapter la colonne selon le fichier)

---

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

---

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

## Bash – Redirection:

<b>Utiliser sort avec l’entrée clavier (stdin): </b>

Trier des mots en ordre inverse.

```
sort -r

```

Ensuite tu tapes :

```
travaille
tartine
tram
pomme
banane

```

Puis :

```
Ctrl + D

```

Explication:

sort sans fichier → lit depuis le clavier (stdin)

- " -r "→ ordre inverse

- " Ctrl + D " → fin de saisie

Résultat : mots triés Z → A

---

<b>Compter mots et caractères avec wc:</b>

```
wc

```

Tape un texte :

```
Bonjour tout le monde

```

Puis :

```
Ctrl + D

```

Explication:

- wc lit depuis le clavier

- affiche : lignes - mots - caractères

Exemple :

```
1 4 23

```

Comprendre Ctrl + D :

Rôle

- envoie les données tapées à l’application

- indique fin de fichier (EOF)

Sans Ctrl + D, le programme attend encore du texte.

Utiliser tr (remplacer caractères):

Essayer :

```
tr '.,' ', '

```

Tape :

```
3.14,2.5

```

Puis Ctrl + D:

Résultat:

```
3,14 2,5

```

Explication:

remplace :
. → ,

, → espace

---

<b>Comprendre tr ',' '\n'</b>

```
tr ',' '\n'

```

Tape :

```
pomme,banane,orange

```

Puis Ctrl + D:

Résultat:

```
pomme
banane
orange

```

Explication:

- " , "→ remplacé par retour à la ligne (\n)

- Sert à transformer une liste en colonnes

### 2 - Redirection de l'entrée standard

<b>Créer le fichier enum.txt:</b>

```
nano enum.txt

```

Écris par exemple :

```
pomme,banane,orange,kiwi,fraise,raisin

```

Puis :

```
Ctrl + S → sauvegarder

Ctrl + X → quitter

```

<b>Afficher l’énumération ligne par ligne avec tr:</b>

```
tr ',' '\n' < enum.txt

```

Explication de la commande:

- tr ',' '\n'

- remplace :

- " , " → retour à la ligne (\n)

- " < enum.txt "

- redirige l’entrée standard (stdin)

au lieu du clavier → lit depuis le fichier

Résultat attendu:

```

pomme
banane
orange
kiwi
fraise
raisin

```

<b>Comprendre la redirection:</b>

Sans redirection.

- tr ',' '\n'

- attend que tu tapes au clavier

Avec redirection.

- tr ',' '\n' < enum.txt

Lit directement depuis le fichier.

Donc :

- pas besoin de taper le texte

- traitement automatique

---

<b>Comparaison avec sort:</b>

```
sort < unordered.txt

```

Equivaut à:

```
sort unordered.txt

```

Explication:

sort accepte :

- fichier en argument

- OU entrée standard

<b>Pourquoi la redirection est importante ?</b>

Pour des commandes comme tr :

- elles ne prennent pas de fichier directement

- donc < fichier est indispensable

### 3 - Redirection de la sortie standard:

Concaténer tous les fichiers quote dans un fichier.

```
cat quote* > quotes-all.txt

```

Explication:

- cat quote\* → concatène tous les fichiers quote

- " > "→ redirige la sortie vers un fichier

- quotes-all.txt → fichier créé (ou écrasé)

Rien ne s’affiche à l’écran → tout va dans le fichier.

---

<b>Créer un fichier avec echo:</b>

```
echo "hello, world" > greetings.txt

```

Explication:

- echo → affiche du texte

- " > "→ redirige dans un fichier

- " > " crée greetings.txt avec le contenu

<b>Ajouter du texte à la fin du fichier:</b>

```
echo "how are you doing ?" >> greetings.txt

```

Explication:

- " >> " → ajoute à la fin (sans écraser)

- " > " → écrase

---

<b>Observer les changements avec tail:</b>

Terminal 1 :

```
tail -f greetings.txt

```

Explication:

- tail -f → affiche les dernières lignes

- reste actif → affiche les nouvelles lignes en direct

Terminal 2 :

```
echo "new line" >> greetings.txt

```

Résultat :

la nouvelle ligne apparaît automatiquement dans le terminal 1

---

<b>Attention à la redirection:</b>

```
sort unordered.txt > unordered.txt

```

Résultat:

Le fichier devient vide.

Explication importante.

Bash fait la redirection avant d’exécuter la commande.

Donc:

- unordered.txt est vidé

- puis sort lit un fichier vide

Bonne méthode:

```
sort unordered.txt > sorted.txt

```

ou

```
sort unordered.txt -o unordered.txt

```

---

### 4 - Rediriger les erreurs vers un fichier:

Exemple:

```
ls fichier-inexistant 2> erreurs.txt

```

Explication:

- ls fichier-inexistant → génère une erreur

- " 2> "→ redirige la sortie d’erreur (stderr)

- erreurs.txt → fichier contenant l’erreur

Résultat :

- rien ne s’affiche à l’écran

erreur écrite dans erreurs.txt

<b>Voir le contenu du fichier d’erreurs: </b>

```
cat erreurs.txt

```

Exemple :

ls: cannot access 'fichier-inexistant': No such file or directory

---

<b>Ajouter des erreurs à la suite: </b>

```
ls autre-fichier 2>> erreurs.txt

```

Explication:

- " 2>> " → ajoute à la fin du fichier

- ne supprime pas le contenu existant

### 5 - Composition de commandes:

Donner les 10 plus grosses villes d’Europe

```
sort cities/eu.\*.tsv -t $'\t' -k 3 -n -r | head -n 10

```

Explication:

- sort → trie les villes

- " -t $'\t' "→ séparateur = tabulation"

- " -k 3 "→ colonne population (supposée)

- " -n "→ tri numérique

- " -r "→ du plus grand au plus petit

- " | "→ envoie le résultat à la commande suivante

- head -n 10 → prend les 10 premières

Résultat : les 10 villes les plus peuplées.

---

<b>Les 10 plus grosses villes par ordre alphabétique:</b>

```
sort cities/eu.\*.tsv -t $'\t' -k 3 -n -r | head -n 10 | sort

```

Explication:

- première partie → trouve les 10 plus grandes villes

- deuxième sort → trie ces 10 villes alphabétiquement

Nom des 3 plus grosses planètes

```
sort planets.csv -t ',' -k 2 -g -r | head -n 3 | cut -d ',' -f 1

```

Explication:

- " -k 2 " → colonne volume

- " -g "→ notation scientifique (ex: 6e10)

- " -r " → plus grand → plus petit

- " head -n 3 "→ top 3

```
cut -f 1 → extrait le nom

```

Résultat : noms des 3 plus grosses planètes.

<b>Nouvelle notion : les pipes |</b>

Exemple général :

```
commande1 | commande2 | commande3

```

Explication:

- " | "(pipe) = relie les commandes

- sortie de la 1 → entrée de la 2

Exemple simple:

```
sort fichier.txt | head -n 5

```

Trie puis prend les 5 premiers.

---

<b>Pourquoi utiliser les pipes ?</b>

Sans pipe :

```
sort data.txt > temp.txt
head temp.txt

```

Avec pipe :

```
sort data.txt | head

```

- plus simple

- pas de fichier temporaire

---

<b>Notion de filtre:</b>

Un filtre :

- lit depuis stdin

- écrit vers stdout

Exemples :

```
sort
head
cut
grep

```

Pas des filtres :

```
echo
ls

```

### 6 - Tubes:

1. 10 plus grosses villes d’Europe

```
sort cities/eu.*.tsv -t $'\t' -k 3 -n -r | head -n 10

```

Explication:

- sort → trie par population

- " -n " -r → du plus grand au plus petit

- " | " → envoie le résultat à head

- head -n 10 → garde les 10 premières

---

<b>Les 10 plus grosses villes (ordre alphabétique):</b>

```
sort cities/eu.\*.tsv -t $'\t' -k 3 -n -r | head -n 10 | sort

```

Explication:

- trouver les 10 plus grandes villes

- sort final → tri alphabétique

<b>Nom des 3 plus grosses planètes:</b>

```
sort planets.csv -t ',' -k 2 -g -r | head -n 3 | cut -d ',' -f 1

```

Explication:

- tri par volume (-g)

- head → top 3

- cut → extrait le nom

---

<b>Nombre de lignes d’erreur dans apache.log:</b>

```
grep -i error apache.log | wc -l

```

Explication:

grep -i error → lignes contenant "error"

```
wc -l → compte les lignes

```

<b>Lignes les plus fréquentes (sans date):</b>

```
cut -c 12- apache.log | sort | uniq -c | sort -n -r | head -n 3

```

Explication:

- cut -c 12- → enlève la date

- sort → regroupe lignes identiques

- uniq -c → compte occurrences

- sort -n -r → plus fréquent en haut

- head -n 3 → top 3

---

<b>Comprendre les pipes:</b>

```
commande1 | commande2 | commande3

```

Fonctionnement:

```
sortie de commande1 → entrée de commande2
sortie de commande2 → entrée de commande3

```

- pas de fichiers temporaires

- tout se fait en mémoire

Exemple inutile:

```
sort values.seq | echo

```

Echo n’utilise pas l’entrée → résultat perdu.

### 7 - Résultat intermédiaire:

Exemple donné

```
sort -n values.seq | tee sorted-values.seq | head -n 3

```

Explication:

```
sort -n values.seq → trie les nombres

```

tee sorted-values.seq :

Enregistre le résultat dans un fichier.

- et le transmet à la suite

- head -n 3 → affiche les 3 premiers

Résultat :

- fichier complet trié sauvegardé

- seulement 3 lignes affichées

---

<b>Rôle de tee:</b>

tee = copie le flux

- entrée → copiée vers fichier

- entrée → continue dans la pipeline

Très utile pour :

- déboguer

- sauvegarder des résultats intermédiaires

<b>Que fait ce code ?</b>

```
tee f

```

Ensuite tu tapes :

```
Hello, world

```

Puis :

```
Ctrl + D

```

Résultat.

affiche :

```
Hello, world

```

crée un fichier f contenant :

```
Hello, world

```

Explication:

```
tee f lit depuis le clavier (stdin)

```

Ecrit :

dans le fichier f

dans la sortie standard (écran)

Donc double sortie :

- écran

- fichier

---

<b>Schéma mental:</b>

```
clavier → tee → écran

↓

fichier

```

Attention:

```
tee f

```

Ecrase le fichier f s’il existe.

Pour ajouter :

```
tee -a f

```

### 6 - Linux et variables d’environnement:

<b>Commandes de base Linux:</b>

Exercice 1 — pwd

```
pwd

```

Explication:

- Affiche le chemin du dossier courant.

- ex : /home/g12345

---

<b>Exercice 2 — tree:</b>

tree

Explication:

Affiche l’arborescence des fichiers et dossiers.

---

<b>Exercice 3 — afficher welcome:</b>

```
cat welcome

```

Explication:

- cat → affiche le contenu d’un fichier

- chemin relatif → pas de / au début

<b>Exercice 4 — lister tous les dossiers personnels:</b>

Chemin absolu :

```
ls /home

```

Chemin relatif :

```
ls ../

```

<b>Exercice 5 — jokers:</b>

Enseignants (3 lettres) :

```
ls /home/???

```

Étudiants (ex: g123xx) :

```
ls /home/g123\*

```

Explication:

- " ? "→ 1 caractère

- → plusieurs caractères

- Raccourcis de chemin

<b> Exercice 6: </b>

Contenu de ton dossier (absolu):

```
   ls ~

```

Dossier du prof:

```
   ls ~prof
```

Version relative:

```
   ls .

```

---

<b>Exercice 7 — comprendre chemin:</b>

```
~mcd/../../home

```

Explication:

```
~mcd → home de mcd

```

- " .. "→ remonter

- résultat → /home

---

<b>Exercice 8 — chemins relatifs:</b>

Relatifs :

```
./tds/td2

tds/td2/Hello.java

```

Copier un fichier.

---

<b>Exercice 9:</b>

Exemple :

```
cp ~/welcome ~/dev1/td2/

```

Explication:

- cp → copier

- source → destination

---

<b>Exercice 10:</b>

```
ls ~mcd

```

<b>Exercice 11:</b>

- " ~foo" → home de foo

- "~/foo" → dossier foo dans ta home

Changer mot de passe.

<b>Exercice 12:</b>

```
passwd

```

Manuel

<b>Exercice 13:</b>

```
man nano

```

<b>Exercice 14</b>

Oui :

- aucun dossier → optionnel

- plusieurs dossiers → possible (...)

<b>Exercice 15:</b>

```
man nano

```

Puis chercher :

```
/J

```

Variables d’environnement.

Expérience 1

```
VAR=12

echo $VAR

```

<b>Exercice 17:</b>

Commande Résultat.

echo VAR affiche "VAR"

```
$VAR=12 erreur
VAR=$VAR garde valeur

```

echo $VAR + 30 affiche "12 + 30"

VAR=$VAR+30 texte "12+30"

VAR="$VAR + 30" "12 + 30"

VAR=VAR valeur = "VAR"

Prompt

<b>Exercice 18:</b>

```
PS1="Bonjour ! "

```

<b>Exercice 19</b>

```
nano ~/.bashrc

```

Ajouter :

```
PS1="Bonjour ! "

PATH

```

<b>Exercice 20:</b>

```
echo $PATH

```

<b>Exercice 21 (avec tr):</b>

```
echo $PATH | tr ':' '\n'

```

<b>Exercice 22</b>

```
which nano

```

Vérifier dans PATH.

Tutoriel PATH:

```
PATH=

nano # ne marche plus

/usr/bin/nano # marche

```

### TD7 - Permissions et groupes:

<b>Exercice 1 — voir le propriétaire des fichiers du dossier personnel:</b>

```
ls -l

```

Explication:

- " ls " liste les fichiers.

- " -l " affiche la version détaillée.

- Une des colonnes indique le propriétaire du fichier.

Exemple :

```
-rw-r--r-- 1 g12345 users 120 Sep 10 10:00 welcome

```

Ici :

propriétaire = g12345.

groupe = users 2. Groupes d’utilisateurs

---

<b>Exercice 2 — voir les groupes:</b>

Vos groupes

```
groups

```

Groupes d’un autre utilisateur

```
groups mcd

```

Explication:

- groups affiche les groupes d’un utilisateur.

- le premier groupe est le groupe principal.

Réponses à donner.

Les groupes auxquels vous appartenez : avec groups.

Votre groupe principal : le premier affiché.

Les groupes du professeur : avec groups loginProf.

Groupe en commun : souvent users.

Groupe commun avec les autres étudiants : souvent etudiants 3.

Groupe d’un fichier

<b>Exercice 3 — voir le groupe de vos fichiers:</b>

```
ls -l

```

Explication:

- Dans l’affichage détaillé :

- une colonne = propriétaire.

- la colonne suivante = groupe 4. Vérifier les droits sur nano

<b>Exercice 4:</b>

Trouver où est nano :

```
which nano

```

Puis regarder ses permissions :

```
ls -l /usr/bin/nano

```

Explication:

which nano donne le chemin complet de l’exécutable.

ls -l montre les permissions.

Réponse attendue:

    Oui, nano doit être exécutable par vous, sinon vous ne pourriez pas le lancer.

    Non, vous ne pouvez normalement pas le modifier, car ce fichier appartient à

    l’administrateur. 5. Permissions en octal

<b>Exercice 5 — valeur de rwx:</b>

```
r = 4
w = 2
x = 1

```

Donc :

```
rwx = 4 + 2 + 1 = 7

```

<b>Exercice 6 — valeur de r-x:</b>

```
r-x = 4 + 0 + 1 = 5

```

<b>Exercice 7 — à quoi correspond 3:</b>

```
3 = -wx

```

car :

pas lecture = 0

écriture = 2

exécution = 1 6. Changer les permissions avec des nombres

<b>Exercice 9:</b>

Créer un fichier vide

```
touch test.txt

```

Voir ses permissions

```
ls -l test.txt

```

Mettre :

propriétaire = lecture seule = 4

groupe = lecture + écriture = 6

autres = lecture seule = 4

```
chmod 464 test.txt

```

Vérifier

```
ls -l test.txt

```

Explication:

touch crée un fichier vide.

chmod modifie les permissions.

464 signifie :

```
user = 4 = r--

group = 6 = rw-

others = 4 = r--

```

<b>Exercice 10 — fichier modifiable par tout le monde mais lisible seulement par vous:</b>

Créer le fichier :

```
echo "petit texte" > brol

```

Mettre les droits :

```
chmod 622 brol

```

Explication:

propriétaire = 6 = lecture + écriture

groupe = 2 = écriture seule

autres = 2 = écriture seule

Remarque:

C’est une situation un peu étrange en pratique : les autres peuvent modifier sans lire.

Changer les permissions avec des lettres.

<b>Exercice 11 — donner l’écriture au groupe:</b>

```
chmod g+w test.txt

```

Explication:

```
g = groupe

```

= ajouter

w = écriture

<b>Exercice 12 — aucun droit pour les autres:</b>

```
chmod o= test.txt

```

Explication:

- " o "= others

- " = = " imposer exactement

- rien après = = aucun droit

Changer le groupe d’un fichier.

<b>Exercice 13</b>

Voir le groupe des fichiers.

```
   ls -l

```

Créer un fichier test:

```
touch fichier-test

```

Changer son groupe:

```
chgrp etudiants fichier-test

```

Vérifier:

```
ls -l fichier-test

```

Explication:

- chgrp change le groupe du fichier.

- Vous pouvez seulement mettre un groupe dont vous êtes membre.

Réponse:

- Vous pouvez mettre ce fichier dans vos groupes, par exemple users ou etudiants.
- Vous ne pouvez pas le mettre dans enseignants si vous n’êtes pas membre de ce groupe.

Fichier lisible/modifiable par les étudiants, inaccessible aux enseignants.

Expérience 1:

Créer le fichier :

```
touch examen

```

Changer le groupe :

```
chgrp etudiants examen

```

Mettre les droits :

```
chmod 660 examen

```

Explication:

- propriétaire = rw-

- groupe etudiants = rw-

- autres = ---

Ainsi :

vous + étudiants : lecture/écriture

enseignants : aucun droit

<b>Exercice 14 — fichier gossip:</b>

Créer le fichier :

```
touch gossip

```

Changer le groupe :

```
chgrp etudiants gossip

```

Donner les droits :

```
chmod 660 gossip

```

Explication:

Même logique que pour examen.

Permissions sur les dossiers.

<b>Exercice 15 — voir les noms des fichiers, sans lire leur contenu:</b>

Créer le dossier et le fichier :

```
mkdir dir1

echo "secret" > dir1/file

```

Mettre les droits :

```
chmod 711 dir1

chmod 000 dir1/file

```

Explication:

Pour le dossier :

```
r permet de lister son contenu

x permet d’entrer/traverser

```

Une solution plus simple pour “tout le monde voit les noms mais pas le contenu du fichier” :

```
chmod 755 dir1
chmod 000 dir1/file

```

Ainsi :

- on peut faire ls dir1

- on ne peut pas lire dir1/file

<b>Exercice 16 — fichier modifiable mais non supprimable:</b>

Créer :

```
mkdir dir2

echo "texte" > dir2/file

```

Donner au fichier :

```
chmod 666 dir2/file

```

Empêcher la suppression via le dossier :

```
chmod 555 dir2

```

Explication:

- supprimer un fichier dépend des droits sur le dossier, pas sur le fichier.

- 555 sur le dossier = lecture/traversée, mais pas écriture

- donc on peut modifier le fichier s’il a w, mais pas le supprimer 11. Umask

<b>Exercice 17 — umask par défaut:</b>

Voir le umask :

```
umask

```

Explication:

Exemple fréquent : 022

Alors :

```
fichier : base 666 → 644
dossier : base 777 → 755

```

Vérifier :

```
touch f1

mkdir d1

ls -l

```

<b>Exercice 18 — changer le umask:</b>

```
umask 027

```

Permissions attendues

```
fichier : 666 - 027 = 640

dossier : 777 - 027 = 750

```

Vérifier :

```
touch f2

mkdir d2

```

ls -l 12. Exercice récapitulatif

<b>Exercice 19.1 — créer td7 avec un fichier et un dossier:</b>

```
mkdir td7

touch td7/fichier

mkdir td7/dossier

```

<b>Exercice 19.2 — afficher le contenu détaillé:</b>

```
ls -l td7

```

Explication des colonnes.

Exemple :

```
-rw-r--r-- 1 g12345 users 0 Sep 10 10:00 fichier

```

1er caractère : type (- fichier, d dossier).

ensuite : permissions

puis : nombre de liens

```
propriétaire

groupe

taille

date

nom

```

Valeurs octales typiques:

- fichier créé par défaut : souvent 644

- dossier créé par défaut : souvent 755

<b>Exercice 19.3 — droits correspondants:</b>

- 451

  propriétaire : 4 = r--

  groupe : 5 = r-x

  autres : 1 = --x

- 742

  propriétaire : 7 = rwx

  groupe : 4 = r--

  autres : 2 = -w-

- 254

  propriétaire : 2 = -w-

  groupe : 5 = r-x

  autres : 4 = r--

- 650

  propriétaire : 6 = rw-

  groupe : 5 = r-x

  autres : 0 = ---

<b>Exercice 19.4 — fichier :</b>

- propriétaire peut lire et modifier

- groupe peut lire

- autres peuvent exécuter

Droits

```
propriétaire = rw- = 6

groupe = r-- = 4

autres = --x = 1

```

Donc :

641

<b>Exercice 19.5 — dossier :</b>

- propriétaire peut lister, créer/supprimer, traverser

- groupe peut lister uniquement

- autres peuvent traverser uniquement

Attention.

Pour un dossier :

- lister = r

- traverser = x

- créer/supprimer = w et en pratique aussi x

Donc :

```
propriétaire = rwx = 7

groupe = r-- = 4

autres = --x = 1

```

Donc :

```
741

```

Remarque:

En pratique, “lister uniquement” sur un dossier sans x est très limité : on peut voir les noms dans certains cas, mais on ne peut pas vraiment entrer ou utiliser les éléments.

### TD 8 – Administration et scripts:

<b>Expérience 1 — tester tree:</b>

```
tree

```

Explication:

- tree affiche l’arborescence d’un dossier.

- Si la commande n’est pas installée, Linux affiche une erreur du type command not found.

---

<b>Expérience 2 — installer tree:</b>

Mettre à jour la liste des paquets

```
   sudo apt update

```

Explication:

- sudo exécute la commande avec les droits administrateur.

- apt update met à jour la liste des logiciels disponibles.

Installer tree:

```
sudo apt install tree

```

Explication:

- apt install installe un logiciel.

- ici, on installe la commande tree.

Tester:

```
tree

```

---

<b>Exercice 1 — voir ses groupes:</b>

```
groups

```

Explication:

affiche les groupes auxquels appartient l’utilisateur courant.

sur Ubuntu, pour utiliser sudo, il faut généralement être dans le groupe sudo.

---

Exercice 2 — afficher /etc/shadow

sudo cat /etc/shadow

Explication:

- cat affiche le contenu d’un fichier.

- /etc/shadow est protégé.

- sans sudo, accès refusé.

- avec sudo, on peut le lire si on a le droit d’utiliser sudo. 5. Lien entre Linux et Windows dans WSL

---

<b>Expérience 3:</b>

Voir le disque C:

```
ls /mnt/c

```

Explication:

- /mnt/c correspond au disque C: de Windows vu depuis Linux.

- Créer un fichier dans Windows depuis Linux

- touch /mnt/c/Users/VotreLogin/test-wsl.txt

Explication:

- touch crée un fichier vide.

- le fichier sera visible ensuite dans l’explorateur Windows.

- Inversement

- Créer un fichier sous Windows dans ton dossier personnel, puis vérifier depuis Linux :

- ls /mnt/c/Users/VotreLogin 4. Monter et démonter une partition

---

<b>Expérience 4:</b>

Vérifier qu’on n’est pas dans /mnt/c

```
pwd

```

Démonter C:

```
   sudo umount /mnt/c

```

Explication:

- umount démonte une partition.

- après cela, /mnt/c ne montre plus le disque C:.

Vérifier:

```
ls /mnt/c

```

Créer un dossier et un fichier:

```
sudo mkdir /mnt/windows

touch /mnt/windows/test.txt

```

Monter C: ailleurs

sudo mount -t drvfs C: /mnt/windows

Explication:

- mount monte une partition.

- -t drvfs indique le type utilisé par WSL pour accéder au disque Windows.

- C: est monté sur /mnt/windows.

Vérifier:

```
ls /mnt/windows

```

Le fichier test.txt n’est plus visible car le contenu de C: recouvre ce dossier.

Démonter à nouveau

```
sudo umount /mnt/windows

ls /mnt/windows

```

Le fichier test.txt réapparaît.

Exécutables et scripts

Expérience 5 — programme Python.

Créer hello.py

```
nano hello.py

```

Mettre :

print("Hello") 2. Voir les permissions

ls -l hello.py 3. Lancer avec Python

python3 hello.py

Explication:

- Ici, c’est python3 qui est l’exécutable.

- hello.py est juste un fichier lu par Python.

- Donc il n’a pas besoin du droit x.

---

<b>Expérience 6 — rendre hello.py exécutable:</b>

Modifier le fichier:

```
nano hello.py

```

Ajouter comme première ligne :

```
#!/usr/bin/python3

print("Hello") 2. Ajouter le droit d’exécution

chmod u+x hello.py 3. Exécuter directement

```

./hello.py

Explication:

#! s’appelle le shebang.

il indique quel programme doit exécuter le fichier.

./hello.py lance le script du dossier courant. 6. Votre premier script bash

Exercice 3

Créer script.sh

```
   nano script.sh

```

Contenu :

```
#!/bin/bash

```

echo "Bonjour" 2. L’exécuter avec source

```
source script.sh

```

Explication:

source exécute le contenu du fichier dans le shell courant. 3.

Le rendre exécutable:

```
chmod u+x script.sh

```

./script.sh 4.

Le placer dans bin et adapter PATH.

Créer le dossier s’il n’existe pas :

```
mkdir -p ~/bin

mv script.sh ~/bin/

```

Ajouter ~/bin au PATH :

```
export PATH="$HOME/bin:$PATH"

```

Tester :

script.sh

Pour rendre ça permanent.

Ajouter dans ~/.bashrc :

```
export PATH="$HOME/bin:$PATH" 7. Script secret

```

---

<b>Exercice 4 — créer un script secret:</b>

Créer ~/bin/secret :

```
nano ~/bin/secret

```

Contenu :

```
#!/bin/bash

touch journal

chmod 600 journal

```

Puis :

```
chmod u+x ~/bin/secret

```

Explication:

- touch journal crée le fichier journal.

- chmod 600 journal :

- propriétaire : lecture + écriture

- autres : aucun droit 8. Paramètres d’un script

---

<b>Exercice 5 — secret nomFichier:</b>

Modifier le script :

```
nano ~/bin/secret

```

Contenu :

```
#!/bin/bash

touch "$1"

chmod 600 "$1"

```

Explication:

- $1 = premier paramètre reçu.

- "$1" protège les noms contenant des espaces.

Utilisation :

```
secret monfichier

```

---

<b>Exercice 6 — afficher le nombre de paramètres:</b>

Créer un script :

```
nano ~/bin/nbparams

```

Contenu :

```
#!/bin/bash

echo $#

```

Puis :

```

chmod u+x ~/bin/nbparams

```

Explication:

" $# " = nombre de paramètres reçus. 9. Alternatives if

---

<b>Exercice 7 — erreur si pas exactement 1 paramètre:</b>

```
nano ~/bin/secret

```

Contenu :

```
#!/bin/bash



if [[$# -ne 1]]; then

echo "Erreur : il faut exactement un paramètre."

else

touch "$1"

chmod 600 "$1"

fi

```

Explication:

```
[[$# -ne 1]] teste si le nombre de paramètres est différent de 1.

-ne = not equal.

```

---

<b>Exercice 8 — script est la:</b>

Créer ~/bin/estla :

```
nano ~/bin/estla

```

Contenu :

```
#!/bin/bash



if [[$# -ne 1]]; then

echo "Erreur : il faut exactement un paramètre."

else

who | grep "^$1 "

fi

```

Puis :

```
chmod u+x ~/bin/estla

```

Explication:

- who affiche les utilisateurs connectés.

- grep "^$1 " garde les lignes commençant par le login donné.

Utilisation :

estla g12345

---

<b>Exercice 9 — erreur si le fichier existe déjà:</b>

Modifier secret :

```
nano ~/bin/secret

```

Contenu :

```
#!/bin/bash

if [[$# -ne 1]]; then

echo "Erreur : il faut exactement un paramètre."

elif [[-e "$1"]]; then

echo "Erreur : le fichier existe déjà."

else

touch "$1"

chmod 600 "$1"

fi

```

Explication:

```

-e "$1" teste si le fichier existe. 10. Tester le succès d’une commande

```

Exemple général :

```
if touch test.txt; then
echo "Réussi"
else
echo "Échec"
fi

```

Explication:

- si la commande réussit, le code de retour vaut 0.

- if teste ce succès. 11. Récupérer la sortie d’une commande

Exemple :

```
moi=$(whoami)

echo "Je suis $moi"

```

Explication:

- " $(...) "récupère la sortie d’une commande.

- ici, whoami donne le nom de l’utilisateur. 12. Script : vérifier qu’un fichier contient au moins n mots

<b>Exercice 10:</b>

Créer un script :

```
nano ~/bin/complet

```

Contenu :

```
#!/bin/bash

FICHIER=$1
N=$2

NBMOTS=$(wc -w < "$FICHIER")

if [[$NBMOTS -ge $N]]; then
echo "Le fichier $FICHIER est complet"
fi

```

Puis :

```
chmod u+x ~/bin/complet

```

Explication:

- wc -w compte les mots.

- < "$FICHIER" redirige le fichier vers wc.

- NBMOTS=$(...) stocke le résultat.

- -ge = greater or equal.

Utilisation :

complet texte.txt 100 13. Exercice récapitulatif — archivage d’un dossier

<b>Exercice 11:</b>

Créer le dossier des archives :

```
mkdir -p ~/archive

```

Créer le script :

```
nano ~/bin/archiver

```

Contenu :

```
#!/bin/bash

if [[$# -ne 1]]; then

echo "Erreur : il faut exactement un paramètre."

exit 1

fi

DOSSIER=$1

if [[! -d "$DOSSIER"]]; then

echo "Erreur : $DOSSIER n'est pas un dossier du répertoire courant."

exit 2

fi


DATE=$(date +"%F@%T")

ARCHIVE="$HOME/archive/${DOSSIER}-${DATE}.tgz"

if tar -czf "$ARCHIVE" "$DOSSIER"; then

TAILLE=$(wc -c < "$ARCHIVE")

echo "Archive créée : $ARCHIVE"

echo "Taille : $TAILLE octets"

else

echo "Erreur pendant la création de l'archive."

exit 3

fi

```

Puis :

```
chmod u+x ~/bin/archiver

```

Explication:

- if [[$# -ne 1]] : vérifie le nombre de paramètres.

- [[! -d "$DOSSIER"]] : vérifie que c’est bien un dossier.

- date +"%F@%T" : date/heure au bon format.

- tar -czf : crée une archive compressée.

- wc -c : taille en octets.

- exit 1, exit 2, exit 3 : codes d’erreur.

Utilisation :

```
archiver exp1

```

1. Stopper un processus

<b>Exercice 1 — lancer nl puis le suspendre:</b>

```
nl

```

Tape quelques lignes, puis :

```
Ctrl + Z

```

Explication:

- nl attend du texte au clavier.

- Ctrl + Z suspend le processus.

- Bash affiche un message du type :

- [1]+ Stopped nl

1 est le numéro du job.

<b>Exercice 2 — lancer Python puis le suspendre:</b>

```
python3

```

Tape par exemple :

```
2+2

print("bonjour")

```

Puis :

Ctrl + Z

Explication:

Python tourne dans le terminal.

```
Ctrl + Z le met en pause.

```

Le numéro entre crochets augmente si tu as déjà suspendu d’autres jobs.

<b>Exercice 3 — lancer nano puis le suspendre:</b>

```
nano

```

Écris quelques lignes, puis suspends-le avec :

```
Ctrl + Z

```

ou selon la version :

- Ctrl + T puis Ctrl + Z

- Vérifier la version de nano

```
nano --version

```

Explication:

- selon la version, la suspension de nano fonctionne différemment.

- si tu quittes Bash avec un job suspendu, Bash avertit que des jobs

- existent encore.

Afficher les processus du shell.

<b>Exercice 4 — afficher la liste des job.</b>

jobs

Explication:

jobs montre les processus lancés depuis ce terminal uniquement.

exemple :

- [1]- Stopped nl

- [2]+ Stopped python3

<b>Exercice 5 — dans une deuxième session Bash:</b>

Dans un autre terminal, lance et suspends quelques commandes, puis :

- jobs

Explication

- chaque terminal a sa propre liste de jobs.

- les numéros recommencent à partir de 1. 3. Reprendre un processus

<b>Exercice 6 — reprendre nano:</b>

D’abord voir les jobs :

- jobs

Puis reprendre celui de nano, par exemple le job 3 :

```
fg %3

```

Explication:

- fg = foreground

- reprend un job suspendu au premier plan

- on peut à nouveau interagir avec lui 4. Reprendre un processus en

- arrière-plan

<b>Exercice 7:</>

Lancer une commande longue

```
find / -name "brol.txt" > found 2> errors

```

La suspendre:

```
Ctrl + Z

```

La relancer en arrière-plan.

Si c’est le job 1 :

bg %1 4.

Vérifier l’état.

jobs

Explication:

- bg = background

- le processus continue sans bloquer le terminal

- on ne peut plus interagir avec lui au clavier

<b>Exercice 8 — lancer directement en arrière-plan:</b>

```
find / -name "brol.txt" > found 2> errors &

```

Explication:

- & à la fin lance directement la commande en arrière-plan

- Bash rend immédiatement la main 5. Tuer un processus

<b>Exercice 9 — lancer nano en arrière-plan puis le tuer:</b>

Lancer :

```
nano &

```

Voir les jobs :

```
jobs

```

Tuer le job 1 :

```
kill -SIGKILL %1

```

Explication:

- kill envoie un signal à un processus

- SIGKILL termine brutalement

- toutes les modifications non sauvegardées sont perdues 6. Observer tous les processus avec top

<b>Exercice 10 — démarrer top:</b>

```
top

```

Explication

- top affiche tous les processus du système

- touches utiles :

      q → quitter

      flèches → défiler 7. PID et jobs

<b>Exercice 11 — lancer un processus en arrière-plan et le tuer depuis un autre terminal</b>

Dans terminal 1 :

```
nano &

jobs -l

```

Exemple de sortie :

- [1]+ 3456 Running nano &

- 3456 = PID

Dans terminal 2 :

```
kill -SIGKILL 3456

```

Explication:

- %1 = numéro de job

- 3456 = PID, unique dans tout le système

- le PID permet d’agir depuis un autre terminal

<b>Exercice 12 — sort | uniq | nl puis suspendre:</b>

```
sort | uniq | nl

```

Tape quelques lignes puis :

```
Ctrl + Z

```

Ensuite :

```
jobs -l

```

Explication:

- une pipeline lance plusieurs processus

- jobs -l affiche les jobs avec leurs PID

<b>Exercice 13 — tuer nano avec son PID trouvé dans top:</b>

Dans terminal 1 :

```
nano

```

Dans terminal 2 :

```
top

```

Repère le PID de nano, puis :

```
kill -SIGKILL PID

```

Réponse attendue.

Dans le premier terminal, nano se ferme brutalement.

Pseudo-répertoire /proc

<b>Exercice 14 — voir le fichier status d’un processus:</b>

Lance une application, par exemple :

```
nano &

jobs -l

```

Prends son PID, par exemple 3456, puis :

```
cat /proc/3456/status

```

Explication:

- /proc est un pseudo-répertoire créé par Linux

- /proc/<pid>/status contient des informations sur le processus

<b>Exercice 15 — observer les descripteurs de fichiers:</b>

```
nl
nl

```

Dans un autre terminal, trouve son PID avec top ou jobs -l, puis :

```
ls -l /proc/PID/fd 2. nl > output.txt

nl > output.txt
```

Puis :

```
ls -l /proc/PID/fd 3. nl 2> error.log

nl 2> error.log

```

Puis :

```
ls -l /proc/PID/fd
```

Explication:

Dans fd/ :

```
0 = entrée standard
1 = sortie standard
2 = sortie d’erreur

```

Tu verras vers quoi pointent ces flux selon les redirections.

<b>Exercice 16 — pipeline sort | uniq | nl:</b>

Lancer :

```
sort | uniq | nl

```

Trouver les trois PID, puis pour chacun :

```
ls -l /proc/PID/fd

```

Question 2:

```
echo 'hello' > /proc/<nl-pid>/fd/0

```

Réponse:

Cela envoie hello dans l’entrée standard du processus nl.

Signaux:

<b>Exercice 17 — boucle infinie Python</b>

Lancer :

```
python3

```

Puis :

```
while True: print("oups")

```

Arrêter avec :

```
Ctrl + C

```

Explication:

- Ctrl + C envoie le signal SIGINT

- Même chose avec kill

- Trouver le PID du Python, puis :

  kill -SIGINT PID

      ou :

  kill -2 PID

<b>Exercice 18 — Ctrl + C dans Python sans code lancé:</b>

Lancer :

```
python3

```

Puis faire :

```
Ctrl + C

```

Réponse:

Non, Python ne quitte pas forcément ; il intercepte souvent SIGINT et rend simplement la main à l’invite Python.

Maîtriser top

<b>Exercice 19 — ne garder que certaines colonnes:</b>

Dans top :

appuie sur f

garde seulement :

```
PID
USER
S
%CPU
COM
TTY

```

Appuie sur q pour revenir.

Explication:

- f ouvre la gestion des colonnes

- Space active/désactive un champ

<b>Exercice 20 — opérations dans top:</b>

Déplacer TTY à gauche:

```
f

```

- sélectionner TTY

- touche pour déplacer

- remonter jusqu’à gauche

Trier par ordre croissant selon TTY

- sélectionner TTY

- s pour trier

- R pour inverser l’ordre si nécessaire

N’afficher que vos processus:

Dans top :

```
u

```

Puis entrer votre login:

Afficher les commandes complètes.

Dans top :

c 5. Mettre en évidence les processus en cours

Selon la configuration de top, cela peut se voir via la colonne S ou certaines options visuelles.

Processus parent

<b>Exercice 21 — ajouter la colonne PPID:</b>

Dans top :

```
f

```

activer PPID

```
q

```

Explication:

- PPID = PID du processus parent

<b>Exercice 22 — retrouver la chaîne des parents:</b>

Lancer nano dans un terminal :

```
nano

```

Dans un autre terminal :

```
top

```

Repérer :

- PID de nano

- son PPID

- puis chercher ce parent

puis le parent du parent, etc.

Explication:

- chaque processus a un parent

- cela forme un arbre de processus
