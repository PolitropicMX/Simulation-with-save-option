import pygame, sys
import numpy as np
from math import *
from Mac_sprites import Mac

class Draw3d:
    def __init__(self,screen,scale,cubepos):
        self.projection_matrix = np.matrix([
            [1,0,0],
            [0,1,0]])
        self.screen = screen
        self.scale = scale
        self.cubepos = cubepos
         
     
    def projection(self,points,showpoints,feature,color):# Reicbe una lista de
    # puntos 3d y devuelve una lista de listas que en realidad son las coordenadas
    # de donde esta el punto 3d pero proyectado en 2d
    # f(Lista de puntos Puntos 3D) = lista de puntos 2d proyectados sobre screen
        i = 0
        projected_points = [[n,n] for n in range(len(points))]
        for point in points:
            rotated2d = np.dot(self.rotations[2], point.reshape((3,1)))
            rotated2d = np.dot(self.rotations[1], rotated2d)
            rotated2d = np.dot(self.rotations[0], rotated2d)
            
            projected2d = np.dot(self.projection_matrix, rotated2d)
            
            x = int(projected2d[0][0] * self.scale) + self.cubepos[0]
            y = int(projected2d[1][0] * self.scale) + self.cubepos[1]

            projected_points[i] = [x,y]
            if showpoints:
                pygame.draw.circle(self.screen, "Black", (x,y), 5)
            if feature == 'star':
                self.star(color,x,y)
            elif feature == 'no':
                pass
            else:
                self.text(feature,x,y,20,color)
            i += 1
        return projected_points

    def set_rotations(self,rotations):
        self.rotations = rotations

    def star(self,color,x,y):# AQUI YA ESTA STAR
        pygame.draw.circle(self.screen, color, (x,y), 5)
        pygame.draw.line(self.screen,color,(self.cubepos[0],self.cubepos[1]),(x,y))

    def drawtubo(self,tubo,isflowing,segundero,state,showpoints):# FUNCION TTPO DRAW
        extremos = self.projection(tubo,showpoints,'no','no')# los extremos 3D proyectalos en screen 2D 
        pygame.draw.line(self.screen,(200,200,200),(extremos[0][:]),(extremos[1][:]),6)#Tuberia gris (OFF)
        if isflowing:
            self.flujo((extremos[0][:]),(extremos[1][:]),5,segundero,state)# flujo proyectados sobre la tuberia (ON)

    def flatsurface(self,n,planes):# Funcion tipo DRAW
        # "n" : LA MITAD DEL LADO DE UN CUADRADO
        # planes: los puntos 3d que forman la rejilla o el plano 
        m = 2*n+1# EL LADO DEL CUADRADO + 1
        projectedsurfaces = self.projection(planes,False,'no','no')# 3D to proj_2D
        for i in range(int(2*m)):
            pygame.draw.line(self.screen,(0,0,10),(projectedsurfaces[i*2][0],projectedsurfaces[i*2][1]),(projectedsurfaces[2*i+1][0],projectedsurfaces[2*i+1][1]))

    def drawcube(self,points,showpoints):# FUNCION TIPO DRAW
    # Recibe un listado de puntos 3D Y DIBUJA LAS ARISTAS DE LOS VERTICES CONTENIDOS EN LA LISTA DE PUNTOS 3D
    # PROYECTADOS A 2D
        projected_points  = self.projection(points,showpoints,'no','no')# De 3D a "d proyectados en screen
        for i in range(4):# esta funcion dibuja las aristas del cubo
            pygame.draw.line(self.screen,"Black",(projected_points[i][0],projected_points[i][1]),(projected_points[i+4][0],projected_points[i+4][1]))
            pygame.draw.line(self.screen,"Black",(projected_points[i*2][0],projected_points[i*2][1]),(projected_points[i*2+1][0],projected_points[i*2+1][1]))
            if i >= 2:
                q = i+2
                pygame.draw.line(self.screen,"Black",(projected_points[q][0],projected_points[q][1]),(projected_points[q+2][0],projected_points[q+2][1]))
            else:
                pygame.draw.line(self.screen,"Black",(projected_points[i][0],projected_points[i][1]),(projected_points[i+2][0],projected_points[i+2][1]))

    def flujo(self,A,B,mass,segundero,state):# FUNCION TIPO DRAW
        chunks = 100
        dx = (B[0]-A[0])/chunks
        dy = (B[1]-A[1])/chunks
        listpositions = np.ones((chunks+1,2))
        for it in range(chunks+1):
            listpositions[it,0] = A[0] + it*dx
            listpositions[it,1] = A[1] + it*dy
        for i in range(chunks):
            f = int((255*sin(0.7*i+segundero)**2))
            # por que 255*sin()**2?
            #   como sin()**2 tiene un rango entre 0 y 1, al multriplicarlo por un
            #   numero n da una variacion entre cero y ese numero n
            # el segundero es lo que actua como un desfasador lo que hace que se mueva en un sentido
            if state == 'liq':
                pygame.draw.line(self.screen,(0,f,f),(listpositions[i,:]),(listpositions[i+1,:]),int(mass))
            elif state == 'vap':
                pygame.draw.line(self.screen,(f,0,0),(listpositions[i,:]),(listpositions[i+1,:]),int(mass))
            elif state == 'wst':
                v = int(f/2+20)
                pygame.draw.line(self.screen,(v,v,v),(listpositions[i,:]),(listpositions[i+1,:]),int(mass))



