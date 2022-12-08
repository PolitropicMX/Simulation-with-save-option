import numpy as np
class Save_module:
    def __init__(self):
        self.titulos = []# la memoria de los titulos
    def active_module(self,ac,qa,te):
        self.ac = ac
        self.qa = qa
        self.te = te
        self.run = True
        
        while self.run:
            print('Quieres crear un archivo nuevo?')
            self.option = input('>>> ')
            if self.option == 'si':
                print('ingrese el nombre del archivo')
                self.nombrearchivo = input('>>> ')
                self.f = open("names.txt", "a")
                self.f.write('<>')
                self.f.write(self.nombrearchivo)
                self.f.close()
                self.file = open(f'{self.nombrearchivo}.txt',"x")
                print('Se ha creado un documento vacio')
                self.file.close()
            elif self.option == 'no':
                self.run = False
            else:
                print('Se muestra la lista de archivos guardados')
                self.f = open("names.txt", "r")# Abre y lee un archivo
                
                self.strtitulos = str(self.f.read())# string de titulos
                self.initiallimit = 2
                # este for itera a traves del strign colectando todos los titulos
                for i,j in enumerate(self.strtitulos):
                    if j == '<' and not i == 0:
                        self.titulos.append(self.strtitulos[self.initiallimit: i])
                        self.initiallimit = i+2
                    if i == len(self.strtitulos)-1:
                        self.titulos.append(self.strtitulos[self.initiallimit: i])
                for i,j in enumerate(self.titulos):
                    print(f'{i} titulo: {j}')
                print('Que archivo quieres editar?')
                self.quearchivo = input('>>> ')
                if self.quearchivo in self.titulos:
                    print('Si existe')
                    print('Que desea Hacer? 1=guardar 2=abrir')
                    self.quehacer = input('>>> ')
                    if self.quehacer == '1':
                        print('Guardar Cambios')
                        self.archivoabierto = open(f'{self.quearchivo}.txt','w')
                        #### Primer Dato ####
                        self.archivoabierto.write(f'ac=[')
                        for index,punto3d in enumerate(self.ac):
                            self.archivoabierto.write('[')
                            for i,componente in enumerate(punto3d):
                                self.archivoabierto.write(f'{componente}')
                                if i != len(punto3d)-1:# No añadas una coma al ultimo elemento
                                    self.archivoabierto.write(',')
                            self.archivoabierto.write(']')
                            if index != len(self.ac)-1:# no añadir coma al ultimo elemento
                                self.archivoabierto.write(',')
                        self.archivoabierto.write(']')
                        #### Segundo dato
                        self.archivoabierto.write(f'qa=[')
                        for index,who in enumerate(self.qa):
                            self.archivoabierto.write(f'{who}')
                            if index != len(self.qa)-1:# No añadas una coma al ultimo elemento
                                self.archivoabierto.write(',')
                        self.archivoabierto.write(']')
                        #### Tercer dato
                        self.archivoabierto.write(f'te=[')
                        for index,punto3d in enumerate(self.te):
                            self.archivoabierto.write('[')
                            for i,componente in enumerate(punto3d):
                                self.archivoabierto.write(f'{componente}')
                                if i != len(punto3d)-1:# No añadas una coma al ultimo elemento
                                    self.archivoabierto.write(',')
                            self.archivoabierto.write(']')
                            if index != len(self.te)-1:# no añadir coma al ultimo elemento
                                self.archivoabierto.write(',')
                        self.archivoabierto.write(']')
                        self.archivoabierto.close()
                        return self.ac,self.qa,self.te
                    if self.quehacer == '2':
                        print('Abrir archivo')
                        self.archivoabierto = open(f'{self.quearchivo}.txt','r')
        ##                print(str(archivoabierto.read()))
                        self.raw_material = str(self.archivoabierto.read())
                        # AHORA A TRAERLOS A LA VIDA
                        self.colector = ''
                        self.suplist = []
                        self.acList = []
                        self.qaList = []
                        self.teList = []
                        print(self.raw_material)
                        self.parenthesesopen = 0
                        self.fas = False
                        for index,letter in enumerate(self.raw_material):
##                            print(parenthesesopen)
                            if letter == '[':
                                self.parenthesesopen += 1
                            elif letter == ']':
                                pass
                                if self.colector == '':
                                    pass
                                else:
                                    if self.parenthesesopen == 2:
                                        self.suplist.append(float(self.colector))
                                        if self.fas:
                                            self.acList.append(np.array(self.suplist))
                                        else:
                                            self.teList.append(np.array(self.suplist))
                                        self.suplist = []
                                    if self.parenthesesopen == 1:
                                        self.qaList.append(str(self.colector))
##                                print(colector)
                                self.colector = ''
                                self.parenthesesopen -= 1
                            elif letter == ',':
                                if self.colector == '':
                                    pass
                                else:
                                    if self.parenthesesopen == 2:
                                       self.suplist.append(float(self.colector))
                                    elif self.parenthesesopen == 1:
                                        self.qaList.append(str(self.colector))
                                print(self.suplist)
                                self.colector = ''
        ##                    elif letter == '':
        ##                    elif letter == '':
                            elif letter == '=':
                                pass
                            elif letter == 'a':
                                self.fas = True
                            elif letter == 'c':
                                pass
                            elif letter == 'q':
                                pass
                            elif letter == 't':
                                self.fas = False
                            elif letter == 'e':
                                pass
                            else:
                                self.colector = self.colector + letter
                    
                        print('Se cargaran los archivos')
                        print(f'{self.acList}')
                        print(f'{self.qaList}')
                        print(f'{self.teList}')
                        return self.acList,self.qaList,self.teList       
                else:
                    print('no existe')
                self.f.close()
                    
