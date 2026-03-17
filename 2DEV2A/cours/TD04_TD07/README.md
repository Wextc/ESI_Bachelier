## TD 04 – Scrabble

Les packest => Packages:

C'est un dossier qui permet d'organisier le code source, de telle sorte que les classes ont un lien logique soient regroupées ensembles. Il attrubue un nom unique à ce regroupement, ce qui évite les collisions entre classe différentes. Il regroupement des classes ne dépend que du fait que les classes soient liées sémantiquement, et pas du fait qu'une classe soit static ou pas.

Avantage;

Code claire

Maintenance plus simple

Exemple:

Une application Java qui gère les étudiants, les profs et l'administration va classer toutes les classes relatives aux étdudiants dans un packet à part et va faire la même choses pour les profs et l'administration.

Dans l'exercice le packages s'appelle g12345.scrabble.

```
src/main/java  =>clique droit sur java: choisi New : choisi Packagages : donne nom g12345.scrabble

```

### 1.1 Une classe Letter

classe : Letter

attribut: char letter (il a une visibilité privée car on utilise un getter)

Un constructeur: Letter (le constructeur porte le même nom que sa classe)

```
public class Letter {

    // attribut privé
    private char letter;

    // constructeur
    public Letter(char letter) {
        this.letter = letter;
    }

    // getter
    public char getLetter() {
        return letter;
    }
}


```

Dans la classe Main

```
public class App {

    public static void main(String[] args) {

        Letter l = new Letter('A');

        System.out.println(l.getLetter());
    }

}

```

Le résultat suivant est affiché:

```
A
```

### 1.2 Une classe Board

La classe Board représente le plateau de jeu du Scrabble. Ce plateau est constitué d’une grille de 15 lignes et 15 colonnes, soit 225 cases au total, sur lesquelles les lettres peuvent être placées. Pour stocker ces lettres, la classe utilise un tableau à deux dimensions nommé squares. Ce tableau contient des objets de type Letter, ce qui signifie que chaque case du plateau peut contenir une lettre ou être vide. L’attribut est déclaré private afin de respecter le principe d’encapsulation : il ne peut être modifié directement que depuis l’intérieur de la classe.

Le constructeur de la classe Board ne reçoit aucun paramètre. Son rôle est simplement d’initialiser le plateau de jeu. Lorsqu’un objet Board est créé, le constructeur instancie un tableau Letter[15][15]. Toutes les cases sont initialement vides, c’est-à-dire qu’elles contiennent la valeur null, ce qui indique qu’aucune lettre n’y est placée.

La classe contient ensuite une méthode appelée get qui permet d’obtenir la lettre située à une position donnée sur le plateau. Cette méthode reçoit deux paramètres : row et col, qui correspondent respectivement à la ligne et à la colonne de la case recherchée. Avant d’accéder au tableau, la méthode vérifie que ces indices sont bien compris entre 0 et 14. Si les valeurs sont en dehors de ces limites, la méthode lance une exception IllegalArgumentException, ce qui indique que les paramètres fournis ne sont pas valides. Si les indices sont corrects, la méthode retourne simplement la valeur contenue dans squares[row][col], qui peut être une lettre ou null si la case est vide.

La classe propose également une méthode setLetters, qui permet de placer plusieurs lettres d’un coup sur le plateau. Cette méthode reçoit quatre paramètres : la ligne (row) et la colonne (col) de départ, la direction dans laquelle les lettres doivent être placées (Direction.HORIZONTAL ou Direction.VERTICAL), ainsi qu’un tableau de lettres à placer (Letter[] letters). La première lettre sera placée à la position indiquée par row et col, et les suivantes seront placées soit vers la droite si la direction est horizontale, soit vers le bas si la direction est verticale.

Avant de placer les lettres, la méthode effectue plusieurs vérifications. Elle vérifie d’abord que la position de départ est valide et qu’elle se trouve bien à l’intérieur du plateau. Ensuite, pour chaque lettre du tableau, elle calcule la position où elle doit être placée. Elle vérifie que cette position ne dépasse pas les limites du plateau et que la case correspondante est libre, c’est-à-dire que la valeur dans le tableau est null. Si une case est déjà occupée ou si la position dépasse la taille du plateau, la méthode lance une exception IllegalArgumentException.

