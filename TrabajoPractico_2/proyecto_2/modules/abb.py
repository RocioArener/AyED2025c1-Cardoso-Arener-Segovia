class NodoArbol:
    def __init__(self,clave,valor):
        self.clave = clave
        self.valor = valor
        self.hijoIzquierdo = None
        self.hijoDerecho = None
        self.padre = None
        self.altura = 1
        self.factorEquilibrio = 0

class ABB:
    def __init__(self):
        self.raiz = None
        self.tamano = 0


    def agregar(self, clave, valor): 
        self.raiz = self._agregar(self.raiz, clave, valor) 

    def _agregar(self, nodo, clave, valor): 
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
        return self._balancear(nodo)
    

    def obtener(self,clave):
       return self._obtener(clave,self.raiz)

    def _obtener(self,clave,nodo):
       if not nodo:
           return None
       elif nodo.clave == clave:
           return nodo.valor
       elif clave < nodo.clave: #si la clave es menor, le pasa a _obtener los nuevos parametros, siendo la clave y el hijo izquierdo del nodo actual
           return self._obtener(clave,nodo.hijoIzquierdo) 
       else: # lo mismo que arriba, pero con el hijo derecho
           return self._obtener(clave,nodo.hijoDerecho)


    def _balancear(self, nodo):
        if nodo is None:
            return nodo
        nodo.altura = 1 + max(self.altura(nodo.hijoIzquierdo), self.altura(nodo.hijoDerecho)) #se actualiza la altura del nodo, siendo 1 + la máxima altura de sus hijos
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

    
    def actualizarEquilibrio(self,nodo):
        if nodo.factorEquilibrio > 1 or nodo.factorEquilibrio < -1:
            self.reequilibrar(nodo)
            return
        if nodo.padre != None:
            if nodo.esHijoIzquierdo():
                    nodo.padre.factorEquilibrio += 1
            elif nodo.esHijoDerecho():
                    nodo.padre.factorEquilibrio -= 1

            if nodo.padre.factorEquilibrio != 0:
                    self.actualizarEquilibrio(nodo.padre)

    def rotarIzquierda(self,rotRaiz):
        nuevaRaiz = rotRaiz.hijoDerecho
        rotRaiz.hijoDerecho = nuevaRaiz.hijoIzquierdo
        if nuevaRaiz.hijoIzquierdo != None:
            nuevaRaiz.hijoIzquierdo.padre = rotRaiz
        nuevaRaiz.padre = rotRaiz.padre
        if rotRaiz.esRaiz():
            self.raiz = nuevaRaiz
        else:
            if rotRaiz.esHijoIzquierdo():
                    rotRaiz.padre.hijoIzquierdo = nuevaRaiz
            else:
                rotRaiz.padre.hijoDerecho = nuevaRaiz
        nuevaRaiz.hijoIzquierdo = rotRaiz
        rotRaiz.padre = nuevaRaiz
        rotRaiz.factorEquilibrio = rotRaiz.factorEquilibrio + 1 - min(nuevaRaiz.factorEquilibrio, 0)
        nuevaRaiz.factorEquilibrio = nuevaRaiz.factorEquilibrio + 1 + max(rotRaiz.factorEquilibrio, 0)
            
    def rotarDerecha(self,rotRaiz):
        nuevaRaiz = rotRaiz.hijoIzquierdo 
        rotRaiz.hijoIzquierdo = nuevaRaiz.hijoDerecho
        if nuevaRaiz.hijoDerecho != None:
            nuevaRaiz.hijoDerecho.padre = rotRaiz  
        nuevaRaiz.padre = rotRaiz.padre
        if rotRaiz.esRaiz():
            self.raiz = nuevaRaiz
        else:
            if rotRaiz.esHijoDerecho():
                rotRaiz.padre.hijoDerecho = nuevaRaiz
            else:
                rotRaiz.padre.hijoIzquierdo = nuevaRaiz
        nuevaRaiz.hijoDerecho = rotRaiz
        rotRaiz.padre = nuevaRaiz
        rotRaiz.factorEquilibrio = rotRaiz.factorEquilibrio - 1 - max(nuevaRaiz.factorEquilibrio, 0)
        nuevaRaiz.factorEquilibrio = nuevaRaiz.factorEquilibrio - 1 + min(rotRaiz.factorEquilibrio, 0)
        
    def altura(self, nodo=None):
        if nodo is None:
            return 0
        return 1 + max(self.altura(nodo.hijoIzquierdo), self.altura(nodo.hijoDerecho))

if  __name__ == "__main__":
    # Ejemplo de uso del NodoArbol
    arbol= ABB()
    arbol.agregar(5, "valor raiz")  
    arbol.agregar(3, "valor 3")
    arbol.agregar(7, "valor 7")
    print(arbol.obtener(5))  # Debería imprimir "valor raiz"

