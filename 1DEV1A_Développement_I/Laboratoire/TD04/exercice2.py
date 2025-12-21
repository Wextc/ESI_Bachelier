# Demande des deux nombres à l'utilisateur
nbre1 = int(input("Choisissez le premier nombre : "))
nbre2 = int(input("Choisissez le deuxième nombre : "))

# Comparaison sans utiliser max()
if nbre1 > nbre2:
    print(nbre1, "est plus grand que", nbre2)
elif nbre2 > nbre1:
    print(nbre2, "est plus grand que", nbre1)
else:
    print("Les deux nombres sont égaux :", nbre1)