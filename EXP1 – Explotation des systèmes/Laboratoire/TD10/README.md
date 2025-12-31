# Synthèse qui reprend toutes les commandes

## TD09 GIT

### Configuration Git

```
git config
git config --global user.name "Votre Nom"
git config --global user.email "email@exemple.com"
git config --local user.name "Votre Nom"
git config --local user.email "email@exemple.com"
```

### Clonage de dépôt

```
git clone <url-du-depot> [nom-dossier]
git clone https://git.esi-bru.be/exp1/git-discover mon-projet
git clone https://git.esi-bru.be/6*****/git-discover
```

### Historique des commits

```
git log
git log --oneline
git log --name-status
git log -n <nombre>
git log -n 2
git log -n 5
git log -n 5 --oneline

```

### Recherche dans l’historique par fichier

```
git log --name-status test.py
git log --name-status readme.md
git log --name-status todo.txt
git log --name-status logo.png
git log --follow --name-status -- readme.md

```

### Premier et dernier commit

```
git rev-list --max-parents=0 main
git rev-parse main
git rev-list --count main
```

### Comparaison de versions (diff)

```
git diff <id1> <id2>
git diff HEAD HEAD~1
git diff HEAD~1 HEAD
git diff HEAD HEAD~2
git diff $(git rev-list --max-parents=0 main) main
git diff 24e284aec4fb17adeea7ab290ce3b1b705d68a33 aa133d0aa3f8f744ce50567ce622b8705b580f6e
```

### Fichiers binaires (logo.png)

```
git log --oneline -- logo.png
git show MOD^:logo.png > logo_before.png
git show MOD:logo.png > logo_after.png

```

### Fichiers renommés (readme.md)

```
git show REN^:README.txt
git show REN:readme.md
```

### Aide Git

```
git --help
git <commande> --help
git log --help

```

### Références symboliques

```
HEAD
HEAD~1
HEAD~2
HEAD~3
```
