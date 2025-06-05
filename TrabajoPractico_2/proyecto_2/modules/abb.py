class NodoArbol: # Clase que representa un nodo en el árbol binario de búsqueda balanceado
    def __init__(self,clave,valor):
        self.clave = clave
        self.valor = valor
        self.hijoIzquierdo = None
        self.hijoDerecho = None
        self.padre = None
        self.altura = 1
        self.factorEquilibrio = 0

    def esRaiz(self): # Método que verifica si el nodo es la raíz del árbol
        return self.padre is None    

    def __str__(self): # Método que devuelve una representación en cadena del nodo
        izq = str(self.hijoIzquierdo) if self.hijoIzquierdo else ""
        der = str(self.hijoDerecho) if self.hijoDerecho else ""
        return f"{izq}({self.clave}: {self.valor}){der}"

class ABB: # Clase que representa un árbol binario de búsqueda balanceado (AVL)
    def __init__(self):
        self.raiz = None
        self.tamano = 0

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
           return nodo.valor
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

    
    # def actualizarEquilibrio(self,nodo):
    #     if nodo.factorEquilibrio > 1 or nodo.factorEquilibrio < -1:
    #         self.reequilibrar(nodo)
    #         return
    #     if nodo.padre != None:
    #         if nodo.esHijoIzquierdo():
    #                 nodo.padre.factorEquilibrio += 1
    #         elif nodo.esHijoDerecho():
    #                 nodo.padre.factorEquilibrio -= 1

    #         if nodo.padre.factorEquilibrio != 0:
    #                 self.actualizarEquilibrio(nodo.padre)

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

    def encontrarMin(self, nodo):
        if nodo is None:
            return None
        while nodo.hijoIzquierdo is not None:
            nodo= nodo.hijoIzquierdo
        return nodo

    def eliminar(self,clave):
        if self.tamano > 1:
            nodoAEliminar = self._obtener(clave,self.raiz)
            if nodoAEliminar:
                self.remover(nodoAEliminar)
                
                self.raiz=self._balancear(self.raiz)
                self.tamano = self.tamano-1
            else:
                raise KeyError('Error, la clave no está en el árbol')
        elif self.tamano == 1 and self.raiz.clave == clave:
            self.raiz = None
            self.tamano = self.tamano - 1
        else:
            raise KeyError('Error, la clave no está en el árbol')

    def __delitem__(self,clave):
        self.eliminar(clave)

    def remover(self,nodoActual):
        if nodoActual.esHoja(): #hoja
            if nodoActual == nodoActual.padre.hijoIzquierdo:
               nodoActual.padre.hijoIzquierdo = None
            else:
               nodoActual.padre.hijoDerecho = None
        elif nodoActual.tieneAmbosHijos(): #interior
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
        self._balancear(nodoActual.padre)
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

