# Prueba de la camara

from camera import Save

Aparatos = [[ 0.5,  1.5,  0.5],
 [ 2.5,  1.5, -2.5]]
queaparatos = ['10', '8']
extremostubos= [[ 0.5,  1.5,  0.5],
 [-2.5,  1.5,  0.5],
 [-2.5,  1.5,  0.5],
 [-2.5,  1.5, -2.5],
 [-2.5,  1.5, -2.5],
 [ 2.5,  1.5, -2.5]]
cuantostubos = 3

strlist = '[[0,1,2],[3,4,5]]'
nowlist = list(strlist)
print(nowlist)

run = True
while run:
    print('Quieres crear un archivo nuevo?')
    option = input('>>> ')
    if option == 'si':
        print('ingrese el nombre del archivo')
        nombrearchivo = input('>>> ')
        f = open("names.txt", "a")
        f.write('<>')
        f.write(nombrearchivo)
        
        f.close()
        file = open(f'{nombrearchivo}.txt',"x")
        print('Se ha creado un documento vacio')
        file.close()
    elif option == 'no':
        run = False
    else:
        print('Se muestra la lista de archivos guardados')
        f = open("names.txt", "r")# Abre y lee un archivo
        titulos = []# la memoria de los titulos
        strtitulos = str(f.read())# string de titulos
        initiallimit = 2
        # este for itera a traves del strign colectando todos los titulos
        for i,j in enumerate(strtitulos):
            if j == '<' and not i == 0:
                titulos.append(strtitulos[initiallimit: i])
                initiallimit = i+2
            if i == len(strtitulos)-1:
                titulos.append(strtitulos[initiallimit: i])
        for i,j in enumerate(titulos):
            print(f'{i} titulo: {j}')
        print('Que archivo quieres editar?')
        quearchivo = input('>>> ')
        if quearchivo in titulos:
            print('Si existe')
            print('Que desea Hacer? 1=guardar 2=abrir')
            quehacer = input('>>> ')
            if quehacer == '1':
                print('Guardar Cambios')
                archivoabierto = open(f'{quearchivo}.txt','w')
                #### Primer Dato ####
                archivoabierto.write(f'ac=[')
                for index,punto3d in enumerate(Aparatos):
                    archivoabierto.write('[')
                    for i,componente in enumerate(punto3d):
                        archivoabierto.write(f'{componente}')
                        if i != len(punto3d)-1:# No añadas una coma al ultimo elemento
                            archivoabierto.write(',')
                    archivoabierto.write(']')
                    if index != len(Aparatos)-1:# no añadir coma al ultimo elemento
                        archivoabierto.write(',')
                archivoabierto.write(']')
                #### Segundo dato
                archivoabierto.write(f'qa=[')
                for index,who in enumerate(queaparatos):
                    archivoabierto.write(f'{who}')
                    if index != len(queaparatos)-1:# No añadas una coma al ultimo elemento
                        archivoabierto.write(',')
                archivoabierto.write(']')
                #### Tercer dato
                archivoabierto.write(f'te=[')
                for index,punto3d in enumerate(extremostubos):
                    archivoabierto.write('[')
                    for i,componente in enumerate(punto3d):
                        archivoabierto.write(f'{componente}')
                        if i != len(punto3d)-1:# No añadas una coma al ultimo elemento
                            archivoabierto.write(',')
                    archivoabierto.write(']')
                    if index != len(extremostubos)-1:# no añadir coma al ultimo elemento
                        archivoabierto.write(',')
                archivoabierto.write(']')
                archivoabierto.close()
            if quehacer == '2':
                print('Abrir archivo')
                archivoabierto = open(f'{quearchivo}.txt','r')
##                print(str(archivoabierto.read()))
                raw_material = str(archivoabierto.read())
                # AHORA A TRAERLOS A LA VIDA
                colector = ''
                suplist = []
                acList = []
                qaList = []
                teList = []
                print(raw_material)
                parenthesesopen = 0
                fas = False
                for index,letter in enumerate(raw_material):
                    print(parenthesesopen)
                    if letter == '[':
                        parenthesesopen += 1
                    elif letter == ']':
                        pass
                        if colector == '':
                            pass
                        else:
                            if parenthesesopen == 2:
                                suplist.append(float(colector))
                                if fas:
                                    acList.append(suplist)
                                else:
                                    teList.append(suplist)
                                suplist = []
                            if parenthesesopen == 1:
                                qaList.append(float(colector))
                        print(colector)
                        colector = ''
                        parenthesesopen -= 1
                    elif letter == ',':
                        if colector == '':
                            pass
                        else:
                            if parenthesesopen == 2:
                               suplist.append(float(colector))
                            elif parenthesesopen == 1:
                                qaList.append(float(colector))
                        print(colector)
                        colector = ''
##                    elif letter == '':
##                    elif letter == '':
                    elif letter == '=':
                        pass
                    elif letter == 'a':
                        fas = True
                    elif letter == 'c':
                        pass
                    elif letter == 'q':
                        pass
                    elif letter == 't':
                        fas = False
                    elif letter == 'e':
                        pass
                    else:
                        colector = colector + letter
                print(acList,qaList,teList)

                        
                        
                        
                    
                            
        else:
            print('no existe')
        f.close()
