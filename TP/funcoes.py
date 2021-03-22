import math

def media(A):
    n = len(A)
    media = 0.0
    for i in range(0, n):
        media += A[i]

    return media/n


def desvio_padrao(A):
    n = len(A)
    m = media(A)
    s = 0.0
    for i in range(0, n):
        s += pow(A[i] - m, 2)

    return math.sqrt(s/(n-1))

def read_file(str):
    file = open(str, 'r')
    lista = []

    for i in file:
        lista.append(float(i))
    file.close()
    return lista

# def write(str, altura):
#     lista = read_file(str)
#     m = media(lista)
#     dp = desvio_padrao(lista)
#     file = open('saida', 'w')
#     file.write(str(altura) + ' ')
#     file.write(str(m) + ' ')
#     file.write(str(dp) + '\n')

