# class Nodo:
#     def __init__(self, nombre,email,pais):
#         self.nombre = nombre
#         self.email = email
#         self.pais = pais
#         self.izquierda = None
#         self.derecha = None
class Nodo:
    def __init__(self, persona):
        self.persona = persona
        self.derecha = None
        self.izquierda = None