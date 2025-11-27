## 2.1.1 Systèmes d'exploitation

Interraction de l'utilisateur avec le SE de 2 manière.

- L'interface en ligne de commande (CLI)=> via l'interpréteur de commande

- L' interface utilisateur graphique (GUI).

#### Interpréteur de commandes -

Interface utilisateur qui permet aux utilisateurs de demander des tâches spécifiques à partir de l'ordinateur. Ces requêtes peuvent être effectuées via l'interface CLI ou GUI.

#### Noyau -

élément qui assure la communication entre le matériel informatique et les logiciels, et gère le mode d'utilisation des ressources matérielles pour satisfaire la configuration logicielle.

#### Matériel -

partie physique d'un ordinateur qui intègre des éléments électroniques.

## 2.1.2 Interface utilisateur

interface utilisateur graphique (GUI) =>

- exemples: Windows, macOS, Linux KDE, Apple iOS ou Android

Avantage :

Convivial.

Facile d'utilisation:

Facile à apprendre

- Désavantage:

- Peu fiable

- Pas facile à débeuguer les problèmes éventuels sous-jaçants du système.

Les professionnels de l'IT vont utiliser les CLI pour travailler.

Tous les périphériques CISCO utilisent utilisent le SE => CISCO IOIS.

Chaque types de commutateurs et de routeur utilisent différentes version de CISCO IOS, telle que IOS XE, IOS XR et NX-OS.

Le SE des routeurs domestiques s'appellent FIRMWARE.

## 2.1.3 Objectif d'un OS

Les SE CISCO IOS permet d'interagir avec les périphériques et de leur de donner des instructions comme on l'aurait fait avecc un ordinateur normal.

La version de l'IOS dépend du type de périphérique utilisé et des fonctions nécessaires.

En plus des fonctionnalités par défauts des périphériques réseau, il possible de rajouter des fonctionnalités supplémentaires.

## 2.1.4 Méthodes d'accès

Les switches n'ont pas besoins d'être configurés, car il se contentent de transferrer le traffic.

<b>Console</b>
Il s'agit d'un port de gestion permettant un accès hors réseau à un périphérique Cisco.

L'accès hors bande désigne l'accès via un canal de gestion dédié qui est utilisé uniquement pour la maintenance des périphériques. L'avantage d'utiliser un port de console est que le périphérique est accessible même si aucun service réseau n'a été configuré, par exemple en effectuant la configuration initiale du périphérique réseau. Un ordinateur exécutant un logiciel d'émulation de terminal et un câble de console spécial pour se connecter à l'appareil sont nécessaires pour une connexion à la console.

<b>wSSH (Secure Shell)</b>

L’accès SSH permet d’établir à distance une session CLI sécurisée via une interface réseau active.
Contrairement à la console, SSH nécessite que l’équipement dispose d'une adresse IP configurée et que les services SSH soient activés.

La plupart des versions de Cisco IOS intègrent un serveur SSH et un client SSH, permettant d’ouvrir des sessions sécurisées entre équipements.

<b>Telnet</b>

Telnet est un moyen non sécurisé d'établir une session CLI à distance via une interface virtuelle sur un réseau. Contrairement à SSH, Telnet ne fournit pas de connexion sécurisée et cryptée et ne doit être utilisé que dans un environnement de travaux pratiques. Les informations d'authentification des utilisateurs, les mots de passe et les commandes sont envoyés sur le réseau en clair. La meilleure pratique consiste à utiliser SSH au lieu de Telnet. Cisco IOS inclut à la fois un serveur Telnet et un client Telnet.

<b>Le port AUX</b>

Utiliser dans le passé pour se connecter aux périphériques réseaux, avant l'usage généraliser d'internet.

Il n'a pas besoin d'avoir une carte réseau configurer car il est accessible hors réseau.

Utile pour les dépannages sans le réeaux est DOWN.

## 2.1.5 Programmes d'émulation de terminal

On peut se connecter à un périphérique réseau via une connexion série sur un port console, via une connexion ssh et telnet.

## 2.1.6 Vérifiez votre compréhension - Accès à Cisco IOS

Questions voir cours.

## 2.2.1 Modes de commande principaux

L'utilisation de l'interface graphiques donne à l'administrateur réseau plus de flexibilité et de contrôl que l'interface GUI.

Par mesure de sécurité CISCO IOS possède 2 modes d'accès à la la gestion:

- Mode d'exécution utilisateur:

  Fonctionnalités limitées

  Fait pour seulement des opérations de base de surveillance - pas de configuration possible.

  L'invite CLI se termine par >

- Mode d'exécution privilégié:

  Donne accès a la possibilité de configurer les périphériques réseaux

  L'invite de commande se termine par #

## 2.2.2 Mode de configuration et sous-modes de configuration

<b>Mode de configuration</b>

Permet de créer des modifications qui affectent les périphériques réseaux dans leur ensembles.

Se termine par l'invite (config)#.

On fait définit l'accès de ce mode avant les autres modes de configurations spécifiques(les sous modes de configuration).

- Les sous mode de configuration permet de configurer les fonctions spéciales du périphérique IOS.

<b>Mode de configuration de ligne :</b>

configuration via console, SSH, Telnet et accès AUX.

<b>Mode de configuration d'interface : </b>

configuration de l'interface réseau d'un port du commutateur d'un routeur.

Invite de commande Switch(config-line)#

Par défaut tout invite commence par le nom du périphérique puis précise le nom de la commande.

## 2.2.4 Naviguer entre les différents modes IOS

Pour passer du mode utilisateur à mode privilégié = (ou mode actif) vous fait la commande:

```
enable

```

Et pour l'opération inverse suivante vous faite:

```
disable

```

Pour passer en mode configuration globale, il faut la commande suivante (MPrivilégié):

```
configure terminal

```

Et pour l'opération inverse suivante vous faite:

```
global exit

```

Il existe plusieurs sous-mode de congurations. Mais voici un exemple.

Pour passer à un sous mode spécifiques ligne.

```
Switch(config)# line console 0

Switch(config-line)# exit

Switch(config)#


```

Il faut utiliser la commande exit pour sortir du sous-mode de configuration.

```
Switch(config-line)# exit

Switch(config)#

```

Les différentes lignes commande permettent de naviguer dans les différents types de mode et sous-modes.

Permet de passer d'un sous-mode du mode configuration global aux modes situés plus hauts dans la hiérarchie des modes.

```
Switch(config-line)# exit

```

Pour passer d'un sous-mode à un mode d'exécution privilégié CTR+Z ou

```
Switch(config-line)# end

```

Pour passer d'un sous-mode de configuration à un autre.

```
Switch(config-line)# interface FastEthernet 0/1

Switch(config-if)#

```

## 2.2.5 Vidéo - Naviguer entre les différents modes de commande IOS

<b>Remarque</b>

Par défaut on est en mode util. exec. mode. De là il faut faut naviguer vers les autres mode.

Pour configurer un commutateur vous devez être en mode config mode. Pour cela vous devez changer de mode pour pour le mode de configuration global. Seulement, depuis le mode exécution privilégié ce n'est pas possible, ainsi il faut passer par le mode d'éxécution privilégié.
