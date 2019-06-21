#!/usr/bin/env python

import sys

#Integrantes del grupo 5: Bonardi, Grevino,  Robles.
# -------------------------------------------
#FUNCION 1
#--------------------------------------------
#Devuelve si el texto input es un mapa o no.

def es_mapa(texto):
  #lee y lista el archivo
  archivo = open(texto)
  lista_de_filas = archivo.read().splitlines()
  archivo.close()
  alto_mapa = len(lista_de_filas)
  respuesta = True

  #archivo vacio lo definimos como mapa
  if alto_mapa > 0:
    ancho_mapa = len(lista_de_filas[0])
    if ancho_mapa == 0:
      #archivos en blanco con algun ENTER no son mapas
      respuesta = False
    else:
      #Cuando el mapa no es vacio, verifica que todas las filas 
      #tengan el mismo ancho que la primera
      it_fila = 0
      while it_fila < alto_mapa:
        fila = lista_de_filas[it_fila]
        if len(fila) == ancho_mapa:
          col = 0
          #en cada fila revisa que haya solamente 0s o 1s
          while col < ancho_mapa:
            if (fila[col]!='0' and fila[col]!='1'):
              respuesta = False
            col = col+1
        else:
          #como la fila no tiene el ancho del mapa, no es mapa.
          respuesta = False
        it_fila = it_fila+1
  return respuesta


if sys.argv[1] == "es_mapa":
  texto = str(sys.argv[2])
  if es_mapa(texto):
    print('Si, es un mapa.')
  else:
    print('El archivo no representa un mapa: no es rectangular o tiene caracteres distintos de 0 y 1.')
 
   
# -------------------------------------------
# -------------------------------------------
#FUNCION AUXILIAR
# Lee un archivo y lo convierte en una lista de las filas.

texto = str(sys.argv[2])
def listar_texto(texto):
  archivo = open(texto)
  lista_de_filas = archivo.read().splitlines()
  archivo.close()
  i=0
  while i<len(lista_de_filas):
    lista_de_filas[i] = list(map(int, list(lista_de_filas[i])))
    i=i+1
  return lista_de_filas

# -------------------------------------------
# -------------------------------------------


#FUNCION 2
#-------------------------------------------
#Devuelve la cantidad de paredes en un mapa.

def cantidad_paredes(texto):
    # recorre todas las posiciones del mapa y suma su contenido
    # ya que 1 es pared y 0 no lo es
    mapa = listar_texto(texto)
    alto_mapa = len(mapa)
    cantidad_de_paredes = 0
    if alto_mapa>0:
      ancho_mapa = len(mapa[0])
      fila = 0
      while fila <  alto_mapa:
        col = 0
        while col < ancho_mapa:
          cantidad_de_paredes = cantidad_de_paredes + mapa[fila][col]
          col = col +1
        fila = fila +1
    return cantidad_de_paredes


if sys.argv[1]== "cantidad_paredes":
  texto = str(sys.argv[2])
  if es_mapa(texto):
     cant_paredes = cantidad_paredes(texto)
     print('El mapa tiene', cant_paredes, 'paredes.')
  else:
     print('El archivo no representa un mapa: no es rectangular o tiene caracteres distintos de 0 y 1.')


# -------------------------------------------
# -------------------------------------------

#FUNCION 3
#-------------------------------------------
# Devuelve la cantidad de espacios vacíos (0's rodeados completamente por 1's)en un mapa.

def espacios_rodeados(texto):
    mapa = listar_texto(texto)
    alto_mapa = len(mapa)
    espacios_rodeados = 0
    # si el mapa es vacio, no hace nada y se devuelve 0
    if alto_mapa>0:
      ancho_mapa = len(mapa[0])
      fila=1
      while fila < alto_mapa -1:
        col=1
        while col < ancho_mapa -1:
          if esta_rodeado(mapa, fila, col):
            espacios_rodeados = espacios_rodeados + 1
          col=col+1
        fila=fila+1
    return espacios_rodeados

   
def esta_rodeado(mapa, fila, col):
    return (mapa[fila-1][col-1]==1 and mapa[fila-1][col]==1 and mapa[fila-1][col+1]==1 and #recorro columna izquierda
            mapa[fila][col-1]==1 and mapa[fila][col]==0 and mapa[fila][col+1]==1 and #recorro columna central
            mapa[fila+1][col-1]==1 and mapa[fila+1][col]==1 and mapa[fila+1][col+1]==1) #recorro columna derecha



if sys.argv[1]== "espacios_rodeados":
  texto = str(sys.argv[2])
  if es_mapa(texto):
    resultado = espacios_rodeados (texto)
    print('El mapa tiene', resultado, 'huecos rodeados de paredes.')
  else:
    print('El archivo no representa un mapa: no es rectangular o tiene caracteres distintos de 0 y 1.')



# -------------------------------------------
# -------------------------------------------
#FUNCION 4
#--------------------------------------------
# Devuelve las dimensiones de un mapa: alto (numero de filas) y ancho (numero de columnas).

def dimensiones(texto):
    mapa = listar_texto(texto)
    alto_mapa = len(mapa)
    ancho_mapa = 0
    if alto_mapa>0:
      ancho_mapa=len(mapa[0])
    return ancho_mapa,  alto_mapa

if sys.argv[1]== "dimensiones":
  texto = str(sys.argv[2])
  if es_mapa(texto):
    ancho = dimensiones (texto)[0]
    alto = dimensiones (texto)[1]
    print('El mapa tiene', ancho, 'cuadrados de ancho y', alto, 'de alto.')
  else:
    print('El archivo no representa un mapa: no es rectangular o tiene caracteres distintos de 0 y 1.')


# -------------------------------------------
# -------------------------------------------

#FUNCION 5
#--------------------------------------------
# Devuelve la densidad arquitectonica de un mapa, definida como #paredes/#espacios total

def densidad(texto):
  cant_paredes = cantidad_paredes(texto)
  cant_espacios_total = dimensiones(texto)[0]* dimensiones (texto)[1]
  if cant_espacios_total == 0:
    den_arq = 0
  else:
    den_arq = cant_paredes/cant_espacios_total
  return den_arq

if sys.argv[1]== "densidad":
  texto = str(sys.argv[2])
  if es_mapa(texto):
    densidad_arq = densidad(texto)
    print('La densidad arquitectonica es de', densidad_arq)
  else:
    print('El archivo no representa un mapa: no es rectangular o tiene caracteres distintos de 0 y 1.')


# -------------------------------------------
# -------------------------------------------
#FUNCION 6
#--------------------------------------------
# Devuelve la secuencia horizontal mas larga de espacios vacios (0's) dentro de un mapa.

def corredor_horizontal_mas_largo(texto):
    mapa = listar_texto(texto)
    alto_mapa = len(mapa)
    max_final = 0

    if alto_mapa>0:
        ancho_mapa = len(mapa[0])
        fila = 0
        while fila <  alto_mapa:
            col = 0
            max_temporal = 0
            while col < ancho_mapa:
                if ( mapa[fila][col] == 0):
                    max_temporal = max_temporal + 1
                    if max_temporal > max_final:
                        max_final = max_temporal
                else:
                    max_temporal = 0
                col = col +1
            fila = fila +1
    return max_final


if sys.argv[1]== "corredor_horizontal_mas_largo":
    texto = str(sys.argv[2])
    if es_mapa(texto):
        resultado = corredor_horizontal_mas_largo(texto)
        print('El corredor horizontal mas largo tiene longitud', resultado)
    else:
        print('El archivo no representa un mapa: no es rectangular o tiene caracteres distintos de 0 y 1.')
   

# -------------------------------------------
