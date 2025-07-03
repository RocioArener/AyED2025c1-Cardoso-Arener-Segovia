# módulo para organizar funciones o clases utilizadas en nuestro proyecto
# Crear tantos módulos como sea necesario para organizar el código

class MonticuloBinario:
    """
    Implementación de una Cola de Prioridad mediante un Montículo Binario de Mínimos.

    Esta estructura de datos mantiene los elementos en un orden tal que el elemento
    con la menor prioridad (en este caso, el primer elemento de la tupla)
    siempre se encuentra en la raíz del montículo. Utiliza una lista para
    representar el árbol completo.
    """
    def __init__(self):
        """
        Inicializa un montículo binario vacío.

        El montículo se representa con una lista donde el primer elemento (índice 0)
        es un cero para simplificar la aritmética de los índices.
        """
        self.listaMonticulo=[0]
        self.tamanoActual=0

    def infiltArriba(self,i):
        """
        Mueve un nodo hacia arriba en el árbol para mantener la propiedad del montículo.

        Args:
            i (int): El índice del nodo a infiltrar hacia arriba.

        Complejidad: O(log n), donde n es el tamaño del montículo. En el peor caso,
                     el elemento sube desde la hoja hasta la raíz, recorriendo la
                     altura del árbol, que es logarítmica.
        """
        while i // 2 > 0:
            if self.listaMonticulo[i][0] < self.listaMonticulo[i // 2][0] :
                tmp = self.listaMonticulo[i // 2]
                self.listaMonticulo[i // 2] = self.listaMonticulo[i]
                self.listaMonticulo[i] = tmp
            i = i // 2

    def infiltAbajo(self,i):
        """
        Mueve un nodo hacia abajo en el árbol para mantener la propiedad del montículo.

        Args:
            i (int): El índice del nodo a infiltrar hacia abajo.

        Complejidad: O(log n), donde n es el tamaño del montículo. En el peor caso,
                     el elemento baja desde la raíz hasta una hoja, recorriendo la
                     altura del árbol.
        """
        while i*2 <= self.tamanoActual:
            hm = self.hijoMin(i)
            if self.listaMonticulo[i][0] > self.listaMonticulo[hm][0]:
                tmp = self.listaMonticulo[i]
                self.listaMonticulo[i] = self.listaMonticulo[hm]
                self.listaMonticulo[hm] = tmp
            i = hm

    def hijoMin(self,i):
        """
        Encuentra el índice del hijo con el menor valor.

        Args:
            i (int): El índice del nodo padre.

        Returns:
            int: El índice del hijo con el menor valor.

        Complejidad: O(1), ya que solo realiza un par de comparaciones y cálculos.
        """
        if i * 2 + 1 > self.tamanoActual:
            return i * 2
        else:
            if self.listaMonticulo[i*2][0] < self.listaMonticulo[i*2+1][0]:
                return i * 2
            else:
                return i * 2 + 1
    
    def insertar(self,k):
        """
        Agrega un nuevo elemento al montículo.

        Args:
            k (tuple): El elemento a insertar.

        Complejidad: O(log n), dominada por la llamada a `infiltArriba`.
        """
        self.listaMonticulo.append(k)
        self.tamanoActual = self.tamanoActual + 1
        self.infiltArriba(self.tamanoActual)

    def eliminarMin(self):
        """
        Elimina y devuelve el elemento con la mínima prioridad (la raíz).

        Returns:
            tuple: El elemento que estaba en la raíz del montículo.

        Complejidad: O(log n), dominada por la llamada a `infiltAbajo`.
        """
        valorSacado = self.listaMonticulo[1]
        self.listaMonticulo[1] = self.listaMonticulo[self.tamanoActual]
        self.tamanoActual = self.tamanoActual - 1
        self.listaMonticulo.pop()
        self.infiltAbajo(1)
        return valorSacado

    def decrementarClave(self, vertice, nuevaDistancia):
        """
        Actualiza la distancia (prioridad) de un vértice en el montículo.

        Args:
            vertice (Vertice): El objeto vértice cuya clave debe ser decrementada.
            nuevaDistancia (float/int): El nuevo valor de la distancia (prioridad).
        
        Complejidad: O(n), donde n es el tamaño del montículo. La implementación
                     actual realiza una búsqueda lineal (O(n)) para encontrar el vértice.
                     Luego, `infiltArriba` es O(log n). El término dominante es O(n).
        """
        for i in range(1, self.tamanoActual + 1):
            if self.listaMonticulo[i][1] == vertice:
                self.listaMonticulo[i] = (nuevaDistancia, vertice)
                self.infiltArriba(i)
                break

    def estaVacia(self):
        """
        Verifica si el montículo está vacío.

        Returns:
            bool: True si el montículo no tiene elementos, False en caso contrario.
        
        Complejidad: O(1).
        """
        return self.tamanoActual == 0        

    def contiene(self, vertice):

        return vertice in self.posiciones
    
    def mostrar(self):
        print (self.listaMonticulo[1:])
    
    def __str__(self):
        return str(self.listaMonticulo[1:])
    
    def __contains__(self, vertice):
        """
        Permite el uso del operador 'in' para verificar la existencia de un vértice.

        Args:
            vertice (Vertice): El vértice a buscar en el montículo.

        Returns:
            bool: True si el vértice está en el montículo, False en caso contrario.

        Complejidad: O(n), ya que realiza una búsqueda lineal sobre la lista interna.
        """
        return vertice in [v[1] for v in self.listaMonticulo[1:]]
    
# if __name__=="__main__":