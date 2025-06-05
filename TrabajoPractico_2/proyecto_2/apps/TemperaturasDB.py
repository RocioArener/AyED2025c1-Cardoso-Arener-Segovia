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
        self.avl.agregar(fecha, temperatura)


    def devolver_temperatura(self, fecha): #devuelve la medida de temperatura en la fecha determinada.
        if not isinstance(fecha, datetime.date):
            raise ValueError("La fecha debe ser una instancia de datetime.date")
        return self.avl.obtener(fecha)

    def max_temp_rango(self, fecha1, fecha2):
        if not isinstance(fecha1, datetime.date) or not isinstance(fecha2, datetime.date):
            raise ValueError("Las fechas deben ser instancias de datetime.date")
        if fecha1 > fecha2:
            raise ValueError("fecha1 debe ser menor o igual que fecha2")

        def buscar_max(nodo):
            if nodo is None:
                return None
            max_izq = max_der = max_centro = None

            if nodo.clave > fecha2:
                return buscar_max(nodo.hijoIzquierdo)
            elif nodo.clave < fecha1:
                return buscar_max(nodo.hijoDerecho)
            else:
                max_izq = buscar_max(nodo.hijoIzquierdo)
                max_der = buscar_max(nodo.hijoDerecho)
                max_centro = nodo.valor

            candidatos = [x for x in [max_izq, max_der, max_centro] if x is not None]
            return max(candidatos) if candidatos else None

        return buscar_max(self.avl.raiz)    

    def min_temp_rango(self,fecha1, fecha2): #devuelve la temperatura mínima entre los rangos fecha1 y fecha2 inclusive (fecha1 < fecha2). Esto no implica que los intervalos del rango deban ser fechas incluidas previamente en el árbol.
        if not isinstance(fecha1, datetime.date) or not isinstance(fecha2, datetime.date):
            raise ValueError("Las fechas deben ser instancias de datetime.date")        
        if fecha1 > fecha2:
            raise ValueError("fecha1 debe ser menor o igual que fecha2")
        
        def buscar_min(nodo):
            if nodo is None:
                return None
            min_izq = min_der = min_centro = None

            if nodo.clave > fecha2:
                return buscar_min(nodo.hijoIzquierdo)
            elif nodo.clave < fecha1:
                return buscar_min(nodo.hijoDerecho)
            else:
                min_izq = buscar_min(nodo.hijoIzquierdo)
                min_der = buscar_min(nodo.hijoDerecho)
                min_centro = nodo.valor

            candidatos = [x for x in [min_izq, min_der, min_centro] if x is not None]
            return min(candidatos) if candidatos else None
        return buscar_min(self.avl.raiz)
    
    def temp_extremos_rango(self,fecha1, fecha2): #devuelve la temperatura mínima y máxima entre los rangos fecha1 y fecha2 inclusive (fecha1 < fecha2).
            return self.min_temp_rango(fecha1, fecha2), self.max_temp_rango(fecha1, fecha2)
    
    def borrar_temperatura(self,fecha): #recibe una fecha y elimina del árbol la medición correspondiente a esa fecha.
        if not isinstance(fecha, datetime.date):
            raise ValueError("La fehca debe ser instancia de datetime.date")
        if self.avl.obtener(fecha) is not None: #bajamos el tamaño si la fecha se encuentra dentro.
            self.tamano -=1
        self.avl.eliminar(fecha)

    def devolver_temperaturas(self, fecha1, fecha2):# devuelve un listado de las mediciones de temperatura en el rango recibido por parámetro con el formato “dd/mm/aaaa: temperatura ºC”, ordenado por fechas. 
        if not isinstance(fecha1, datetime.date) or not isinstance(fecha2, datetime.date):
            raise ValueError("Las fechas deben ser instancias de datetime.date")
        if fecha1>fecha2:
            raise ValueError("fecha1 debe ser <= fecha2")
        lista=[]
        def recorrido_inorder(nodo):
            if nodo in None:
                return
            if nodo.clave >=fecha1:
                recorrido_inorder(nodo.hijoIzquierdo)
            if fecha1 <=nodo.clave <=fecha2:
                lista.append(f"{nodo.clave.strftime('%d/%m/%Y'): {nodo.valor}}°C")
            if nodo.clave <=fecha2:
                recorrido_inorder(nodo.hijoDerecho)
        recorrido_inorder(self.avl.raiz)
        return lista

    def cantidad_muestras(self):# devuelve la cantidad de muestras de la BD.
        return self.tamano

    def __str__(self):
        return "\n".join(self.devolver_temperaturas(datetime.date.min, datetime.date.max))






        # def longitud(self):
    #     return self.tamano

    # def __len__(self):
    #     return self.tamano
    