Si toutes les vérifications sont correctes, la méthode parcourt à nouveau le tableau de lettres et les place effectivement dans les cases correspondantes du plateau. Chaque lettre est alors stockée dans le tableau squares à la position calculée.

Ainsi, la classe Board permet de gérer le plateau de jeu : elle crée la grille de lettres, permet de consulter le contenu d’une case et offre une méthode sécurisée pour placer des mots sur le plateau tout en vérifiant que les règles de base sont respectées.

```
package g12345.scrabble;

public class Board {

    private Letter[][] squares;

    public Board() {
        squares = new Letter[15][15];
    }

    public Letter get(int row, int col) {
        if (row < 0 || row >= 15 || col < 0 || col >= 15) {
            throw new IllegalArgumentException("row et col doivent être entre 0 et 14");
        }
        return squares[row][col];
    }

    public void setLetters(int row, int col, Direction d, Letter[] letters) {
        if (row < 0 || row >= 15 || col < 0 || col >= 15) {
            throw new IllegalArgumentException("row et col doivent être entre 0 et 14");
        }

        if (letters == null) {
            throw new IllegalArgumentException("letters ne peut pas être null");
        }

        for (int i = 0; i < letters.length; i++) {
            int currentRow = row;
            int currentCol = col;

            if (d == Direction.HORIZONTAL) {
                currentCol = col + i;
            } else if (d == Direction.VERTICAL) {
                currentRow = row + i;
            }

            if (currentRow < 0 || currentRow >= 15 || currentCol < 0 || currentCol >= 15) {
                throw new IllegalArgumentException("Le mot déborde du plateau");
            }

            if (squares[currentRow][currentCol] != null) {
                throw new IllegalArgumentException("Une case est déjà occupée");
            }
        }

        for (int i = 0; i < letters.length; i++) {
            if (d == Direction.HORIZONTAL) {
                squares[row][col + i] = letters[i];
            } else {
                squares[row + i][col] = letters[i];
            }
        }
    }
}
```

Et il te faut aussi l’énumération Direction demandée dans ce point :

```
package g12345.scrabble;

public enum Direction {
    HORIZONTAL,
    VERTICAL
}

```

Dans app:

```
package g12345.scrabble;

public class App {
    public static void main(String[] args) {
        Board board = new Board();
        Letter[] letters = new Letter[] { new Letter('A'), new Letter('B') };

        board.setLetters(0, 0, Direction.HORIZONTAL, letters);

        System.out.println(board.get(3, 4)); // null
        System.out.println(board.get(0, 1).getLetter()); // B
    }
}
```

### 1.3 Une classe Bag

La classe Bag représente le sac contenant toutes les lettres disponibles dans le jeu. Elle possède un attribut privé letters, qui est une liste d’objets Letter. Cette liste contient toutes les lettres qui peuvent encore être tirées par les joueurs.

Dans le constructeur, la liste est créée avec new ArrayList<>(). Ensuite, on ajoute des lettres dans le sac. Dans cet exemple simple, on ajoute toutes les lettres de l’alphabet. Après avoir ajouté les lettres, la méthode Collections.shuffle() est utilisée pour mélanger la liste, ce qui permet d’obtenir un tirage aléatoire.

La méthode draw() permet de tirer une seule lettre du sac. Elle vérifie d’abord si le sac est vide. Si c’est le cas, elle retourne null. Sinon, elle enlève la première lettre de la liste avec remove(0) et la retourne.

La méthode draw(int n) permet de tirer plusieurs lettres en une seule fois. Elle crée une nouvelle liste appelée drawn qui contiendra les lettres tirées. Ensuite, une boucle répète l’opération n fois (ou jusqu’à ce que le sac soit vide). À chaque tour, la méthode draw() est appelée et la lettre obtenue est ajoutée à la liste drawn. Finalement, cette liste est retournée.

Cette classe permet donc de gérer le sac de lettres : elle contient toutes les lettres du jeu, les mélange et fournit des méthodes pour tirer une ou plusieurs lettres au hasard.

