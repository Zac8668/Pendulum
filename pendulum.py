from dataclasses import dataclass
from math import pi, sin, cos

class Pendulum:
    def __init__(self, pivot:list, length, angle:float = 0, gravity = -0.03, friction = 0.96):
        self.pivot = pivot
        self.length = length
        self.angle = angle
        self.bob = self.bob_pos()
        
        self.gravity = gravity
        self.friction = friction
        
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
        
        self.angle_velocity *= self.friction
        
        self.bob = self.bob_pos()

    def update(self):
        self.check_angle()

        self.check_physics()
        
class DoublePendulum:
    def __init__(self, pivot:list, length, angle:float = 0, gravity = 1, friction = 0.96):
        self.pivot = pivot
        self.length1 = length
        self.angle1 = angle
        self.bob1 = self.bob1_pos()
        self.mass1 = 10
        self.velocity1 = 0
        self.acceleration1 = 0
        
        self.length2 = length
        self.angle2 = angle
        self.bob2 = self.bob2_pos()
        self.mass2 = 10
        self.velocity2 = 0
        self.acceleration2 = 0
        
        self.GRAVITY = gravity
        self.FRICTION = friction
        
    def bob1_pos(self):
        x = self.length1 * sin(self.angle1) + self.pivot[0]
        y = self.length1 * cos(self.angle1) + self.pivot[1]

        bob_pos = [x, y]
        return bob_pos
    
    def bob2_pos(self):
        x = self.length2 * sin(self.angle2) + self.bob1[0]
        y = self.length2 * cos(self.angle2) + self.bob1[1]

        bob_pos = [x, y]
        return bob_pos
    
    def check_angle(self):
        if self.angle1 > pi * 2:
            self.angle1 -= pi * 2
        elif self.angle1 < 0:
            self.angle1 += pi * 2
        
        if self.angle2 > pi * 2:
            self.angle2 -= pi * 2
        elif self.angle2 < 0:
            self.angle2 += pi * 2
            
        self.bob1 = self.bob1_pos()
        self.bob2 = self.bob2_pos()
        
    def calc_acc1(self):
        dividend1 = -self.GRAVITY * (2 * self.mass1 + self.mass2) * sin(self.angle1)
        dividend2 = -self.mass2 * self.GRAVITY * sin(self.angle1 - 2 * self.angle2)
        dividend3 = -2 * sin(self.angle1 - self.angle2) * self.mass2
        dividend4 = self.velocity2 ** 2 * self.length2 + self.velocity1 ** 2 * self.length1 * cos(self.angle1 - self.angle2)
        
        dividend = dividend1 + dividend2 + dividend3 * dividend4
        
        divisor = self.length1 * (2 * self.mass1 + self.mass2 - self.mass2 * cos(2 * self.angle1 - 2 * self.angle2))
        
        return dividend / divisor
    
    def calc_acc2(self):
        dividend1 = 2 * sin(self.angle1 - self.angle2)
        dividend2 = self.velocity1 ** 2 * self.length1 * (self.mass1 * self.mass2)
        dividend3 = self.GRAVITY * (self.mass1 + self.mass2) * cos(self.angle1)
        dividend4 = self.velocity2 ** 2 * self.length2 * self.mass2 * cos(self.angle1 - self.angle2)
        
        dividend = dividend1 * (dividend2 + dividend3 + dividend4)
        
        divisor = self.length2 * (2 * self.mass1 + self.mass2 - self.mass2 * cos(2 * self.angle1 - 2 * self.angle2))
        
        return dividend / divisor
        
    def check_physics(self):
        self.acceleration1 = self.calc_acc1()
        
        self.velocity1 += self.acceleration1
        self.angle1 += self.velocity1
        
        self.acceleration2 = self.calc_acc2()
        
        self.velocity2 += self.acceleration2
        self.angle2 += self.velocity2
        
        self.velocity1 *= self.FRICTION
        self.velocity2 *= self.FRICTION
        
        self.bob1 = self.bob1_pos()
        self.bob2 = self.bob2_pos()

    def update(self):
        self.check_angle()
        self.check_physics()
        