from dataclasses import dataclass
from math import pi, sin, cos

class Pendulum:
    def __init__(self, pivot:list, length, angle:float = 0, gravity = -0.01):
        self.pivot = pivot
        self.length = length
        self.angle = angle
        self.bob = self.bob_pos()
        
        self.gravity = gravity
        self.angle_velocity = 0
        self.angle_acceleration = 0
        
    def bob_pos(self):
        x = self.length * sin(self.angle) + self.pivot[0]
        y = self.length * cos(self.angle) + self.pivot[1]

        bob_pos = [x, y]
        return bob_pos
    
    def check_angle(self):
        if self.angle > pi * 2:
            self.angle -= pi * 2
        elif self.angle < 0:
            self.angle += pi * 2
            
        self.bob = self.bob_pos()
        
    def check_physics(self):
        self.angle_acceleration = self.gravity * sin(self.angle)
            
        self.angle += self.angle_velocity
        self.angle_velocity += self.angle_acceleration
        
        self.angle_velocity *= 0.99
        
        self.bob = self.bob_pos()

    def update(self):
        self.check_angle()

        self.check_physics()
        