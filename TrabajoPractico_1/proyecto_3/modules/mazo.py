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
    
    def sacar_carta_arriba(self, mostrar=False):
        carta = self.mazo.extraer()
        carta.visible = mostrar  # Establece la visibilidad de la carta según el argumento
        return carta
    # def sacar_carta_arriba(self):
    #     carta=self.mazo.extraer()
    #     carta.visible= True
    #     carta.__str__()
    #     return carta
        
    def poner_carta_abajo(self, carta):
        self.mazo.agregar_al_inicio(carta)
    
    def __len__(self):
        return self.mazo.__len__()

if __name__ == '__main__':
    try:
        Mazo.sacar_carta_arriba()
    except:
        raise DequeEmptyError()
            