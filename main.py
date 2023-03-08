from os import remove
from clase import *
from le import *





def crearTabla(ruta, columas, filas, celdasVivas):
    """Crea una tabla usando Graphviz"""
    contenido = open(ruta, 'w')

    """serivira para poder darle inicio a nuestra tabla en graphviz"""
    contenido.write('digraph L{ a0[shape=none label=<<TABLE border="1" cellspacing="0" cellpadding="15">\n')

    
    for i in range(filas):
        contenido.write('<TR>')
        for s in range(columas):
            contenido.write('<TD></TD>')
        contenido.write("</TR>")


    """servira para ponerle fin a nuestra tabla en graphviz"""
    contenido.write('\n</TABLE>>];}')
    contenido.close()

def eliminarArchivo(ruta):
    remove(ruta)

root = 'prueba2.dot'
colum = 10
row = 10

def agregarOrganismo(columna, fila):
    print('se agrego un aroganismo a la posicion x: ', columna, ' Y: ', fila)


celdaV = CeldaViva(2,3,'5454', 'red')
celdV2 = CeldaViva(4,2,'3456','yellow')
celdV3 = CeldaViva(6,2,'5432','gray')

organismoA = Organismo('badfka32', 'tipo A', 'red')
organismoB = Organismo('bfadk34', 'tipo B', 'yellow')
organismoC = Organismo('54fda43', 'tipo C', 'azul')


try:
    if __name__ == "__main__":
        lista = ListaDoblementeEnlazada()
        lista2 = ListaDoblementeEnlazada()
        lista.agregar_inicio(organismoA)
        lista.agregar_inicio(organismoB)
        lista.agregar_inicio(organismoC)
        lista2.agregar_inicio(celdaV)
        lista2.agregar_inicio(celdV2)
        lista2.agregar_inicio(celdV3)
       # lista.agregar_inicio(34)
        #lista.recorrer_inicio()
        lista.obtener()
        lista.obtenerCodigo()
        print('???????????????????????????????')
        lista2.obtener()
        



except Exception as e:
    print(e)

mue = Muestra('esto es una prueba', '4321fbs', 6,7)

#miMuestra = Muestra('Esto es una prueba', '5211', 10, 10)

#eliminarArchivo(root)
#eliminarArchivo('prueba1.dot')
#crearTabla(root, mue.columnas, mue.filas)

