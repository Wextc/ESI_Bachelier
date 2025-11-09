## Questions et réponses de base

Que signifie le mot terminal dans le contexte de Bash ?

→ C’est une application qui transmet les caractères tapés au système d’exploitation et affiche à l’écran les réponses textuelles reçues.

---

Quelle est la différence entre un terminal et un interpréteur de commandes ?

→ Le terminal gère uniquement l’affichage et la saisie de texte, tandis que l’interpréteur (comme Bash) exécute réellement les commandes.

---

Quel est le rôle du caractère ESC (n°27) dans un terminal ?

→ Il permet de produire des séquences d’échappement pour afficher des couleurs ou d’autres effets visuels dans le terminal.

---

Cite deux exemples d’interpréteurs de commandes autres que Bash.

→ cmd.exe et PowerShell (il y a aussi Zsh, par exemple).

---

Bash est-il préinstallé sur Windows ?

→ Non, il faut l’installer manuellement sur Windows (par exemple via Git Bash), contrairement à macOS ou Linux où il est déjà présent.

---

Comment démarre-t-on une session Bash sur Windows avec Git Bash ?

→ En cliquant avec le bouton droit sur un dossier et en sélectionnant « Git Bash Here ».

---

Que représente le symbole $ dans une invite de commande ?

→ C’est le prompt : il indique que Bash attend une commande de l’utilisateur.

---

Quelle commande permet de changer de répertoire dans Bash ?

→ cd (abréviation de change directory).

---

Quelle commande affiche le contenu du répertoire courant ?

→ ls (abréviation de list files).

---

Bash fait-il une différence entre les majuscules et les minuscules ?

→ Oui, Bash est sensible à la casse (case sensitive).

---

Que signifie cd .. ?

→ Cela permet de remonter au répertoire parent.

---

Quelle est la différence entre un chemin absolu et un chemin relatif ?

→ Le chemin absolu commence à partir de la racine /, alors que le chemin relatif part du répertoire courant.

---

Quel caractère Bash utilise-t-il comme séparateur de répertoires ?

→ Le slash /.

---

Quelle option de ls permet d’afficher le contenu dans l’ordre inverse ?

→ L’option courte -r ou longue --reverse.

---

Que fait la touche Tab ↹ dans Bash ?

→ Elle active l’autocomplétion des noms de fichiers ou des commandes.

---

## Questions de compréhension

Pourquoi la commande voir les fichiers provoque-t-elle une erreur ?

→ Parce que “voir” n’est pas une commande Bash reconnue — Bash affiche donc “command not found”.

---

Que signifie “répertoire courant” ?

→ C’est le dossier dans lequel on se trouve actuellement dans Bash.

---

Que représente la partie ~/Desktop/working dans l’invite Bash ?

→ C’est le chemin du répertoire courant dans lequel l’utilisateur travaille.

---

Pourquoi les fichiers commençant par un point (.) sont-ils cachés ?

→ Parce qu’en Unix/Linux, un fichier dont le nom commence par . est considéré comme caché par convention.

---

Pourquoi utiliser .. dans un chemin absolu a-t-il peu d’intérêt ?

→ Parce qu’un chemin absolu décrit déjà l’emplacement complet depuis la racine, donc remonter (..) n’a généralement pas de sens.

---

Que se passe-t-il si on exécute cd images/.. ?

→ On entre dans images, puis .. fait revenir au répertoire parent : on revient donc au répertoire initial.

---

Quelle est la différence entre /c/ et C:/ dans Git Bash ?

→ Ce sont deux façons équivalentes d’écrire le chemin d’un disque Windows ; Git Bash utilise /c/ pour rester cohérent avec la syntaxe Unix.

---

Pourquoi doit-on parfois mettre un nom de fichier entre apostrophes ' ' ?

→ Pour que Bash reconnaisse le nom complet s’il contient des espaces ou des caractères spéciaux.

---

Que se passe-t-il si un nom de fichier contient un espace et qu’on ne l’échappe pas ?

→ Bash croit qu’il s’agit de deux arguments distincts et renvoie une erreur.

---

Quelle est la différence entre une option courte et une option longue ?

→ L’option courte est précédée d’un seul tiret (-r), la longue de deux tirets (--reverse).

---

## Questions ouvertes / de réflexion

Explique la différence entre Bash et l’interface graphique Windows Explorer.

→ Windows Explorer est une interface visuelle (on clique, on voit les icônes), tandis que Bash est une interface textuelle où tout se fait par des commandes.

---

En quoi les chemins relatifs sont-ils pratiques par rapport aux chemins absolus ?

→ Ils sont plus courts et permettent de naviguer facilement dans des sous-dossiers sans devoir taper le chemin complet.

---

Donne un exemple d’utilisation de ls avec une option et explique son effet.