#### THE MURDERER SECTION ####
    def draw_the_murder(self,mur_coor):
        projected_points  = self.projection(mur_coor,True,'no','no')

    
    def text(self,string,xi,yi,size,color):# Funcion tipo DRAW
    # ingresas un string recibes un screen.blit
        font = pygame.font.SysFont('Comic Sans MS', size)
        textsurface = font.render(string,False,color)
        text_rect = textsurface.get_rect(center=(xi,yi))
        self.screen.blit(textsurface,text_rect)

    def addimages(self,titlespos,who_list,scale,cubepos,rotation_x, rotation_y, rotation_z):# FUNCION TIPO CREATE
        images = pygame.sprite.Group()# hERE IT CREATES THE SPRITE
        for i,j in enumerate(titlespos):# TRANSFORMS THE  3D COORDINATE VECTOR INTO 2D PROJECTED VECTOR
            rotated2d = np.dot(self.rotations[2], j.reshape((3,1)))
            rotated2d = np.dot(self.rotations[1], rotated2d)
            rotated2d = np.dot(self.rotations[0], rotated2d)
            title = np.dot(projection_matrix, title2d)
            x = int(title[0][0] * scale) + cubepos[0]
            y = int(title[1][0] * scale) + cubepos[1]
            images.add(Mac(x,y,who_list[i],scale,i))# THEN WE FINALLY ADD TO THE SPRITE GROUP OBJECT CALLED images
            # A CLASS OBJECT FROM Mac CLASS, SO NOW THE OBJECT WITH THE POSITION, THE IMAGE  THE SCALE AND ITS ID ARE LOADED INTO THE SPRITE GROUP OBJECT
            # SO NOW, EVERY MAC OBJECTT STORED IN IMAGES CAN BE DISPLAYED ONTO THE SCREEN
        return images

    @staticmethod
    def tubo (A,B):# FUNCION TIPO CREATE
    # funcion que recibe 2 arrays 3D y los guarda en una lista
    # devuelve una losta con los exxtrems en array
        tube = []
        tube.append(np.matrix([A]))
        tube.append(np.matrix([B]))
        return tube

    @staticmethod
    def cubo(centro,l):# FUNCION TIPO CREATE
    # Recibe un punto 3d y devuelve una lsita de puntos 3d indicando cada vertice
    # crea una lista con todos los vertices de un cubo 
        cubox  = []
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    cubox.append(np.matrix([centro[0]+(-1)**i*l/2,centro[1]+(-1)**j*l/2,centro[2]+(-1)**k*l/2]))

        return cubox
    
    @staticmethod
    def planemaker(n):# FUNCION CREATE LIST , RECIBE UN PARAMETRO Y SOBRE ESE
    # CREA Y DEVUELVE UNA LISTA DE PUNTOS 3D 
        planes = []
        m = 2*n+1# EL LADO DEL CUADRADO + 1
        for i in range(m):# de 0 a Lado del cuadrado
            planes.append(np.matrix([n-i,0,n]))
            planes.append(np.matrix([n-i,0,-n]))
        for i in range(m):
            planes.append(np.matrix([n,0,n-i]))
            planes.append(np.matrix([-n,0,n-i]))
        return planes
    
    @staticmethod
    def starmaker(n):
        star = []
        for i in range(3):
            for j in range(2):
                print(j)
                point = np.zeros((3))
                point[i] = n*(-1**j)
                star.append(point)
        return star
