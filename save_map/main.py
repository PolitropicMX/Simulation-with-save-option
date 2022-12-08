import pygame, sys
from button import Button
import numpy as np
from math import *
from Mac_sprites import *
#### whats added
from class_projection import Draw3d
from draw import Draw
from scroll_menu import Scrollmenu
from class_save import Save_module
##from camera import Camera
####

WIDTH, HEIGHT = 600,600
centro = [WIDTH/2,HEIGHT/2+100]
cubepos = centro
scale = 50


projection_matrix = np.matrix([
    [1,0,0],
    [0,1,0]])

pygame.display.set_caption("3D PROJECTION IN PYGAME")
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
scrollmenu = Scrollmenu(SCREEN,210)
#### Whats added
DRAW3D = Draw3d(SCREEN,scale,centro)
DRAW = Draw()
TUBOS = Draw()
####

# letras
pygame.font.init()

pygame.init()


def rotation(anglex,angley,anglez):
    rotation_z = np.matrix([
        [cos(anglez),-sin(anglez),0],
        [sin(anglez),cos(anglez),0],
        [0,0,1]
        ])

    rotation_y = np.matrix([
        [cos(angley),0,sin(angley)],
        [0,1,0],
        [-sin(angley),0,cos(angley),]
        ])

    rotation_x = np.matrix([
        [1,0,0],
        [0,cos(anglex),-sin(anglex)],
        [0,sin(anglex),cos(anglex)]
        ])
    return rotation_x, rotation_y, rotation_z




n = 5
plane = DRAW3D.planemaker(n)


## AQUI VIENE LO CHIDO: Mac_sprites


def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.SysFont("f", size)

anglex = 0
angley = 0
anglez = 0
velanglex = 0
velangley = 0
velanglez = 0
option1 = 1
option2 = 0
segundero = 0
#### XXX COPY THIS TO IMPORT THE MURDERER TO OTHERS CODE
the_murder_coordinate = [np.matrix([0,0,0])]
player_x = 0.5
player_y = 0.5
player_z = 0.5
player_x_vel = 0
player_y_vel = 0
player_z_vel = 0
id_count = 0 # este numero es para poner numero a las corriente
id_memory = []
id_pos = []# el titlepos de los titulos
text_pos = []
text_memory = []
ismenuRunning = False
text_saver = False
cwho = []
pos = pygame.mouse.get_pos()
scrollmenu = Scrollmenu(SCREEN,210)
save = Save_module()
####
while True:
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Descripcion:pygame.MOUSEBUTTONDOWN se activa cada que
            # cualquier boton del mouse es presionado

            print(scrollmenu.controlspressed(pos))

            if event.button == 1:
                # esta linea se activa cada que se oprime el boton izquierdo del teclado
                if CLEAR_BUTTON.checkForInput(mouse):
                    DRAW.clear()
                    TUBOS.clear()
                    memory = {}
                    cwho = []
                if UNDO_BUTTON.checkForInput(mouse):
                    DRAW.undo()
                    cwho = cwho[0:(len(cwho)-1)]
                if SAVE_BUTTON.checkForInput(mouse):
                    memory,cwho,tubos_memoria = save.active_module(memory,cwho,tubos_memoria)
                    print('Aqui ya se debieron haber cargado')
                    print(memory,cwho,tubos_memoria)
                    DRAW.set_3d_info(memory)
                    TUBOS.set_3d_info(tubos_memoria)
