
#-----------------------------------------------------------------------------

def potencia(a,n):  #ejercicio ilustrativo de potenciacion de orden O(log(n))
  print("llamado")
  if a == 0 and n <= 0:
    print("Indefinido")
  if a != 0 and n == 0:
    return 1
  if a != 0 and n < 0 :
    return 1 / potencia(a,-n)
  if n == 1:
    return a
  if n>1:
    y = potencia(a, n//2)
    if n%2 == 0:
      return y*y
    else:
      return a*y*y


#-----------------------------------------------------------------------------

def ordenar(lista):   #ordena una lista con la estrategia dividir y conquistar
  print("llamado de ordenar")
  n = len(lista)
  if n < 2:
    return lista
  else:
    return combinar( ordenar(lista[0:n//2]), ordenar(lista[n//2:n]) )


def combinar(lista1,lista2):
  print("llamado de combinar")
  if len(lista1) == 0:
    return lista2
  elif len(lista2) == 0:
    return lista1
  else:
    if lista1[0]<lista2[0]:
      return [ lista1[0] ] + combinar(lista1[1:len(lista1)], lista2)
    else:
      return [ lista2[0] ] + combinar(lista1, lista2[1:len(lista2)])

#-----------------------------------------------------------------------------

def hanoi(m):  #resuelve el juego de hanoi con m fichas (solo se puede mover a estacas consecutivas)
  return resolver_hanoi(set_hanoi(m), m)

#-----------------------------------------------------------------------------

def potencia(a,n):
  #ejercicio ilustrativo de potenciacion de orden O(log(n))
  print("llamado")
  if a == 0 and n <= 0:
    print("Indefinido")
  if a != 0 and n == 0:
    return 1
  if a != 0 and n < 0 :
    return 1 / potencia(a,-n)
  if n == 1:
    return a
  if n>1:
    y = potencia(a, n//2)
    if n%2 == 0:
      return y*y
    else:
      return a*y*y


#-----------------------------------------------------------------------------

def ordenar(lista):
  #ordena una lista con la estrategia dividir y conquistar
  print("llamado de ordenar")
  n = len(lista)
  if n < 2:
    return lista
  else:
    return combinar( ordenar(lista[0:n//2]), ordenar(lista[n//2:n]) )


def combinar(lista1,lista2):
  print("llamado de combinar")
  if len(lista1) == 0:
    return lista2
  elif len(lista2) == 0:
    return lista1
  else:
    if lista1[0]<lista2[0]:
      return [ lista1[0] ] + combinar(lista1[1:len(lista1)], lista2)
    else:
      return [ lista2[0] ] + combinar(lista1, lista2[1:len(lista2)])

#-----------------------------------------------------------------------------

def hanoi(m):  #resuelve el juego de hanoi con m fichas
  return resolver_hanoi(set_hanoi(m), m)

def set_hanoi(m):
  return [list(range(m,0,-1)),[],[]]

def resolver_hanoi(lista, m):
  if m == 1:
    return mov23(mov12(lista))
  else:
    return resolver_hanoi(mov23(resolver_hanoi_inv(mov12(resolver_hanoi(lista, m-1)), m-1)), m-1)

def resolver_hanoi_inv(lista, m):
  if m == 1:
    return mov21(mov32(lista))
  else:
    return resolver_hanoi_inv(mov21(resolver_hanoi(mov32(resolver_hanoi_inv(lista, m-1)), m-1)), m-1)

#---------------------------------------------------------------------------------------
#--------------------------movimientos empleados en hanoi-------------------------------
#---------------------------------------------------------------------------------------

def mov12(lista):
  print("movimiento de 1 a 2 en: ", lista)
  n = len(lista[0])
  if n > 0:
    lista[1] = lista[1] + [ lista[0][n-1] ]
    lista[0] = lista[0][0:n-1]
  return lista

def mov23(lista):
  print("movimiento de 2 a 3 en: ", lista)
  n = len(lista[1])
  if n > 0:
    lista[2] = lista[2] + [ lista[1][n-1] ]
    lista[1] = lista[1][0:n-1]
  return lista

def mov32(lista):
  print("movimiento de 3 a 2 en: ", lista)
  n = len(lista[2])
  if n > 0:
    lista[1] = lista[1] + [ lista[2][n-1] ]
    lista[2] = lista[2][0:n-1]
  return lista

def mov21(lista):
  print("movimiento de 2 a 1 en: ", lista)
  #print(lista)
  n = len(lista[1])
  if n > 0:
    lista[0] = lista[0] + [ lista[1][n-1] ]
    lista[1] = lista[1][0:n-1]
  return lista

#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------

def pos_max(lista):
  #encuentra la primera posicion del
  #elemento mayor de una lista no vacia
  #con la estrategia dividir y conquistar
  n = len(lista)
  if n == 1:
    return 0
  elif n == 0:
    return -1
  else:
    i = pos_max( lista[0:n//2] )
    j = pos_max( lista[n//2:n] )
    if lista[i] >= lista[n//2 + j]:
      return i
    else:
      return n//2 + j

#-----------------------------------------------------------------------------
#--------------------------- BACKTRACKING ------------------------------------
#-----------------------------------------------------------------------------

def permutaciones(lista):
  #devuelve listadas las permutaciones de una lista
  n = len(lista)
  if n < 2:
    return [lista]
  else:
    return [ [lista[i]] + y
             for i in range(n)
             for y in permutaciones(lista[0:i] + lista[i+1:n])
             ]

#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------

def recorrer(mapa):
  #responde si se puede ir de la esquina superior izquierda
  #a la esquina inferior derecha en un mapa rectangular
  #de 0s y 1s, pasando solo por 0s adyacentes
  n = len(mapa)
  if n > 0:
    m = len(mapa[0])
    if (mapa[0][0] != 0) or (mapa[n-1][m-1] != 0):
      return False
  else:
    return True
  visitados = []
  actual = [0, 0]
  return avanzar (actual, visitados , mapa, m-1, n-1)

def avanzar(actual, visitados, mapa, a, b):
  #avanza el algoritmo recorrer con estrategia backtracking
  print(actual)
  if actual == [a,b]:
    return True
  else:
    #consideramos las opciones en las que se puede avanzar
    opciones = [x for x in vecinos(mapa, actual) if x not in visitados]
    if len(opciones) == 0:
      #si no hay opciones
      print("recalculando")
    else:
      if len(opciones) > 1:
        #si hay mas de una opcion
        print("bifurcacion")
      for siguiente in opciones:
        #si hay opciones, avanzamos en cada una de ellas
        if avanzar(siguiente, visitados + [actual], mapa, a, b):
          return True
  return False

#---------------AUXILIARES recorrer-------------------------------------------

def vecinos(mapa, actual):
  #lista las posiciones vecinas libres
  respuesta = []
  if libre(mapa, derecha(actual)):
    respuesta = respuesta + [derecha(actual)]
  if libre(mapa, arriba(actual)):
    respuesta = respuesta + [arriba(actual)]
  if libre(mapa, izquierda(actual)):
    respuesta = respuesta + [izquierda(actual)]
  if libre(mapa, abajo(actual)):
    respuesta = respuesta + [abajo(actual)]
  return respuesta

# Mueven la posicion en un mapa en las cuatro direcciones.
def derecha(pos):
    return [pos[0], pos[1]+1]

def izquierda(pos):
    return [pos[0], pos[1]-1]

def arriba(pos):
    return [pos[0]-1, pos[1]]

def abajo(pos):
    return [pos[0]+1, pos[1]]

def libre(mapa, posicion):
  #responde la posicion esta libre en el mapa (i.e. hay un 0)
  n = len(mapa)
  if n > 0:
    m = len(mapa[0])
    if (posicion[0] in range(n)) and (posicion[1] in range(m)):
      return ( mapa[posicion[0]][posicion[1]] == 0 )
  else:
    return False

#-----------------------------------------------------------------------------

def crear_mapa(texto):
  #funcion auxiliar para crear un mapa a partir de un .txt
  archivo = open(texto)
  lista_de_filas = archivo.read().splitlines()
  archivo.close()
  i=0
  while i<len(lista_de_filas):
    lista_de_filas[i] = list(map(int, list(lista_de_filas[i])))
    i=i+1
  return lista_de_filas

#-----------------------------------------------------------------------------
