from nodo import Nodo
import csv

class Persona:
    def __init__(self, name, email, country):
        self.name = name
        self.email = email
        self.country = country

# with open('data.csv') as file:
#     csv_reader = csv.reader(file, delimiter=',')

#     for row in csv_reader:
#         print(row)



class ArbolB:
    def __init__(self, persona):
        self.raiz = Nodo(persona)


    def __agregar_recursivo(self, nodo, persona):
        if persona.name < nodo.persona.name:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(persona)
            else:
                self.__agregar_recursivo(nodo.izquierda, persona)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(persona)
            else:
                self.__agregar_recursivo(nodo.derecha, persona)

    def __inorden_recursivo(self, nodo):
        if nodo is not None:
            self.__inorden_recursivo(nodo.izquierda)
            print(nodo.persona, end=", ")
            self.__inorden_recursivo(nodo.derecha)

    def __preorden_recursivo(self, nodo):
        if nodo is not None:
            print(nodo.persona, end=", ")
            self.__preorden_recursivo(nodo.izquierda)
            self.__preorden_recursivo(nodo.derecha)

    def __postorden_recursivo(self, nodo):
        if nodo is not None:
            self.__postorden_recursivo(nodo.izquierda)
            self.__postorden_recursivo(nodo.derecha)
            print(nodo.persona, end=", ")

    def __buscar(self, nodo, busqueda):
        if nodo is None:
            return None
        if nodo.dato == busqueda:
            return nodo
        if busqueda < nodo.persona:
            return self.__buscar(nodo.izquierda, busqueda)
        else:
            return self.__buscar(nodo.derecha, busqueda)
    
    def obtener_hijo_izquierdo(self, nodo):
        pila = []
        while nodo.izquierda is not None:
            pila.append(nodo.izquierda)
            nodo = nodo.izquierda
        for i in pila:
            print(i.pesona)
            
    
    def obtener_raiz(self):
        return self.raiz.persona

    def agregar(self, persona):
        self.__agregar_recursivo(self.raiz, persona)

    def inorden(self):
        print("Imprimiendo árbol inorden: ")
        # self.__inorden_recursivo(self.raiz)
        self.__inorden_recursivo(self.raiz)
        print("")

    def preorden(self):
        print("Imprimiendo árbol preorden: ")
        self.__preorden_recursivo(self.raiz)
        print("")

    def postorden(self):
        print("Imprimiendo árbol postorden: ")
        self.__postorden_recursivo(self.raiz)
        print("")

    def buscar(self, busqueda):
        return self.__buscar(self.raiz, busqueda)
    

def crear_persona(ruta_archivo):
        personas = []
        with open('data.csv', mode='r', newline='') as archivo_csv:
            lector_csv = csv.DictReader(archivo_csv)
            for fila in lector_csv:
                persona = Persona(
                    name=fila['name'],
                    email=fila['email'],
                    country=fila['country']
                )
                personas.append(persona)
                # print(persona.country)
        return personas            
def insertar_personas(personas):
    
    for persona in personas:
        if persona != None:
            a = ArbolB(persona)
            a.agregar(persona)
            print(persona.name)
        


insertar_personas(crear_persona('/home/maquina6/Escritorio/Tp_final_ayed3_/data.csv'))

# a = Arbol(8)
# a.agregar(3)
# a.agregar(1)
# a.agregar(6)
# a.agregar(4)
# a.agregar(11)
# a.agregar(13)
# a.agregar(100)
# a.agregar(10)
# a.agregar(2)
# a.inorden()
# a.postorden()
# a.preorden()
a = ArbolB()
a.inorden()
