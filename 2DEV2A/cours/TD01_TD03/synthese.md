## TD 01 – Intro Orienté Objet

### Orienté objet En programmation orientée objet (OO)

###### Cours:

un programme est composé d’objets, qui représentent des entités stockées dans la mémoire de l’ordinateur. Ces objets interagissent via l’envoi de messages représentés par des appels de méthodes, des fonctions attachées à un objet.

Chaque objet est dès lors responsable de connaître son propre comportement.

###### Explications:

La programmation orientée objet repose sur l’idée qu’un programme est constitué d’objets qui représentent des entités manipulées par l’ordinateur et stockées en mémoire. Chaque objet regroupe à la fois des données, appelées attributs, et des actions, appelées méthodes. Les attributs décrivent l’état de l’objet, tandis que les méthodes définissent son comportement.

Les objets interagissent entre eux en s’envoyant des messages. Concrètement, cela correspond à des appels de méthodes : lorsqu’un objet souhaite qu’un autre effectue une action, il invoque l’une de ses méthodes.

Ainsi, la communication entre les différentes parties du programme se fait par ces échanges de messages, ce qui permet une organisation claire et structurée du code.

Un principe essentiel de ce paradigme est que chaque objet est responsable de son propre comportement. Cela signifie qu’il gère lui-même ses données et les opérations qui peuvent être réalisées sur celles-ci.

Les autres objets n’accèdent pas directement à ses informations internes, mais passent par les méthodes qu’il met à disposition. Cette manière d’organiser le programme favorise la modularité, la réutilisation du code et une meilleure maintenance.

###### Cours :

Classes Afin de définir ce qu’un objet peut faire dans un programme OO, on définit des classes. Chaque objet appartient à une classe, qui définit
(notamment) les méthodes que cet objet possède.

###### Explications:

Dans la programmation orientée objet, les classes jouent un rôle fondamental, car elles permettent de définir ce qu’un objet peut faire au sein d’un programme. Une classe peut être considérée comme un modèle ou un plan de construction à partir duquel on crée des objets. Elle décrit la structure et le comportement communs à tous les objets qui en sont issus.

Chaque objet appartient à une classe. Cela signifie qu’il est une instance de cette classe et qu’il hérite des caractéristiques qu’elle définit. La classe précise notamment les attributs (les données) que les objets posséderont ainsi que les méthodes (les actions) qu’ils pourront exécuter. Ainsi, tous les objets créés à partir d’une même classe partagent les mêmes types de comportements, même si leurs valeurs internes peuvent être différentes.

En définissant des classes, on organise le programme de manière cohérente et structurée. Les classes permettent de regrouper logiquement les données et les fonctionnalités liées à un même concept, ce qui facilite la compréhension, la réutilisation et la maintenance du code.

###### Cours:

Anatomie d’une classe Java En Java, une classe est définie avec les notations suivantes :

▷ Le mot-clé class indique que nous définissons une nouvelle classe, il est
suivi du nom de la classe

▷ Après le nom de la classe, des accolades {} vont délimiter le contenu

    de la classe : tout ce qui se trouve entre ces accolades fait partie du code

    de la classe, ce qui est en-dehors des accolades n’en fait pas partie.

▷ Le mot-clé public, placé tout devant, est la visibilité de la classe ; nous
y reviendrons plus tard.

```
public class Dog {
}

```

###### Explications:

La visibilité d'une classe:

En Java, la visibilité d’une classe détermine depuis quelles parties du programme cette classe peut être utilisée. Elle est définie par un modificateur d’accès placé devant le mot-clé class. Ce mécanisme permet de contrôler l’accès au code et d’organiser proprement un projet.

Pour les classes dites top-level (définies directement dans un fichier), il existe essentiellement deux niveaux de visibilité : public et la visibilité par défaut (sans mot-clé).

Lorsqu’une classe est déclarée public, elle est accessible depuis n’importe quel autre package du programme. Cela signifie qu’elle peut être utilisée dans d’autres fichiers, à condition d’être importée. En Java, une classe publique doit obligatoirement se trouver dans un fichier portant exactement le même nom qu’elle.

