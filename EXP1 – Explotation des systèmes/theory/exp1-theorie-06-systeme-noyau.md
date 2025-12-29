Un système d’exploitation est un logiciel chargé en mémoire vive (RAM) au démarrage de la machine, dont le rôle est de gérer les ressources matérielles — comme le processeur, la mémoire, les disques ou les périphériques — et de fournir une interface entre le matériel et les programmes utilisateurs.

Le noyau est le cœur du système d’exploitation. Il est indispensable pour l'exécution des la gestion des processus, de la

mémoire, des entrées/sorties et de la communication avec le matériel. Sans noyau, aucun programme ne peut fonctionner. Il

s'exécute en permanence en mémoire.

Le noyau n’est qu’une partie du système d’exploitation : celui-ci inclut également des outils, des bibliothèques et des

programmes permettant à l’utilisateur et aux applications d’interagir avec la machine.

Cela explique le débat autour des termes Linux et GNU/Linux. Linux est strictement le nom du noyau, développé initialement

par Linus Torvalds. En revanche, une distribution complète utilise ce noyau conjointement avec de nombreux outils et

bibliothèques issus du projet GNU. Le terme GNU/Linux désigne donc l’ensemble formé par le noyau Linux et l’environnement

logiciel qui l’accompagne, c’est-à-dire une distribution Linux complète.

---

Pour demander un service au noyau, les programmes utilisent des appels système. Un appel système est une fonction spéciale,

identifiée par un numéro, qui permet par exemple d’ouvrir un fichier, de lire des données, de créer un processus ou de

terminer un programme. Ces appels constituent le seul moyen légal pour un programme utilisateur d’accéder aux ressources du

système. En parallèle, le noyau doit également gérer les interruptions, qui sont des événements déclenchés par le matériel,

comme l’appui sur une touche du clavier ou la fin d’une opération de lecture sur le disque. Lorsqu’une interruption survient,

le noyau interrompt temporairement l’exécution en cours afin de traiter l’événement.

Le noyau joue aussi le rôle de gestionnaire de ressources. Certaines ressources du système ne peuvent pas être partagées

simultanément entre plusieurs processus, comme le processeur, la mémoire vive ou une imprimante. Le noyau veille donc à une

utilisation équitable et ordonnée de ces ressources grâce à différents mécanismes. L’ordonnanceur décide quel processus peut

utiliser le processeur à un instant donné, le chargeur s’occupe de placer les programmes en mémoire, et des composants

spécifiques, comme le spooler d’impression, gèrent l’accès aux périphériques partagés.

Le démarrage du système se fait en deux grandes étapes. Lors de l’allumage de l’ordinateur, la mémoire vive est vide et aucun

programme ne peut encore être exécuté. Un premier programme, appelé firmware, prend le relais. Il s’agit du BIOS ou de

l’UEFI, stocké dans une mémoire non volatile. Ce firmware initialise le matériel et charge ensuite le second élément du

démarrage, le bootloader. Le bootloader, comme GRUB sous Linux, permet de choisir le système d’exploitation à lancer et

charge le noyau en mémoire.

Une fois le système lancé, il est possible d’interroger le noyau afin d’obtenir des informations sur l’état de la machine,

comme la quantité de mémoire disponible, le type de processeur ou la version du noyau utilisée. Ces informations sont

accessibles notamment via le système de fichiers virtuel /proc, qui reflète en temps réel l’état interne du système.

Le noyau bénéficie de privilèges supérieurs à ceux des programmes utilisateurs grâce au mécanisme des rings. Le processeur

distingue différents niveaux de privilèges, dont les plus importants sont le ring 0 et le ring 3. Le noyau s’exécute en ring

0, ce qui lui donne un accès total au matériel et à la mémoire. Les programmes utilisateurs, eux, s’exécutent en ring 3 et

disposent de droits limités. Ils doivent obligatoirement passer par des appels système pour accéder aux ressources, ce qui

garantit la sécurité et la stabilité du système.

---

<b> Quelle est la différence entre le noyau kernel et GNU/Linux? </b>

Le noyau, aussi appelé kernel, est bien ce que l’on appelle Linux. Le mot Linux désigne uniquement le noyau : c’est la partie

centrale du système, chargée de gérer le processeur, la mémoire, les périphériques et l’exécution des programmes.

Cependant, le noyau seul ne suffit pas pour qu’un utilisateur puisse réellement utiliser un ordinateur. Pour interagir avec

le système, il faut un ensemble d’outils, de bibliothèques et de programmes. C’est là qu’intervient GNU.

Le terme GNU/Linux désigne donc un système complet basé sur le noyau Linux, auquel on a ajouté les outils du projet GNU

(comme le shell, les commandes de base, les bibliothèques, etc.), ainsi que d’autres logiciels. Cet ensemble forme ce qu’on

appelle une distribution Linux.

Une distribution GNU/Linux fournit ainsi tout le nécessaire pour que l’utilisateur puisse interagir avec le noyau : un shell,

des commandes, parfois une interface graphique, et un environnement logiciel complet. Le noyau gère le matériel, tandis que

GNU/Linux fournit les outils permettant à l’utilisateur et aux applications de dialoguer avec ce noyau.

<b> Le noyau : </b>
Le noyau ou kernel peut être vu comme une machine logicielle minimale, construite au départ autour des éléments essentiels

que sont le processeur (CPU) et la mémoire vive (RAM). À ce niveau, il fournit les mécanismes fondamentaux permettant