```
package g12345.scrabble;

import java.util.List;
import java.util.ArrayList;
import java.util.Collections;

public class Bag {

    private List<Letter> letters;

    public Bag() {
        letters = new ArrayList<>();

        // Exemple simple : on ajoute les lettres de l'alphabet
        for (char c = 'A'; c <= 'Z'; c++) {
            letters.add(new Letter(c));
        }

        // mélange les lettres
        Collections.shuffle(letters);
    }

    // tire une lettre
    public Letter draw() {
        if (letters.isEmpty()) {
            return null;
        }
        return letters.remove(0);
    }

    // tire n lettres
    public List<Letter> draw(int n) {
        List<Letter> drawn = new ArrayList<>();

        for (int i = 0; i < n && !letters.isEmpty(); i++) {
            drawn.add(draw());
        }

        return drawn;
    }
}
```

### 1.4 La classe principale App

Ce que fait ce code

La méthode main affiche SCRABBLE, crée un sac Bag et un plateau Board, puis lance la boucle de jeu avec run(bag, board), comme montré dans le TD.

td04-mini

La méthode display(Board board) affiche le plateau sous forme de grille. Si une case contient une lettre, elle affiche son caractère. Sinon, elle laisse la case vide. C’est exactement l’idée montrée dans la figure du document.

td04-mini

La méthode display(List<Letter> rack) affiche le chevalet du joueur. J’ai choisi d’afficher chaque lettre avec son indice, par exemple [0:A] [1:B]. C’est utile parce que la commande set demande des indices de lettres du chevalet. Le document précise en effet une commande du type set <row> <col> <direction> <indice lettre> [indice lettre...].

td04-mini

La méthode run contient la boucle de jeu. Elle commence par tirer 7 lettres pour remplir le chevalet. Ensuite, tant que le joueur ne tape pas quit, le programme affiche le plateau et le chevalet, lit une ligne au clavier avec Scanner, puis découpe cette ligne avec split("\\s+"), comme indiqué dans le TD.

td04-mini

Si la commande est quit, la boucle s’arrête.

Si la commande est set, le programme lit la ligne, la colonne, la direction (h pour horizontal ou v pour vertical), puis les indices des lettres dans le chevalet. Il construit un tableau Letter[] à partir des lettres choisies, appelle board.setLetters(...), retire les lettres utilisées du chevalet, puis tire de nouvelles lettres dans le sac pour revenir à 7 lettres.

J’ai aussi ajouté des try/catch pour éviter que le programme plante si l’utilisateur entre une mauvaise commande, un mauvais nombre, ou un indice incorrect.

Exemple de commande

Si le chevalet contient par exemple :

[0:A] [1:B] [2:C] [3:D]

et que tu écris :

set 7 3 h 0 1

alors le programme place A puis B horizontalement à partir de la ligne 7, colonne 3, comme dans l’exemple du PDF.

Remarque importante

Pour que cette classe fonctionne, il faut que :

Board possède bien get(...) et setLetters(...)

Bag possède draw() et draw(int n)

Letter possède getLetter()

Direction contienne HORIZONTAL et VERTICAL