En revanche, si aucun mot-clé n’est précisé, la classe a une visibilité dite package-private (ou visibilité par défaut). Dans ce cas, elle est accessible uniquement par les autres classes situées dans le même package. Elle ne peut pas être utilisée depuis un autre package. Cela permet de limiter l’accès à certaines classes qui ne sont destinées qu’à un usage interne.

Ainsi, la visibilité d’une classe sert à contrôler son niveau d’exposition dans le programme. Déclarer une classe public revient à la rendre accessible partout, tandis que l’absence de modificateur restreint son utilisation au sein de son propre package. Ce principe contribue à la sécurité, à l’encapsulation et à une meilleure organisation du code.

###### Cours:

Méthode Une méthode est un type de fonction utilisé en programmationorientée objet. Une méthode est toujours appelée sur un objet spécifique, et désigne le comportement de cet objet particulier.

```

public class Dog {

    void bark() {
    }

}

```

###### Explications:

En programmation orientée objet, une méthode est une fonction définie à l’intérieur d’une classe. Elle représente un comportement que les objets issus de cette classe peuvent exécuter. Contrairement à une fonction classique, une méthode est toujours associée à un objet précis : elle agit sur cet objet et peut utiliser ses données internes.

Dans l’exemple suivant :

```
public class Dog {

    void bark() {
    }

}

```

La classe Dog définit un type d’objet représentant un chien.
La méthode bark() décrit un comportement propre à cet objet : aboyer.

Le mot-clé void indique que la méthode ne renvoie aucune valeur. Le nom bark correspond à l’action réalisée. Les parenthèses () contiennent les éventuels paramètres (ici, il n’y en a pas). Les accolades {} délimitent le corps de la méthode, c’est-à-dire le code qui sera exécuté lorsqu’elle sera appelée.

Pour utiliser cette méthode, il faut créer un objet Dog, puis appeler la méthode sur cet objet :

```
Dog myDog = new Dog();
myDog.bark();

```

Ici, la méthode bark() est appelée sur l’objet myDog. Cela signifie que c’est ce chien précis qui exécute l’action. Ainsi, une méthode définit le comportement d’un objet particulier et constitue un élément essentiel de la programmation orientée objet.

###### Cours:

Anatomie d’une méthode Java En Java, une méthode doit être définie
au sein d’une classe, avec les notations suivantes :

▷ Un mot-clé qui définit le type de retour de la méthode, c’est-à-direle type du résultat renvoyé par la méthode. Puisqu’ici nous n’avons pasde résultat, le mot-clé void ("vide") est utilisé.

▷ Le nom de la méthode, suivi de parenthèses. Si la méthode prenait desparamètres, ils seraient placés entre ces parenthèses.

▷ Entre accolades, le code de la méthode.

###### Cours:

La méthode main en Java En Java, la méthode principale du programme
possède une structure bien définie :

▷ Elle s’appelle main

▷ Elle reçoit les mots-clés public static dont nous reparlerons plus tard

▷ Son type de retour est void (pas de résultat)

▷ Elle prend un argument de type String[] (un tableau de chaînes dcaractère) qui représente des paramètres passés au programme par exemple dans un terminal. Nous ne les utiliserons pas dans le cadre du cours, mais il faut malgré tout dire à Java qu’ils sont présents.

###### Explication:

Tout d’abord, la méthode doit obligatoirement s’appeler main. Si elle porte un autre nom, le programme ne pourra pas démarrer.

Elle est précédée des mots-clés public et static.

public signifie que la méthode est accessible depuis l’extérieur de la classe.

static indique qu’elle appartient à la classe elle-même et non à un objet particulier. Cela est nécessaire car, au moment où le programme démarre, aucun objet n’a encore été créé.

Le type de retour est void, ce qui signifie que la méthode ne renvoie aucun résultat. Elle exécute simplement des instructions.

