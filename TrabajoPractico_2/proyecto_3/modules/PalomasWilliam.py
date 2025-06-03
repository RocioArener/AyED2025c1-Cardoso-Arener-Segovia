from modules.cola_de_prioridad import MonticuloBinario
import sys

class Vertice:
    def __init__(self,clave):
        self.id = clave
        self.conectadoA = {}

    def agregarVecino(self,vecino,ponderacion=0):
        self.conectadoA[vecino] = ponderacion

    def __str__(self):
        return str(self.id) + ' conectadoA: ' + str([x.id for x in self.conectadoA])

    def obtenerConexiones(self):
        return self.conectadoA.keys()

    def obtenerId(self):
        return self.id

    def obtenerPonderacion(self,vecino):
        return self.conectadoA[vecino]
    

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

    def asignarDistancia(self, distancia):
        self.distancia = distancia
    
    def asignarPredecesor(self, predecesor):
        self.predecesor = predecesor

    def decrementarClave(self, vertice, nuevaDistancia):
        if vertice in self.listaVertices:
            vertice.asignarDistancia(nuevaDistancia)
    
    def ordenAlfabetico(self):
        

def prim(G,inicio):
    cp = MonticuloBinario()
    for v in G:
        v.asignarDistancia(sys.maxsize)
        v.asignarPredecesor(None)
    inicio.asignarDistancia(0)
    cp.construirMonticulo([(v.obtenerDistancia(),v) for v in G])
    while not cp.estaVacia():
        verticeActual = cp.eliminarMin()
        for verticeSiguiente in verticeActual.obtenerConexiones():
          nuevoCosto = verticeActual.obtenerPonderacion(verticeSiguiente)
          if verticeSiguiente in cp and nuevoCosto<verticeSiguiente.obtenerDistancia():
              #verfica que no haya pasado por ese vertice y el nuevo costo sea menor al costo guardado
              verticeSiguiente.asignarPredecesor(verticeActual)
              verticeSiguiente.asignarDistancia(nuevoCosto)
              cp.decrementarClave(verticeSiguiente,nuevoCosto)
    

if __name__ == "__main__":
    g = Grafo()
    ruta="data/aldeas.txt"
    print(ruta)
    g.cargarGrafo(ruta)
    for v in g:
        for w in v.obtenerConexiones():
            print(f"{v.obtenerId()} -> {w.obtenerId()} con ponderacion {v.obtenerPonderacion(w)}")
        print(v)
    print("Vertices del grafo:", g.obtenerVertices())
    print("Vertice 2:", g.obtenerVertice('2'))
    print("Conexiones de A:", g.obtenerVertice('2'))