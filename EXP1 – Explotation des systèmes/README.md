# Bash – Modifier le système de fichiers

### 1 - Créer un répertoire

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

### 2 - Éditeur de texte

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
❓ 5. Aide de nano

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

### 3 - Créer un fichier vide

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

Créer toute la hiérarchie demandée avec un minimum de commandes:

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

#### 4 -

#### 5 -

#### 6 -

#### 7 -

#### 8 -

#### 9 -

```

```
