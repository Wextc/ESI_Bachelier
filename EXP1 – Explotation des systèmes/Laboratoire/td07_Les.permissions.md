# 1 Permissions et groupes

Linux est un système multi-utilisateur : plusieurs personnes (ou processus) peuvent utiliser le même système en même temps.

Pour garantir la sécurité, Linux met en place un mécanisme strict de contrôle d’accès basé sur :

Le propriétaire du fichier/dossier

Le groupe associé

Les permissions accordées aux trois catégories d’utilisateurs :

le propriétaire,

le groupe,

les autres (tout le monde).

## 1.1 Propriétaire d’un fichier/dossier

Chaque fichier ou dossier appartient à un utilisateur du système.

Ce propriétaire est souvent l’utilisateur qui crée le fichier.

Le propriétaire dispose généralement du contrôle principal sur les permissions du fichier.

Pour afficher le propriétaire d’un fichier :

```

ls -l monfichier

```

Exemple de sortie :

```
-rw-r--r-- 1 alice etudiants 1200 Jan 20 10:00 rapport.txt

```

→ Le propriétaire ici est alice.

Le propriétaire d’un fichier a-t-il forcément tous les droits sur ce fichier ?

Non, pas nécessairement.

Même si un utilisateur est propriétaire d’un fichier, il peut choisir de limiter ses propres droits.

Par exemple, il peut mettre un fichier en lecture seule pour éviter de le modifier accidentellement.

Ainsi, être propriétaire ne garantit pas automatiquement tous les droits :

ce sont les permissions définies sur le fichier qui déterminent ce qu’il peut faire.

## 1.2 Les groupes d’utilisateurs

Linux est un système multi-utilisateur. Pour gérer efficacement les permissions, il utilise un mécanisme appelé groupes.

Un groupe est simplement un ensemble d’utilisateurs à qui l’on peut attribuer des droits communs.

<b>Pourquoi utiliser des groupes ?</b>

Les groupes permettent de :

- Donner des permissions à plusieurs utilisateurs en même temps

- Organiser les utilisateurs selon leurs rôles (ex. : etudiants, profs, admin)

- Contrôler l’accès à certains fichiers ou dossiers de manière simple et centralisée

Exemple :

Si un dossier appartient au groupe projetA, tous les utilisateurs membres de ce groupe peuvent y accéder selon les permissions du groupe.

<b> À quels groupes appartient un utilisateur ? </b>

Sous Linux, un utilisateur :

Possède un groupe principal (souvent le même nom que l’utilisateur)

Peut appartenir à plusieurs groupes secondaires

Tu peux voir les groupes d’un utilisateur avec :

```

groups nom_utilisateur


```

La commande groups renseigne sur les groupes auxquels appartient un utilisateur.

- groups : affiche les groupes de l’utilisateur qui exécute la commande.

- groups loginDeLaPersonne : affiche les groupes de l’utilisateur donné.

```

mcd@xray:~> groups

users enseignants

mcd@xray:~> groups g64093

g64093 : users etudiants

```

<b>Qui installe et gère les groupes?</b>

L’administrateur est la personne qui installe un système d’exploitation et le gère au quotidien, y compris l’installation de logiciels, la gestion des comptes utilisateurs et des groupes, les sauvegardes, la gestion des pannes… Sur Linux, on dit aussi le « super utilisateur », le « compte root » ou le «
root».

Sur les serveurs Linux de l’école, il y a trois groupes pour les utilisateurs :

- users : tous les utilisateurs sont dans ce groupe.

- etudiants : tous les étudiants sont dans ce groupe.

- enseignants : tous les professeurs sont dans ce groupe.

#### 1.3 Groupe d’un fichier

Linux gère des groupes d’utilisateurs (comme students, profs, admin, etc.).

Chaque fichier/dossier appartient à un et un seul groupe. Ces groupes sont les mêmes que ceux utilisés pour grouper les utilisateurs.

Ces groupes servent à organiser les utilisateurs ensemble.

