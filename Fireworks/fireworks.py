from random import uniform
from math import sin, cos, radians
from dataclasses import dataclass
from drawzero import *

from common import Vec2, type_color
from consts import GRAVITY, RESISTANCE

class FireworkOptions:
    pos: Vec2
    color: (int,int,int)
    count: int
    speed: (int, int)

    def __init__(self, pos: Vec2, color=C.red, count: int = 50, speed=(5, 10)):
        self.pos = pos.clone()
        self.color = color
        self.count = count
        self.speed = speed

@dataclass
class Ball:
    pos: Vec2
    speed: Vec2

class Firework:
    balls: [Ball]
    color: C
    tcolor: int
    ticks: int
    gradient: Gradient
    is_empty: bool

    def set_color(self, color):
        self.tcolor = type_color(color)
        self.color = color

    def make_balls(self, pos, count, speed):

        for i in range(count):
            speed2 = uniform(speed[0], speed[1])
            a = uniform(-180, 180)
            dx = cos(radians(a))
            dy = sin(radians(a))
            # почему не можем просто Ball(pos, ...)?
            # Если так сделаем то у всех шаров будет позиция указывать на один объект
            self.balls.append(Ball(pos.clone(), Vec2(dx * speed2, dy * speed2)))

    def __init__(self, options: FireworkOptions):
        self.balls = []
        self.ticks = 0
        self.is_empty = False

        self.set_color(options.color)
        self.make_balls(options.pos.clone(), options.count, options.speed)

    def update(self):
        if len(self.balls) == 0:
            self.is_empty = True
            return
        self.ticks += 1
        for i in self.balls:
            i.pos.x += i.speed.x
            i.pos.y += i.speed.y
            i.speed.x *= RESISTANCE
            i.speed.y *= RESISTANCE
            i.speed.y += GRAVITY
            if i.pos.y > 1000 or i.pos.x > 1000 or i.pos.x < 0:
                self.balls.remove(i)

    def draw(self):
        if self.is_empty:
            return
        for i in self.balls:
            if self.tcolor == 0:
                filled_circle(self.color, (i.pos.x, i.pos.y), 4)
            elif self.tcolor == 1:
                filled_circle(self.color(self.ticks), (i.pos.x, i.pos.y), 4)

class Fireworks:
    fireworks = []

    def __init__(self):
        pass

    def make_firework(self, options: FireworkOptions):
        self.fireworks.append(Firework(options))

    def update(self):
        for i in self.fireworks:
            i.update()
            if i.is_empty:
                self.fireworks.remove(i)

    def draw(self):
        for i in self.fireworks:
            i.draw()