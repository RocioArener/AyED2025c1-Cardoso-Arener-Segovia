    # def __setitem__(self,c,v):
    #      self._agregar(c,v)

    # def __getitem__(self,clave):
    #    return self.obtener(clave)

    # def __contains__(self,clave):
    #    if self._obtener(clave,self.raiz):
    #        return True
    #    else:
    #        return False

# def tieneHijoIzquierdo(self):
    #     return self.hijoIzquierdo

    # def tieneHijoDerecho(self):
    #     return self.hijoDerecho

    # def esHijoIzquierdo(self):
    #     return self.padre and self.padre.hijoIzquierdo == self

    # def esHijoDerecho(self):
    #     return self.padre and self.padre.hijoDerecho == self

    # def esRaiz(self):
    #     return not self.padre

    # def esHoja(self):
    #     return not (self.hijoDerecho or self.hijoIzquierdo)

    # def tieneAlgunHijo(self):
    #     return self.hijoDerecho or self.hijoIzquierdo

    # def tieneAmbosHijos(self):
    #     return self.hijoDerecho and self.hijoIzquierdo

    # def reemplazarDatoDeNodo(self,clave,valor,hizq,hder):
    #     self.clave = clave
    #     self.cargaUtil = valor
    #     self.hijoIzquierdo = hizq
    #     self.hijoDerecho = hder
    #     if self.tieneHijoIzquierdo():
    #         self.hijoIzquierdo.padre = self
    #     if self.tieneHijoDerecho():
    #         self.hijoDerecho.padre = self

    # def factorEquilibrio(self):
    #     if self.hijoIzquierdo and self.hijoDerecho:
    #         return self.hijoIzquierdo.factorEquilibrio() - self.hijoDerecho.factorEquilibrio()
    #     elif self.hijoIzquierdo:
    #         return 1
    #     elif self.hijoDerecho:
    #         return -1
    #     else:
    #         return 0

#en apps
    # def eliminar(self,clave):
    #   if self.tamano > 1:
    #      nodoAEliminar = self._obtener(clave,self.raiz)
    #      if nodoAEliminar:
    #          self.remover(nodoAEliminar)
    #          self.tamano = self.tamano-1
    #      else:
    #          raise KeyError('Error, la clave no está en el árbol')
    #   elif self.tamano == 1 and self.raiz.clave == clave:
    #      self.raiz = None
    #      self.tamano = self.tamano - 1
    #   else:
    #      raise KeyError('Error, la clave no está en el árbol')

    # def __delitem__(self,clave):
    #    self.eliminar(clave)

    # def empalmar(self):
    #    if self.esHoja():
    #        if self.esHijoIzquierdo():
    #               self.padre.hijoIzquierdo = None
    #        else:
    #               self.padre.hijoDerecho = None
    #    elif self.tieneAlgunHijo():
    #        if self.tieneHijoIzquierdo():
    #               if self.esHijoIzquierdo():
    #                  self.padre.hijoIzquierdo = self.hijoIzquierdo
    #               else:
    #                  self.padre.hijoDerecho = self.hijoIzquierdo
    #               self.hijoIzquierdo.padre = self.padre
    #        else:
    #               if self.esHijoIzquierdo():
    #                  self.padre.hijoIzquierdo = self.hijoDerecho
    #               else:
    #                  self.padre.hijoDerecho = self.hijoDerecho
    #               self.hijoDerecho.padre = self.padre

    # def encontrarSucesor(self):
    #   suc = None
    #   if self.tieneHijoDerecho():
    #       suc = self.hijoDerecho.encontrarMin()
    #   else:
    #       if self.padre:
    #              if self.esHijoIzquierdo():
    #                  suc = self.padre
    #              else:
    #                  self.padre.hijoDerecho = None
    #                  suc = self.padre.encontrarSucesor()
    #                  self.padre.hijoDerecho = self
    #   return suc

    # def encontrarMin(self):
    #   actual = self
    #   while actual.tieneHijoIzquierdo():
    #       actual = actual.hijoIzquierdo
    #   return actual

    # def remover(self,nodoActual):
    #      if nodoActual.esHoja(): #hoja
    #        if nodoActual == nodoActual.padre.hijoIzquierdo:
    #            nodoActual.padre.hijoIzquierdo = None
    #        else:
    #            nodoActual.padre.hijoDerecho = None
    #      elif nodoActual.tieneAmbosHijos(): #interior
    #        suc = nodoActual.encontrarSucesor()
    #        suc.empalmar()
    #        nodoActual.clave = suc.clave
    #        nodoActual.cargaUtil = suc.cargaUtil

    #      else: # este nodo tiene un (1) hijo
    #        if nodoActual.tieneHijoIzquierdo():
    #          if nodoActual.esHijoIzquierdo():
    #              nodoActual.hijoIzquierdo.padre = nodoActual.padre
    #              nodoActual.padre.hijoIzquierdo = nodoActual.hijoIzquierdo
    #          elif nodoActual.esHijoDerecho():
    #              nodoActual.hijoIzquierdo.padre = nodoActual.padre
    #              nodoActual.padre.hijoDerecho = nodoActual.hijoIzquierdo
    #          else:
    #              nodoActual.reemplazarDatoDeNodo(nodoActual.hijoIzquierdo.clave,
    #                                 nodoActual.hijoIzquierdo.cargaUtil,
    #                                 nodoActual.hijoIzquierdo.hijoIzquierdo,
    #                                 nodoActual.hijoIzquierdo.hijoDerecho)
    #        else:
    #          if nodoActual.esHijoIzquierdo():
    #              nodoActual.hijoDerecho.padre = nodoActual.padre
    #              nodoActual.padre.hijoIzquierdo = nodoActual.hijoDerecho
    #          elif nodoActual.esHijoDerecho():
    #              nodoActual.hijoDerecho.padre = nodoActual.padre
    #              nodoActual.padre.hijoDerecho = nodoActual.hijoDerecho
    #          else:
    #              nodoActual.reemplazarDatoDeNodo(nodoActual.hijoDerecho.clave,
    #                                 nodoActual.hijoDerecho.cargaUtil,
    #                                 nodoActual.hijoDerecho.hijoIzquierdo,
    #                                 nodoActual.hijoDerecho.hijoDerecho)