```
package g12345.scrabble;

import java.util.List;
import java.util.ArrayList;
import java.util.Scanner;

public class App {

    public static void main(String[] args) {
        System.out.println("SCRABBLE");
        Bag bag = new Bag();
        Board board = new Board();
        run(bag, board);
    }

    private static void display(Board board) {
        for (int i = 0; i < 15; i++) {
            System.out.println("+---".repeat(15) + "+");
            for (int j = 0; j < 15; j++) {
                Letter letter = board.get(i, j);
                if (letter != null) {
                    System.out.print("| " + letter.getLetter() + " ");
                } else {
                    System.out.print("|   ");
                }
            }
            System.out.println("|");
        }
        System.out.println("+---".repeat(15) + "+");
    }

    private static void display(List<Letter> rack) {
        System.out.print("Chevalet : ");
        for (int i = 0; i < rack.size(); i++) {
            System.out.print("[" + i + ":" + rack.get(i).getLetter() + "] ");
        }
        System.out.println();
    }

    private static void run(Bag bag, Board board) {
        final Scanner IN = new Scanner(System.in);
        List<Letter> rack = new ArrayList<>();

        // Remplir le chevalet au début
        rack.addAll(bag.draw(7));

        boolean running = true;

        while (running) {
            display(board);
            display(rack);

            System.out.println("Commande : quit ou set <row> <col> <h|v> <indice lettre> [indice lettre...]");
            String in = IN.nextLine();
            String[] elements = in.split("\\s+");

            if (elements.length == 0 || elements[0].isEmpty()) {
                System.out.println("Commande invalide.");
                continue;
            }

            String command = elements[0];

            if (command.equals("quit")) {
                running = false;

            } else if (command.equals("set")) {
                try {
                    if (elements.length < 5) {
                        System.out.println("Commande set invalide.");
                        continue;
                    }

                    int row = Integer.parseInt(elements[1]);
                    int col = Integer.parseInt(elements[2]);

                    Direction direction;
                    if (elements[3].equalsIgnoreCase("h")) {
                        direction = Direction.HORIZONTAL;
                    } else if (elements[3].equalsIgnoreCase("v")) {
                        direction = Direction.VERTICAL;
                    } else {
                        System.out.println("Direction invalide. Utilisez h ou v.");
                        continue;
                    }

                    Letter[] lettersToPlace = new Letter[elements.length - 4];

                    for (int i = 4; i < elements.length; i++) {
                        int rackIndex = Integer.parseInt(elements[i]);

                        if (rackIndex < 0 || rackIndex >= rack.size()) {
                            throw new IllegalArgumentException("Indice de chevalet invalide");
                        }

                        lettersToPlace[i - 4] = rack.get(rackIndex);
                    }

                    board.setLetters(row, col, direction, lettersToPlace);

                    // Supprimer du chevalet les lettres utilisées
                    List<Integer> usedIndexes = new ArrayList<>();
                    for (int i = 4; i < elements.length; i++) {
                        usedIndexes.add(Integer.parseInt(elements[i]));
                    }

                    // On supprime en ordre décroissant pour éviter le décalage des indices
                    usedIndexes.sort((a, b) -> b - a);
                    for (int index : usedIndexes) {
                        rack.remove(index);
                    }

                    // Recompléter le chevalet à 7 lettres
                    rack.addAll(bag.draw(7 - rack.size()));

                } catch (NumberFormatException e) {
                    System.out.println("Erreur : un nombre attendu est invalide.");
                } catch (IllegalArgumentException e) {
                    System.out.println("Erreur : " + e.getMessage());
                }

            } else {
                System.out.println("Commande inconnue.");
            }
        }

        System.out.println("Fin du jeu.");
    }
}
```

## TD 05 – JUnit – Les tests unitaires

### Les types d’erreurs

Un programme peut mener à trois sortes d’erreurs 1 :

1. il peut ne pas compiler ;

2. il peut se planter à l’exécution (par exemple si on demande une division par 0) ;

3. il peut fournir un résultat incorrect.

Le 1er cas est facile à détecter puisqu’il suffit au développeur de demander une compilation 2 pour obtenir la liste complète des erreurs de ce type.

Les deux derniers cas sont plus délicats. Comment savoir qu’on a bien testé toutes les parties de code ? Qu’on a bien testé tous les cas particuliers ? Cela demande une réflexion, une planification des cas à tester.

### 1.2 Tester quoi et quand ?

Commençons par quelques réflexions sur les tests.

1. Nous allons tester chaque méthode séparement. L’idée est que si toutes les
   méthodes sont correctes, le programme le sera aussi 3 .

2. Pour chaque méthode, il faut imaginer tous les cas qui pourraient poser problème. Concrètement, il faut trouver les paramètres à donner à la fonction pour que tous les cas particuliers soient testés. Par exemple, si une méthode doit réagir différement si son paramètre est négatif ou pas, il faudra au minimum la tester avec un nombre négatif et un nombre non négatif.

3. Dans une situation réelle, une application est composée de milliers de méthodes. Si chacune nécessite quelques tests, le nombre total de tests est colossal.

4. Lorsqu’on apporte une modification dans le code (pour le corriger, le rendre plus lisible ou parce qu’on ajoute une fonctionnalité) il est possible qu’on crée une erreur là où il n’y en avait pas. Pour être sûr, il faut dès lors tout retester.
   On comprend bien qu’il faut mettre en place une procédure de tests la plus rapideet facile possible si on veut pouvoir l’exécuter régulièrement. Pour toutes ces raisons, tester à la main chaque cas planifié n’est pas envisageable ; une seule solution :

l’automatisation.

### 2 JUNIT

Plus qu’une simple bibliothèque, un framework définit une boite à outils qui facilite le développement d’une application tout en imposant un cadre à son architecture.

## TD 06 – Le débogage
