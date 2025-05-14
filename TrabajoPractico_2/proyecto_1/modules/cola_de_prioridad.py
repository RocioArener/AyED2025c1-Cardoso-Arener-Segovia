# módulo para organizar funciones o clases utilizadas en nuestro proyecto
# Crear tantos módulos como sea necesario para organizar el código
import time
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
    
    def len(self,lista):
        self.tamanoActual=len(lista)

    def mostrar(self):
        return self.listaMonticulo[1:]
    
# class Cola_prioridad():
#     def __init__(self):
#         self.cola_prioridad=MonticuloBinario()


#     def llega_paciente(self,paciente):
#         if paciente.get_riesgo == 
#         self.cola_prioridad.insertar(paciente)

#     def atender_paciente(self):
#         self.cola_prioridad.eliminarMin()


if __name__=="__main__":
   mont= MonticuloBinario()
   mont.insertar(2)
   mont.insertar(5)
   mont.insertar(5)
   mont.insertar(10)
   mont.insertar(1)
   mont.insertar(4)
   mont.insertar(14)
   mont.eliminarMin()
   print(mont.mostrar())