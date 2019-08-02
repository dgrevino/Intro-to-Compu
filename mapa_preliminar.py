#--------------------------------------------------------------
#----------------- TAD Mapa -----------------------------------
#--------------------------------------------------------------

class Mapa:
  def __init__(self, nombre_archivo):
    if es_mapa(nombre_archivo):
      self.matriz = listar_texto(nombre_archivo)
      self.alto = len(self.matriz)
      self.paredes = 0
      if(self.alto > 0):
        self.ancho = len(self.matriz[0])
        fila = 0
        while fila <  self.alto:
          col = 0
          while col < self.ancho:
            self.paredes = self.paredes + self.matriz[fila][col]
            col = col +1
          fila = fila +1
      else:
        self.ancho = 0

        
  def es_posicion_valida(self, pos):
    return ((0 <= pos[0] < self.alto) and (0 <= pos[1] < self.ancho))



  def posicion(self, pos):
    respuesta = 1
    if self.es_posicion_valida(pos):
      respuesta = self.matriz[pos[0]][pos[1]]
    return respuesta


  def alto(self):
    return self.alto
  
  def ancho(self):
    return self.ancho
  
  
  def cantidad_paredes(self):
    return self.paredes



  def corredor_horizontal_mas_largo(self):
    max_final = 0
    if(self.alto > 0):
      fila = 0
      while fila < self.alto:
        col = 0
        max_temporal = 0
        while col < self.ancho:
          if (self.matriz [fila][col] == 0):
            max_temporal = max_temporal + 1
            if max_temporal > max_final:
              max_final = max_temporal
          else:
            max_temporal = 0
          col = col +1
        fila = fila +1
    return max_final
  
  
  
  
  def densidad_arquitectonica(self):
    paredes = self.paredes
    total = self.alto* self.ancho
    if total == 0:
      densidad = 0
    else:
      densidad = paredes/total
    return densidad

  def alcanzar_con_mano_derecha(self, pos_inicial, pos_destino):
    pos_actual = pos_inicial
    print(pos_actual)
    respuesta = False
    #caso trivial
    if pos_inicial == pos_destino:
        respuesta = True

    #empiezo hacia la derecha, si se puede
    if (self.posicion(derecha(pos_inicial)) == 0 and
        (self.posicion(abajo(pos_inicial)) == 1 or
         self.posicion(derecha(abajo(pos_inicial))) == 1)):
        pos_anterior = pos_inicial
        pos_actual = derecha(pos_inicial)
        print(pos_actual, " empezando hacia la derecha")
        while pos_actual != pos_inicial and (respuesta == False):
            if pos_actual == pos_destino:
                respuesta = True
                print("Llegamos.")
            else:
                var_auxiliar = pos_actual
                pos_actual = avanzar(self, pos_anterior, pos_actual)
                print(pos_actual)
                pos_anterior = var_auxiliar
                
    #empiezo hacia arriba, si se puede
    if (self.posicion(arriba(pos_inicial)) == 0 and
        (self.posicion(derecha(pos_inicial)) == 1 or
         self.posicion(arriba(derecha(pos_inicial))) == 1)):
        pos_anterior = pos_inicial
        pos_actual = arriba(pos_inicial)
        print(pos_actual, " empezando hacia arriba")
        while pos_actual != pos_inicial and (respuesta == False):
            if pos_actual == pos_destino:
                respuesta = True
                print("Llegamos.")
            else:
                var_auxiliar = pos_actual
                pos_actual = avanzar(self, pos_anterior, pos_actual)
                print(pos_actual)
                pos_anterior = var_auxiliar

    #empiezo hacia la izquierda, si se puede
    if (self.posicion(izquierda(pos_inicial)) == 0 and
        (self.posicion(arriba(pos_inicial)) == 1 or
         self.posicion(izquierda(arriba(pos_inicial))) == 1)):
        pos_anterior = pos_inicial
        pos_actual = izquierda(pos_inicial)
        print(pos_actual, " empezando hacia la izquierda")
        while pos_actual != pos_inicial and (respuesta == False):
            if pos_actual == pos_destino:
                respuesta = True
                print("Llegamos.")
            else:
                var_auxiliar = pos_actual
                pos_actual = avanzar(self, pos_anterior, pos_actual)
                print(pos_actual)
                pos_anterior = var_auxiliar
                
    #empiezo hacia abajo, si se puede
    if (self.posicion(abajo(pos_inicial)) == 0 and
        (self.posicion(izquierda(pos_inicial)) == 1 or
         self.posicion(abajo(izquierda(pos_inicial))) == 1)):
        pos_anterior = pos_inicial
        pos_actual = abajo(pos_inicial)
        print(pos_actual, " empezando hacia abajo")
        while pos_actual != pos_inicial and (respuesta == False):
            if pos_actual == pos_destino:
                respuesta = True
            else:
                var_auxiliar = pos_actual
                pos_actual = avanzar(self, pos_anterior, pos_actual)
                print(pos_actual)
                pos_anterior = var_auxiliar
    return respuesta

