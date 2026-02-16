def lettre_vers_nombre(c):
    c = c.lower()
    return ord(c) - ord('a') 

print(lettre_vers_nombre("A"))