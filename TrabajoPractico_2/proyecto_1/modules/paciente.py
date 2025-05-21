# -*- coding: utf-8 -*-

from random import randint, choices
import time
import datetime

nombres = ['Leandro', 'Mariela', 'Gastón', 'Andrea', 'Antonio', 'Estela', 'Jorge', 'Agustina']
apellidos = ['Perez', 'Colman', 'Rodriguez', 'Juarez', 'García', 'Belgrano', 'Mendez', 'Lopez']

niveles_de_riesgo = [1, 2, 3]
descripciones_de_riesgo = ['crítico', 'moderado', 'bajo']
# probabilidades de aparición de cada tipo de paciente
probabilidades = [0.1, 0.3, 0.6] 

class Paciente:
    def __init__(self,fecha_y_hora):
        n = len(nombres)
        self.__nombre = nombres[randint(0, n-1)]
        self.__apellido = apellidos[randint(0, n-1)]
        self.__riesgo = choices(niveles_de_riesgo, probabilidades)[0]
        self.__descripcion = descripciones_de_riesgo[self.__riesgo-1]   
        self.__fecha_y_hora=fecha_y_hora

    def get_nombre(self):
        return self.__nombre
    
    def get_hora(self):
        return self.__fecha_y_hora

    def get_apellido(self):
        return self.__apellido
    
    def get_riesgo(self):
        return self.__riesgo
    
    def get_descripcion_riesgo(self):
        return self.__descripcion
    
    def __str__(self):
        cad = self.__nombre + ' '
        cad += self.__apellido + '\t -> '
        cad += str(self.__riesgo) + '-' + self.__descripcion
        cad += "  "+str(self.__fecha_y_hora)
        return cad
    def __repr__(self):
        cad = self.__nombre + ' '
        cad += self.__apellido + '\t -> '
        cad += str(self.__riesgo) + '-' + self.__descripcion
        cad += "  "+str(self.__fecha_y_hora)
        return cad
    
    def __lt__(self,otro):
        if self.get_riesgo() < otro.get_riesgo():
            return True
        elif self.get_riesgo() == otro.get_riesgo():
            if self.get_hora() < otro.get_hora():
                return True

# if __name__=="__main__":
#     ahora = datetime.datetime.now()
#     p1= Paciente(ahora)
#     time.sleep(3)
#     ahora = datetime.datetime.now()
#     p2= Paciente(ahora)
#     print(p1)
#     print(p2)
#     if p1<p2:
#         print ("p1 es mas urgente que p2")
#         print(p1)

#     else:
#         print("p2 es mas urgente que p1")
#         print(p2)
#     print(p1.get_hora())
        
        