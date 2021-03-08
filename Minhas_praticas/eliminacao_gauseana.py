import math
import numpy as np


def eliminacao_gauseana(A):
    n = len(A)
    #print("n:", n)

    #escalonamento
    for i in range(0,n-1):
        pivo = A[i][i]
        k=i
        while(pivo == 0 and k != n):
            E = A[i]
            A[i] = A[k+1]
            A[k+1] = E
            k += 1
            pivo = A[i][i]

        #print("pivo:", pivo)
        for j in range (i+1, n):
            escalar = A[j][i]/pivo
            A[j] = A[j] - escalar*np.asarray(A[i])
            #print(A)
    print("matriz escalonada", A)

    #substituicao regressiva
    x = [0]*n
    for i in range(n-1, -1, -1):
        somatoria = 0
        #somatoria
        for j in range(n-1, 0, -1):
            temp = np.asarray(A[i][j])*x[j]
            somatoria = somatoria + temp
        #print("somatoria", somatoria)
        x[i] = (A[i][n] - somatoria)/A[i][i]
        #print(x)

    print("vetor final: ", x)
    return x
