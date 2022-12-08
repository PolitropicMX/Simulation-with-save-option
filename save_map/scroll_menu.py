import pygame, sys, math
import numpy as np

class Key(pygame.sprite.Sprite):
    def __init__(self,xpos,ypos,size,image,id):
        super(Key, self).__init__()
        self.image = pygame.image.load('images/'+image).convert()
        self.image = pygame.transform.scale(self.image,(size,size))
        self.clicked = False
        self.rect = self.image.get_rect()
        self.rect.x = xpos 
        self.rect.y = ypos
        self.id = id
        self.linkready = False
        self.links = []


class Scrollmenu:# ESTO VA ANTES DE ENTRAR AL LOOP PRINCIPAL
    def __init__(self,screen,blacktowhite):
        # screen
        self.screen = screen
        # color
        self.blacktowhite = blacktowhite
        # La coordinada inicial y ancho y altura de la ventana
        self.X,self.Y,self.W,self.H = 80,100,500,300
        # el espacio entre la ventana y los contenidos
        self.lml = 40
        # las dimensiones de la barra scroll
        self.wbs,self.hbs = 20,self.H-2*self.lml
        # el desfase entre barra scroll y el boton scroll
        self.sbmb = 1
        # el tamanio de el boton scroll
        self.sbmbsize = self.wbs-2*self.sbmb
        # el limite maximo de la barra scroll
        self.downerlimit = self.Y+self.lml+self.sbmb
        # el limite minimo de la barra scroll
        self.upperlimit = self.Y+self.lml+self.hbs-self.sbmb-self.sbmbsize
        # el range de movimiento del boton scroll
        self.scrollbuttonrange = self.upperlimit- self.downerlimit
        # las dimensiones de la showpanel
        self.wsp,self.hsp = self.W-2*self.lml-2*self.wbs,self.H-2*self.lml
        #ELEMENTOS
        # numero de celdas 
        self.n,self.m = 6,5
        # desfase entre showpanel y los elementos
        self.lme = 5
        # las dimensiones de cada elemento
        self.ew,self.eh = 70,70
        # el limite superior de los elementos
        self.element_list_top_limit = self.Y+self.lml+self.lme
        # el rango de movimiento
        self.element_list_range = (self.eh+10)*6
        # el limite inferior de los elementos
        self.element_list_bottom_limit = self.element_list_top_limit-self.element_list_range+self.hsp
        #### THE IMPORTANT STUFF OF DRAG AND DROP
        # THE SCROLL BUTTON
        self.sb_list = pygame.sprite.Group()# contenedor que guarda vrios sprites
        self.sb_list.add(Key(self.X+self.W-self.lml-self.wbs+self.sbmb,self.Y+self.lml+self.sbmb,18,'button.png','button'))# el primer y unico sprite
        # THE CELLS
        self.rows_list = [pygame.sprite.Group() for i in range(self.n)]
        # Se crea un grupo de sprites por cada fila de imagenes
        for row,element in enumerate(self.rows_list):
            # se itera a traves de estos grupos de sprites
            for i in range(self.m):
                # se añade en las posiciones deseadas cada boton
                element.add(Key(self.X+self.lml+self.lme+i*(self.eh+self.lme),self.element_list_top_limit+row*(self.eh+10),70,'button.png',i+(row*5+1)))
        # THE IMAGES/ICONS
        self.icons_list = [pygame.sprite.Group() for i in range(self.n)]
        for row,icon in enumerate(self.icons_list):
            for j in range(self.m):
                if j+(row*5+1) >= 31:
                    break
                icon.add(Key(self.X+self.lml+self.lme+j*(self.eh+self.lme),self.element_list_top_limit+row*(self.eh+10),70,str(j+(row*5+1))+'.png',i+(row*5+1)))


    def update(self,pos):# ESTO VA DESPUES DE LOS FOR.EVENT(COONTROLES)
        # Se vuelven a dibujar los elementos 
        # La ventana principal
        pygame.draw.rect(self.screen,(200,200,200),(self.X,self.Y,self.W,self.H))
        # La Barra Scroll
        pygame.draw.rect(self.screen,(150,150,150),(self.X+self.W-self.lml-self.wbs,self.Y+self.lml,self.wbs,self.hbs))
        # Showpanel
        pygame.draw.rect(self.screen,(100,100,100),(self.X+self.lml,self.Y+self.lml,self.wsp,self.hsp))
        
        #Boton Scroll
        # esto hace que el scrollbutton se mueva junto con el cursor
        for key in self.sb_list:
            if key.clicked == True:
                if pos[1] < self.downerlimit:
                    key.rect.y = self.downerlimit
                elif pos[1] > self.upperlimit:
                    key.rect.y = self.upperlimit
                else:
                    key.rect.y = pos[1]-(key.rect.height/2)
            self.sb_list.draw(self.screen)
        # Los cuadritos 
        for i,row in enumerate(self.rows_list):
            for j,element in enumerate(row):
                if element.clicked:# si el elemento es clickeado...
                    if pos[1] < self.downerlimit:# si la osicion del cursor es arriba de
                        # la barra de scroll
                        element.rect.y = self.element_list_top_limit+i*(self.eh+10)
                    elif pos[1] > self.upperlimit:# Si la posicion es por debajo de la
                        # barra de scroll
                        element.rect.y = self.element_list_bottom_limit+i*(self.eh+10)
                    else:# Si el cursor esta entre los dos intervalos
                        element.rect.y = self.element_list_top_limit-(self.element_list_range-self.hsp)*((pos[1]-(self.element_list_top_limit))/self.scrollbuttonrange)+i*(self.eh+10)
                if element.rect.y > (self.Y+self.lml+self.lme-self.sbmbsize/3) and element.rect.y < (self.Y+self.lml+self.hsp-self.sbmbsize):
                    row.draw(self.screen)

        # Las imagenes
        for i,row in enumerate(self.icons_list):
            for j,element in enumerate(row):
                if element.clicked:
                    if pos[1] < self.downerlimit:
                        element.rect.y = self.element_list_top_limit+i*(self.eh+10)
                    elif pos[1] > self.upperlimit:
                        element.rect.y = self.element_list_bottom_limit+i*(self.eh+10)
                    else:
                        element.rect.y = self.element_list_top_limit-(self.element_list_range-self.hsp)*((pos[1]-(self.element_list_top_limit))/self.scrollbuttonrange)+i*(self.eh+10)
                if element.rect.y > (self.Y+self.lml+self.lme-self.sbmbsize/3) and element.rect.y < (self.Y+self.lml+self.hsp-self.sbmbsize):
                    row.draw(self.screen)
    
    def controlspressed(self,pos):
        for key in self.sb_list:
            if key.rect.collidepoint(pos):
                key.clicked = True
                for row in self.rows_list:
                    for element in row:
                        element.clicked = True
                for row in self.icons_list:
                    for element in row:
                        element.clicked = True
        for i,row in enumerate(self.rows_list):
            for j,element in enumerate(row):
                if element.rect.collidepoint(pos):
                    return element.id
                    
    def for_button_2(self,pos):
        for key in self.sb_list:
            if key.rect.collidepoint(pos):
                key.linkready = True
                count = 0
                links = []
                for key in self.sb_list :
                    if key.linkready == True:
                        count += 1
                        links.append(key.id)
                if count == 2:
                    for key in self.sb_list:
                        if key.linkready == True:
                               key.linkready = False
                               count += 1
                               key.links += links
    def controlsreleased(self,pos):
        for key in self.sb_list:
            key.clicked = False
            for row in self.rows_list:
                for element in row:
                    element.clicked = False
            for row in self.icons_list:
                for element in row:
                    element.clicked = False

    

        
