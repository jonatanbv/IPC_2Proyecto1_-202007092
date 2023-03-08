

class OrganismoVivo:
    def __init__(self, fila, columna, codigo):
        self.fila = fila
        self.columna = columna
        self.codigo = codigo
        self.next_organismo = None
        self.previous_organismo = None



class Muestra:
    def __init__(self):
        self.head = None
        self.firs_organismo = None
        self.Last_organism = None
    
    def add_organism(self, fila, columna, codigo):
        new_organismo = OrganismoVivo(fila, columna, codigo)
        if self.firs_organismo is None:
            self.firs_organismo = new_organismo
            self.Last_organism = new_organismo
        else:
            new_organismo.previous_organismo = self.Last_organism
            self.Last_organism.next_organismo = new_organismo
            self.Last_organism = new_organismo

    def size(self):
        size = 0
        current = self.firs_organismo

        while current:
            size +=1
            current = current.next_organismo

        return size

    def mostrar_organismos(self):
        current_organismo = self.firs_organismo
        while current_organismo:
            print(f'{current_organismo.fila} - {current_organismo.columna} - {current_organismo.codigo}')
            current_organismo = current_organismo.next_organismo
    
    def add_organismo_vivo(self, fila, columna, codigo):
        new_organismo = OrganismoVivo(fila, columna, codigo)

        new_organismo.previous_organismo = self.Last_organism
        self.Last_organism.next_organismo = new_organismo
        self.Last_organism = new_organismo
        
        current_organismo = self.firs_organismo
        while current_organismo:
            if current_organismo.codigo == new_organismo.codigo:
                if current_organismo.fila == new_organismo.fila:
                    print(f'{current_organismo.fila} - {current_organismo.columna} - {current_organismo.codigo} : estan en la misma fila')
                else:
                    print(f'{current_organismo.fila} - {current_organismo.columna} - {current_organismo.codigo} : son iguales')
            else:
                print(f'{current_organismo.fila} - {current_organismo.columna} - {current_organismo.codigo}')
            current_organismo = current_organismo.next_organismo

    def delete_organismo(self, codigo):
        current_organismo = self.firs_organismo
        while current_organismo:
            if current_organismo.codigo == codigo:
                if current_organismo == self.firs_organismo:
                    self.firs_organismo = current_organismo.next_organismo
                    self.firs_organismo.previous_organismo = None
                elif current_organismo == self.Last_organism:
                    self.Last_organism = current_organismo.previous_organismo
                    self.Last_organism.next_organismo = None
                else:
                    current_organismo.previous_organismo.next_organismo = current_organismo.next_organismo
                    current_organismo.next_organismo.previous_organismo = current_organismo.previous_organismo
                return True
            current_organismo = current_organismo.next_organismo
        return False
    
    def revisar(self):
        current_organismo = self.firs_organismo
        while current_organismo:
            current_previus = current_organismo.next_organismo.codigo
            print(f'Codigo anterior: {current_previus} // {current_organismo.fila} - {current_organismo.columna} - {current_organismo.codigo}// Codigo Organismo Siguiente: ')
            current_organismo = current_organismo.next_organismo


    def obtener_nodo_en_posicion(self, posicion):
        nodo_actual = self.firs_organismo
        for i in range(posicion):
            nodo_actual = nodo_actual.next_organismo
        return nodo_actual
    
    def obtener_anterior_actual(self, posicion):
        nodo_actual = self.obtener_nodo_en_posicion(posicion)
        nodo_anterior = nodo_actual.previous_organismo
        nodo_siguiente = nodo_actual.next_organismo

        nombre_anterior = nodo_anterior.codigo if nodo_anterior is not None else None
        nombre_actual = nodo_actual.codigo
        nombre_siguiente = nodo_siguiente.codigo if nodo_siguiente is not None else None

        return (f'codigo anterior: {nombre_anterior} codigo actual: {nombre_actual} codigo siguiente: {nombre_siguiente}')
    
    def traverse(self):
        current = self.firs_organismo
        previous = None
        next = current.next_organismo

        while current:
            print(f'Previous node: {previous.codigo}' if previous else None)
            print(f'Current Node: {current.codigo}')
            print(f'next Node: {next.codigo}' if next else None)
            print('===========')

            previous = current
            current = next
            next = current.next_organismo if current else None


muestra = Muestra()

muestra.add_organism(4,6,'fff333')
muestra.add_organism(4,6,'bbb333')
muestra.add_organism(7,4,'adfa32')
muestra.add_organism(6,3,'abdfa3')


"""#muestra.mostrar_organismos()
#muestra.add_organismo_vivo(4,6,'fafdd32')
print('========despues de agregar un organismo vivo==========')
#muestra.mostrar_organismos()

#print('===eliminando====')
#muestra.delete_organismo('fff333')
muestra.mostrar_organismos()

print('\n============agregar organismo vivo============')
muestra.add_organismo_vivo(4,1,'bbb333')
print('\n')

print('\n==================revisar===================')
muestra.revisar()"""

pos2 = muestra.obtener_nodo_en_posicion(2)
print(pos2.codigo)
print('=========== prueba =============')
print(muestra.obtener_anterior_actual(2))
print('=============fa;f ==============')
muestra.traverse()
#print(muestra.size())