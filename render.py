import sys

import pygame
from pendulum import Pendulum
from math import pi

class Render:
    def __init__(self):
        pygame.init()
        
        self.screen_res = [512,512]
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(self.screen_res)
        self.fps = 30
        
        pivot = [self.screen_res[0] / 2, self.screen_res[1] / 4]
        self.pend = Pendulum(pivot, 100, pi - 0.001)
        
    def draw_text(self, text:str, pos):
        text_img = pygame.font.SysFont('Calibri', 20).render(text, True, (255,255,255))
        text_rect = text_img.get_rect()
        text_rect.topleft = pos
        self.screen.blit(text_img, text_rect)
        
    def mainloop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                    
            pressed = pygame.key.get_pressed()
            
            if pressed[pygame.K_UP]:
                self.pend.angle_velocity += 0.05
                self.pend.update()
                
            if pressed[pygame.K_DOWN]:
                self.pend.angle_velocity -= 0.05
                self.pend.update()

            self.screen.fill((0, 0, 0))
            
            #update screen
            self.pend.update()
            
            #draw some text
            self.draw_text(f'angle: {self.pend.angle:.6f}', [10, 10])
            self.draw_text(f'angle acceleration: {self.pend.angle_acceleration:.6f}', [10, 30])
            self.draw_text(f'angle velocity: {self.pend.angle_velocity:.6f}', [10, 50])
            
            #draw pendulum
            pygame.draw.line(self.screen, (255, 255, 255), self.pend.pivot, [self.pend.bob[0] - 1, self.pend.bob[1]], 3)
            pygame.draw.circle(self.screen, (255, 255, 255), self.pend.bob, 8)
            
            #update screen
            pygame.display.flip()
            self.clock.tick(self.fps)
        
r = Render()

r.mainloop()
    