##                    camera.take_photo(memory,cwho,memorytubos, pointstubos)
                if ismenuRunning:
                    # Solo cuando el menun esta activo
                    if CLOSE_MENU_BUTTON.checkForInput(mouse):
                        ismenuRunning = False
                    if scrollmenu.controlspressed(pos) is None :
                        # cuando el argumento recibido sea un None
                        pass
                    elif 31 <= int(scrollmenu.controlspressed(pos)):
                        # Si por alguna razon el argumento es igual o mayor a
                        # 31, solo que siga la ventana abierta
                        ismenuRunning = True
                    elif 14 == int(scrollmenu.controlspressed(pos)):
                        # Cuando se añade un numero
                        id_count += 1
                        id_pos.append(np.matrix([halo_x,halo_y,halo_z]))# la memoria donde se guardan las posiciones de los numeros
                        id_memory.append(id_count)# el elemento a guardar
                    elif 15 == int(scrollmenu.controlspressed(pos)):
                        # Cuando se añade un texto    
                        text_pos.append(np.matrix([halo_x,halo_y,halo_z]))# Se guarda la posicion de dondeel texto ira
                        what_text = input('Ingrese el texto: ')
                        text_memory.append(what_text)# Se guarda el texto 
                    else:
                        # Si no es anda de lo anterior, significa que es menor a 31
                        # o igual a 0 asi que es valido y se guarda
                        cwho.append(str(scrollmenu.controlspressed(pos)))
                        print(cwho)
                        ismenuRunning = False
            elif event.button == 2:
                scrollmenu.for_button_2(pos)
        if event.type == pygame.MOUSEBUTTONUP:
            scrollmenu.controlsreleased(pos)
            ####
        if event.type == pygame.KEYDOWN:
            ## XXX COPY THIS TO IMPORT THE MURDERER TO OTHERS CODE
            # THE ENVIRONTMENT
            if event.key == pygame.K_q:# Z dir
                velanglez = -0.05
            if event.key == pygame.K_w:# x dir
                velanglex = -0.05
            if event.key == pygame.K_a:# y dir
                velangley = 0.05
            if event.key == pygame.K_e:# z dir
                velanglez = 0.05
            if event.key == pygame.K_d:# y dir
                velangley = -0.05
            if event.key == pygame.K_s:# x dir
                velanglex = 0.05
            ## XXX COPY THIS TO IMPORT THE MURDERER TO OTHERS CODE
            # THE MURDER CONTROL PLACE
            if event.key == pygame.K_u:# y dir
                player_y_vel = 0.05
            if event.key == pygame.K_i:# x dir
                player_x_vel = 0.05
            if event.key == pygame.K_o:# Z dir
                player_y_vel = -0.05
            if event.key == pygame.K_l:# x dir
                player_z_vel = 0.05
            if event.key == pygame.K_k:# Z dir
                player_x_vel = -0.05
            if event.key == pygame.K_j:# Z dir
                player_z_vel = -0.05
##            XXX WHEN ADDING A 3D POINT
            if event.key == pygame.K_f:
                if not ismenuRunning:
                    DRAW.add3dpoint([halo_x,halo_y,halo_z],False)
                ismenuRunning = True
