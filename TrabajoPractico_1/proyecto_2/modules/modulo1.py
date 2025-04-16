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
        aux=None
        if posicion < 0 or posicion > self.size:
            raise Exception("Posición inválida")
        if posicion == 0:
            aux=self.primero
            self.primero = None
            return aux
        elif posicion == self.size or posicion==None:
            aux=self.ultimo
            self.ultimo = None
            return aux
        else:
            for i in range(self.size):
                item=Nodo(self.dato)
                aux=item
                item.anterior.anterior=item.siguiente
                item.siguiente.siguiente=item.anterior
            return aux
    
    def copiar(self):
        lista_Copia=[]
        if self.size==0:
            raise Exception("Lista Vacia")
        aux =self.primero
        Nodo.anterior=None
        while aux!= None:
            lista_Copia+=aux
            aux =aux.siguiente
        return lista_Copia
    
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
        
    def concatenar(lista,self):
        self.ultimo.siguiente=
        
            
        
        

                




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
