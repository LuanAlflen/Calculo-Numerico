import numpy as np

def decomposicao_LU(A):
    n = len(A)
    #criando LU (nao sei como criar e um jeito mais facil)
    LU = []
    B = [0]*(n+1)
    for i in range(n):
        for j in range(n+1):
            if(j==n):
                B[i] = A[i][j]

    for i in range(n):
        linha = []
        for j in range(n):
            linha.append(0)
        LU.append(linha)

    # print(LU)

    for i in range(0,n):
        for j in range (0, n):
            if(i>=j):
                somatoria = 0
                for k in range(0, j):
                    somatoria += LU[i][k]*LU[k][j]
                LU[i][j] = A[i][j] - somatoria
            else:
                somatoria = 0
                for k in range(0, i):
                    somatoria += LU[i][k] * LU[k][j]
                LU[i][j] = (A[i][j] - somatoria)/LU[i][i]

    #print("LU: \n", LU)
    return LU, B

def resolver_LU(LU, B):
    n = len(LU)
    y = [0]*n
    x = [0]*n
    for i in range(0, n):
        somatoria = 0
        for j in range(0, i):
            somatoria += LU[i][j]*y[j]
        y[i] = (B[i] - somatoria)/LU[i][i]

    for i in range(n-1, -1, -1):
        somatoria = 0
        for j in range(i+1, n):
            somatoria += LU[i][j]*x[j]
        x[i] = y[i] - somatoria
    return x