# Somar as matrizes e criar ma matriz C com as respectivas somas (exemplo: l1 c1 da matriz A + l1 c1 da matriz B)

A = [
    [1, 2],
    [3, 4]
]

B = [
    [5, 6],
    [7, 8]
]

linhas_index = []
for linha in range(len(A)):
    colunas_index = []
    for coluna in range(len(A[linha])):
        colunas_index.append(coluna)
    linhas_index.append(colunas_index)
print(linhas_index)


# def verificar_tamanho_matrizes():


def soma_matrizes(A, B):
    if len(A) == len(B) and len(A[0]) == len(B[0]):
        C = []
        for linha in range(len(A)):
            linhaSoma = []
            for coluna in range(len(A[linha])):
                linhaSoma.append(A[linha][coluna] + B[linha][coluna])
            C.append(linhaSoma)
        return C
    else:
        return 'As matrizes não tem a mesma quantidade de linhas e/ou colunas'


