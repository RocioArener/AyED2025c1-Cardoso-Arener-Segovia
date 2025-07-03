from modules.cola_de_prioridad import MonticuloBinario
import sys

class Vertice:
    """
    Representa un vértice (o nodo) en un grafo.
    """
    def __init__(self,clave, distancia=sys.maxsize, predecesor=None):
        """
        Inicializa un nuevo vértice.

        Args:
            clave (any): El identificador único del vértice.
            distancia (float/int, optional): Distancia desde un origen. Defaults to sys.maxsize.
            predecesor (Vertice, optional): Vértice predecesor en un camino. Defaults to None.
        
        Complejidad: O(1).
        """
        self.distancia = distancia
        self.predecesor = predecesor
        self.id = clave
        self.conectadoA = {}

    def agregarVecino(self,vecino,ponderacion=0):
        """
        Agrega una conexión desde este vértice a otro.

        Args:
            vecino (Vertice): El objeto vértice al que se conecta.
            ponderacion (int, optional): El peso de la arista. Defaults to 0.
        
        Complejidad: O(1) en promedio para la inserción en el diccionario.
        """
        self.conectadoA[vecino] = ponderacion

    def __str__(self):
        return str(self.id) + ' conectado a: ' + str([x.id for x in self.conectadoA])

    def obtenerConexiones(self):
        return self.conectadoA.keys()

    def obtenerId(self):
        return self.id

    def obtenerPonderacion(self,vecino):
        return self.conectadoA[vecino]
    
    def asignarDistancia(self, distancia):
        self.distancia = distancia

    def asignarPredecesor(self, predecesor):
        self.predecesor = predecesor
    
    def obtenerDistancia(self):
        return self.distancia
    

    

class Grafo:
    """
    Implementación de un TAD Grafo utilizando una lista de adyacencias.
    """
    def __init__(self):
        """
        Inicializa un grafo vacío.
        
        Complejidad: O(1).
        """
        self.listaVertices = {}
        self.numVertices = 0

    def agregarVertice(self,clave):
        """
        Agrega un nuevo vértice al grafo.

        Args:
            clave (any): El identificador del nuevo vértice.

        Returns:
            Vertice: El nuevo objeto vértice creado.

        Complejidad: O(1) en promedio para la inserción en el diccionario.
        """
        self.numVertices = self.numVertices + 1
        nuevoVertice = Vertice(clave)
        self.listaVertices[clave] = nuevoVertice
        return nuevoVertice

    def obtenerVertice(self,n):
        """
        Busca y devuelve un vértice del grafo.

        Args:
            n (any): La clave del vértice a buscar.

        Returns:
            Vertice or None: El objeto vértice si se encuentra, de lo contrario None.
        
        Complejidad: O(1) en promedio para la búsqueda en el diccionario.
        """
        if n in self.listaVertices:
            return self.listaVertices[n]
        else:
            return None
        
    def ordenarGrafo(self,):
        """
        Devuelve una lista de las claves de los vértices ordenadas alfabéticamente.

        Returns:
            list: Una lista de las claves de los vértices ordenadas.
        
        Complejidad: O(V log V), donde V es el número de vértices, debido al
                     costo del algoritmo de ordenamiento `sorted()`.
        """
        grafo_ordenado = sorted(self.listaVertices, key=lambda item: item[0])   
        return grafo_ordenado

    def agregarArista(self,origen,destino,costo=0):
        """
        Agrega una arista dirigida y ponderada entre dos vértices.

        Args:
            origen (any): La clave del vértice de origen.
            destino (any): La clave del vértice de destino.
            costo (int, optional): El peso de la arista. Defaults to 0.
        
        Complejidad: O(1) en promedio, ya que involucra búsquedas e inserciones
                     en diccionarios.
        """
        if origen not in self.listaVertices:
            nv = self.agregarVertice(origen)
        if destino not in self.listaVertices:
            nv = self.agregarVertice(destino)
        self.listaVertices[origen].agregarVecino(self.listaVertices[destino], costo)

    def obtenerVertices(self):
        """
        Devuelve las claves de los vértices del grafo.
        
        Complejidad: O(V) para crear la lista de claves.
        """
        return self.listaVertices.keys()

    def __iter__(self):
        """Permite iterar sobre los objetos vértice del grafo."""
        return iter(self.listaVertices.values())
    
    def cargarGrafo(self,archivo):
        """
        Carga un grafo desde un archivo de texto.

        Args:
            archivo (str): La ruta al archivo de datos.

        Complejidad: O(E_file), donde E_file es el número de líneas (aristas)
                     en el archivo, ya que `agregarArista` es O(1).
        """
        with open("data/aldeas.txt", 'r') as f:
            for linea in f:
                #print(linea)
                datos = linea.strip().split(',')
                #print(datos)
                origen = datos[0].strip()
                a = datos[1].strip()
                costo = datos[2].strip()
                print(f"Agregando arista de {origen} a {a} con costo {costo}")
                self.agregarArista(origen, a, int(costo)) 


    def prim(self,inicio):
        """
        Ejecuta el algoritmo de Prim para encontrar el Árbol de Expansión Mínimo (AEM).

        Args:
            inicio (Vertice): El vértice desde el cual comenzar a construir el AEM.
        
        Complejidad Teórica: O((V+E) log V) o O(E log V) con una implementación
                              optimizada de la cola de prioridad.
        
        Complejidad de esta Implementación: O(E * V). La ineficiencia se debe
                                             a que las operaciones `in cp` y
                                             `decrementarClave` dentro del bucle
                                             son O(V) en lugar de O(log V). El bucle
                                             se ejecuta E veces en el peor caso, llevando
                                             a una complejidad total de O(E * V).
        """
        cp = MonticuloBinario()
        for v in self:
            v.asignarDistancia(sys.maxsize)
            v.asignarPredecesor(None)
        inicio.asignarDistancia(0)
        for v in self:
            cp.insertar((v.obtenerDistancia(), v))
            
        while not cp.estaVacia():
            verticeActual = cp.eliminarMin()[1]
            for verticeSiguiente in verticeActual.obtenerConexiones():
                nuevoCosto = verticeActual.obtenerPonderacion(verticeSiguiente)
                if verticeSiguiente in cp and nuevoCosto < verticeSiguiente.obtenerDistancia():
                    verticeSiguiente.asignarPredecesor(verticeActual)
                    verticeSiguiente.asignarDistancia(nuevoCosto)
                    cp.decrementarClave(verticeSiguiente,nuevoCosto)
            print(f"El mensaje se envia desde aldea {verticeSiguiente.obtenerId()} a aldea {verticeActual.obtenerId()} ")  

        
if __name__ == "__main__":
    g = Grafo()
    ruta="data/aldeas.txt"
    print(ruta)
    g.cargarGrafo(ruta)

    print("------------------------") 
    print("Grafo ordenado:") 
    print(g.ordenarGrafo()) # devuelve el grafo ordenado alfabeticamente por los nombres de origen
    print("------------------------")
    g.prim(g.obtenerVertice('Peligros'))  # Ejecuta el algoritmo de Prim a partir del vértice 'Peligros'
    distancia=0
    for v in g:
        distancia+=v.obtenerDistancia()
    print("------------------------")
    print(f'La suma de todas las distancias recorridas por todas las palomas enviadas desde cada palomar es {distancia} leguas')
    print("------------------------")
   # Obtiene las conexiones del vértice 'Peligros'
