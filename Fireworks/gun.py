from drawzero import *
from math import cos, sin, atan2, pi, radians

from common import Vec2, type_color
from fireworks import Fireworks, FireworkOptions

class Bullet:
    pos: Vec2
    speed: Vec2
    args: FireworkOptions
    is_move: bool
    tcolor: int
    color: (int,int,int)

    def __init__(self, pos, color, args: FireworkOptions):
        self.args = args
        self.pos = pos
        self.is_move = True
        self.tcolor = type_color(color)
        self.color = color
        x = self.pos.x - self.args.pos.x
        y = self.pos.y - self.args.pos.y
        rad = atan2(y, x) / pi * 180
        rad = 360 if rad < 0 else rad + 360
        self.speed = Vec2(-cos(radians(rad)) * 5, -sin(radians(rad)) * 5)

    def update(self):
        if self.is_move:
            self.pos.x += self.speed.x
            self.pos.y += self.speed.y
        if self.pos.y <= self.args.pos.y:
            self.is_move = False
    def draw(self):
        circle("red", (self.pos.x, self.pos.y), 2)

class Gun:
    bullets: [Bullet]
    fireworks: Fireworks

    def __init__(self, fireworks: Fireworks):
        self.bullets = []
        self.fireworks = fireworks

    def push_bullet(self, options: FireworkOptions):
        self.bullets.append(Bullet(Vec2(500, 1000), C.white, options))

    def update(self):
        for i in self.bullets:
            i.update()
            if not i.is_move:
                self.fireworks.make_firework(i.args)
                self.bullets.remove(i)
        self.fireworks.update()

    def draw(self):
        for i in self.bullets:
            i.draw()
        self.fireworks.draw()
        filled_circle("white", (500, 1000), 7)