# módulo para organizar funciones o clases utilizadas en nuestro proyecto
# Crear tantos módulos como sea necesario para organizar el código

class MonticuloBinario:
    def __init__(self):
        self.listaMonticulo=[0]
        self.tamanoActual=0

    def infiltArriba(self,i):
        while i // 2 > 0:
            if self.listaMonticulo[i][0] < self.listaMonticulo[i // 2][0] :
                tmp = self.listaMonticulo[i // 2]
                self.listaMonticulo[i // 2] = self.listaMonticulo[i]
                self.listaMonticulo[i] = tmp
            i = i // 2

    def infiltAbajo(self,i):
        while i*2 <= self.tamanoActual:
            hm = self.hijoMin(i)
            if self.listaMonticulo[i][0] > self.listaMonticulo[hm][0]:
                tmp = self.listaMonticulo[i]
                self.listaMonticulo[i] = self.listaMonticulo[hm]
                self.listaMonticulo[hm] = tmp
            i = hm

    def hijoMin(self,i):
        if i * 2 + 1 > self.tamanoActual:
            return i * 2
        else:
            if self.listaMonticulo[i*2][0] < self.listaMonticulo[i*2+1][0]:
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

    def decrementarClave(self, vertice, nuevaDistancia):
        for i in range(1, self.tamanoActual + 1):
            if self.listaMonticulo[i][1] == vertice:
                self.listaMonticulo[i] = (nuevaDistancia, vertice)
                self.infiltArriba(i)
                break

    def estaVacia(self):
        return self.tamanoActual == 0        

    def contiene(self, vertice):
        return vertice in self.posiciones
    
    def mostrar(self):
        print (self.listaMonticulo[1:])
    
    def __str__(self):
        return str(self.listaMonticulo[1:])
    
    def __contains__(self, vertice):
        return vertice in [v[1] for v in self.listaMonticulo[1:]]
    
# if __name__=="__main__":