##            XXX
            if event.key == pygame.K_t:
                TUBOS.add3dpoint([halo_x,halo_y,halo_z],False)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                pass
            if event.key == pygame.K_UP:
                pass
            ## XXX COPY THIS TO IMPORT THE MURDERER TO OTHERS CODE
            # THE ENVIRONTMENT UP Keys
            if event.key == pygame.K_q:
                velanglez = 0
            if event.key == pygame.K_w:
                velanglex = 0
            if event.key == pygame.K_e:
                velanglez = 0
            if event.key == pygame.K_a:
                velangley = 0
            if event.key == pygame.K_s:
                velanglex = 0
            if event.key == pygame.K_d:
                velangley = 0
            if event.key == pygame.K_1:
                option1 = 0
            if event.key == pygame.K_2:
                option2 = 0
            # WHEN KEY MURDERER ARE ALL UP
            if event.key == pygame.K_u:# y dir
                player_y_vel = 0
            if event.key == pygame.K_i:# x dir
                player_x_vel = 0
            if event.key == pygame.K_o:# Z dir
                player_y_vel = -0
            if event.key == pygame.K_l:# x dir
                player_z_vel = 0
            if event.key == pygame.K_k:# Z dir
                player_x_vel = -0
            if event.key == pygame.K_j:# Z dir
                player_z_vel = -0

    pos = pygame.mouse.get_pos()
    
    #print(dimension)
    SCREEN.fill("White")
    memory, lines = DRAW.get_3d_info()# Recibe memory y count 
    if text_saver:
        memory = memory[0:(len(memory)-1)]
        text_saver = False
    #estructura para el dibujado de lineas
    tubos_memoria,extremos_tubos = TUBOS.get_3d_info()# Recibe memory y count

    ####
    # Descripcion: esta fncion devuelve un punto 3d  en un punto proyectado
    proj = DRAW3D.projection(tubos_memoria,False,'no','no')
    # Descripcion: renvia a Draw su propia base de datos de los puntos pero proyectados
    # a 2d
    TUBOS.set_2d_proj(proj)
    TUBOS.line3d(SCREEN,False)
    rotation_x, rotation_y, rotation_z = rotation(anglex,angley,anglez)
    DRAW3D.set_rotations([rotation_x, rotation_y, rotation_z])

    for i in range(id_count):
        DRAW3D.projection(id_pos[i],False,str(id_memory[i]),"Black")
    for i,j in enumerate(text_pos):
        DRAW3D.projection(text_pos[i],False,text_memory[i],'Black')
    DRAW3D.flatsurface(n,plane)
    ## XXX COPY THIS TO IMPORT THE MURDERER TO ANOTHER CODE
    # adding to the position 
    player_x += player_x_vel
    player_y += player_y_vel
    player_z += player_z_vel
    # ESTABLECEMOS LAS COORDENADAS INICIALES EN Murderer
    the_murder_coordinate = [np.matrix([player_x,player_y,player_z])]# incrementos en 3d
    DRAW3D.draw_the_murder(the_murder_coordinate)
    # XXXX THE MURDERER CUBE XXXX
    halo_x = ceil(player_x)-0.5
    halo_y = ceil(player_y)-0.5
    halo_z = ceil(player_z)-0.5
    DRAW3D.drawcube(DRAW3D.cubo((halo_x,halo_y,halo_z),1),False)
    DRAW3D.text(str([halo_x,halo_y,halo_z]),200,20,20,"Blue")   
    anglez += velanglez
    angley += velangley
    anglex += velanglex
    segundero += 1
    # 3 lineas obigatorias para escribir un boton
    CLEAR_BUTTON = Button(image=None, pos=(80, 550), 
                        text_input="CLEAR", font=get_font(25), base_color="Black", hovering_color="Blue")
    CLEAR_BUTTON.changeColor(mouse)
    CLEAR_BUTTON.update(SCREEN)
    # 3 lineas obigatorias para escribir un boton
    UNDO_BUTTON = Button(image=None, pos=(140, 550), 
                        text_input="UNDO", font=get_font(25), base_color="Black", hovering_color="Blue")
    UNDO_BUTTON.changeColor(mouse)
    UNDO_BUTTON.update(SCREEN)

    # 3 lineas obigatorias para escribir un boton
    SAVE_BUTTON = Button(image=None, pos=(250, 550), 
                        text_input="SAVE", font=get_font(25), base_color="Black", hovering_color="Blue")
    SAVE_BUTTON.changeColor(mouse)
    SAVE_BUTTON.update(SCREEN)
    CLOSE_MENU_BUTTON = Button(image=None, pos=(100, 40), 
                            text_input="CLOSE MENU WINDOW", font=get_font(25), base_color="Black", hovering_color="Blue")
    if ismenuRunning:# Cuando la ventana esta activa    
        CLOSE_MENU_BUTTON.changeColor(mouse)
        CLOSE_MENU_BUTTON.update(SCREEN)
        scrollmenu.update(pos)
    # Se necesita tener una lista de posiciones 3d y de identificadores
    # del mismo tamamo
    if len(cwho) > 0 and len(memory) == len(cwho):
        images = addimages(memory,cwho,scale,centro,rotation_x, rotation_y, rotation_z)
        images.draw(SCREEN)
    elif len(memory) > len(cwho) and not ismenuRunning:
        DRAW.delete_last_point()
    #print(segundero)
    pygame.display.update()