Enfin, elle possède un paramètre : String[] args. Il s’agit d’un tableau de chaînes de caractères. Ce tableau contient les arguments éventuellement passés au programme lors de son lancement (par exemple depuis un terminal). Même si ces paramètres ne sont pas utilisés, leur présence est obligatoire pour que la signature de la méthode soit correcte.

Ainsi, la méthode main possède une forme imposée par Java. Elle sert de point de départ à l’exécution du programme et permet d’y écrire les premières instructions qui seront réalisées.

###### Cours:

Java : un langage typé Java est un langage fortement typé :
il faudra toujours préciser le type des valeurs avec lesquelles on travaille. Vous l’avez déjà vu lors de la définition d’une méthode : on doit préciser le type de sa
valeur de retour.

De même, lorsqu’on utilise une variable pour la première fois en Java, il faudra déclarer celle-ci en précisant son type :

Dog médor;

Une fois le type d’une variable déclarée, ce type ne peut plus changer. Une variable en Java aura donc toujours le même type, tant qu’elle existe.

###### Explications:

Java est un langage fortement typé, ce qui signifie que chaque donnée manipulée dans un programme possède un type clairement défini, et que ce type doit toujours être précisé. Le compilateur vérifie que les opérations effectuées sont cohérentes avec les types utilisés, ce qui permet d’éviter de nombreuses erreurs.

On observe déjà cette règle lors de la définition d’une méthode : il est obligatoire d’indiquer le type de retour (par exemple void, int, String, etc.). Java doit savoir à l’avance quel type de valeur la méthode renverra.

De la même manière, lorsqu’on déclare une variable pour la première fois, il faut préciser son type. Par exemple :

```
Dog médor;

```

Ici, on déclare une variable nommée médor de type Dog. Cela signifie que cette variable pourra uniquement contenir une référence vers un objet de type Dog.

Une caractéristique essentielle de Java est que le type d’une variable ne peut pas changer après sa déclaration. Une fois qu’une variable est déclarée avec un certain type, elle conservera ce type durant toute son existence. On ne pourra pas, par exemple, utiliser plus tard cette même variable pour stocker un objet d’un autre type incompatible.

Ce typage strict renforce la sécurité et la fiabilité du programme, car les erreurs de type sont détectées dès la compilation plutôt qu’au moment de l’exécution.

###### Cours:

Prenez le temps de commenter votre code ! Dans tout travail de programmation, la maintenance du code est nettement plus coûteuse que son écriture. Il est donc essentiel de rendre le code aussi lisible que possible, et la documentation est un outil pratique dans ce but. Prenez donc le réflexe de toujours commenter votre code Java en utilisant des commentaires Javadoc !

## TD 02 – Intro OO - Partie 2

###### Cours: Que se passe-t-il si on veut avoir plusieurs chiens ?

###### Explications:

La classe, c’est comme un moule : elle définit quelles propriétés et quels comportements auront tes objets. Une fois que la classe est prête, tu peux créer autant d’objets que tu veux, un peu comme si tu faisais plusieurs copies basées sur ce moule. Pour cela, tu utilises le mot-clé "new" suivi du nom de ta classe et des parenthèses. Par exemple, si tu as une classe "Voiture", tu peux faire : "Voiture maVoiture = new Voiture();". Chaque "new Voiture()" te donne un nouvel objet indépendant, avec ses propres valeurs pour les attributs définis dans la classe.

Dans la classe Dog on a :

```
public class Dog {

    void bark() {
    }

}

```

Une fois que tu as défini ta classe, tu peux ensuite instancier des objets de cette classe (donc créer des instances) dans ta classe qui contient la méthode principale (généralement appelée "main"). C’est là que tu vas manipuler tes objets, appeler leurs méthodes et orchestrer les actions. En gros, la classe main est le point d’entrée où tu mets tout en action.

```
Dog milou = new Dog();
milou.bark();

```

Les attributs:

Une méthode, c’est une action ou un comportement que l’objet peut accomplir, tandis qu’un attribut (ou une propriété) est une donnée, une caractéristique, qui décrit l’état ou les particularités de cet objet. Les deux vont de pair pour modéliser des objets en programmation orientée objet. Tout comme les variables en Java, les attributs on un type qui ne change pas une fois l’attribut déclaré.

