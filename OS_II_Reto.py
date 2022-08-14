#Importamos la libreria "pygame"
import pygame


#inicializamos la libreria
pygame.init()

#creamos una pantalla
screen = pygame.display.set_mode((800,400))




while True:

    
    #creamos el evento "quit" para poder cerrar la pantalla
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

            
    #condicional la cual si se presiona la tecla espacio imprime en pantalla un mensaje
    keybind = pygame.key.get_pressed()
    if keybind[pygame.K_SPACE]:
        print("Hola Mundo")
    else: print("Hola")


        
    #FPS
    pygame.display.update()
