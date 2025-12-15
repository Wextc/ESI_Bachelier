import random

def liste_entiers_aleatoires(n, nmin, nmax):
    return [random.randint(nmin, nmax) for _ in range(n)]
res = liste_entiers_aleatoires(10, 5, 9)
print(res)