→ ls -r affiche les fichiers dans l’ordre inverse ; ls -l affiche plus d’informations (taille, date, droits…).

---

Que fait la commande echo \*.txt si le répertoire contient plusieurs fichiers texte ?

→ Elle affiche la liste des fichiers .txt (par exemple help.txt readme.txt).

---

Pourquoi la commande echo _.txt ne montre pas le motif _.txt lui-même ?

→ Parce que Bash remplace le motif par les fichiers correspondants avant d’exécuter la commande.

---

Explique à quoi servent les motifs (patterns) et les jokers (\_, ?) dans Bash.

→ Ils servent à sélectionner plusieurs fichiers selon un schéma de nom (ex. : \_.txt = tous les fichiers texte).

---

Donne un exemple d’expansion de noms de fichiers avec ? et un autre avec \*.

→ ls a?c correspond à abc, adc, a5c…
ls a\*c correspond à ac, abc, ahelloc, etc.

---

Pourquoi la commande ls \* n’affiche-t-elle pas les fichiers commençant par un point ?

→ Parce que par défaut, les fichiers cachés (commençant par .) sont exclus des expansions de noms.

---

Comment afficher aussi les fichiers cachés avec ls ?

→ En ajoutant l’option -a → ls -a.

---

Quelle est la différence entre une option, un argument et une commande ?

→ La commande est l’action principale (ls),

l’option modifie son comportement (-l),

l’argument précise sur quoi elle agit (ex. : ls Documents/).

---

## Nouvelles questions avec réponses

Que se passe-t-il lorsque Bash affiche “command not found” ?

→ Cela signifie que le mot tapé ne correspond à aucune commande reconnue par Bash.

---

Quelle est la structure de base d’une invite Bash ?

→ Elle affiche le nom d’utilisateur, le nom de l’ordinateur, l’environnement (MINGW64), et le répertoire courant, suivis du signe $.

---

Que signifie le terme “MINGW64” dans l’invite Bash de Git ?

→ C’est l’environnement d’exécution utilisé pour Git Bash sur Windows (mais il n’a pas d’importance pour l’usage courant).

---

Quand une nouvelle invite $ s’affiche, que cela indique-t-il ?

→ Que Bash est prêt à recevoir une nouvelle commande.

---

Quelle est la différence entre le comportement de Bash et celui de l’explorateur Windows lorsqu’on change de dossier ?

→ Bash ne montre pas automatiquement le contenu du dossier après un cd, contrairement à l’explorateur.

---

Quelle commande affiche le contenu d’un répertoire, y compris les fichiers cachés ?

→ ls -a

---

Comment se déplacent les fichiers affichés par la commande ls par défaut ?

→ Ils sont affichés par ordre alphabétique.

---

Pourquoi les fichiers cachés sous Unix n’ont-ils pas besoin de métadonnées spéciales ?

→ Parce que le point initial (.) dans leur nom suffit à les cacher.

---

Quelle commande permet d’afficher les fichiers d’un dossier parent sans y entrer ?

→ ls ..

---

Quelle commande permet d’aller directement à la racine du disque C sous Git Bash ?

→ cd /c/

---

Pourquoi Bash utilise-t-il / au lieu de \ pour séparer les répertoires ?

→ Parce qu’il a été développé pour les systèmes Unix, qui utilisent le slash /.

---

Comment se déplacer de “Desktop/working/images” à “Desktop/working” sans écrire le chemin complet ?

→ Avec cd ..

---

Que signifie le signe ~ dans un chemin comme ~/Desktop ?

→ C’est un raccourci pour le dossier personnel (home) de l’utilisateur.

---

Quelle commande permet de revenir dans le répertoire précédent (celui d’avant le dernier cd) ?

→ cd -

---

Que se passe-t-il si une commande Bash est mal orthographiée (ex. : “LS” au lieu de “ls”) ?

→ Bash affiche une erreur, car il est sensible à la casse.

---

Que fait la commande ls -l \*.txt ?

→ Elle affiche les détails (droits, taille, date, etc.) de tous les fichiers terminant par .txt.

---

Pourquoi ls _.txt peut renvoyer “_.txt” sans rien d’autre ?

→ Parce qu’aucun fichier correspondant au motif n’a été trouvé.

---

Quelle commande peut-on utiliser pour tester une expansion de motif sans vraiment lister les fichiers ?

→ echo \*.txt

---

Pourquoi la commande echo _.txt affiche la liste des fichiers au lieu du motif _.txt ?

→ Parce que Bash remplace le motif avant d’exécuter la commande.

---

Comment forcer Bash à reconnaître le caractère \_ comme un texte littéral et non comme un motif ?

→ En le protégant avec des guillemets ('\_') ou un backslash (\*).

---

