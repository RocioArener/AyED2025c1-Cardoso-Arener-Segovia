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
    
    def longitud(self): # Método que devuelve el tamaño del árbol
        return self.tamano

    def __len__(self): # Método que devuelve el tamaño del árbol creado para el test
        return self.tamano

    def __str__ (self):
        if self.raiz is None:
            return "Árbol vacío"
        return str(self.raiz)

    def agregar(self, clave, valor): #Método para agregar un nuevo nodo al árbol.
        self.raiz = self._agregar(self.raiz, clave, valor) 

    def _agregar(self, nodo, clave, valor): #Método recursivo para agregar un nuevo nodo al árbol.
        if nodo is None: #crea un nuevo nodo si no hay ninguno, es decir cuando llega al lugar correcto
            nodo = NodoArbol(clave, valor)
            self.tamano += 1
            return nodo
        elif clave < nodo.clave: #si la clave es menor, pasa a _agregar los nuevos parametros, siendo la clave y 
                                 #el hijo izquierdo del nodo actual
            nodo.hijoIzquierdo = self._agregar(nodo.hijoIzquierdo, clave, valor)
            nodo.hijoIzquierdo.padre = nodo #redirecciona el pointer
        else: #si la clave es mayor o igual, le pasa a _agregar los nuevos parametros, 
              #siendo la clave y el hijo derecho del nodo actual
            nodo.hijoDerecho = self._agregar(nodo.hijoDerecho, clave, valor)
            nodo.hijoDerecho.padre = nodo #redirecciona el pointer 
        return self.balancear(nodo)
    

    def obtener(self,clave): #Metodo para obtener el valor asociado a una clave en el árbol
        nodo = self._obtenerNodo(clave, self.raiz) #busca el nodo
        if nodo is None:
            raise Exception(f"Clave {clave} no encontrada en el árbol")
        return nodo.cargaUtil #devuelve la carga util del nodo encontrado
    

    def _obtener(self,clave,nodo): # Método recursivo para obtener el valor asociado (carga util) a una clave en el árbol
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
        nuevaraiz = nodo.hijoDerecho # asigna como nueva raiz al hijo derecho del nodo
        nodo.hijoDerecho = nuevaraiz.hijoIzquierdo # asigna el hijo izquierdo del nuevo nodo como hijo derecho del nodo actual
        nuevaraiz.hijoIzquierdo = nodo # asigna el nodo actual como hijo izquierdo del nuevo nodo
        # Actualiza la altura y factor de equilibrio del nodo actual 
        nodo.altura = 1 + max(self.altura(nodo.hijoIzquierdo), self.altura(nodo.hijoDerecho))
        nodo.factorEquilibrio = self.altura(nodo.hijoIzquierdo) - self.altura(nodo.hijoDerecho)
        # Actualiza la altura y factor de equilibrio de la nueva raíz
        nuevaraiz.altura = 1 + max(self.altura(nuevaraiz.hijoIzquierdo), self.altura(nuevaraiz.hijoDerecho))
        nuevaraiz.factorEquilibrio = self.altura(nuevaraiz.hijoIzquierdo) - self.altura(nuevaraiz.hijoDerecho)
        
        return nuevaraiz 
       
    def rotarDerecha(self, nodo):
        nuevaraiz = nodo.hijoIzquierdo # asigna como nueva raiz al hijo izquierdo del nodo
        nodo.hijoIzquierdo = nuevaraiz.hijoDerecho # asigna el hijo derecho del nuevo nodo como hijo izquierdo del nodo actual
        nuevaraiz.hijoDerecho = nodo # asigna el nodo actual como hijo derecho del nuevo nodo
        # Actualiza la altura y factor de equilibrio del nodo actual
        nodo.altura = 1 + max(self.altura(nodo.hijoIzquierdo), self.altura(nodo.hijoDerecho)) 
        nodo.factorEquilibrio = self.altura(nodo.hijoIzquierdo) - self.altura(nodo.hijoDerecho)
        # Actualiza la altura y factor de equilibrio de la nueva raíz
        nuevaraiz.altura = 1 + max(self.altura(nuevaraiz.hijoIzquierdo), self.altura(nuevaraiz.hijoDerecho))
        nuevaraiz.factorEquilibrio = self.altura(nuevaraiz.hijoIzquierdo) - self.altura(nuevaraiz.hijoDerecho)
        return nuevaraiz 
    

    def altura(self, nodo=None): # Método para calcular la altura del árbol
        if nodo is None:
            return 0
        return 1 + max(self.altura(nodo.hijoIzquierdo), self.altura(nodo.hijoDerecho))


    def eliminar(self, clave): # Método para eliminar un nodo del árbol
        if self.tamano > 1: # si el árbol tiene más de un nodo, se procede a eliminar
            nodoAEliminar = self._obtenerNodo(clave, self.raiz) # busca el nodo a eliminar con la calve ingresada
            if nodoAEliminar: # si el nodo a eliminar existe, se procede a eliminarlo
                self.raiz = self._remover(self.raiz, clave)
                self.tamano -= 1
            else: # si el nodo a eliminar no existe, se lanza una excepción
                raise KeyError('Error, la clave no está en el árbol')
        elif self.tamano==1 and self.raiz.clave==clave: # si el arbol tiene un solo nodo, lo elimina directamente (es la raiz)
            self.raiz = None
            self.tamano = 0
        else:
            raise KeyError('Error, la clave no está en el árbol')
    
    def encontrarMin(self): # Método para encontrar el nodo con la clave mínima en el árbol
      actual = self
      while actual.tieneHijoIzquierdo():
          actual = actual.hijoIzquierdo
      return actual
    
    def _encontrarMin(self, nodo): # Método recursivo para encontrar el nodo con la clave mínima en un subárbol
        while nodo.hijoIzquierdo:
            nodo = nodo.hijoIzquierdo
        return nodo

    def _obtenerNodo(self, clave, nodo): # Método recursivo para obtener el nodo con la clave especificada
        if not nodo:
            return None
        elif nodo.clave == clave:
            return nodo
        elif clave < nodo.clave: # si la clave es menor, busca en el hijo izquierdo y le pasa a _obtenerNodo los nuevos parametros.
            return self._obtenerNodo(clave, nodo.hijoIzquierdo) 
        else: # si la clave es mayor, busca en el hijo derecho y le pasa a _obtenerNodo los nuevos parametros.
            return self._obtenerNodo(clave, nodo.hijoDerecho) 
        
    def _remover(self, nodo, clave): # Método recursivo para eliminar un nodo con la clave especificada
        if not nodo:
            return nodo
        
        # Si la clave es menor, se busca en el subárbol izquierdo el nodo a eliminar
        if clave < nodo.clave:
            nodo.hijoIzquierdo = self._remover(nodo.hijoIzquierdo, clave)
            if nodo.hijoIzquierdo:
                nodo.hijoIzquierdo.padre = nodo
        # Si la clave es mayor, se busca en el subárbol derecho el nodo a eliminar
        elif clave > nodo.clave:
            nodo.hijoDerecho = self._remover(nodo.hijoDerecho, clave)
            if nodo.hijoDerecho:
                nodo.hijoDerecho.padre = nodo

        else: #cuando se encuentra el nodo a eliminar (nodo.clave == clave)
            # Caso 1: Nodo hoja
            if not nodo.hijoIzquierdo and not nodo.hijoDerecho:
                return None
            # Caso 2: Nodo con un hijo
            elif not nodo.hijoIzquierdo: # si tiene hijo derecho, lo conecta con el padre del nodo a eliminar(actual)
                temp = nodo.hijoDerecho
                temp.padre = nodo.padre
                return temp # nodo que queda en el lugar del nodo eliminado
            elif not nodo.hijoDerecho: # si tiene hijo izquierdo, lo conecta con el padre del nodo a eliminar(actual)
                temp = nodo.hijoIzquierdo
                temp.padre = nodo.padre
                return temp # nodo que queda en el lugar del nodo eliminado
            # Caso 3: Nodo con dos hijos
            else: # reemplaza el valor del nodo y elimina al sucesor
                sucesor = self._encontrarMin(nodo.hijoDerecho)
                # Encuentra el sucesor (el nodo con la clave mínima en el subárbol derecho)
                # Reemplaza la clave y  la carga util del nodo a eliminar con la del sucesor
                nodo.clave = sucesor.clave 
                nodo.cargaUtil = sucesor.cargaUtil
                nodo.hijoDerecho = self._remover(nodo.hijoDerecho, sucesor.clave) # elimina el sucesor del subárbol derecho
                if nodo.hijoDerecho: #conecta al hijo derecho con el padre del nodo actual
                    nodo.hijoDerecho.padre = nodo
        
        # Actualizar altura y balancear
        nodo.altura = 1 + max(self.altura(nodo.hijoIzquierdo), self.altura(nodo.hijoDerecho))
        return self.balancear(nodo)
    
    def _inorden(self, nodo): # usamos yield porque necesitamos recorrer toda la lista, es mas eficiente y devuelve uno por uno los elementos
        if nodo is not None:
            yield from self._inorden(nodo.hijoIzquierdo)
            yield (nodo.clave, nodo.cargaUtil)
            yield from self._inorden(nodo.hijoDerecho)

    # funciones creadas para el test que verifica el correcto funcionamiento del árbol(sobrecarga de metodos)
    def __iter__(self):
        yield from self._inorden(self.raiz)

    def __setitem__(self, clave, valor):
        self.agregar(clave, valor)

    def __getitem__(self, clave):
        return self.obtener(clave)

    def __delitem__(self, clave):
        self.eliminar(clave)

    def __contains__(self,clave):
        if self._obtener(clave,self.raiz):
            return True
        else:
            return False



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

