import pygame
import math
import random

def main():
    pygame.init()
    width = 800
    height = 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Floppy Bird')
    clock = pygame.time.Clock()
    running = True
    pygame.font.init()

    death_screen = False
    game_on = False
    speed = 1
    score = 0
    pipe_counted = False
    pipe_spacing = 350
    pipe_gap = 170
    y_pos = 240
    x_pos = 80


    my_font = pygame.font.SysFont('font/Pixeltype.ttf', 40)

    bg_scroll = 0
    bg_surf = pygame.image.load('images/Bg.png').convert()
    bg_tiles = math.ceil(width / bg_surf.get_width()) + 1

    #Main menu rectangles
    play_btn_rect = pygame.Rect(width / 2 - 100, height / 2 - 100, 200, 80)
    quit_btn_rect = pygame.Rect(width / 2 - 100, height / 2 + 0, 200, 80)

    play_btn_surface = pygame.transform.scale(pygame.image.load('images/Play.png').convert() , (play_btn_rect.width, play_btn_rect.height))
    quit_btn_surface = pygame.transform.scale(pygame.image.load('images/Quit.png').convert() , (quit_btn_rect.width, quit_btn_rect.height))
    play_btn_text = my_font.render(f"PLAY", False, (60, 60, 60))
    quit_btn_text = my_font.render(f"Quit", False, (10, 10, 10))
    death_menu_surface = pygame.transform.scale(pygame.image.load('images/Death_bg.png').convert() , (width - 300, height - 200))


    def show_menu():

        draw_bg()
        ground.draw()
        #play button
        screen.blit(play_btn_surface, (play_btn_rect.centerx - play_btn_surface.get_width() / 2, play_btn_rect.centery - play_btn_surface.get_height() / 2))
        screen.blit(play_btn_text, (play_btn_rect.centerx - play_btn_text.get_width() / 2, play_btn_rect.centery - play_btn_text.get_height() / 2))
        #pygame.draw.rect(screen, "Blue", play_btn_rect , 2)

        #Quit button
        screen.blit(quit_btn_surface, (quit_btn_rect.centerx - quit_btn_surface.get_width() / 2, quit_btn_rect.centery - quit_btn_surface.get_height() / 2))
        screen.blit(quit_btn_text, (quit_btn_rect.centerx - quit_btn_text.get_width() / 2, quit_btn_rect.centery - quit_btn_text.get_height() / 2))
        #pygame.draw.rect(screen, "Blue", quit_btn_rect , 2)

    def death_menu():
        draw_bg()
        player.draw()
        pipe1.draw()
        pipe2.draw()
        pipe3.draw()
        ground.draw()


        #Draw menu BG
        screen.blit(death_menu_surface, (150, 25))

        #play button
        screen.blit(play_btn_surface, (play_btn_rect.centerx - play_btn_surface.get_width() / 2, play_btn_rect.centery - play_btn_surface.get_height() / 2))
        screen.blit(play_btn_text, (play_btn_rect.centerx - play_btn_text.get_width() / 2, play_btn_rect.centery - play_btn_text.get_height() / 2))
        #pygame.draw.rect(screen, "Blue", play_btn_rect , 2)

        #Quit button
        screen.blit(quit_btn_surface, (quit_btn_rect.centerx - quit_btn_surface.get_width() / 2, quit_btn_rect.centery - quit_btn_surface.get_height() / 2))
        screen.blit(quit_btn_text, (quit_btn_rect.centerx - quit_btn_text.get_width() / 2, quit_btn_rect.centery - quit_btn_text.get_height() / 2))
        #pygame.draw.rect(screen, "Blue", quit_btn_rect , 2)

        #show score
        dead_surface = my_font.render(f"GAME OVER !", False, ("red"))
        score_surface = my_font.render(f"Your High score: {score}", False, ("white"))
        screen.blit(dead_surface, (width / 2 - dead_surface.get_width() / 2, 100))
        screen.blit(score_surface, (width / 2 - score_surface.get_width() / 2, 150))

    def draw_bg():
        for i in range(0, bg_tiles):
            screen.blit(bg_surf, (bg_surf.get_width() * i + bg_scroll, 0))

    def show_score(score):
        score_surface = my_font.render(f"Score: {score}", False, ("white"))
        screen.blit(score_surface, (20, 20))




    class Player:
        def __init__(self, player_x,player_y):
            self.surface = pygame.image.load('images/Bird.png').convert_alpha()
            self.surface = pygame.transform.scale(self.surface, (50, 50))
            self.player_x = player_x
            self.player_y = player_y
            self.rect = self.surface.get_rect()
            self.rect.x = self.player_x
            self.rect.y = self.player_y
            self.y_velocity = 0
            self.gravity = 0.5
            self.jump_force = 10
            self.jumping = False
            self.cooldown = 0
        


        def jump(self, input):
            #trigger event listner
            if input[pygame.K_UP] and self.cooldown <= 0 and self.rect.top > 0:
                self.y_velocity = -self.jump_force
                self.jumping = True
                self.cooldown = 20
            
            self.y_velocity += self.gravity
            self.rect.y += self.y_velocity

            if self.cooldown > 0:
                self.cooldown -= 1


        def draw(self):
            screen.blit(self.surface, (self.rect.x, self.rect.y))
            #pygame.draw.rect(screen, 'green', self.rect, 1)

        def collision(self):
            return (
                self.rect.colliderect(ground.rect)
                or self.rect.colliderect(pipe1.rect1)
                or self.rect.colliderect(pipe1.rect2)
                or self.rect.colliderect(pipe2.rect1)
                or self.rect.colliderect(pipe2.rect2)
                or self.rect.colliderect(pipe3.rect1)
                or self.rect.colliderect(pipe3.rect2)
            )


    class Ground:
        
        def __init__(self):
            self.surface = pygame.image.load('images/Ground.png').convert()
            self.gnd_x = 0
            self.gnd_y = height - self.surface.get_height()
            self.rect = self.surface.get_rect()
            self.rect.x = self.gnd_x
            self.rect.y = self.gnd_y
            self.tiles = math.ceil(width / self.surface.get_width()) + 2 
            self.scroll = 0

        def draw(self):
            for i in range(0, self.tiles):
                screen.blit(self.surface, (self.surface.get_width() * i - i + self.scroll, bg_surf.get_height() - 10))
            #pygame.draw.rect(screen, 'yellow', self.rect, 1)
            if abs(self.scroll)  > self.surface.get_width():
                self.scroll = 0


    class Pipe:
        def __init__(self, pipe_x_pos):
            self.off_screen = False
            self.pipe_w = 80
            self.pipe_h = 800
            self.counted = False

            self.pipe_x = pipe_x_pos

            self.surface1 = pygame.transform.scale((pygame.image.load('images/Pipe.png').convert_alpha()), (150, 400))
            self.pipe1_y = random.randint(200, 400)
            self.rect1 = self.surface1.get_rect()

            self.surface2 = pygame.transform.rotate(pygame.transform.scale((pygame.image.load('images/Pipe.png').convert_alpha()), (150, 400)), 180)
            self.pipe2_y = self.pipe1_y - pipe_gap - self.surface2.get_height()
            self.rect2 = self.surface2.get_rect()

            self.rect1.width = self.rect1.width - 70
            self.rect2.width = self.rect2.width - 70



        def draw(self):
            if game_on:
                self.pipe_x-= speed

                self.rect1.y = self.pipe1_y + 30
                self.rect1.x = self.pipe_x + 35
                self.rect2.x = self.pipe_x + 35
                self.rect2.y = self.pipe2_y - 30

                screen.blit(self.surface1, (self.pipe_x, self.pipe1_y))
                screen.blit(self.surface2, (self.pipe_x, self.pipe2_y))
                #pygame.draw.rect(screen, "Blue", self.rect1, 1)
                #pygame.draw.rect(screen, "Blue", self.rect2, 1)
            else:
                pass
                

        

    #create the objects
    player = Player(x_pos, y_pos)
    ground = Ground()
    pipe1 = Pipe(width + 20)
    pipe2 = Pipe(pipe1.pipe_x + random.randint(400, width))
    pipe3 = Pipe(pipe2.pipe_x + random.randint(400, width))

    #Main game loop
    while running:
        
        input = pygame.key.get_pressed()
        #Quit when the user click the X on the screen
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if play_btn_rect.collidepoint(event.pos):
                        game_on = True
                        y_pos = 240
                        x_pos = 80
                        

                    elif quit_btn_rect.collidepoint(event.pos):
                        running = False
                        exit()



        #fill frame
        screen.fill("black")

        #If the game has started
        if game_on :
            #update objects
                #set speed
            speed = min(speed + 1/500, 6)
            bg_scroll -= 0.5 * speed
            ground.scroll -= 1 * speed

                #Repeat Background
            if abs(bg_scroll) > bg_surf.get_width():
                bg_scroll = 0

                #Set pipe positions
            pipes = [pipe1, pipe2, pipe3]

            for pipe in pipes:
                    #Updating the postion of the pipes
                if pipe.pipe_x < -150:
                    pipe.pipe_x = max(p.pipe_x for p in pipes) + pipe_spacing
                    pipe.pipe1_y = random.randint(150, 350)
                    pipe.pipe2_y = pipe.pipe1_y - pipe_gap - pipe.surface2.get_height()
                    pipe_counted = False
                    #score systeme
                elif pipe.pipe_x < player.player_x and pipe_counted == False:
                    score += 1
                    pipe_counted = True

                #Check movement and collsion
            player.jump(input)
            if player.collision():
                game_on = False
                death_screen = True
                death_menu()
                player = Player(x_pos, y_pos)
                ground = Ground()
                pipe1 = Pipe(width + 20)
                pipe2 = Pipe(pipe1.pipe_x + random.randint(400, width))
                pipe3 = Pipe(pipe2.pipe_x + random.randint(400, width))

                #show objects
            draw_bg()
            player.draw()
            pipe1.draw()
            pipe2.draw()
            pipe3.draw()
            ground.draw()
            show_score(score)
        
        elif game_on == False and death_screen == False:
            show_menu()

        elif death_screen:
            game_on = False
            death_menu()

        #update frame
        pygame.display.update()

        #Frame limiter
        clock.tick(60) / 1000

main()

pygame.quit()
    