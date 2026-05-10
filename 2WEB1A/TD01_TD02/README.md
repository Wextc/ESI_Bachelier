## Synthèse

Le langage HTML est composé de balises qui servent notamment à décrire les éléments de page. Lorsqu’il s’agit d’encadrer un

élément pour lui donner une signification :

la balise de début (ouvrante) contient un mot-clé entre < et > (chevrons) ;

la balise de fin (fermante) contient ce même mot-clé entre </ et >.

**_Élément_**

Un élément est une partie d’une page web, délimitée par une balise ouvrante et une balise fermante.

**_Contenu_**

On appelle contenu ce qui se trouve à l’intérieur des balises ouvrante et fermante. Ce contenu peut être
composé de texte ou d’éléments (appelés les enfants de l’élément de départ).

**_*Attribut*_**

Un attribut est placé dans une balise ouvrante. Il est de la forme nom="valeur" et permet de donner des
précisions sur la balise. Certains attributs sont valides dans toutes les balises ; d’autres sont spécifiques à
certaines balises.

```
<h1>Ma première page web</h1>

<p> : indique un paragraphe (séparé du reste par un retour à la ligne).

<ul> : indique le début d’une liste à puces.

<li> : indique un élément de la liste.

<a> : permet de définir un hyperlien, vers un autre site ou une autre page du site.

```

**_Rafraichir la page_**

Dans le navigateur web, tapez sur la touche F5 .

**_Indentation en HTML_**

L’indentation du code n’a pas l’importance qu’elle a en Python. Elle est toutefois cruciale pour les
humains qui vont lire le code. Pour corriger l’indentation de votre code, cliquez-doit pour avoir le menu
contextuel et choisissez Format Document .

## TD02 Découverte de CSS et Javascript

## CSS

Le fichier servira à définir les règles de mise en forme de la page.

"link" permet de lier le fichier html au fichier css.

```
 <link rel="stylesheet" href="style.css">

```

Le html et le css ne permettent que d'afficher les pages.

Pour le user interaction, il faut introduire Javascript.

Le JS permet de déterminer aussi le comportement des pages.

Nous pouvons utiliser un langage plus strict au niveau du typage des variables grâce à use strict.

```
"use strict";

```

C'est une bonne pratique de le mettre.

<b>scripts:</b>

La balise script permet de lier le fichier html au fichier js.

L'attribut defer permet de lancer le fichier js après que la html ait entièrement chargé.

```

<script src="nom.js" defer></script>

```

<b>Console:</b>

Cela montre que JavaScript peut changer de comportement selon le type de données (nombre ou texte), et qu’il est important de

bien contrôler ces types pour obtenir le résultat attendu.

```
console.log("Hello, world!");

  3+4 et => 7
 "3"+"4" concaténation => "34"
 Number("3")+Number("4") Transformation en int => 7.

```
