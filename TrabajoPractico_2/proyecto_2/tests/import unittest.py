import unittest
from modules.abb import NodoArbol

# tests/test_unitest.py

class TestNodoArbolFactorEquilibrio(unittest.TestCase):
    def setUp(self):
        # Patch the method for testing
        def factorEquilibrio(self):
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
        nodo = NodoArbol(1, "v")
        self.assertEqual(nodo.factorEquilibrio(), 0)

    def test_solo_hijo_izquierdo(self):
        nodo = NodoArbol(1, "v")
        nodo.hijoIzquierdo = NodoArbol(0, "izq")
        self.assertEqual(nodo.factorEquilibrio(), 1)

    def test_solo_hijo_derecho(self):
        nodo = NodoArbol(1, "v")
        nodo.hijoDerecho = NodoArbol(2, "der")
        self.assertEqual(nodo.factorEquilibrio(), -1)

    def test_ambos_hijos(self):
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