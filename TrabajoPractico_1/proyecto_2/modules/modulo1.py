class Nodo:
    def __init__(self, dato):
        self._dato = dato
        self._siguiente = None
        self._anterior = None

    @property
    def dato(self):
        return self._dato
    
    @dato.setter
    def dato(self, valor):
        self._dato = valor

    @property
    def siguiente(self):
        return self._siguiente
    
    @siguiente.setter
    def siguiente(self, valor):
        self._siguiente = valor
        
    @property
    def anterior(self):
        return self._anterior
    
    @anterior.setter
    def anterior(self, valor):
        self._anterior = valor

class ListaDobleEnlazada:
    def __init__(self):
        self._cabeza = None
        self._cola = None
        self._tamanio = 0
        
    def __iter__(self):
        nodo_actual = self._cabeza
        while nodo_actual is not None:
            yield nodo_actual.dato
            nodo_actual = nodo_actual.siguiente

    @property
    def cabeza(self):
        return self._cabeza
    
    @cabeza.setter
    def cabeza(self, valor):
        self._cabeza = valor
    
    @property
    def cola(self):
        return self._cola
    
    @cola.setter
    def cola(self, valor):
        self._cola = valor
        
    @property
    def tamanio(self):
        return self._tamanio
    
    @tamanio.setter
    def tamanio(self, valor):
        self._tamanio = valor

    def esta_vacia(self):
        return self._cabeza is None

    def __len__(self):
        return self._tamanio

    def agregar_al_final(self, dato):
        nuevo = Nodo(dato)
        if self.esta_vacia():
            self._cabeza = self._cola = nuevo
        else:
            nuevo.anterior = self._cola
            self._cola.siguiente = nuevo
            self._cola = nuevo
        self._tamanio += 1

    def agregar_al_inicio(self, dato):
        nuevo = Nodo(dato)
        if self.esta_vacia():
            self._cabeza = self._cola = nuevo
        else:
            nuevo.siguiente = self._cabeza
            self._cabeza.anterior = nuevo
            self._cabeza = nuevo
        self._tamanio += 1

    def insertar(self, dato, posicion=None):
        if posicion is None:
            return self.agregar_al_final(dato)
        if posicion < 0 or posicion > self._tamanio:
            raise IndexError("Posición inválida")
        if posicion == 0:
            return self.agregar_al_inicio(dato)
        elif posicion == self._tamanio:
            return self.agregar_al_final(dato)
        else:
            nuevo = Nodo(dato)
            actual = self._cabeza
            for _ in range(posicion - 1):
                actual = actual.siguiente
            nuevo.siguiente = actual.siguiente
            nuevo.anterior = actual
            actual.siguiente.anterior = nuevo
            actual.siguiente = nuevo
            self._tamanio += 1

    def extraer(self, posicion=None):
        if self.esta_vacia():
            raise Exception("Lista vacía")
        
        if posicion is None:
            posicion = self._tamanio - 1
        elif posicion < 0:
            posicion=self._tamanio+posicion
            if posicion <0: 
                 raise Exception("Posición inválida")
            
        if posicion <0 or posicion>=self._tamanio:
            raise Exception("Posición inválida")
        
        if posicion == 0:
            nodo = self._cabeza
            self._cabeza = nodo.siguiente
            if self._cabeza:
                self._cabeza.anterior = None
            else:
                self._cola = None
            self._tamanio -= 1
            return nodo.dato
        elif posicion == self._tamanio - 1:
            nodo = self._cola
            self._cola = nodo.anterior
            if self._cola:
                self._cola.siguiente = None
            else:
                self._cabeza = None
            self._tamanio -= 1
            return nodo.dato
        else:
            actual = self._cabeza
            for _ in range(posicion):
                actual = actual.siguiente
            actual.anterior.siguiente = actual.siguiente
            actual.siguiente.anterior = actual.anterior
            self._tamanio -= 1
            return actual.dato

    def copiar(self):
        lista_copia = ListaDobleEnlazada()
        actual = self._cabeza
        while actual is not None:
            lista_copia.agregar_al_final(actual.dato)
            actual = actual.siguiente
        return lista_copia

    def invertir(self):
        actual = self._cabeza
        aux = None
        while actual is not None:
            aux = actual.anterior
            actual.anterior = actual.siguiente
            actual.siguiente = aux
            actual = actual.anterior
        aux = self._cabeza
        self._cabeza = self._cola
        self._cola = aux

    def concatenar(self, lista_extra):
        if lista_extra.esta_vacia():
            return
        lista_a_concatenar = lista_extra.copiar()
        if self.esta_vacia():
            self._cabeza = lista_a_concatenar.cabeza
            self._cola = lista_a_concatenar.cola
        else:
            lista_a_concatenar.cabeza.anterior = self._cola
            self._cola.siguiente = lista_a_concatenar.cabeza
            self._cola = lista_a_concatenar.cola
            
        self._tamanio += lista_extra.tamanio

    def __add__(self, lista_extra):
        copia = self.copiar()
        copia.concatenar(lista_extra.copiar())
        return copia
