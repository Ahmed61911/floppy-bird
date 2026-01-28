import pygame


def main():
    pygame.init()
    width = 1280
    height = 720
    game_font = pygame.font.Font('font/Pixeltype.ttf', 32)
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    running = True
    
        

    #Main game loop
    while running:

        #Quit when the user click the X on the screen
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                exit()

        #fill frame
        screen.fill("black")

        

        #update frame
        pygame.display.flip()

        #Frame limiter
        clock.tick(60)

main()
pygame.quit()
    