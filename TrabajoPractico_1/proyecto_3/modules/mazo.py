# mazo.py
#C:\Users\alumno\Desktop\AyED2025c1-Cardoso-Arener-Segovia\TrabajoPractico_1\proyecto_2\modules
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'proyecto_2','modules')))

from modulo1 import ListaDobleEnlazada


class DequeEmptyError(Exception):      
    def __init__(self, mensaje="Ya no quedan elementos para extraer"):
        super().__init__(mensaje)
        
        
class Mazo():
    def __init__(self):
        self.mazo=ListaDobleEnlazada()

    def poner_carta_arriba(self, carta):
        self.mazo.agregar_al_final(carta) 
    
    def sacar_carta_arriba(self):
        carta=self.mazo.extraer()
        carta.visible=True
        return carta
        
    def poner_carta_abajo(self, carta):
        self.mazo.agregar_al_inicio(carta)
    
    def len(self):
        return self.mazo.tamanio()

if __name__ == '__main__':
    try:
        Mazo.sacar_carta_arriba()
    except:
        raise DequeEmptyError()
            