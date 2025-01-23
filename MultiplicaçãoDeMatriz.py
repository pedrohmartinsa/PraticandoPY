#Mulplicando matrizes

from VerificarTamanhoDasMatrizes import verificando_se_sao_iguais

A = [
    [1, 2],
    [3, 4]
]

B = [
    [5, 6],
    [7, 8]
]
C = []
for i in range(len(A)):
    for j in range(len(A)):
        for k in range(len(A)):
            print(i, j, k)
