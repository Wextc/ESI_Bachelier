



def adresse_valide(email):
    if email[0] != "@" and email[0] != "."  and email[-1] != "@" and  email[-1] != "."   and "." in email   and email.count("@") ==1:
        return True
    else:
        return False
        