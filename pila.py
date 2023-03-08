

class Nodo():
    dato = None
    siguiente = None

    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None



def agregarAlFinalizar(nodo_inicial, dato):
    nuevo_nodo = Nodo(dato)
    if nodo_inicial == None:
        nodo_inicial = nuevo_nodo
        return nodo_inicial
    temporal = nodo_inicial
    while temporal.siguiente:
        temporal = temporal.siguiente
    temporal.siguiente = nuevo_nodo
    return nodo_inicial


def agregarAlInicio(nodo_inicial, dato):
    nuevo_nodo = Nodo(dato)
    nuevo_nodo.siguiente = nodo_inicial
    return nuevo_nodo


def imprimirLista(nodo):
    while nodo != None:
        print(f"tenemos {nodo.dato}")
        nodo = nodo.siguiente

    
def obtenerCabeza(nodo_inicial):
    return nodo_inicial

def obtener_cola(nodo_inicial):
    temporal = nodo_inicial
    while temporal.siguiente:
        temporal = temporal.siguiente

    return temporal

def existe(nodo, busqueda):
    while nodo != None:
        if nodo.dato == busqueda:
            return True
        nodo = nodo.siguiente
    return False


def eliminar(nodo, busqueda):
    if nodo == None:
        return 
    if nodo.dato == busqueda:
        return nodo.siguiente

    temporal = nodo
    while temporal.siguiente != None:
        if temporal.siguiente.dato == busqueda:
            if temporal.siguiente.siguiente != None:
                temporal.siguiente = temporal.siguiente.siguiente
            
            else:
                temporal.siguiente = None
                return nodo
        temporal = temporal.siguiente
    
    return nodo

class Muestra:
    def __init__(self, codigo, descripcion):
        self.codigo = codigo
        self.descripcion = descripcion
        

def main():
    lista = None
    lista = agregarAlFinalizar(lista, Muestra('nose', 'nose'))
    lista = agregarAlFinalizar(lista, '2')
    lista = agregarAlFinalizar(lista, '3')
    lista = agregarAlInicio(lista, '4')

    print('antes de eliminar: ')
    imprimirLista(lista) # basquetbol, box, futbol

    lista = eliminar(lista, '2')
    print('despues de eliminar: ')
    imprimirLista(lista)


main()