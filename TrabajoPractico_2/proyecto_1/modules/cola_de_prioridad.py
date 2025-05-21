# módulo para organizar funciones o clases utilizadas en nuestro proyecto
# Crear tantos módulos como sea necesario para organizar el código
import time
from modules.paciente import Paciente
# from modules.paciente import Paciente

class MonticuloBinario:
    def __init__(self):
        self.listaMonticulo=[0]
        self.tamanoActual=0
    


    def infiltArriba(self,i):
        while i // 2 > 0:
            if self.listaMonticulo[i] < self.listaMonticulo[i // 2] :
                tmp = self.listaMonticulo[i // 2]
                self.listaMonticulo[i // 2] = self.listaMonticulo[i]
                self.listaMonticulo[i] = tmp
            i = i // 2

    def infiltAbajo(self,i):
        while i*2 <= self.tamanoActual:
            hm = self.hijoMin(i)
            if self.listaMonticulo[i] > self.listaMonticulo[hm]:
                tmp = self.listaMonticulo[i]
                self.listaMonticulo[i] = self.listaMonticulo[hm]
                self.listaMonticulo[hm] = tmp
            i = hm

    def hijoMin(self,i):
        if i * 2 + 1 > self.tamanoActual:
            return i * 2
        else:
            if self.listaMonticulo[i*2] < self.listaMonticulo[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1
    
    def insertar(self,k):
        self.listaMonticulo.append(k)
        self.tamanoActual = self.tamanoActual + 1
        self.infiltArriba(self.tamanoActual)

    def eliminarMin(self):
        valorSacado = self.listaMonticulo[1]
        self.listaMonticulo[1] = self.listaMonticulo[self.tamanoActual]
        self.tamanoActual = self.tamanoActual - 1
        self.listaMonticulo.pop()
        self.infiltAbajo(1)
        return valorSacado
    
    # def len(self,lista):
    #     self.tamanoActual=len(lista)

    def mostrar(self):
        print (self.listaMonticulo[1:])
    
    def __str__(self):
        return str(self.listaMonticulo[1:])
    
if __name__=="__main__":
   mont= MonticuloBinario()
   p1= Paciente("2023-10-01 12:00:00")
   p2= Paciente("2023-10-01 12:00:01")
   mont.insertar(p1)
   mont.insertar(p2)
#    mont.insertar(5)
#    mont.insertar(10)
#    mont.insertar(1)
#    mont.insertar(4)
#    mont.insertar(14)
#    mont.eliminarMin()
   mont.mostrar()