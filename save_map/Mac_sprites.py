import pygame
import numpy as np
from math import *

projection_matrix = np.matrix([
    [1,0,0],
    [0,1,0]])

# ---------------------------------------------------------------        
##XXXX COPY THIS TO IMPORT THE FUNCTION OF ADDING SEVERAL IMAGES
#-----------------------------------------------------------------
# titlespos is  the collections of al 3d positions
# who_list is the collection of all the names of each position
def addimages(titlespos,who_list,scale,cubepos,rotation_x, rotation_y, rotation_z):# FUNCION TIPO CREATE
    images = pygame.sprite.Group()# hERE IT CREATES THE SPRITE
    for i,j in enumerate(titlespos):# TRANSFORMS THE  3D COORDINATE VECTOR INTO 2D PROJECTED VECTOR
        title2d = np.dot(rotation_z, titlespos[i].reshape((3,1)))
        title2d = np.dot(rotation_y, title2d)
        title2d = np.dot(rotation_x, title2d)
        title = np.dot(projection_matrix, title2d)
        x = int(title[0][0] * scale) + cubepos[0]
        y = int(title[1][0] * scale) + cubepos[1]
        images.add(Mac(x,y,who_list[i],scale,i))# THEN WE FINALLY ADD TO THE SPRITE GROUP OBJECT CALLED images
        # A CLASS OBJECT FROM Mac CLASS, SO NOW THE OBJECT WITH THE POSITION, THE IMAGE  THE SCALE AND ITS ID ARE LOADED INTO THE SPRITE GROUP OBJECT
        # SO NOW, EVERY MAC OBJECTT STORED IN IMAGES CAN BE DISPLAYED ONTO THE SCREEN
    return images

#--------------------------------------------------------------------------------------

class Mac(pygame.sprite.Sprite):# Clase hija
    def __init__(self,xpos,ypos,who,scale,id):# asks this for a x annd y position and a reference
        super(Mac, self).__init__()
        self.who = who# who is a number string, always it most be a string
        # bc off the line of code below, it references to the name of the image
        # you want to use
        if self.who == "None":
            self.image = pygame.image.load("images/button.png").convert_alpha()
        else:
            self.image = pygame.image.load("images/"+self.who+".png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(scale,scale))
        if self.who == "11":
            self.image = pygame.transform.scale(self.image,(2*scale,scale))
        # the height and width of a given image
        self.rect = self.image.get_rect(center=(xpos, ypos))# this is the cntral position of the image
        self.id = id# adds an ID variable
