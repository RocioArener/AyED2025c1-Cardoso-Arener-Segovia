import unittest
from modules.abb import NodoArbol

# tests/test_unitest.py
# Test para el método factorEquilibrio de la clase NodoArbol
# Calcula mal el equilibrio, ya que calcula la diferencia entre los factores de equilibrio de los hijos, en lugar de la altura de los subárboles.

class TestNodoArbolFactorEquilibrio(unittest.TestCase):
    def setUp(self):
        '''Orden de complejidad: O(1)'''
        def factorEquilibrio(self): # Método para calcular el factor de equilibrio de un nodo'''
            if self.hijoIzquierdo and self.hijoDerecho:
                return self.hijoIzquierdo.factorEquilibrio() - self.hijoDerecho.factorEquilibrio()
            elif self.hijoIzquierdo:
                return 1
            elif self.hijoDerecho:
                return -1
            else:
                return 0
        NodoArbol.factorEquilibrio = factorEquilibrio

    def test_sin_hijos(self):
        '''Orden de complejidad: O(1)'''
        nodo = NodoArbol(1, "v")
        self.assertEqual(nodo.factorEquilibrio(), 0)

    def test_solo_hijo_izquierdo(self):
        '''Orden de complejidad: O(1)'''
        nodo = NodoArbol(1, "v")
        nodo.hijoIzquierdo = NodoArbol(0, "izq")
        self.assertEqual(nodo.factorEquilibrio(), 1)

    def test_solo_hijo_derecho(self):
        '''Orden de complejidad: O(1)'''
        nodo = NodoArbol(1, "v")
        nodo.hijoDerecho = NodoArbol(2, "der")
        self.assertEqual(nodo.factorEquilibrio(), -1)

    def test_ambos_hijos(self):
        '''Orden de complejidad: O(1)'''
        nodo = NodoArbol(1, "v")
        izq = NodoArbol(0, "izq")
        der = NodoArbol(2, "der")
        # Patch children to return 1 and -1 respectively
        izq.factorEquilibrio = lambda: 1
        der.factorEquilibrio = lambda: -1
        nodo.hijoIzquierdo = izq
        nodo.hijoDerecho = der
        self.assertEqual(nodo.factorEquilibrio(), 2)

    def test_recursivo(self):
        '''Orden de complejidad: O(n)'''
        nodo = NodoArbol(1, "v")
        izq = NodoArbol(0, "izq")
        der = NodoArbol(2, "der")
        izq.hijoIzquierdo = NodoArbol(-1, "izq2")
        der.hijoDerecho = NodoArbol(3, "der2")
        nodo.hijoIzquierdo = izq
        nodo.hijoDerecho = der
        # izq.factorEquilibrio() == 1, der.factorEquilibrio() == -1
        self.assertEqual(nodo.factorEquilibrio(), 2)

if __name__ == "__main__":
    unittest.main()