Les groupes auxquels un fichier peut appartenir sont exactement ces mêmes groupes.

Cela signifie que si un fichier appartient au groupe etudiants, tous les utilisateurs membres du groupe etudiants peuvent bénéficier des permissions du groupe définies pour ce fichier.

Visualisez les groupes auxquels appartiennent un fichiers.

```
ls -l mon_fichier

```

![permission_fichier_grp](https://github.com/Wextc/ESI_Bachelier/blob/main/EXP1%20%E2%80%93%20Explotation%20des%20syst%C3%A8mes/Laboratoire/img/groups_fichiers.png)

Visualisez les groupes auxquels appartiennent plusieurs fichier d'un dossier fichiers.

```

ls -l fichier1 fichier2 fichier3

```

Visualisez les groupes auxquels appartiennent tous les fichiers d’un dossier, depuis le dossier parent.

```
 ls -l nom_du_dossier

```

Visualisez les groupes auxquels appartiennent tous les fichiers l'intérieur d’un dossier.

```
ls -l

```

#### 1.4 Catégories de personnes

Sous Linux, chaque fichier ou dossier appartient toujours à deux entités : un propriétaire, qui est l’utilisateur à qui il appartient, et un groupe, c’est-à-dire un ensemble d’utilisateurs. Lorsqu’on attribue des permissions à un fichier ou à un dossier, Linux ne traite pas tous les utilisateurs de la même manière. Il distingue en réalité trois catégories de personnes, et chacune peut recevoir des droits différents.

La première catégorie est celle du propriétaire. C’est l’utilisateur qui possède le fichier. Il dispose généralement de plus de permissions que les autres et peut même choisir de modifier les droits qui lui sont accordés. Cependant, il n’a pas automatiquement tous les droits : ce sont les permissions définies sur le fichier qui déterminent ce qu’il peut faire.

La deuxième catégorie rassemble les utilisateurs du groupe associé au fichier. Tous les membres de ce groupe héritent des permissions définies pour le groupe. Il est important de noter que le propriétaire n’est pas inclus dans cette catégorie, même s’il appartient lui-même au groupe : il est toujours traité séparément dans la première catégorie. Par exemple, si un fichier appartient au groupe etudiants, tous les utilisateurs faisant partie de ce groupe auront les droits spécifiés pour celui-ci.

Enfin, la troisième catégorie regroupe tous les autres utilisateurs du système, c’est-à-dire ceux qui ne sont ni le propriétaire ni membres du groupe du fichier. Ils disposent en général des permissions les plus limitées, car ce sont les utilisateurs les plus « éloignés » du fichier du point de vue de la sécurité.

![permission_cat_personnes](https://github.com/Wextc/ESI_Bachelier/blob/main/EXP1%20%E2%80%93%20Explotation%20des%20syst%C3%A8mes/Laboratoire/img/categorie_de_personnes.png)

<b>Le propriétaire (user)</b>

C’est la personne à qui appartient le fichier.

Il ne reçoit pas automatiquement tous les droits :

ce sont les permissions définies pour lui qui déterminent ce qu’il peut faire.

Exemple : le propriétaire peut décider de se retirer lui-même les droits d’écriture pour éviter une erreur.

✔️ Le propriétaire peut avoir tous les droits, mais seulement si on les lui donne.

<b>Le groupe (group)</b>

Tous les utilisateurs qui appartiennent au groupe du fichier.

Ils ont uniquement les droits que l’on attribue au groupe.

Souvent utilisé pour partager des fichiers dans une équipe (ex. groupe projet1).

✔️ Le groupe a les droits qu’on lui accorde explicitement.

<b>Les autres (others)</b>

Tous les utilisateurs restants du système.

Ils ont en général le minimum de droits (souvent aucun).

✔️ Ce sont les droits les plus restrictifs pour protéger le fichier du reste du système.

#### 1.5 Les permissions sur un fichier

Sous Linux, chaque fichier peut être associé à trois types de permissions : la lecture, l’écriture et l’exécution. La permission de lecture, représentée par la lettre r (pour read), permet à un utilisateur de consulter le contenu d’un fichier. Avec ce droit, il peut par exemple utiliser des commandes comme cat ou less pour afficher son contenu. La permission d’écriture, notée w (write), autorise l’utilisateur à modifier le fichier. Il peut ainsi l’éditer avec un éditeur comme nano et en changer le contenu. Enfin, la permission d’exécution, symbolisée par x (execute), concerne les fichiers exécutables, c’est-à-dire les programmes ou les scripts que le système peut lancer directement. Par exemple, la commande nano correspond elle-même à un fichier exécutable présent quelque part sur le disque.

Ces permissions apparaissent toujours dans le même ordre — r, w, x — et lorsqu’une permission n’est pas accordée, elle est remplacée par un tiret (-). En observant les permissions du fichier welcome dans un exemple précédent, on peut les interpréter ainsi : pour le propriétaire, identifié ici comme g12345, les permissions sont rw- ; cela signifie qu’il peut lire le fichier et en modifier le contenu, mais qu’il ne peut pas l’exécuter. Les utilisateurs appartenant au groupe users disposent exactement des mêmes permissions. En revanche, les autres utilisateurs du système, c’est-à-dire ceux qui ne sont ni le propriétaire ni membres du groupe associé, ne disposent que du droit de lecture : ils peuvent consulter le fichier, mais ne peuvent ni le modifier ni l’exécuter.

À noter enfin que le tout premier caractère affiché avant les permissions n’en fait pas partie. Il sert simplement à indiquer la nature de l’élément : un d signifie qu’il s’agit d’un dossier, alors qu’un tiret indique qu’il s’agit d’un fichier ordinaire.

![permission_cat_personnes](https://github.com/Wextc/ESI_Bachelier/blob/main/EXP1%20%E2%80%93%20Explotation%20des%20syst%C3%A8mes/Laboratoire/img/categorie_de_personnes.png)

Vérifier que le fichier qui contient nano est bien exécutable par vous. Pouvez-vous le
modifier ?

```
ls -l $(which nano)

```

On a :

```
-rwxr-xr-x 1 root root 234000 Jan 12 10:00 /usr/bin/nano

```

#### 1.6 Modifier les permissions

Nous savons maintenant qu’un fichier possède un propriétaire et un groupe, et que chacun de ces ensembles d’utilisateurs peut recevoir des permissions différentes. Nous savons également lire et interpréter les permissions affichées par Linux. La question suivante est donc logique : comment peut-on modifier ces permissions ?

Pour cela, Linux met à disposition la commande chmod, qui permet de changer les autorisations d’un fichier ou d’un dossier. Son utilisation générale est la suivante :
chmod permissions fichier.

Il existe deux manières de préciser ces permissions : en utilisant des nombres ou en utilisant des lettres. La méthode numérique est idéale lorsque l’on souhaite définir toutes les permissions d’un coup, car elle impose un ensemble complet et sans ambiguïté. À l’inverse, la méthode alphabétique est plus pratique lorsqu’on veut seulement ajouter ou retirer quelques droits sans modifier les autres.

Lorsque l’on choisit la méthode par nombres, les permissions sont exprimées en octal. Chaque type de permission correspond alors à une valeur précise :
la permission de lecture vaut 4, celle d’écriture vaut 2, et celle d’exécution vaut 1. Pour déterminer les permissions finales, il suffit d’additionner ces valeurs. Par exemple, une permission de lecture et d’écriture correspond à la valeur 6 (4 + 2), tandis qu’une permission complète (lecture, écriture et exécution) correspond à 7 (4 + 2 + 1). Ce système permet donc de représenter chaque ensemble de permissions par un simple chiffre, et d’obtenir un code final à trois chiffres : un pour le propriétaire, un pour le groupe et un pour les autres utilisateurs.

![permission_cat_personnes](https://github.com/Wextc/ESI_Bachelier/blob/main/EXP1%20%E2%80%93%20Explotation%20des%20syst%C3%A8mes/Laboratoire/img/permission_en_nbr.png)

#### 1.7 Modifier le groupe

La permission 644 est l’un des réglages les plus courants sous Linux, notamment pour les fichiers textes, les pages web, ou tout fichier qui doit être lisible par d’autres mais modifiable uniquement par son propriétaire.

Pour comprendre cette valeur, il faut rappeler que chaque chiffre représente les droits accordés à une catégorie d’utilisateurs :

le premier 6 concerne le propriétaire du fichier,

le second 4 concerne le groupe,

le troisième 4 concerne tous les autres utilisateurs.

Le chiffre 6 correspond à la combinaison de la lecture (4) et de l’écriture (2).
Il donne donc les permissions rw- : le propriétaire peut lire et modifier le fichier.

Les deux autres chiffres, 4 et 4, correspondent chacun à la permission de lecture seule.
Le groupe et les autres utilisateurs peuvent donc uniquement lire le fichier, sans pouvoir le modifier ni l’exécuter.

Concrètement, une permission 644 signifie que seul le propriétaire peut modifier le fichier, tandis que tout le reste du système peut simplement le consulter. C’est une permission sûre et très utilisée, car elle protège l’intégrité du fichier tout en permettant sa lecture.

drwxrwxr-x,

le premier caractère (d) indique la nature de l’élément : ici, il s’agit d’un dossier (directory).

d → dossier

- → fichier normal

l → lien symbolique

etc.

les neuf caractères suivants correspondent aux permissions, et ils sont divisés en trois groupes de trois :

```

rwx   rwx   r-x
│     │     │
│     │     └── permissions des "autres" (others)
│     └──────── permissions du groupe
└────────────── permissions du propriétaire


```

![permission_cat](https://github.com/Wextc/ESI_Bachelier/blob/main/EXP1%20%E2%80%93%20Explotation%20des%20syst%C3%A8mes/Laboratoire/img/permission_cat.png)

Ces trois blocs décrivent donc les droits accordés aux trois catégories d’utilisateurs de Linux :

le propriétaire (user)

le groupe (group)

tous les autres (others)

Les lettres indiquent quel type de permission est accordé :

r → lecture

w → écriture

x → exécution / accès

- → permission non accordée

<b>Que signifie 777 ?</b>

Le code 777 correspond à trois chiffres :

7 pour le propriétaire

7 pour le groupe

7 pour les autres utilisateurs

Or, le chiffre 7 représente la combinaison de toutes les permissions :

4 = lecture (r)

2 = écriture (w)

1 = exécution (x)

4 + 2 + 1 = 7, donc rwx.

<b>Donc 777 signifie :</b>

Propriétaire : rwx

Groupe : rwx

Autres : rwx

Autrement dit :

out le monde peut lire, écrire et exécuter le fichier ou le dossier.

<b>Attention : 777 est très dangereux</b>

777 donne à n’importe quel utilisateur du système le droit :

de modifier le fichier,

de l’effacer,

ou de l’exécuter.

On l’utilise normalement jamais sur un fichier sensible, et très rarement sur un dossier.

<b>Exercice 5 — Quel nombre correspond aux permissions rwx ?</b>

Les permissions :

```

r = 4

w = 2

x = 1

```

On additionne :

```
4 + 2 + 1 = 7

```

👉 rwx correspond donc au nombre 7.

<b> Exercice 6 — Quel nombre correspond aux permissions r-x ?</b>

Les permissions ici :

r = 4

- = 0

x = 1

On additionne :
4 + 0 + 1 = 5

👉 r-x correspond donc au nombre 5.

<b>Exercice 7 — À quelles permissions correspond le nombre 3 ?</b>

On décompose 3 :

```
3 = 2 (w) + 1 (x)

```

Donc permissions :

```
-wx

```

Le nombre 3 correspond aux permissions -wx.

#### 1.8 Récapitulons

#### 1.9 Permissions sur les dossiers
