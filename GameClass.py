import pygame
import math
import random
import constants

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
        pygame.draw.rect(screen, 'green', self.rect, 1)

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
        pygame.draw.rect(screen, 'yellow', self.rect, 1)
        if abs(self.scroll)  > self.surface.get_width():
            self.scroll = 0



class Pipe:
    def __init__(self, pipe_x_pos):
        self.off_screen = False
        self.pipe_w = 80
        self.pipe_h = 800

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
        self.pipe_x-= speed

        self.rect1.y = self.pipe1_y + 30
        self.rect1.x = self.pipe_x + 35
        self.rect2.x = self.pipe_x + 35
        self.rect2.y = self.pipe2_y - 30

        screen.blit(self.surface1, (self.pipe_x, self.pipe1_y))
        screen.blit(self.surface2, (self.pipe_x, self.pipe2_y))
        pygame.draw.rect(screen, "Blue", self.rect1, 1)
        pygame.draw.rect(screen, "Blue", self.rect2, 1)
            
