liste1 = [1,2,3]
print(len(liste1))
print(0 in liste1)
liste1.append(15)
liste1.reverse()
print(liste1)
# Affiche un élément choisi dont on connait l'indice de départ et de fin
liste1 = [1,2,3]
liste4 = liste1[2:3]
print("Affiche l'élément qui commence à l'index 2 et se termine à l'index 3 :",liste1[2:3])

# Compte la récurrence de l'élément dans count(...)
liste5 = [15,15,15, 3, 2, 1]
print("Compte la récurrence de l'élément 15: ",liste5.count(15))
print("Compte la récurrence de l'élément 3: ",liste5.count(3)) # liste6 = liste5.count(3)  print(liste6) :> donne même résultat.

#Insert. On prend l'élément d'index 1 puis avant lui  on insert 7.
liste6 = liste5.insert(1,7)
print("Insertion :",liste5)

# Modification. On prend l'élément d'index 1 et on le remplace par 7
liste5 = [15,15,15, 3, 2, 1]
liste5[1] = 7
print("Modification :",liste5)

# Remplace l'élément situé à entre l'index 1 et 3 l'array > [10, 12, 14, 16]

liste1 = [1, 2, 3, 5, 6, 7, 8, 9, "a", "b", "c", "d", "e", "f", "g", "h"]

liste1[1:3] = [10, 12, 14, 16]

print("Liste modifiée", liste1)

# Copie la liste
liste1 = [1, 2, 3, 5, 6, 7, 8, 9]
liste2 = ["a", "b", "c", "d", "e", "f", "g", "h"]
liste3 = liste1.copy() 
print("Liste copiée :", liste3)  # [1, 2, 3, 5, 6, 7, 8, 9]

# Si ton objectif est de combiner liste1 et liste2
liste3 =  liste2 + liste1
print("Liste1 et liste2 sont concotenaté :", liste3)

# Extraire valeur
liste3 = [1, 2, 3, 5, 6, 7, 8, 9, "a", "b", "c", "d", "e", "f", "g", "h"]
liste1 = liste3[8:]
print("La valeur de liste1 :", liste1)

# extrayez de la liste1 l’élément en 4ème position ;

liste1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print("Elément à l'indice 4 position : ", liste1[3])

# triez liste1 en ordre ascendant (du plus petit au plus grand) ;

liste1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
liste2 = [1, 2, 3, 5, 6, 7, 8, 9]
liste1.sort()
print("Liste1 triée par ordre ascendant :", liste1)


# triez liste2 en ordre descendant (du plus grand au plus petit) ;
liste2 = [1, 2, 3, 5, 6, 7, 8, 9]
liste2.sort(reverse=True)
print("Liste inversée :", liste2)


# cherchez l’indice d’une valeur présente dans liste2 ;
liste1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
liste2 = [1, 2, 3, 5, 6, 7, 8, 9]
print("La valeur de l'élément avec l'indice 7 : ",liste2.index(7))



# recherchez l’indice d’une valeur non présente dans liste2 ;

liste1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
liste2 = [1, 2, 3, 5, 6, 7, 8, 9]
# liste2.index(100) # ValueError: 100 is not in list. Impossible


#supprimez une valeur présente dans liste2 ;
liste1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
liste2 = [1, 2, 3, 5, 6, 7, 8, 9]
liste2.remove(6)
print("Liste2 sans l'élément de valeur 6:", liste2) # résutat :  [9, 8, 7, 5, 3, 2, 1]


# que se passe-t-il si vous supprimez une valeur non présente dans liste2 ?
liste2 = [1, 2, 3, 5, 6, 7, 8, 9]
#liste2.remove(100) # ValueError: list.remove(x): x not in list 

 
# Ajoute à la fin de liste1 les éléments de liste2 situés entre la 3ième et la 7ième position inclues ;
liste1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
liste2 = [1, 2, 3, 5, 6, 7, 8, 9]
liste1.extend(liste2[2:7])
print("Insertion des éléments entre l'indice 2 et 7 de liste2 qui étend liste1 :",liste1)


# Supprime toutes les valeurs de liste2 ;
liste2 = [1, 2, 3, 5, 6, 7, 8, 9]
liste2.clear()
print("Liste vidée :", liste2) # Résultal :   []



# Supprimer le premier élément
liste1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
del liste1[0]
print("Liste sans le premier élémment ici 'a': ", liste1)







