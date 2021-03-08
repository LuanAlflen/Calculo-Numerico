#! /usr/bin/python3
# -*- coding: utf-8 -*-
#_________________________________________________________
# Universidade Federal de Santa Catarina
# Departamento de Engenharias da Mobilidade
# Curso de Cálculo Numérico
# Prof. Alexandre Zabot
# https://zabot.paginas.ufsc.br
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

import matplotlib.pylab as plt
import numpy as np


def P2(x,a):
  """
  Calcula um polinômio de ordem 2
  P2(x) = a0 + a1*x + a2*x**2
  
  Recebe:
    x => Escalar ou vetor onde calcular P2
    a => Vetor com coeficientes
  
  Retorna:
    Polinômio calculado em x
  """
  return ( a[0] + a[1]*x + a[2]*x*x )


x = np.linspace(-1,1,100)


plt.plot( x, P2(x,[0,0,1] ) , "b-", label="$P_2(x) = x^2$" )
plt.plot( x, P2(x,[2,-1,3]) , "r-", label="$P_2(x) = 2 - x + 3x^2$" )


plt.grid()
plt.margins(0.1)
plt.legend()
plt.show()

print("Oi luan...")




