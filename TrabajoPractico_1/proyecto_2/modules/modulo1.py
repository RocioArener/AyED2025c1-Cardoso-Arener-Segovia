class Nodo:
    def __init__(self, dato):
        self.dato=dato
        self.siguiente=None
        self.anterior=None

class ListaDobleEnlazada:
    def __init__(self):
        self.cabeza=None
        self.cola=None
        self.size=0

    def __iter__(self):
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            yield nodo_actual.dato
            nodo_actual = nodo_actual.siguiente

    def esta_vacia(self):
        return self.cabeza==None
    
    def __len__(self):
        return self.size
        
    def agregar_al_final(self, dato):
        nuevo=Nodo(dato)
        if self.esta_vacia():
            self.cabeza =self.cola=nuevo
        else:
            nuevo.anterior=self.cola
            self.cola.siguiente=nuevo
            self.cola=nuevo
            self.cola.siguiente=None
        self.size+=1

    def agregar_al_inicio(self, dato):
        nuevo=Nodo(dato)
        if self.esta_vacia():
            self.cabeza=self.cola=nuevo
        else:
            nuevo.siguiente=self.cabeza
            self.cabeza.anterior=nuevo
            self.cabeza=nuevo
            self.cabeza.anterior=None
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
            actual = self.cabeza
            # Avanzamos hasta la posición anterior a donde insertaremos
            for _ in range(posicion - 1):
                actual = actual.siguiente
            # Conectamos el nuevo nodo
            nuevo.siguiente = actual.siguiente
            nuevo.anterior = actual
            actual.siguiente.anterior = nuevo
            actual.siguiente = nuevo
            self.size += 1
            
    def extraer(self, posicion=None):
        if self.esta_vacia():
            raise Exception("Lista vacía")
        if posicion == self.size or posicion==None:
            posicion=self.size -1   
        if posicion < 0 or posicion > self.size:
            raise Exception("Posición inválida")
        #Primer elemento
        if posicion ==0:
            nodo=self.cabeza
            self.cabeza=nodo.siguiente
            if self.cabeza:
                self.cabeza.anterior= None
            else:
                self.cola= None
            self.size-=1
            return nodo.dato
        #Ultimo elemento
        elif posicion == self.size-1:
            nodo=self.cola
            self.cola =nodo.anterior
            if self.cola:
                self.cola.siguiente=None
            else:
                self.cabeza = None
            self.size-=1
            return nodo.dato
        #Cualquier otro elemento
        else:
            actual=self.cabeza
            for i in range(posicion):
                actual= actual.siguiente
            actual.anterior.siguiente=actual.siguiente
            if actual.siguiente:
                actual.siguiente.anterior=actual.anterior
                actual.anterior.siguiente = actual.siguiente
                self.size-=1
            return actual.dato
        
    def copiar(self):
        if self.size==0:
            raise ValueError("Lista vacia")
        nueva_lista = ListaDobleEnlazada()
        actual = self.cabeza
        while actual is not None:
            nueva_lista.agregar_al_final(actual.dato)
            actual = actual.siguiente
        return nueva_lista

    def invertir(self):
        actual=self.cabeza
        aux=None
        while actual!=None:
            aux=actual.anterior
            actual.anterior=actual.siguiente
            actual.siguiente=aux
            actual=actual.anterior    
        if aux!=None:
            self.cabeza=aux.anterior
        
    def concatenar(self, lista_extra):
        if lista_extra.esta_vacia():
            return
        if self.esta_vacia():
            self.cabeza= lista_extra.cabeza
            self.cola= lista_extra.ultimo
        else:
            self.cola.siguiente = lista_extra.cabeza
            lista_extra.cabeza.anterior=self.cola
            self.cola=lista_extra.ultimo
        self.size+=lista_extra.size

    def __add__(self, lista_extra):
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
