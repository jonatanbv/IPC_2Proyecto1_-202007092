class Organismo:
    def __init__(self, codigo, nombre, color):
        self.codigo = codigo
        self.nombre = nombre
        self.color = color

    def mostrar(self):
        if not None:
            print(f'nombre: {self.nombre}')
            print(f'codigo: {self.codigo}')
            print(f'color: {self.color}')


class CeldaViva:
    def __init__(self, fila, columna, codigo, color):
        self.fila = fila
        self.columna = columna
        self.codigo = codigo
        self.color = color

    def mostrar(self):
        print(f'columna: {self.columna}')
        print(f'fila: {self.fila}')
        print(f'codigo: {self.codigo}')
        print(f'color: {self.color}')

    def color(self):
        return print(f'color: {self.color}')


class Muestra:
    def __init__(self, descripcion, codigo, filas, columnas):
        self.descripcion = descripcion
        self.codigo = codigo
        self.filas = filas
        self.columnas = columnas

    def mostrarInfo(self):
        print(f'Descripcion: {self.descripcion}')
        print(f'Codigo: {self.codigo}')
        print(f'Filas: {self.filas}')
        print(f'Columnas: {self.columnas}')


