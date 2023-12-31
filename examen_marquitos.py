# -*- coding: utf-8 -*-
"""Examen Marquitos

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KWw95KKIsKGTJux_egHlLbwThs9fpPbx
"""

import numpy as np
plat=120000
gold=80000
silv=50000
ganancias = np.array([])
asientos_disponibles=([i for i in range(1,11)],[i for i in range(11,21)],[i for i in range(21,31)],[i for i in range(31,41)],[i for i in range(41,51)],[i for i in range(51,61)],[i for i in range(61,71)],[i for i in range(71,81)],[i for i in range(81,91)],[i for i in range(91,101)])
listado_asistentes = []
matriz_asiento = np.array(asientos_disponibles)
def comprar_entradas():
  while True:
    cant = int(input('Ingrese la cantidad de entradas que desea llevar (Máximo 3): '))
    if cant > 0 or cant <= 3:
      print('         -------ESCENARIO-------\n')
      for i in range(10):
        print(matriz_asiento[i])
      print('\nPrecios:\n   -Platinum: $120.000 (1 - 20)\n   -Gold:      $80.000 (21 - 50)\n   -Silver:   $50.000 (51 - 100)\n')
      for i in range(cant):
        asiento=int(input('Ingrese el asiento que desea: '))
        nom = input('Ingrese su nombre)')
        rut = input('Ingrese su rut')
      break
    else:
      print('\n       Ingrese una cantidad entre 0 y 3\n')

def mostrar_ubicaciones():
 for i in range(10):
  print(asientos_disponibles[i])

def ver_listado():
  for i in range(len(listado_asistentes)):
    print(listado_asistentes[i])

def mostrar_ganancias():
  for i in range(len(ganancias)):
   print(ganancias[i])

def salir():
  print('¡Hasta Pronto!')
  print('Marcos del Canto, 12/07/23')

while True:
  try:
    op = int(input('''    MICHAEL JAM - Creativos.cl

    1  -Comprar entradas
    2  -Mostrar ubicaciones disponibles
    3  -Ver listado asistentes
    4  -Mostrar Ganancias
    5  -Salir\n

    Opcion seleccionada:'''))
    if op == 1:
      comprar_entradas()
    if op == 2:
      mostrar_ubicaciones()
    if op == 3:
      ver_listado()
    if op == 4:
      mostrar_ganancias()
    if op == 5:
      salir()
      break
  except:
    print('Algo salió mal')