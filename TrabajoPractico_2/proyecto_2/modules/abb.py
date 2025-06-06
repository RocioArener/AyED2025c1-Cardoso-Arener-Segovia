class NodoArbol: # Clase que representa un nodo en el árbol binario de búsqueda balanceado
    def __init__(self,clave,valor):
        self.clave = clave
        self.cargaUtil = valor
        self.hijoIzquierdo = None
        self.hijoDerecho = None
        self.padre = None
        self.altura = 1
        self.factorEquilibrio = 0
    
    def tieneHijoIzquierdo(self):
        return self.hijoIzquierdo

    def tieneHijoDerecho(self):
        return self.hijoDerecho

    def esHijoIzquierdo(self):
        return self.padre and self.padre.hijoIzquierdo == self

    def esHijoDerecho(self):
        return self.padre and self.padre.hijoDerecho == self

    def esRaiz(self):
        return not self.padre

    def esHoja(self):
        return not (self.hijoDerecho or self.hijoIzquierdo)

    def tieneAlgunHijo(self):
        return self.hijoDerecho or self.hijoIzquierdo

    def tieneAmbosHijos(self):
        return self.hijoDerecho and self.hijoIzquierdo

    def esRaiz(self): # Método que verifica si el nodo es la raíz del árbol
        return self.padre is None    

    def __str__(self): # Método que devuelve una representación en cadena del nodo
        izq = str(self.hijoIzquierdo) if self.hijoIzquierdo else ""
        der = str(self.hijoDerecho) if self.hijoDerecho else ""
        return f"{izq}({self.clave}: {self.cargaUtil}){der}"
    
    def reemplazarDatoDeNodo(self,clave,valor,hizq,hder):
        self.clave = clave
        self.cargaUtil = valor
        self.hijoIzquierdo = hizq
        self.hijoDerecho = hder
        if self.tieneHijoIzquierdo():
            self.hijoIzquierdo.padre = self
        if self.tieneHijoDerecho():
            self.hijoDerecho.padre = self

