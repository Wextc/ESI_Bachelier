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

![Texte alternatif de l'image](https://github.com/Wextc/ESI_Bachelier/blob/main/EXP1%20%E2%80%93%20Explotation%20des%20syst%C3%A8mes/Laboratoire/img/groups_fichiers.png)

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

#### 1.5 Les permissions sur un fichier

#### 1.6 Modifier les permissions

#### 1.7 Modifier le groupe

#### 1.8 Récapitulons

#### 1.9 Permissions sur les dossiers
