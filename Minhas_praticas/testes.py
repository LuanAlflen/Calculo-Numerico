import bisseccao
import newton
import eliminacao_gauseana
import decomposicao_LU
import math


def f1(x):
    y = math.exp(x) + x
    return y

def f2(x):
    y = math.pow(x, 3) + 4* math.pow(x, 2) - 10
    return y

def f3(x):
    y = math.cos(x) - x
    return y

def f4(x):
    y = -math.sin(x) - 1
    return y


print("metodo bisseccao \n")
print("iteracoes |  ponto    |     erro")
bisseccao.bisseccao(f3, 0, 1, 1e-4)
print("\n----------------------------------\n")
print("metodo de newton \n")
print("iteracoes |  ponto    |     erro")
newton.newton(f3, f4, 3.1415/2, 1e-2)
print("\n----------------------------------\n")
print("metodo da eliminacao gauseana \n")
matriz1 = [[1, 2, -3, 4, 7], [1, 2, 4, 7, -1], [2, 7, 1, 3, 5], [8, 3, 2, 1, 2]]
print("matriz: ", matriz1)
eliminacao_gauseana.eliminacao_gauseana(matriz1)
print("\n----------------------------------\n")
matriz2 = [[1, 1, 0, 3, 4], [2, 1, -1, 1, 1], [3, -1, -1, 2, -3], [-1, 2, 3, -1, 4]]
print("metodo da decomposicao LU \n")
LU, B = decomposicao_LU.decomposicao_LU(matriz2)
print("matriz: ", matriz2)
x = decomposicao_LU.resolver_LU(LU, B)
print("vetor final: ",x)



