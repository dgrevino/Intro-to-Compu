def listartexto(filepath): #funcion auxiliar que toma un texto formado por numeros
                           #y devuelve una lista formada por por sus filas, a su vez listadas

  lines_list = open(filepath).read().splitlines() #lista cuyos elementos son las filas del archivo txt input

  return [list(map(int, list(sub))) for sub in lines_list] #listamos los elementos de cada entrada y los convertimos en enteros



def es_mapa(texto): #funcion que responde si el texto input es un mapa,
                    #esto es, un arreglo cuadrado de 0's y 1's

  lista = open(texto).read().splitlines() #lista cuyos elementos son las filas del archivo txt input
  no = 'El archivo no representa un mapa: no es rectangular o tiene caracteres distintos de 0 y 1.'
  si = 'Si, es un mapa.'  #abreviamos por "no" y "si" las dos respuestas posibles

  m = len(lista) #cantidad de filas del texto input
  
  if m==0:
    print(si) #consideramos mapa al mapa vacio
  
  else:
    n = len(lista[0]) #elegimos como longitud de referencia a la de la primera fila
    
    
    B=True #booleano auxiliar para salir de los dos ciclos
    for k in range(m):
        sub = lista[k] #tomamos la fila k-esima
        if len(sub)==n and B==True: #aqui chequeamos que la fila tenga la longitud de referencia
          for i in range(n):
            if sub[i]!='0' and sub[i]!='1':  #aqui chequeamos que todos los elementos sean 0 o 1
              B=False   #truco para salir de los dos ciclos
              print(no)
              break
        else:
          if B==True:
            print(no) #si falla alguna condicion, respondemos que no es mapa
            break
        if k==m-1 and B==True:
          print(si) #si tiene todas las condiciones, respondemos que es un mapa
    


def cantidad_paredes(texto): #funcion que cuenta la cantidad de paredes (1's) del texto input

  lista = listartexto(texto) #convertimos el texto input en una lista de listas de enteros
  m = len(lista) #cantidad de filas del texto input
  s = 0 #variable en la cual sumamos la cantidad de paredes

  if m>0: #contemplamos el caso m=0 del mapa vacio
    n = len(lista[0]) #cantidad de cuadrados en cada fila
    for i in range(m):
      for j in range(n):
        s = s + lista[i][j]
  print('El mapa tiene', s, 'paredes.')



def cantidad_paredes_aux(lista):
  #funcion auxiliar que DEVUELVE la cantidad de paredes
                                 #de una lista obtenida a partir de un texto input
                                 #sera usada en las funciones espacios_rodeados y densidad
  
  m = len(lista) #cantidad de filas del texto input
  s = 0 #variable en la cual sumamos la cantidad de paredes

  if m>0: #contemplamos el caso m=0 del mapa vacio
    n = len(lista[0]) #cantidad de cuadrados en cada fila
    for i in range(m):
      for j in range(n):
        s = s + lista[i][j]
  return s



def espacios_rodeados(texto): #funcion que responde la cantidad de huecos
                              #(0's rodeados de 1's) del texto input
  
  lista = listartexto(texto) #convertimos el texto input en una lista de listas de enteros
  m = len(lista) #cantidad de filas del texto input
  s = 0 #variable en la cual sumamos la cantidad de espacios rodeados

  if m>0: #contemplamos el caso m=0 del mapa vacio
    n = len(lista[0]) #cantidad de cuadrados en cada fila
    lista_aux = listartexto(texto) #lista auxiliar de listas de 0's y 1's, que sera
                                   #llenada con 1 en la entrada i-j si y solo si 
                                   #lista tiene un hueco en esa entrada
    
    for i in range(m): #agregamos columnas de 1's a los lados del texto
      lista[i] = [1] + lista[i] + [1]

    lista = [[1]] + lista + [[1]]  
    for j in range(n+1):        #agregamos filas de 1's arriba y abajo del texto
      lista[0] = lista[0] + [1]
      lista[m+1] = lista[m+1] + [1]

    #una vez rodeado el texto de 1's podemos proceder de la misma manera
    #sobre todas las entradas para verificar si es o no un hueco
    for i in range(m):
      for j in range(n):
        if lista[i][j]==1 and lista[i+1][j]==1 and lista[i+2][j]==1 and lista[i][j+1]==1 and lista[i+1][j+1]==0 and lista[i+2][j+1]==1 and lista[i][j+2]==1 and lista[i+1][j+2]==1 and lista[i+2][j+2]==1:
          lista_aux[i][j] = 1
        else:
          lista_aux[i][j] = 0
    s = cantidad_paredes_aux(lista_aux) #calculamos la cantidad de huecos
                                        #como la cantidad de paredes
                                        #de la lista auxiliar
  print('El mapa tiene', s, 'huecos rodeados de paredes.')



def dimensiones(texto):

  lista = listartexto(texto) #convertimos el texto input en una lista de listas de enteros
  m = len(lista) #cantidad de filas del texto input
  n = 0 #contemplanos el caso del mapa vacio

  if m>0:
    n=len(lista[0])

  print('El mapa tiene', n, 'cuadrados de ancho y', m, 'de alto.')

  

def corredor_horizontal_mas_largo(texto):
  lista = listartexto(texto) #convertimos el texto input en una lista de listas de enteros
  m = len(lista) #cantidad de filas del texto input
  s = 0 #contemplanos el caso del mapa vacio

  if m>0:
    n = len(lista[0])
    
    for i in range(m):      #contamos la cantidad de 0's horizontales
      contador = 0
      for j in range(n):    #a partir de la entrada i-j
        if lista[i][j]==0:
          contador = contador +1
          if contador > s:
            s = contador
        else:
           contador = 0

  print('El corredor horizontal mas largo tiene longitud', s)

  

def densidad(texto):

  lista = listartexto(texto) #convertimos el texto input en una lista de listas de enteros
  m = len(lista) #cantidad de filas del texto input
  s = 0 #contemplanos el caso del mapa vacio

  if m>0:
    n=len(lista[0])
    s=cantidad_paredes_aux(lista)/(m*n)

  print('La densidad arquitectonica es de', s)    



