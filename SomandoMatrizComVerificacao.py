# Somar as matrizes e criar ma matriz C com as respectivas somas (exemplo: l1 c1 da matriz A + l1 c1 da matriz B)

from VerificarTamanhoDasMatrizes import verificando_se_sao_iguais

A = [
    [1, 2, 3],
    [4, 5, 6]
]

B = [
    [7, 8, 9],
    [10, 11, 12]
]

def soma_matrizes(A, B):
    if verificando_se_sao_iguais(A, B) == True:
        C = []
        for linha in range(len(A)):
            linhaSoma = []
            for coluna in range(len(A[linha])):
                linhaSoma.append(A[linha][coluna] + B[linha][coluna])
            C.append(linhaSoma)
        return C
    else:
        return 'As matrizes não tem a mesma quantidade de linhas e/ou colunas'


print(soma_matrizes(A, B))
