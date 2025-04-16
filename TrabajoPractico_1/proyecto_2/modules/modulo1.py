class Nodo:
    def __init__(self, dato):
        self.dato=dato
        self.siguiente=None
        self.anterior=None

class ListaDoblementeEnlazada:
    def __init__(self):
        self.primero=None
        self.ultimo=None
        self.size=0

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
        if posicion < 0 or posicion > self.tamanio:
            raise IndexError("Posición inválida")
        if posicion == 0:
            return self.agregar_al_inicio(item)
        elif posicion == self.tamanio:
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
            self.tamanio += 1



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
