def ler_linhas_colunas_matriz(matriz):
    linhasIndex = []
    for linha in range(len(matriz)):
        colunasIndex = []
        for coluna in range(len(matriz[linha])):
            colunasIndex.append(coluna)
        linhasIndex.append(colunasIndex)
    return linhasIndex

def verificando_se_sao_iguais(A, B):
    if ler_linhas_colunas_matriz(A) == ler_linhas_colunas_matriz(B):
        return True
    else:
        return False