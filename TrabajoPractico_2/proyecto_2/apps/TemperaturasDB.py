from modules.abb import ABB
import datetime

# Implementación de la clase BaseTemperaturas que utiliza un árbol AVL para almacenar temperaturas asociadas a fechas.

class BaseTemperaturas:
    def __init__(self, ):
        self.avl = ABB()    
        self.tamano=0

    def guardar_temperatura(self, temperatura, fecha): #guarda la medida de temperatura asociada a la fecha.
        # Verifica que la fecha sea una instancia de datetime.date y que la temperatura sea un número.
        '''Orden de complejidad: O(log n) en el caso promedio'''
        if not isinstance(fecha, datetime.date):
            raise ValueError("La fecha debe ser una instancia de datetime.date")
        if not isinstance(temperatura, (int, float)):
            raise ValueError("La temperatura debe ser un número")
        self.avl.agregar(fecha, temperatura)


    def devolver_temperatura(self, fecha): #devuelve la medida de temperatura en la fecha determinada.
        '''Orden de complejidad: O(log n)'''
        if not isinstance(fecha, datetime.date):
            raise ValueError("La fecha debe ser una instancia de datetime.date")
        return self.avl.obtener(fecha)


    def max_temp_rango(self, fecha1, fecha2): #devuelve la temperatura máxima entre los rangos fecha1 y fecha2 inclusive (fecha1 < fecha2).
        '''Orden de complejidad: O(log n) en el caso promedio y O(n) en el peor caso'''
        # Verifica que las fechas sean instancias de datetime.date y que fecha1 sea menor o igual a fecha2.
        if not isinstance(fecha1, datetime.date) or not isinstance(fecha2, datetime.date):
            raise ValueError("Las fechas deben ser instancias de datetime.date")
        if fecha1 > fecha2:
            raise ValueError("fecha1 debe ser menor o igual que fecha2")

        # Función recursiva para buscar la temperatura máxima en el rango dado.
        def buscar_max(nodo):
            '''Orden de complejidad: O(log n) en el caso promedio y O(n) en el peor caso'''
            if nodo is None:
                return None
            max_izq = max_der = max_centro = None
            # Compara la clave del nodo con las fechas para determinar en qué subárbol buscar.
            # Si la clave del nodo es mayor que fecha2, busca recursivamente en el subárbol izquierdo.
            if nodo.clave > fecha2:
                return buscar_max(nodo.hijoIzquierdo)
            # Si la clave del nodo es menor que fecha1, busca recursivamente en el subárbol derecho.
            elif nodo.clave < fecha1:
                return buscar_max(nodo.hijoDerecho)
            # Si la clave del nodo está dentro del rango, compara las temperaturas.
            else:
                max_izq = buscar_max(nodo.hijoIzquierdo)
                max_der = buscar_max(nodo.hijoDerecho)
                max_centro = nodo.cargaUtil

            candidatos = [x for x in [max_izq, max_der, max_centro] if x is not None]
            return max(candidatos) if candidatos else None

        return buscar_max(self.avl.raiz) #busca la temperatura máxima en el árbol AVL a partir de la raíz. 


    def min_temp_rango(self,fecha1, fecha2): #devuelve la temperatura mínima entre los rangos fecha1 y fecha2 inclusive (fecha1 < fecha2). Esto no implica que los intervalos del rango deban ser fechas incluidas previamente en el árbol.
        '''Orden de complejidad: O(log n) en el caso promedio y O(n) en el peor caso'''
        # Verifica que las fechas sean instancias de datetime.date y que fecha1 sea menor o igual a fecha2.
        if not isinstance(fecha1, datetime.date) or not isinstance(fecha2, datetime.date):
            raise ValueError("Las fechas deben ser instancias de datetime.date")        
        if fecha1 > fecha2:
            raise ValueError("fecha1 debe ser menor o igual que fecha2")
        
        # Función recursiva para buscar la temperatura mínima en el rango dado.
        def buscar_min(nodo):
            '''Orden de complejidad: O(log n) en el caso promedio y O(n) en el peor caso'''
            if nodo is None:
                return None
            min_izq = min_der = min_centro = None
            # Compara la clave del nodo con las fechas para determinar en qué subárbol buscar.
            # Si la clave del nodo es mayor que fecha2, busca recursivamente en el subárbol izquierdo.
            if nodo.clave > fecha2:
                return buscar_min(nodo.hijoIzquierdo)
            # Si la clave del nodo es menor que fecha1, busca recursivamente en el subárbol derecho.
            elif nodo.clave < fecha1:
                return buscar_min(nodo.hijoDerecho)
            # Si la clave del nodo está dentro del rango, compara las temperaturas.
            else:
                min_izq = buscar_min(nodo.hijoIzquierdo) 
                min_der = buscar_min(nodo.hijoDerecho)
                min_centro = nodo.cargaUtil 

            candidatos = [x for x in [min_izq, min_der, min_centro] if x is not None]
            return min(candidatos) if candidatos else None
        return buscar_min(self.avl.raiz)# busca la temperatura mínima en el árbol AVL a partir de la raíz.
    

    def temp_extremos_rango(self,fecha1, fecha2): 
        #devuelve la temperatura mínima y máxima entre los rangos fecha1 y fecha2 inclusive (fecha1 < fecha2).
        '''Orden de complejidad: O(log n) en el caso promedio y O(n) en el peor caso'''
        return self.min_temp_rango(fecha1, fecha2), self.max_temp_rango(fecha1, fecha2)
    
    
    def borrar_temperatura(self,fecha): #recibe una fecha y elimina del árbol la medición correspondiente a esa fecha.
        '''Orden de complejidad: O(log n)'''
        if not isinstance(fecha, datetime.date):
            raise ValueError("La fecha debe ser instancia de datetime.date")
        self.avl.eliminar(fecha) 


    def devolver_temperaturas(self, fecha1, fecha2):
        '''Orden de complejidad: O(n)'''
        # devuelve un listado de las mediciones de temperatura en el rango recibido por parámetro con el formato “dd/mm/aaaa: temperatura ºC”, ordenado por fechas. 
        # Verifica que las fechas sean instancias de datetime.date y que fecha1 sea menor o igual a fecha2.
        if not isinstance(fecha1, datetime.date) or not isinstance(fecha2, datetime.date):
            raise ValueError("Las fechas deben ser instancias de datetime.date")
        if fecha1>fecha2:
            raise ValueError("fecha1 debe ser <= fecha2")
        
        lista=[]

        # Función recursiva para recorrer el árbol en orden y agregar las temperaturas al listado.
        def recorrido_inorder(nodo):
            if nodo is None:
                return
            if nodo.clave >= fecha1: # Si la clave del nodo es mayor o igual a fecha1, recorre el subárbol izquierdo.
                recorrido_inorder(nodo.hijoIzquierdo)
            if fecha1 <=nodo.clave <=fecha2: # Si la clave del nodo está dentro del rango, agrega la temperatura al listado.
                lista.append(f"{nodo.clave.strftime('%d/%m/%Y')}: {nodo.cargaUtil}°C")
            if nodo.clave <=fecha2: # Si la clave del nodo es menor o igual a fecha2, recorre el subárbol derecho.
                recorrido_inorder(nodo.hijoDerecho)
        recorrido_inorder(self.avl.raiz) # inicia el recorrido desde la raíz del árbol AVL.
        return lista

    def cantidad_muestras(self):# devuelve la cantidad de muestras de la base.
        '''Orden de complejidad: O(1)'''
        return self.avl.tamano # usa la funcion tamano del árbol AVL para obtener la cantidad de muestras.

    def __str__(self):
        return "\n".join(self.devolver_temperaturas(datetime.date.min, datetime.date.max))