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
    
    def obtenerDistancia(self):
        return self.distancia
    

    

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
        if n in self.listaVertices:
            return self.listaVertices[n]
        else:
            return None
        
    def ordenarGrafo(self,):
        grafo_ordenado = sorted(self.listaVertices, key=lambda item: item[0])   
        return grafo_ordenado

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


    def prim(self,inicio):
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