#--------------------------------------------------------------
#--------------- Auxiliares -----------------------------------
#--------------------------------------------------------------
# Avanza una posicion siguiendo la regla de la mano derecha.

def avanzar(self, pos_anterior, pos_actual):

    #si miro hacia la derecha
    if pos_actual == derecha(pos_anterior):
        if self.posicion(abajo(pos_actual)) == 0:
            nueva_pos = abajo(pos_actual)
        else:
            if self.posicion(derecha(pos_actual)) == 0:
                nueva_pos = derecha(pos_actual)
            else:
                if self.posicion(arriba(pos_actual)) == 0:
                    nueva_pos = arriba(pos_actual)
                else:
                    nueva_pos = pos_anterior

    #si miro hacia arriba                
    if pos_actual == arriba(pos_anterior):
        if self.posicion(derecha(pos_actual)) == 0:
            nueva_pos = derecha(pos_actual)
        else:
            if self.posicion(arriba(pos_actual)) == 0:
                nueva_pos = arriba(pos_actual)
            else:
                if self.posicion(izquierda(pos_actual)) == 0:
                    nueva_pos = izquierda(pos_actual)
                else:
                    nueva_pos = pos_anterior

    #si miro hacia arriba                
    if pos_actual == izquierda(pos_anterior):
        if self.posicion(arriba(pos_actual)) == 0:
            nueva_pos = arriba(pos_actual)
        else:
            if self.posicion(izquierda(pos_actual)) == 0:
                nueva_pos = izquierda(pos_actual)
            else:
                if self.posicion(abajo(pos_actual)) == 0:
                    nueva_pos = abajo(pos_actual)
                else:
                    nueva_pos = pos_anterior

    #si miro hacia abajo
    if pos_actual == abajo(pos_anterior):
        if self.posicion(izquierda(pos_actual)) == 0:
            nueva_pos = izquierda(pos_actual)
        else:
            if self.posicion(abajo(pos_actual)) == 0:
                nueva_pos = abajo(pos_actual)
            else:
                if self.posicion(derecha(pos_actual)) == 0:
                    nueva_pos = derecha(pos_actual)
                else:
                    nueva_pos = pos_anterior
    return nueva_pos

#--------------------------------------------------------------
# Mueven la posicion en un mapa en la direccion indicada.

def derecha(pos):
    return [pos[0], pos[1]+1]

def izquierda(pos):
    return [pos[0], pos[1]-1]

def arriba(pos):
    return [pos[0]-1, pos[1]]

def abajo(pos):
    return [pos[0]+1, pos[1]]

#--------------------------------------------------------------
# Lee un archivo y lo convierte en una lista de las filas.

def listar_texto(texto):
  archivo = open(texto)
  lista_de_filas = archivo.read().splitlines()
  archivo.close()
  i=0
  while i<len(lista_de_filas):
    lista_de_filas[i] = list(map(int, list(lista_de_filas[i])))
    i=i+1
  return lista_de_filas

#--------------------------------------------------------------
#Devuelve si el texto input es un mapa o no.

def es_mapa(texto):
  #lee y lista el archivo
  archivo = open(texto)
  lista_de_filas = archivo.read().splitlines()
  archivo.close()
  alto_mapa = len(lista_de_filas)
  if alto_mapa == 0:
    #archivo vacio lo definimos como mapa
    return True    
  ancho_mapa = len(lista_de_filas[0])
  if ancho_mapa == 0:
    #archivos en blanco con algun ENTER no son mapas
    return False
  else:
    # Cuando el mapa no es vacio, verifica que todas las filas 
    #tengan el mismo ancho de la primera
    it_fila = 0
    while it_fila < alto_mapa:
      fila = lista_de_filas[it_fila]
      if len(fila)==ancho_mapa:
        col = 0
        #por cada fila, revisa que tengan solo 0s y 1s
        while col < ancho_mapa:
          if (fila[col]!='0' and fila[col]!='1'):
            return False
          col = col+1
      else:
          # como la fila no tiene el ancho del mapa, no es mapa.
          return False
      it_fila = it_fila+1
    return True
