import pygame


pygame.init()

screen = pygame.display.set_mode((800,400))




while True:

    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    keybind = pygame.key.get_pressed()
    if keybind[pygame.K_SPACE]:
        print("Hola Mundo")
    else: print("Hola")


    pygame.display.update()