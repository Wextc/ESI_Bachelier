seconde = float(input("Les seconde : "))
minute = float(input("Les minutes :"))
heure = float(input("Les heures :"))

if seconde <= 60 and minute <= 60:     
    resultat= seconde + minute * 60 + heure * 3600
    print("Le résultat est : ", resultat)
else:
    print("Les secondes et / ou minutes doivent être égales à 60")


