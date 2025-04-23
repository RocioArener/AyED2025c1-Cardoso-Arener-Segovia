# mazo.py

from proyecto_2.modules.modulo1 import ListaDobleEnlazada  # Importa la clase ListaDobleEnlazada
from modules.carta import Carta

class DequeEmptyError(Exception):
    pass  # Define una excepción personalizada para cuando el mazo está vacío

class Mazo:
    def __init__(self):
        self.cabeza=None
        self.ultimo=None
        self.size=0

    def __iter__(self):
        nodo_actual = self.cabeza
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
    def ultimo(self):
        return self._ultimo
    
    @ultimo.setter
    def ultimo(self, valor):
        self._ultimo = valor
        
    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, valor):
        self._size = valor

    def poner_carta_arriba(self, carta):
        ListaDobleEnlazada.agregar_al_final(carta) 
    
    def sacar_carta_arriba(self, carta):
        ListaDobleEnlazada.extraer(self.size-1)
    
    def poner_carta_abajo(self, carta):
        ListaDobleEnlazada.agregar_al_inicio(carta)
    
