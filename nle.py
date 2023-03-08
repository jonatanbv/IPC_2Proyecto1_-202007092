import xml.etree.ElementTree as ET

try:
    xml_file = open('info.xml') #apertura
    #print(xml_file.read())
    if xml_file.readable():

        xml_data = ET.fromstring(xml_file.read())
        #print(xml_data)

        lst_organismos = xml_data.findall('listaOrganismos')

        for listas in lst_organismos:
            print('========== ListaOrganismos > organismos===========')
            for lis in listas:
               print(f"codigo: {lis.find('codigo').text}")
               print(f"nombre: {lis.find('nombre').text}")
        
        print('=============================================')

        lista_muestras = xml_data.findall('listadoMuestras')

        for elementos in lista_muestras:
            for el in elementos:
                print('================= listadoMuestras > Muestras =============')
                print(f"Codigo: {el.find('codigo').text}")
                print(f"descripcion: {el.find('descripcion').text}")
                print(f"filas: {el.find('filas').text}")
                print(f"columnas: {el.find('columnas').text}")
                #print(el)
                                
                celdaViva = el.find('listadoCeldasVivas')
                #print(len(celdaViva))
                print('==========================================================')
                for celdaV in celdaViva:
                    print('================== celdasVivas =========================')
                    print(f"fila: {celdaV.find('fila').text}")
                    print(f"columna: {celdaV.find('columna').text}")
                    print(f"codigoOrganismo: {celdaV.find('codigoOrganismo').text}")
    else:
        print(False)
except Exception as err:
    print('Error: ', err)
finally:
    xml_file.close() #cierre de documento