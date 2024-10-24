
import csv
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.izquierda = None
        self.derecha = None
class Persona:
    def __init__(self, name, email, country):
        self.name = name
        self.email = email
        self.country = country


class Arbol:
    def __init__(self):
        self.raiz = None
    
    def insertar(self, dato, criterio):
        nuevo_nodo = Nodo(dato)
        if self.raiz is None:
            self.raiz = nuevo_nodo
            return
        else:
            self._insertar_rec(self.raiz, nuevo_nodo, criterio)

    def _insertar_rec(self, actual, nuevo_nodo, criterio):
        if criterio == "nombre":
            if nuevo_nodo.dato.name < actual.dato.name:
                if actual.izquierda is None:
                    actual.izquierda = nuevo_nodo
                else:
                    self._insertar_rec(actual.izquierda, nuevo_nodo, criterio)
            else:
                if actual.derecha is None:
                    actual.derecha = nuevo_nodo
                else:
                    self._insertar_rec(actual.derecha, nuevo_nodo, criterio)
        if criterio == "pais":
            if nuevo_nodo.dato.country < actual.dato.country:
                if actual.izquierda is None:
                    actual.izquierda = nuevo_nodo
                else:
                    self._insertar_rec(actual.izquierda, nuevo_nodo, criterio)
            else:
                if actual.derecha is None:
                    actual.derecha = nuevo_nodo
                else:
                    self._insertar_rec(actual.derecha, nuevo_nodo, criterio)
        if criterio == "email":
            if nuevo_nodo.dato.email < actual.dato.email:
                if actual.izquierda is None:
                    actual.izquierda = nuevo_nodo
                else:
                    self._insertar_rec(actual.izquierda, nuevo_nodo, criterio)
            else:
                if actual.derecha is None:
                    actual.derecha = nuevo_nodo
                else:
                    self._insertar_rec(actual.derecha, nuevo_nodo, criterio)

    def mostrar(self, criterio):
        print(criterio)
        self._mostrar_rec(self.raiz, criterio)

    def _mostrar_rec(self, nodo, criterio):
        if nodo is not None:
            self._mostrar_rec(nodo.izquierda, criterio)
            if criterio == "nombre":
                print(nodo.dato.name)
            elif criterio == "email":
                print(nodo.dato.email)
            else:
                print(nodo.dato.country)
            # print(nodo.dato.name)
            self._mostrar_rec(nodo.derecha, criterio)

def crear_persona(ruta_archivo):
        personas = []
        with open(ruta_archivo, mode='r', newline='') as archivo_csv:
            lector_csv = csv.DictReader(archivo_csv)
            for fila in lector_csv:
                persona = Persona(
                    name=fila['name'],
                    email=fila['email'],
                    country=fila['country']
                )
                personas.append(persona)
                #print(persona.country)
        return personas 

def insertar_personas(personas):
    a = Arbol()
    for persona in personas:
        a.insertar(persona, criterio)
    return a
                
personas = crear_persona('/home/maquina6/Escritorio/Practica3/Tp_final_ayed3_/data.csv')

criterio = input("escriba un criterio de orden para el arbol, puede ser por nombre, email o pais: ")

def escribir_nuevo_csv(csv):
    csv = insertar_personas(personas)
    with open('ordenado.csv', 'w', newline='') as archivo_csv:
        datos = [
            csv.datos
        ]
        escritor_csv = csv.writer(archivo_csv)
        for fila in datos:
            escritor_csv.writerow(fila)
    

a = Arbol()
b = insertar_personas(personas)
b.mostrar(criterio)


