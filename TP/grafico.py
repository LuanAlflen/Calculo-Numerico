import matplotlib.pylab as plt
import numpy as np

with open('dados_reduzidos.txt') as f:
    dados = [[float(x) for x in line.split()] for line in f]

# print(dados)

x = np.linspace(1, 6, 100)
for i in range(len(dados)):
    plt.errorbar(dados[i][0], dados[i][1], yerr=dados[i][2], fmt="or")

plt.plot(x, (x/9.81)**(0.5), "b-")

plt.xlabel('Altura(m)')
plt.ylabel('Tempo(s)')
plt.title('Resultados do experimento')
plt.margins(0.1)
plt.show()
