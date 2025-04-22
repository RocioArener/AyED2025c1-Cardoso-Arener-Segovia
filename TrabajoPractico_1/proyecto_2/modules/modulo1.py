""""""
class Nodo:
    def __init__(self, dato):
        self.dato=dato
        self.siguiente=None
        self.anterior=None

class ListaDobleEnlazada:
    def __init__(self):
        self.primero=None
        self.ultimo=None
        self.size=0

    @property
    def cabeza(self):
        """Get the first node (like an Instagram story)."""
        return self._primero
    
    @cabeza.setter
    def cabeza(self, nodo):
        """Set the first node (but only if it's valid)."""
        if nodo is not None and not isinstance(nodo, Nodo):
            raise TypeError("Solo nodos")
        self._primero = nodo

    def esta_vacia(self):
        return self.primero==None
    
    def __len__(self):
        return self.size
        
    def agregar_al_final(self, dato):
        nuevo=Nodo(dato)
        if self.esta_vacia():
            self.primero =self.ultimo=nuevo
        else:
            nuevo.anterior=self.ultimo
            self.ultimo.siguiente=nuevo
            self.ultimo=nuevo
        self.size+=1

    def agregar_al_inicio(self, dato):
        nuevo=Nodo(dato)
        if self.esta_vacia():
            self.primero=self.ultimo=nuevo
        else:
            nuevo.siguiente=self.primero
            self.primero.anterior=nuevo
            self.primero=nuevo
        self.size+=1
    
    def insertar(self, item, posicion=None):
        if posicion is None:
            return self.agregar_al_final(item)
        if posicion < 0 or posicion > self.size:
            raise IndexError("Posición inválida")
        if posicion == 0:
            return self.agregar_al_inicio(item)
        elif posicion == self.size:
            return self.agregar_al_final(item)
        else:
            nuevo = Nodo(item)
            actual = self.primero
            # Avanzamos hasta la posición anterior a donde insertaremos
            for _ in range(posicion - 1):
                actual = actual.siguiente
            # Conectamos el nuevo nodo
            nuevo.siguiente = actual.siguiente
            nuevo.anterior = actual
            actual.siguiente.anterior = nuevo
            actual.siguiente = nuevo
            self.size += 1
            
    def extraer(self, item, posicion=None):
        if self.esta_vacia():
            raise Exception("Lista vacía")
        if posicion == self.size or posicion==None:
            posicion=self.size -1   
        if posicion < 0 or posicion > self.size:
            raise Exception("Posición inválida")
        #Primer elemento
        if posicion ==0:
            nodo=self.primero
            self.primero=nodo.siguiente
            if self.primero:
                self.primero.anterior= None
            else:
                self.ultimo= None
            self.size-=1
            return nodo.dato
        #Ultimo elemento
        elif posicion == self.size-1:
            nodo=self.ultimo
            self.ultimo =nodo.anterior
            if self.ultimo:
                self.ultimo.siguiente=None
            else:
                self.primero = None
            self.size-=1
            return nodo.dato
        #Cualquier otro elemento
        else:
            actual=self.primero
            for i in range(posicion):
                actual= actual.siguiente
                aux=item
                actual.anterior.siguiente=actual.siguiente
                actual.siguiente.anterior=actual.anterior
                self.size-=1
            return actual.dato
        
    def copiar(self):
        if self.size==0:
            raise ValueError("Lista vacia")
        nueva_lista = ListaDobleEnlazada()
        actual = self.primero
        while actual is not None:
            nueva_lista.agregar_al_final(actual.dato)
            actual = actual.siguiente
        return nueva_lista

    def invertir(self):
        actual=self.primero
        aux=None
        while actual!=None:
            aux=actual.anterior
            actual.anterior=actual.siguiente
            actual.siguiente=aux
            actual=actual.anterior    
        if aux!=None:
            self.primero=aux.anterior
        
    def concatenar(self, lista_extra):
        if lista_extra.esta_vacia():
            return
        if self.esta_vacia():
            self.primero= lista_extra.primero
            self.ultimo= lista_extra.ultimo
        else:
            self.ultimo.siguiente = lista_extra.primero
            lista_extra.primero.anterior=self.ultimo
            self.ultimo=lista_extra.ultimo
        self.size+=lista_extra.size

    def _add_(self, lista_extra):
        copia=self.copiar()
        copia.concatenar(lista_extra.copiar())
        return copia
      
            
        
        

                




    # def recorrer_inicio(self):
    #     aux=self.primero
    #     while aux != None:
    #         print(aux.dato)
    #         aux=aux.siguiente

    # def recorrer_final(self):
    #     aux=self.ultimo
    #     while aux:
    #         print(aux.dato)
    #         aux=aux.anterior

    # def eliminar_inicio(self):
    #     if self.vacia():
    #         print("Lista vacia")
    #     elif self.primero.siguiente==None:
    #         self.primero=self.ultimo=None
    #         self.size=0
    #     else:
    #         self.primero=self.primero.siguiente
    #         self.primero.anterior=None
    #         self.size-=1

    # def eliminar_final(self):
    #     if self.vacia():
    #         print("Lista vacia")
    #     elif self.primero.siguiente== None:
    #         self.primero = self.ultimo = None
    #         self.size=0
    #     else:
    #         self.ultimo=self.ultimo.anterior
    #         self.ultimo.siguiente=None
    #         self.size-=1
