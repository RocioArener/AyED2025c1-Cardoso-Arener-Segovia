from modules.abb import ABB
import datetime

class BaseTemperaturas:
    def __init__(self, ):
        self.avl = ABB()    

    def guardar_temperatura(self, temperatura, fecha): #guarda la medida de temperatura asociada a la fecha.
        if not isinstance(fecha, datetime.date):
            raise ValueError("La fecha debe ser una instancia de datetime.date")
        if not isinstance(temperatura, (int, float)):
            raise ValueError("La temperatura debe ser un número")
        self.avl.insertar(fecha, temperatura)



    def devolver_temperatura(fecha): #devuelve la medida de temperatura en la fecha determinada.
        pass
    def max_temp_rango(fecha1, fecha2): #devuelve la temperatura máxima entre los rangos fecha1 y fecha2 inclusive (fecha1 < fecha2). Esto no implica que los intervalos del rango deban ser fechas incluidas previamente en el árbol.
        pass
    def min_temp_rango(fecha1, fecha2): #devuelve la temperatura mínima entre los rangos fecha1 y fecha2 inclusive (fecha1 < fecha2). Esto no implica que los intervalos del rango deban ser fechas incluidas previamente en el árbol.
        pass
    def temp_extremos_rango(fecha1, fecha2): #devuelve la temperatura mínima y máxima entre los rangos fecha1 y fecha2 inclusive (fecha1 < fecha2).
        pass
    def borrar_temperatura(fecha): #recibe una fecha y elimina del árbol la medición correspondiente a esa fecha.
        pass
    def devolver_temperaturas(fecha1, fecha2):# devuelve un listado de las mediciones de temperatura en el rango recibido por parámetro con el formato “dd/mm/aaaa: temperatura ºC”, ordenado por fechas. 
        pass
    def cantidad_muestras():# devuelve la cantidad de muestras de la BD.
        pass