# Marcelo Valenzuela Barrera
# 20.774.817-K

# Librerias necesarias
import numpy as np
import random

# create_line: int --> numpy_array
# Función que crea una lista de numpy con 0 en todas las posiciones, excepto en la última, donde hay un 1
# La función devuelve dicha lista
def create_line(n):
  assert type(n) == int
  fila = np.zeros(n)
  fila[n-1] = 1
  return fila

# move: int, bool --> int
# Función que simulá el comportamiento de la cola y cuenta cuantos pasos se dieron para que el último elemento termine al principio de la cola
# La función retorna la cantidad de pasos dados
# verificar_cola se utiliza para imprimir la cola.
def move(n, verificar_cola = False):
  assert type(verificar_cola) == bool

  # Se crea la cola
  cola = create_line(n) 
  # Contador              
  i = 0                                

  # Se ejecutan las siguientes instrucciones mientras el "1" no este en el primer lugar
  while cola[0] != 1:
    # Se genera un número entero aleatorio entre 0 y n-1, incluyendo los extremos
    change = random.randint(0, n-1)    

    # Se obtiene la posición del 1
    pos = np.where(cola==1)[0][0]      

    # Si el primer elemento se mueve detras o donde esta el 1, el 1 avanza una posición
    if change >= pos:                  
      cola[pos-1] = 1
      cola[pos] = 0
    # Pase lo que pase, se aumenta el contador en 1
    i += 1  

  # Se imprime la cola si asi se desea y se devuelve la cantidad de pasos tomados
  if verificar_cola:
    print(cola)
    return i
    
  # Se imprime la cantidad de pasos tomados
  return i


# test_mean: int int --> float
# Función que obtiene la cantidad de pasos de m colas de tamaño n y calcula el promedio de pasos usados.
# La función devuelve el promedio de los pasos.
def test_mean(n, m):
  assert type(n+m) == int
  assert m != 0
  # Variable para guardar la sumatoria
  test = 0
  # Se obtienen los pasos de cada cola
  for i in range(m):
    test += move(n)
  # Se devuelve el promedio
  return test/m

# harmonic_number: int --> float
# Función que calcula recursivamente el n-esimo número harmonico
# La función devuelve el número ármonico
def harmonic_number(n):
  assert type(n) == int
  assert n > 0
  # Se devuelve 1 si n = 1
  if n == 1:
    return 1
  # Se hace la recursión
  return 1/n + harmonic_number(n-1)


# Se realizá una prueba con 100 colas de 100 tamaño
print ("Pasos promedio: ", test_mean(100, 100))
# Se imprime la cantidad de pasos esperados según el analisis matematico
print ("pasos esperados: ", harmonic_number(99)*100)
