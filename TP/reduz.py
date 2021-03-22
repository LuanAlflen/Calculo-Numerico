import funcoes

lista = funcoes.read_file('altura1.5.txt')
file = open('dados_reduzidos.txt', 'w')
altura = 1.5
for number in lista:
    m = funcoes.media(lista)
    dp = funcoes.desvio_padrao(lista)
    file.write(str(altura) + ' ')
    file.write(str(m) + ' ')
    file.write(str(dp) + '\n')
    altura += 1.0
    if altura == 6.5:
        break
    lista = funcoes.read_file('altura' + str(altura) + '.txt')