d’exécuter des programmes, de gérer le temps processeur et d’allouer la mémoire.

<b> Le pilote drvier :</b>
Le noyau ne se limite pas à ces ressources de base. Il étend ses capacités grâce aux pilotes de périphériques. Les

pilotes sont des modules logiciels qui permettent au noyau de communiquer avec le matériel. Ils servent d’intermédiaires

entre le noyau et les périphériques physiques, comme le clavier, l’écran, la souris, le disque dur ou la carte réseau.

Grâce aux pilotes, le noyau peut recevoir des informations provenant des périphériques (par exemple, une touche pressée sur

le clavier) et envoyer des commandes vers eux (comme afficher du texte à l’écran). Sans ces pilotes, le noyau serait

incapable d’interagir avec le matériel externe.

Rôle:

Son rôle principal est de servir d’intermédiaire entre le matériel et les programmes utilisateurs.

<b> Les appels systèmes: </b>

Pour demander un service au noyau, les programmes utilisent des appels système. Un appel système est une fonction spéciale,

identifiée par un numéro, qui permet par exemple d’ouvrir un fichier, de lire des données, de créer un processus ou de

terminer un programme.

Ces appels constituent le seul moyen légal pour un programme utilisateur d’accéder aux ressources du

système. En parallèle, le noyau doit également gérer les interruptions, qui sont des événements déclenchés par le matériel,

comme l’appui sur une touche du clavier ou la fin d’une opération de lecture sur le disque. Lorsqu’une interruption survient,

le noyau interrompt temporairement l’exécution en cours afin de traiter l’événement.

<b> Le rôle du noyau :</b>
En plus des appels système et des interruptions, le noyau gère aussi :

Les processus :

Il crée, exécute, suspend et termine les programmes.

Il décide lequel utilise le processeur à un instant donné (ordonnancement).

Le processeur (CPU):

Il partage le temps du CPU entre les processus pour que plusieurs programmes semblent s’exécuter en même temps.

La mémoire (RAM):

Il alloue la mémoire aux programmes, empêche qu’ils écrivent n’importe où et protège la mémoire des autres processus.

Les périphériques:

Il contrôle l’accès au clavier, à la souris, au disque, à l’imprimante, à la carte réseau via des pilotes (drivers).

Les fichiers et les données:

Il permet d’ouvrir, lire, écrire et fermer des fichiers sur le disque de manière sécurisée.

Le démarrage du système:

Il est chargé par le bootloader et devient le premier programme actif du système.

La sécurité et les privilèges:

Il sépare le mode utilisateur du mode noyau (rings) pour éviter qu’un programme fasse n’importe quoi.

Les services système (démons):

Il lance et supervise les services qui tournent en arrière-plan (réseau, impression, planification…).

Le noyau joue aussi le rôle de gestionnaire de ressources. Certaines ressources du système ne peuvent pas être partagées

simultanément entre plusieurs processus, comme le processeur, la mémoire vive ou une imprimante. Le noyau veille donc à une

utilisation équitable et ordonnée de ces ressources grâce à différents mécanismes. L’ordonnanceur décide quel processus peut

utiliser le processeur à un instant donné, le chargeur s’occupe de placer les programmes en mémoire, et des composants

spécifiques, comme le spooler d’impression, gèrent l’accès aux périphériques partagés.

<b> Le démarrage du système : </b>

Le démarrage du système se fait en deux grandes étapes. Lors de l’allumage de l’ordinateur, la mémoire vive est vide et aucun

programme ne peut encore être exécuté. Un premier programme, appelé firmware, prend le relais. Il s’agit du BIOS ou de

l’UEFI, stocké dans une mémoire non volatile. Ce firmware initialise le matériel et charge ensuite le second élément du

démarrage, le bootloader. Le bootloader, comme GRUB sous Linux, permet de choisir le système d’exploitation à lancer et

charge le noyau en mémoire.

<b> Le système de fichiers virtuel /proc: </b>

Une fois le système lancé, il est possible d’interroger le noyau afin d’obtenir des informations sur l’état de la machine,

comme la quantité de mémoire disponible, le type de processeur ou la version du noyau utilisée. Ces informations sont

accessibles notamment via le système de fichiers virtuel /proc, qui reflète en temps réel l’état interne du système.

<b>Les privilèges :</b>

Le noyau bénéficie de privilèges supérieurs à ceux des programmes utilisateurs grâce au mécanisme des rings. Le processeur

distingue différents niveaux de privilèges, dont les plus importants sont le ring 0 et le ring 3. Le noyau s’exécute en ring

0, ce qui lui donne un accès total au matériel et à la mémoire. Les programmes utilisateurs, eux, s’exécutent en ring 3 et

disposent de droits limités. Ils doivent obligatoirement passer par des appels système pour accéder aux ressources, ce qui

garantit la sécurité et la stabilité du système.

<b> Démons : </b>

Enfin, le système d’exploitation comprend des programmes particuliers appelés démons. Ces petits programmes sont lancés au

démarrage du système et s’exécutent en permanence en arrière-plan. Ils fournissent des services essentiels comme la gestion

du réseau, l’écoute des demandes d’impression ou la planification de tâches. L’ensemble du système d’exploitation repose donc

sur une combinaison de code, comprenant les appels système, la gestion des interruptions, l’ordonnanceur et les démons, ainsi

que sur des données stockées en mémoire et sur disque, qui décrivent l’état du système.
