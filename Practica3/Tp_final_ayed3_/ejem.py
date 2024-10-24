class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.izquierda = None
        self.derecha = None

class Arbol:
    def __init__(self):
        self.raiz = None
    
    def insertar(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.raiz is None:
            self.raiz = nuevo_nodo
            return
        else:
            self._insertar_rec(self.raiz, nuevo_nodo)

    def _insertar_rec(self, actual, nuevo_nodo):
        if nuevo_nodo.dato < actual.dato:
            if actual.izquierda is None:
                actual.izquierda = nuevo_nodo
            else:
                self._insertar_rec(actual.izquierda, nuevo_nodo)
        else:
            if actual.derecha is None:
                actual.derecha = nuevo_nodo
            else:
                self._insertar_rec(actual.derecha, nuevo_nodo)

    def mostrar(self):
        self._mostrar_rec(self.raiz)

    def _mostrar_rec(self, nodo):
        if nodo is not None:
            self._mostrar_rec(nodo.izquierda)
            print(nodo.dato)
            self._mostrar_rec(nodo.derecha)


a = Arbol()
a.insertar('luciana')
a.insertar('alba')
a.insertar('z')
a.insertar('j')
a.insertar('d')
a.mostrar()
