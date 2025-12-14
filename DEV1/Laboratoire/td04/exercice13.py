import math

# Saisie des coordonnées et du rayon
x = float(input("Entrez la valeur de x : "))
y = float(input("Entrez la valeur de y : "))
xc = float(input("Entrez la valeur de xc (centre du cercle en x) : "))
yc = float(input("Entrez la valeur de yc (centre du cercle en y) : "))
r = float(input("Entrez le rayon du cercle : "))

# Calcul de la distance entre le point et le centre
distance = math.sqrt((x - xc)**2 + (y - yc)**2)

# Vérification de l’appartenance au cercle
if distance <= r:
    print(True)
else:
    print(False)
