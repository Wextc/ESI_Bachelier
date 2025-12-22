
M1 = [[1,2,3],[4,5,6],[7,8,9]]
M2 = [[9,8,7],[6,5,4],[3,2,1]]

def add_matrices(M1, M2):
    length = len(M1)
    resultat = []
    for i in range(length):
        row = []
        for j in range(length):
            row.append(M1[i][j] + M2[i][j])
        resultat.append(row)
    return resultat
    

print(add_matrices(M1, M2))