from modules.cola_de_prioridad import MonticuloBinario
import sys

class Vertice:
    def __init__(self,clave, distancia=sys.maxsize, predecesor=None):
        self.distancia = distancia
        self.predecesor = predecesor
        self.id = clave
        self.conectadoA = {}

    def agregarVecino(self,vecino,ponderacion=0):
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
    

class Grafo:
    def __init__(self):
        self.listaVertices = {}
        self.numVertices = 0

    def agregarVertice(self,clave):
        self.numVertices = self.numVertices + 1
        nuevoVertice = Vertice(clave)
        self.listaVertices[clave] = nuevoVertice
        return nuevoVertice

    def obtenerVertice(self,n):
        lista = list(self.listaVertices.keys()) #convierto el diccionario a lista
        if n in self.listaVertices:
            return self.listaVertices[n]
        else:
            return None
        
    def ordenarGrafo(self,):
        grafo_ordenado = sorted(self.listaVertices, key=lambda item: item[0])   
        return grafo_ordenado

    def __contains__(self,n):
        return n in self.listaVertices

    def agregarArista(self,origen,destino,costo=0):
        if origen not in self.listaVertices:
            nv = self.agregarVertice(origen)
        if destino not in self.listaVertices:
            nv = self.agregarVertice(destino)
        self.listaVertices[origen].agregarVecino(self.listaVertices[destino], costo)

    def obtenerVertices(self):
        return self.listaVertices.keys()

    def __iter__(self):
        return iter(self.listaVertices.values())
    
    def cargarGrafo(self,archivo):
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

    # def asignarDistancia(self, distancia):
    #     self.distancia = distancia
    
    # def asignarPredecesor(self, predecesor):
    #     self.predecesor = predecesor

    # def decrementarClave(self, vertice, nuevaDistancia):
    #     if vertice in self.listaVertices:
    #         vertice.asignarDistancia(nuevaDistancia)
    

def prim(G,inicio):
    # Obtener el objeto Vertice desde el ID
    inicio = G.obtenerVertice(inicio.id)
    if inicio is None:
        raise ValueError(f"El vértice {inicio.id} no existe en el grafo")
    cp = MonticuloBinario()
    for v in G:
        v.asignarDistancia(sys.maxsize)
        v.asignarPredecesor(None)
    inicio.asignarDistancia(0)
    for v in G:
        cp.insertar((v.obtenerDistancia(), v))
    while not cp.estaVacia():
        distanciaActual, verticeActual = cp.eliminarMin()
        for verticeSiguiente in verticeActual.obtenerConexiones():
            nuevoCosto = verticeActual.obtenerPonderacion(verticeSiguiente)
        #   if verticeSiguiente in cp and nuevoCosto<verticeSiguiente.obtenerDistancia():
        #       verticeSiguiente.asignarPredecesor(verticeActual)
        #       verticeSiguiente.asignarDistancia(nuevoCosto)
        #       cp.decrementarClave(verticeSiguiente,nuevoCosto)
            if nuevoCosto < verticeSiguiente.obtenerDistancia():
                verticeSiguiente.asignarPredecesor(verticeActual)
                verticeSiguiente.asignarDistancia(nuevoCosto)
                # Actualizar la prioridad en el montículo
                cp.insertar((nuevoCosto, verticeSiguiente))
        
    # while not colaprioridad.estaVacia():
    #     verticeActual = colaprioridad.eliminarMin()
    #     for verticeSiguiente in verticeActual.obtenerConexiones():
    #       nuevoCosto = verticeActual.obtenerPonderacion(verticeSiguiente)
    #       if verticeSiguiente in colaprioridad and nuevoCosto<verticeSiguiente.obtenerDistancia():
    #           #verfica que no haya pasado por ese vertice y el nuevo costo sea menor al costo guardado
    #           verticeSiguiente.asignarPredecesor(verticeActual)
    #           verticeSiguiente.asignarDistancia(nuevoCosto)
    #           colaprioridad.decrementarClave(verticeSiguiente,nuevoCosto)         
    
if __name__ == "__main__":
    g = Grafo()
    ruta="data/aldeas.txt"
    print(ruta)
    g.cargarGrafo(ruta)

    # Para cada aldea, mostrar de qué vecina debería recibir la noticia, y a qué vecinas debería enviar réplicas, 
    # siendo que se está enviando el mensaje de la forma más eficiente a las 21 aldeas. Tomar en cuenta que desde 
    # Peligros solamente se envían noticias a una o más aldeas vecinas.

    for v in g: #Itera sobre cada vértice (aldea) en el grafo
        for vecino in v.obtenerConexiones(): #Itera sobre las conexiones del vértice v
            print(f"{v.obtenerId()} -> {vecino.obtenerId()} con ponderacion {v.obtenerPonderacion(vecino)}")
        print(v)
    
    print("vertice:", v)# se imprime el ultimo v porque es el ultimo que queda guardado al recorrer todo el grafo
    print("------------------------")
    print("Grafo ordenado:") 
    print(g.ordenarGrafo()) # devuelve el grafo ordenado alfabeticamente por los nombres de origen
    print("------------------------")
    print("Vertices del grafo:", g.obtenerVertices())
    print("------------------------")
    print("Vertice 2:", g.obtenerVertice('2')) #no se puede encontrar el vertice '2' porque id son los nombresde los
    #publos y obtener vertices devuelve los  vecinos de cada vertice (pueblo)
    v = g.obtenerVertice('Cebolla')  # Obtiene el vértice con id 'Cebolla'
    print("------------------------")
    print("cada pueblo deberia enviarle mensajes a:", prim(g, g.obtenerVertice('Peligros')))  # Ejecuta el algoritmo de Prim a partir del vértice 'Peligros'
    print("------------------------")
