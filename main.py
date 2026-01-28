import pygame
import math


def main():
    pygame.init()
    width = 800
    height = 600
    score = 0
    game_font = pygame.font.Font('font/Pixeltype.ttf', 32)
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    running = True
    pygame.display.set_caption('Floppy Bird')
    speed = 1

    bg_surf = pygame.image.load('images/Bg.png').convert()
    bird_surf = pygame.image.load('images/Bird.png').convert_alpha()
    dead_bird_surf = pygame.image.load('images/Dead_bird.png').convert_alpha()
    gnd_surf = pygame.image.load('images/Ground.png').convert()
    pipe_surf = pygame.image.load('images/Pipe.png').convert_alpha()

    bird_surf = pygame.transform.scale(bird_surf, (50, 50))
    bird_rect = bird_surf.get_rect()


    bg_tiles = math.ceil(width / bg_surf.get_width()) + 1
    gnd_tiles = math.ceil(width / gnd_surf.get_width()) + 2
    bg_scroll = 0
    gnd_scroll = 0

    bird_x = 80
    bird_y = 200

    def show_bg():
        for i in range(0, bg_tiles):
            screen.blit(bg_surf, (bg_surf.get_width() * i + bg_scroll, 0))
        


    def show_ground():
        for i in range(0, gnd_tiles):
            screen.blit(gnd_surf, (gnd_surf.get_width() * i - i + gnd_scroll, bg_surf.get_height() - 10))

    def show_bird():
        screen.blit(bird_surf, (bird_x, bird_y))
        bird_rect.x = bird_x
        bird_rect.y = bird_y
        pygame.draw.rect(screen, "red", bird_rect, 1)

    def control_bird(key):
        if key[pygame.K_UP]:
                bird_y -= 10
        elif key[pygame.K_DOWN]:
                bird_y += 10
            
                

        

    #Main game loop
    while running:
        key = pygame.key.get_pressed()
        #Quit when the user click the X on the screen
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                exit()

        #fill frame
        screen.fill("black")
        show_bg()
        show_ground()
        show_bird()

        gnd_scroll -= 3 * speed
        bg_scroll -= 1 * speed

        speed += (1 /  500)

        if abs(bg_scroll) > bg_surf.get_width():
            bg_scroll = 0

        if abs(gnd_scroll)  > gnd_surf.get_width():
            gnd_scroll = 0

        if key[pygame.K_UP]:
                bird_y -= 10
        elif key[pygame.K_DOWN]:
                bird_y += 10


        #update frame
        pygame.display.update()

        #Frame limiter
        clock.tick(60)

main()
pygame.quit()
    