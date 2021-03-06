import sys

import pygame
from pendulum import Pendulum, DoublePendulum
from math import pi, hypot

class Render:
    def __init__(self):
        pygame.init()
        
        self.screen_res = [512,512]
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(self.screen_res)
        self.fps = 60
        
        pivot = [self.screen_res[0] / 2, self.screen_res[1] / 6]
        self.pend = DoublePendulum(pivot, 150, pi / 2)
        
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
                elif event.type == pygame.MOUSEMOTION:
                    mouse_motion = event.rel

            self.screen.fill((0, 0, 0))
            
            left_click = pygame.mouse.get_pressed()[0]
            right_click = pygame.mouse.get_pressed()[2]
                
            if left_click and mouse_motion:
                self.pend.angle1 += mouse_motion[0] * 0.01
                self.pend.bob1 = self.pend.bob1_pos()
                self.pend.bob2 = self.pend.bob2_pos()
            elif right_click and mouse_motion:
                self.pend.angle2 += mouse_motion[0] * 0.01
                self.pend.bob1 = self.pend.bob1_pos()
                self.pend.bob2 = self.pend.bob2_pos()
                
            else:
                color = (255, 255, 255)
                self.pend.update()
            
            #draw some text
            self.draw_text(f'angle1: {self.pend.angle1:.6f}', [10, 10])
            self.draw_text(f'angle1 acceleration: {self.pend.acceleration1:.6f}', [10, 30])
            self.draw_text(f'angle1 velocity: {self.pend.velocity1:.6f}', [10, 50])
            self.draw_text(f'angle2: {self.pend.angle2:.6f}', [10, 70])
            self.draw_text(f'angle2 acceleration: {self.pend.acceleration2:.6f}', [10, 90])
            self.draw_text(f'angle2 velocity: {self.pend.velocity2:.6f}', [10, 110])
            self.draw_text(f'fps: {self.clock.get_fps():.6f}', [10, 130])
            
            #draw pendulum
            pygame.draw.line(self.screen, (255, 255, 255), [self.pend.pivot[0] - 1, self.pend.pivot[1]], [self.pend.bob1[0] - 1, self.pend.bob1[1]], 3)
            pygame.draw.circle(self.screen, color, self.pend.bob1, 8)
            pygame.draw.line(self.screen, (255, 255, 255), [self.pend.bob1[0] - 1, self.pend.bob1[1]], [self.pend.bob2[0] - 1, self.pend.bob2[1]], 3)
            pygame.draw.circle(self.screen, (255, 255, 255), self.pend.bob2, 8)
            
            #update screen
            pygame.display.flip()
            self.clock.tick(self.fps)
        
r = Render()

r.mainloop()
    