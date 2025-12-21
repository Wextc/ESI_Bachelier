def nom_du_mois(mois):
 if (mois==1):
  nom = 'Janvier'
 elif (mois==2):
  nom = 'Février'
 elif (mois==3):
  nom = 'Mars'
 elif (mois==4):
  nom = 'Avril'
 elif (mois==5):
  nom = 'Mai'
 elif (mois==6):
  nom = 'Juin'
 elif (mois==7):
  nom = 'Juillet'
 elif (mois==8):
  nom = 'Aout'
 elif (mois==9):
  nom = 'Septembre'
 elif (mois==10):
  nom = 'Octobre'
 elif (mois==11):
  nom = 'Novembre'
 elif (mois==12):
  nom = 'Décembre'
 return nom

def afficher_titre(mois, annee):
    print("========================")
    print("      ", nom_du_mois(mois), annee, "       ")
    print("========================")  

afficher_titre(2, 2020)