this.name:

Le mot-clé "this" est utilisé dans une méthode pour faire référence à l’instance courante de l’objet, c’est-à-dire l’objet lui-même. Concrètement, quand tu as un attribut de classe qui porte le même nom qu’un paramètre ou une variable locale, "this" te permet de lever l’ambiguïté. En gros, "this.nomAttribut" désigne l’attribut de l’objet, alors que sans "this", tu parlerais peut-être d’une variable locale ou d’un paramètre.

```
public class Dog {

    String name; // Ceci est un attribut

    void bark() {  // Ceci est la méthode
        System.out.println(this.name + " a dit : Wouf !"); // Ceci est ce que fait la méthode:/> Ici elle affiche name suivit de "Wouf!"
    }

}

```

Le constructeur:

Le constructeur sert à créer l’objet et à initialiser ses attributs quand l’objet naît. Son nom est toujours le même que celui de la classe. Et si tu ne définis aucun constructeur, Java en génère automatiquement un par défaut, sans paramètre, qui ne fait qu'allouer l’objet sans initialisation particulière.

```
public class Dog {

    Dog(String name) {
        this.name = name;
    }
    String name;


    void bark() {  // Ceci est la méthode
        System.out.println(this.name + " a dit : Wouf !");

    }

}

```

Accesseur:

Un accesseur (getter en anglais) est une méthode qui accède àla valeur d’un attribut d’un objet donné, et renvoie simplement la valeur decet attribut.

Un getter, ou accesseur, est une méthode qui te permet de récupérer la valeur d’un attribut privé d’un objet. Il renvoie simplement cette valeur sans la modifier. En gros, c’est un petit pont sûr entre l’intérieur de l’objet et l’extérieur, pour accéder aux données de manière contrôlée.

IntelliJ possède un raccourci pour générer des accesseurs ! Ouvrez de nouveau le menu "Generate"... et choisissez "Getter".

Mutateur:

Un mutateur (setter en anglais) est une méthode qui reçoit une nouvelle valeur à assigner à un attribut de l’objet.

Exercice avec if:

Vous allez ajouter une nouvelle fonctionnalité à vos chiens : la possibilité de courir, et de manger.

Un chien ne peut courir que s’il n’a pas faim ; une fois qu’il a couru, il a faim. Par contre, il peut manger quoi qu’il arrive, et une fois qu’il a mangé, il n’a plus faim.

▷ Ajoutez un attribut hungry, qui dit si le chien a faim ou non. En Java, le type booléen se déclare avec le mot-clé boolean.

Cet attribut ne reçoit pas de valeur en paramètre du constructeur ! Un chien n’a pas faim au moment où il est créé.

```
public class Dog {

    String name;
    int weight;
    boolean hungry;   // nouvel attribut

    // Constructeur
    Dog(String name, int weight) {
        this.name = name;
        this.weight = weight;
        this.hungry = false;  // Un chien n’a pas faim à la création
    }

    void bark() {
        if (this.weight > 30) {
            System.out.println(this.name + " a dit : WOUUUF !");
        }
        else if (this.weight < 10) {
            System.out.println(this.name + " a dit : Yip yip!");
        }
        else {
            System.out.println(this.name + " a dit : Wouf !");
        }
    }

    void run() {
        if (!hungry) {
            System.out.println(this.name + " court dans le jardin !");
            hungry = true;  // Après avoir couru, il a faim
        } else {
            System.out.println(this.name + " ne peut pas courir, il a faim !");
        }
    }

    void eat() {
        System.out.println(this.name + " mange.");
        hungry = false;  // Après avoir mangé, il n’a plus faim
    }

    public static void main(String[] args) {

        Dog medor = new Dog("Médor", 60);

        medor.run();   // Il court
        medor.run();   // Il a faim, il ne peut pas courir
        medor.eat();   // Il mange
        medor.run();   // Il peut recourir
    }
}

```
