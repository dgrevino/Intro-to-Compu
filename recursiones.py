
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
  n = len(lista[1])
  if n > 0:
    lista[0] = lista[0] + [ lista[1][n-1] ]
    lista[1] = lista[1][0:n-1]
  return lista

#-----------------------------------------------------------------------------

