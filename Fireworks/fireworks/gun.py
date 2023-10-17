# libs
from drawzero import *
from math import cos, sin, radians

# self
from fireworks.common import Vec2, type_color, angle
from fireworks.fireworks import Fireworks, FireworkOptions

class Bullet:
    pos: Vec2
    speed: Vec2
    args: FireworkOptions
    is_move: bool
    tcolor: int # enum
    color: (int, int, int) # rgb

    def __init__(self, pos, color, args: FireworkOptions, speed_bust):
        self.args = args
        self.pos = pos
        self.is_move = True
        self.tcolor = type_color(color)
        self.color = color

        angle2 = angle(self.pos.x, self.pos.y, self.args.pos.x, self.args.pos.y)

        self.speed = Vec2(-cos(radians(angle2)) * speed_bust, -sin(radians(angle2)) * speed_bust)

    def update(self):
        # move
        if self.is_move:
            self.pos.x += self.speed.x
            self.pos.y += self.speed.y

        # check move for firework
        if self.speed.y < 0:
            self.is_move = False if self.pos.y <= self.args.pos.y else True
        elif self.speed.y > 0:
            self.is_move = False if self.pos.y >= self.args.pos.y else True
        else:
            self.is_move = False

    def draw(self):
        circle("red", (self.pos.x, self.pos.y), 2)


class Gun:
    bullets: [Bullet]
    fireworks: Fireworks
    pos: Vec2
    bullet_bust: int

    def __init__(self, fireworks: Fireworks, pos: Vec2, bullet_bust: int = 5):
        self.bullets = []
        self.fireworks = fireworks
        self.pos = pos.clone()
        self.bullet_bust = bullet_bust

    def push_bullet(self, options: FireworkOptions):
        self.bullets.append(Bullet(self.pos.clone(), C.white, options, self.bullet_bust))

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
        filled_circle("white", (self.pos.x, self.pos.y), 7)
