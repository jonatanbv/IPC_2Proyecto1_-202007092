from clase import *



class Nodo:

    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None



class ListaDoblementeEnlazada:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.size = 0
    
    def vacia(self):
        return self.primero == None

    def agregar_final(self, dato):
        if self.vacia():
            self.primero = self.ultimo = Nodo(dato)
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = Nodo(dato)
            self.ultimo.anterior = aux
        self.size +=1

    def agregar_inicio(self, dato):
        if self.vacia():
            self.primero = self.ultimo = Nodo(dato)
        else:
            aux = Nodo(dato)
            aux.siguiente = self.primero
            self.primero.anterior = None
            self.primero = aux
        self.size+=1

    def recorrer_inicio(self):
        aux = self.primero
        while aux != None:
            print(aux.dato)
            aux = aux.siguiente

    def recorrer_final(self):
        aux = self.ultimo
        while aux:
            print(aux.dato)
            aux = aux.anterior

    def size(self):
        return self.size

    def eliminar_inicio(self):
        if self.vacia():
            print('lista Vacia')
        elif self.primero.siguiente == None:
            self.primero = self.ultimo = None
            self.size = 0
        else:
            self.primero =self.primero.siguiente
            self.primero.anterior = None
            self.size -= 1 


    def eliminar_final(self):
        if self.vacia():
            print('lista Vacia')
        elif self.primero.siguiente == None:
            self.primero = self.ultimo = None
            self.size = 0
        else:
            self.ultimo = self.ultimo.anterior
            self.ultimo.siguiente = None
            self.size -= 1

    def obtener(self):
        aux = self.primero
        while aux != None:
            print(aux.dato.mostrar())
            print('termino')
            aux = aux.siguiente
    
    def obtenerCodigo(self):
        aux = self.primero
        while aux != None:
            print(aux.dato.codigo)
            aux = aux.siguiente




