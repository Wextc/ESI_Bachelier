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

Le langage CSS permet de spécifier le style (l’apparence) des différents éléments de la page.

Dans le fichier index.html, ajoutez la ligne suivante avant la balise fermante </head>. Elle incorpore le style défini juste avant.

```
 <link rel="stylesheet" href="style.css">

```