class ABB: # Clase que representa un árbol binario de búsqueda balanceado (AVL)
    def __init__(self):
        self.raiz = None
        self.tamano = 0
    
    def longitud(self):
        return self.tamano

    def __len__(self):
        return self.tamano

    def __str__ (self):
        if self.raiz is None:
            return "Árbol vacío"
        return str(self.raiz)

    def agregar(self, clave, valor): # Método para agregar un nuevo nodo al árbol
        self.raiz = self._agregar(self.raiz, clave, valor) 

    def _agregar(self, nodo, clave, valor): # Método recursivo para agregar un nuevo nodo al árbol
        if nodo is None:
            nodo = NodoArbol(clave, valor)
            self.tamano += 1
            return nodo
        elif clave < nodo.clave:
            nodo.hijoIzquierdo = self._agregar(nodo.hijoIzquierdo, clave, valor)
            nodo.hijoIzquierdo.padre = nodo
        else:
            nodo.hijoDerecho = self._agregar(nodo.hijoDerecho, clave, valor)
            nodo.hijoDerecho.padre = nodo
        return self.balancear(nodo)
    

    def obtener(self,clave): #Metodo para obtener el valor asociado a una clave en el árbol
       return self._obtener(clave,self.raiz)

    def _obtener(self,clave,nodo): # Método recursivo para obtener el valor asociado a una clave en el árbol
       if not nodo:
           return None
       elif nodo.clave == clave:
           return nodo.cargaUtil
       elif clave < nodo.clave: #si la clave es menor, le pasa a _obtener los nuevos parametros, siendo la clave y el hijo izquierdo del nodo actual
           return self._obtener(clave,nodo.hijoIzquierdo) 
       else: # lo mismo que arriba, pero con el hijo derecho
           return self._obtener(clave,nodo.hijoDerecho)


    def balancear(self, nodo): # Método para balancear el árbol después de agregar un nuevo nodo
        if nodo is None:
            return nodo
        nodo.altura = 1 + max(self.altura(nodo.hijoIzquierdo), self.altura(nodo.hijoDerecho)) #se actualiza la altura del nodo
        nodo.factorEquilibrio = self.altura(nodo.hijoIzquierdo) - self.altura(nodo.hijoDerecho) #se calcula el factor de equilibrio del nodo, siendo la diferencia de alturas entre sus hijos izquierdo y derecho

        if nodo.factorEquilibrio > 1:
            if nodo.hijoIzquierdo and nodo.hijoIzquierdo.factorEquilibrio < 0:
                nodo.hijoIzquierdo = self.rotarIzquierda(nodo.hijoIzquierdo) 
            return self.rotarDerecha(nodo)
        #si el factor de equilibrio es mayor a 1, significa que el subárbol izquierdo es más alto que el derecho
        #si tiene un hijo izquierdo y este tiene equilibrio negativo, se rota a la izquierda
        #si no, se rota a la derecha
        if nodo.factorEquilibrio < -1:
            if nodo.hijoDerecho and nodo.hijoDerecho.factorEquilibrio > 0:
                nodo.hijoDerecho = self.rotarDerecha(nodo.hijoDerecho)
            return self.rotarIzquierda(nodo)
        #si el factor de equilibrio es menor a -1, significa que el subárbol derecho es más alto que el izquierdo
        #si tiene un hijo derecho y este tiene equilibrio positivo, se rota a la derecha
        #si no, se rota a la izquierda
        return nodo #si esta balanceado, se retorna el nodo sin cambios

    
    def rotarIzquierda(self, nodo):
        nuevaraiz = nodo.hijoDerecho 
        nodo.hijoDerecho = nuevaraiz.hijoIzquierdo
        nuevaraiz.hijoIzquierdo = nodo
       
        nodo.altura = 1 + max(self.altura(nodo.hijoIzquierdo), self.altura(nodo.hijoDerecho))
        nodo.equilibrio = self.altura(nodo.hijoIzquierdo) - self.altura(nodo.hijoDerecho)

        nuevaraiz.altura = 1 + max(self.altura(nuevaraiz.hijoIzquierdo), self.altura(nuevaraiz.hijoDerecho))
        nuevaraiz.equilibrio = self.altura(nuevaraiz.hijoIzquierdo) - self.altura(nuevaraiz.hijoDerecho)
        
        return nuevaraiz 
       
    def rotarDerecha(self, nodo):
        nuevaraiz = nodo.hijoIzquierdo 
        nodo.hijoIzquierdo = nuevaraiz.hijoDerecho 
        nuevaraiz.hijoDerecho = nodo
        
        nodo.altura = 1 + max(self.altura(nodo.hijoIzquierdo), self.altura(nodo.hijoDerecho))
        nodo.equilibrio = self.altura(nodo.hijoIzquierdo) - self.altura(nodo.hijoDerecho) 
        nuevaraiz.altura = 1 + max(self.altura(nuevaraiz.hijoIzquierdo), self.altura(nuevaraiz.hijoDerecho)) #se actualiza la altura de la nueva raíz, siendo 1 + la máxima altura de sus hijos
        nuevaraiz.equilibrio = self.altura(nuevaraiz.hijoIzquierdo) - self.altura(nuevaraiz.hijoDerecho) #se actualiza el factor de equilibrio de la nueva raiz, siendo la diferencia de alturas entre sus hijos izquierdo y derecho

        return nuevaraiz 
    

    def altura(self, nodo=None):
        if nodo is None:
            return 0
        return 1 + max(self.altura(nodo.hijoIzquierdo), self.altura(nodo.hijoDerecho))

    def __contains__(self,clave):
        if self._obtener(clave,self.raiz):
            return True
        else:
            return False
        
    def eliminar(self, clave): # Método para eliminar un nodo del árbol
        if self.tamano > 1:
            nodoAEliminar = self._obtener(clave, self.raiz)
            if nodoAEliminar:
                self.remover(nodoAEliminar)
                self.tamano -= 1
            else:
                raise KeyError('Error, la clave no está en el árbol')
        else:
            self.raiz = None
            self.tamano = 0

    def __delitem__(self,clave):
        self.eliminar(clave)

    
    def empalmar(self): # Conecta al abuelo con el nieto 
       if self.esHoja(): 
           if self.esHijoIzquierdo():
                  self.padre.hijoIzquierdo = None #se fija si el nodo actual es hijo izquierdo del padre
           else:
                  self.padre.hijoDerecho = None #se fija si el nodo actual es hijo derecho del padre
            #elimiina la conexion del padre al hijo      
       elif self.tieneAlgunHijo():
           if self.tieneHijoIzquierdo():
                  if self.esHijoIzquierdo():
                     self.padre.hijoIzquierdo = self.hijoIzquierdo
                  else:
                     self.padre.hijoDerecho = self.hijoIzquierdo
                  self.hijoIzquierdo.padre = self.padre
           else:
                  if self.esHijoIzquierdo():
                     self.padre.hijoIzquierdo = self.hijoDerecho
                  else:
                     self.padre.hijoDerecho = self.hijoDerecho
                  self.hijoDerecho.padre = self.padre

    def encontrarSucesor(self):
      suc = None
      if self.tieneHijoDerecho():
          suc = self.hijoDerecho.encontrarMin()
      else:
          if self.padre:
                 if self.esHijoIzquierdo():
                     suc = self.padre
                 else:
                     self.padre.hijoDerecho = None
                     suc = self.padre.encontrarSucesor()
                     self.padre.hijoDerecho = self
      return suc

    def encontrarMin(self):
      actual = self
      while actual.tieneHijoIzquierdo():
          actual = actual.hijoIzquierdo
      return actual

    
    
    def remover(self,nodoActual):
         if nodoActual.esHoja(): #no tiene hijos
           if nodoActual == nodoActual.padre.hijoIzquierdo:
               nodoActual.padre.hijoIzquierdo = None
           else:
               nodoActual.padre.hijoDerecho = None

         elif nodoActual.tieneAmbosHijos(): #si tiene ambos hijos
           suc = nodoActual.encontrarSucesor()
           suc.empalmar()
           nodoActual.clave = suc.clave
           nodoActual.cargaUtil = suc.cargaUtil

         else: # este nodo tiene un (1) hijo
           if nodoActual.tieneHijoIzquierdo():
             if nodoActual.esHijoIzquierdo():
                 nodoActual.hijoIzquierdo.padre = nodoActual.padre
                 nodoActual.padre.hijoIzquierdo = nodoActual.hijoIzquierdo
             elif nodoActual.esHijoDerecho():
                 nodoActual.hijoIzquierdo.padre = nodoActual.padre
                 nodoActual.padre.hijoDerecho = nodoActual.hijoIzquierdo
             else:
                 nodoActual.reemplazarDatoDeNodo(nodoActual.hijoIzquierdo.clave,
                                    nodoActual.hijoIzquierdo.cargaUtil,
                                    nodoActual.hijoIzquierdo.hijoIzquierdo,
                                    nodoActual.hijoIzquierdo.hijoDerecho)
           else:
             if nodoActual.esHijoIzquierdo():
                 nodoActual.hijoDerecho.padre = nodoActual.padre
                 nodoActual.padre.hijoIzquierdo = nodoActual.hijoDerecho
             elif nodoActual.esHijoDerecho():
                 nodoActual.hijoDerecho.padre = nodoActual.padre
                 nodoActual.padre.hijoDerecho = nodoActual.hijoDerecho
             else:
                 nodoActual.reemplazarDatoDeNodo(nodoActual.hijoDerecho.clave,
                                    nodoActual.hijoDerecho.cargaUtil,
                                    nodoActual.hijoDerecho.hijoIzquierdo,
                                    nodoActual.hijoDerecho.hijoDerecho)



if  __name__ == "__main__":
    # Ejemplo de uso del NodoArbol
    arbol= ABB()
    arbol.agregar(5, "valor raiz")  
    arbol.agregar(3, "valor 3")
    arbol.agregar(7, "valor 7")
    arbol.agregar(2, "valor 2")
    arbol.agregar(4, "valor 4")
    arbol.agregar(6, "valor 6")
    arbol.agregar(8, "valor 8")
    arbol.agregar(100, "valor 100")
    arbol.agregar(1, "valor 1")
    arbol.agregar(10, "valor")
    print(arbol)  # Debería imprimir "valor raiz"

