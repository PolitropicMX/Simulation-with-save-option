
import numpy as np
import pygame
from button import Button
import random

def get_text(screen,size,string,posx,posy): # Returns Press-Start-2P in the desired size
        text = pygame.font.SysFont('Comic Sans MS', size).render(string,True,"white","blue")
        sep = 15
        rect = (posx+sep,posy+sep)
        screen.blit(text,rect)


class Draw():
        # Descripcion: esta clase cuando se instancia en el codigo principal
        # se crean memorias destinadas a crear lineas dibujadas a partir de
        # 2 puntos x y y.
    def __init__(self):
        # 2D properties
        self.memory2d = np.array([])# storage
        self.count2d = 0# number of points collected
        self.points2d = 0# number of lines collectted

        # 3D properties
        self.memory3d = np.array([])# storage
        self.memoryproj2d = np.array([])# storage
        self.colormemory = []
        self.count3d = 0# number of points collected
        self.points3d = 0# number of lines collectted

    # 2D methods
    def line2d(self,screen,showpoints):# funcion tipo DRAW
            # Descripcion: esta es la funcion que dibuja en la ventana princiapl
            # las lineas formadas con los puntos guarddos
        for i in range(self.points2d):
                # Para i = 0,                           [0]  [0]              [0]  [1]                [1]    [0]              [1]    [1]
                # Para i = 1,                           [2]  [0]              [2]  [1]                [3]    [0]              [3]    [1]
                # Para i = 2,                           [4]  [0]              [4]  [1]                [5]    [0]              [5]    [1]
            pygame.draw.line(screen,self.colormemory[i],(self.memory2d[i*2][0],self.memory2d[i*2][1]),(self.memory2d[2*i+1][0],self.memory2d[2*i+1][1]),5)
            if showpoints:
                pygame.draw.circle(screen,(200,100,50),(self.memory2d[i*2][0],self.memory2d[i*2][1]),5)
                pygame.draw.circle(screen,(200,100,50),(self.memory2d[i*2+1][0],self.memory2d[i*2+1][1]),5)

    def line3d(self,screen,showpoints):# funcion tipo DRAW
            # Descripcion: esta es la funcion que dibuja en la ventana princiapl
            # las lineas formadas con los puntos guarddos
        for i in range(self.points3d):
                # Para i = 0,                               [0]  [0]                  [0]  [1]                    [1]    [0]                  [1]    [1]
                # Para i = 1,                               [2]  [0]                  [2]  [1]                    [3]    [0]                  [3]    [1]
                # Para i = 2,                               [4]  [0]                  [4]  [1]                    [5]    [0]                  [5]    [1]
            pygame.draw.line(screen,self.colormemory[i],(self.memoryproj2d[i*2][0],self.memoryproj2d[i*2][1]),(self.memoryproj2d[2*i+1][0],self.memoryproj2d[2*i+1][1]),5)
            if showpoints:
                pygame.draw.circle(screen,(200,100,50),(self.memoryproj2d[i*2][0],self.memoryproj2d[i*2][1]),5)
                pygame.draw.circle(screen,(200,100,50),(self.memoryproj2d[i*2+1][0],self.memoryproj2d[i*2+1][1]),5)

    def line_and_titles(self,screen,color):
        for i in range(self.points):
            # SAME PRINCIPLE AS METHOD ABOVE
                # Para i = 0,                         [0]  [0]            [0]  [1]              [1]    [0]            [1]    [1]
                # Para i = 1,                         [2]  [0]            [2]  [1]              [3]    [0]            [3]    [1]
                # Para i = 2,                         [4]  [0]            [4]  [1]              [5]    [0]            [5]    [1]
            pygame.draw.line(screen,color,(self.memory[i*2][0],self.memory[i*2][1]),(self.memory[2*i+1][0],self.memory[2*i+1][1]),5)
            # DRAW A TEXT AT EACH POINT IN THE COLLECTED LIST OF POINTS
            get_text(screen,20,str(self.memory[i*2][0])+' '+str(self.memory[i*2][1]),self.memory[i*2][0],self.memory[i*2][1]) # Punto inicial
            get_text(screen,20,str(self.memory[i*2+1][0])+' '+str(self.memory[i*2+1][1]),self.memory[i*2+1][0],self.memory[i*2+1][1])#  Punto final
            
    def add2dpoint(self,point):      
        self.memory2d = np.append(self.memory2d,point)# Se añade el punto al memory
        self.memory2d = np.append(self.memory2d,self.count2d)# Se añade  el index al mem
        self.count2d += 1# cada que se añade un punto
        self.memory2d = self.memory.reshape(self.count,3)# cambiar tamaño a: self.count filas y 3 columnas
        if self.count2d%2 == 0:# el el residuo de la op. self.count/2 es cero, then... solo numeros pares tienen residuo cero
                # osea si tienes un numero de puntos par
                    self.points2d += 1

    def add3dpoint(self,point,wantindex):
            # Descripcion: Esta funcion esta destinada en ir en el codigo principal
            # permite enviar desde el codigo principal el punto deseado a añadir
            # y se guarda en el array correspondiente
        self.memory3d = np.append(self.memory3d,point)# Se añade el punto al memory
        self.count3d += 1# cada que se añade un punto
        if wantindex:
                self.memory3d = np.append(self.memory3d,self.count3d)# Se añade  el index al mem
                self.memory3d = self.memory3d.reshape(self.count3d,4)
        else:
                self.memory3d = self.memory3d.reshape(self.count3d,3)# cambiar tamaño a: self.count filas y 3 columnas                
        if self.count3d%2 == 0:# el el residuo de la op. self.count/2 es cero, then... solo numeros pares tienen residuo cero
                # osea si tienes un numero de puntos par
                    self.points3d += 1
                    self.colormemory.append((random.randint(0,255),random.randint(0,255),random.randint(0,255)))

    def get_2d_info(self):# FUNCION TIPO GETTER
        return self.memory2d, self.points2d

    def get_3d_info(self):# FUNCION TIPO GETTER
            # Descripcion: permite enviar la info de los puntos que conforman
            # una linea al codigo principaal
        if len(self.memory3d) == 0:# esto es cuando se inicializa el array
                return self.memory3d, self.points3d
        else:# Cuando se añade el primer punto
                return self.memory3d, self.points3d

    def set_2d_proj(self,proj2d):# FUNCION TIPO SETTER
            # este es la matriz trasnsformada desde el codigo principal
        self.memoryproj2d = proj2d
        

    def clear(self):# FUNCION TIPO CLEAR : REESTABLECE LOS VALORES INICIALES
        # 2D properties
        self.memory2d = np.array([])# storage
        self.count2d = 0# number of points collected
        self.points2d = 0# number of lines collectted

        # 3D properties
        self.memory3d = np.array([])# storage
        self.memoryproj2d = np.array([])# storage
        self.count3d = 0# number of points collected
        self.points3d = 0# number of lines collectted

    def draw_dots(self,points):# FUNCION TIPO DRAW
        for i,j in enumerate(points):
                pygame.draw.circle(screen,(255,255,255),(j[0],j[1]),5)

    def undo(self):
        print(self.memory3d,self.memoryproj2d,self.count3d)
        self.memory3d = self.memory3d[0:(len(self.memory3d)-1)]
        self.memoryproj2d = self.memoryproj2d[0:(len(self.memoryproj2d)-1)]
        self.count3d -= 1
        print(self.memory3d,self.memoryproj2d,self.count3d)

    def delete_last_point(self):
        self.memory3d = self.memory3d[0:(len(self.memory3d)-1)]
        self.count3d -= 1

    def set_3d_info(self,ac):
        self.memory3d = ac
        self.points3d = int(len(self.memory3d)/2)
        self.count3d = int(len(self.memory3d))
        for i in range(self.points3d):
                self.colormemory.append((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