Que se passe-t-il si on appuie deux fois sur la touche Tab ↹ ?

→ Bash affiche la liste de toutes les possibilités d’autocomplétion correspondantes.

---

Comment écrire correctement la commande pour afficher un fichier nommé “mon texte.txt” ?

→ ls 'mon texte.txt' ou ls mon\ texte.txt

---

Que se passe-t-il si un argument ou une option contient un espace non échappé ?

→ Bash le considère comme plusieurs éléments distincts, ce qui provoque souvent une erreur.

---

Pourquoi certaines commandes comme find ou dd ne respectent-elles pas les conventions d’options habituelles ?

→ Parce que les conventions (- ou --) ne sont pas obligatoires en Bash ; certaines commandes ont leur propre syntaxe.

---

Comment afficher la liste des options disponibles pour une commande comme ls ?

→ En tapant man ls (pour ouvrir le manuel) ou ls --help.

---

## Questions sur la visualisation de fichiers

Quelle commande permet de visualiser le contenu d’un fichier texte sans le modifier ?

→ less

---

Quelle est la commande complète pour visualiser le fichier “mon-fichier.txt” ?

→ less mon-fichier.txt

---

Quelle est la particularité de la commande less ?

→ Elle affiche le contenu d’un fichier texte sans permettre de le modifier.

---

Pourquoi préfère-t-on less à cat pour lire de longs fichiers ?

→ Parce que less permet de faire défiler le contenu (haut/bas) alors que cat affiche tout d’un coup.

---

Comment quitter l’affichage d’un fichier dans less ?

→ En appuyant sur la touche q (pour quit).

---

## Questions sur les informations des fichiers

Quelle commande affiche les informations détaillées d’un fichier ?

→ stat

---

Que signifie “stat” ?

→ “file status information” — informations sur l’état d’un fichier.

---

Que permet d’obtenir la commande stat ?

→ Des informations complètes sur un fichier ou un répertoire : taille, droits, propriétaire, et quatre dates (création, modification, accès, changement d’état).

---

Que signifie “Informations sur les fichiers et répertoires non affichées par ls” ?

→ Cela veut dire que ls, même en mode détaillé (ls -l), ne montre pas toutes les métadonnées, contrairement à stat.

---

Combien de dates sont affichées par stat pour chaque fichier ?

→ Quatre dates.

## Questions sur la recherche de fichiers

Quelle commande permet de rechercher un fichier dans un répertoire et ses sous-répertoires ?

→ find

---

Comment rechercher le fichier “example.txt” dans le répertoire texts ?

→ find texts -name example.txt

---

Comment rechercher tous les fichiers ayant l’extension .txt dans le répertoire texts ?

→ find texts -name '\*.txt'

---

Pourquoi faut-il mettre les jokers entre apostrophes dans la commande find ?

→ Pour empêcher Bash d’interpréter le motif avant que find ne s’exécute.

(Sinon, l’expansion \*.txt serait faite par Bash, pas par find.)

---

Que se passe-t-il si on écrit find texts -name \*.txt sans apostrophes ?

→ Bash effectue une expansion de noms de fichiers avant d’exécuter find, donc la recherche ne fonctionne pas comme prévu.

---

Quel est le rôle principal de la commande find ?

→ Rechercher des fichiers selon différents critères : nom, extension, taille, date de modification, etc.

---

La commande find recherche-t-elle aussi dans les sous-répertoires ?

→ Oui, par défaut elle recherche dans le répertoire donné et tous ses sous-dossiers.

---

Peut-on utiliser des jokers (\*) avec find ?

→ Oui, mais il faut les protéger par des guillemets simples pour éviter leur interprétation par Bash.

---

Quelle est la différence entre find et ls ?

→ ls affiche le contenu d’un répertoire, alors que find recherche des fichiers dans toute une arborescence.

---

Pourquoi find est-il plus puissant que ls ?

→ Parce qu’il permet de chercher selon des critères précis (nom, taille, date, extension…) sur tout un ensemble de dossiers.

## Questions sur la fin de session et autres remarques

Quelle commande permet de fermer une session Bash proprement ?

→ exit

---

Pourquoi est-il recommandé de fermer Bash proprement avec exit ?

→ Pour que le terminal termine correctement les processus et sauvegarde les variables ou l’historique.

---

Que signifie “fermer proprement” une session Bash ?

→ Quitter l’interpréteur de commandes sans interrompre brutalement le programme ou le terminal.

---

Quels autres interpréteurs de commandes partagent la plupart des comportements de Bash ?

→ sh et zsh

---

Pourquoi l’ordre alphabétique d’affichage des fichiers peut-il varier selon la langue ?

→ Parce que chaque langue a son propre ordre de tri (localisation différente), que Bash peut adapter via les paramètres de langue.
