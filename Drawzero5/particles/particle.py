from random import uniform
from math import sin, cos, radians
from dataclasses import dataclass
from drawzero import *

from common import type_color
from particles.consts import GRAVITY, RESISTANCE
from typing import Any

class Direction:
    LEFT = 0
    RIGHT = 1
    NONE = 2

class ParticleOptions:
    pos: Pt
    color: Any  # rgb
    count: int
    speed: (int, int)
    dir: int
    life: int

    def __init__(self, pos: Pt, color=C.red, count: int = 50, speed=(5, 10), dir: int = Direction.NONE, life: int = 100):
        self.pos = pos.copy()
        self.color = color
        self.count = count
        self.speed = speed
        self.dir = dir
        self.life = life


@dataclass
class Particle:
    pos: Pt
    speed: Pt


class Particles:
    particles: [Particle]
    color: C
    tcolor: int  # enum
    ticks: int
    gradient: Gradient
    is_empty: bool
    dir: int
    life: int

    def set_color(self, color):
        self.tcolor = type_color(color)
        self.color = color

    def make_particles(self, pos, count, speed):
        for i in range(count):
            speed2 = uniform(speed[0], speed[1])
            a = uniform(180, -180)
            if self.dir == Direction.RIGHT:
                a = uniform(100, -100)
            elif self.dir == Direction.LEFT:
                a = 180 - uniform(100, -100)
            dx = cos(radians(a))
            dy = sin(radians(a))
            self.particles.append(Particle(pos.copy(), Pt(dx * speed2, dy * speed2)))

    def __init__(self, options: ParticleOptions):
        self.particles = []
        self.ticks = 0
        self.is_empty = False
        self.dir = options.dir

        self.set_color(options.color)
        self.make_particles(options.pos.copy(), options.count, options.speed)
        self.life = options.life

    def update(self):
        if len(self.particles) == 0:
            self.is_empty = True
            return
        self.ticks += 1
        for i in self.particles:
            i.pos.x += i.speed.x
            i.pos.y += i.speed.y
            i.speed.x *= RESISTANCE
            i.speed.y *= RESISTANCE
            i.speed.y += GRAVITY
            if i.pos.y > 1000 or i.pos.x > 1000 or i.pos.x < 0 or self.life < self.ticks:
                self.particles.remove(i)

    def draw(self):
        if self.is_empty:
            return
        for i in self.particles:
            if self.tcolor == 0:
                filled_circle(self.color, (i.pos.x, i.pos.y), 4)
            elif self.tcolor == 1:
                filled_circle(self.color(self.ticks), (i.pos.x, i.pos.y), 4)


class ParticleGroup:
    fireworks: []

    def __init__(self):
        self.fireworks = []

    def make_particles(self, options: ParticleOptions):
        self.fireworks.append(Particles(options))

    def update(self):
        for i in self.fireworks:
            i.update()
            if i.is_empty:
                self.fireworks.remove(i)

    def draw(self):
        for i in self.fireworks:
            i.draw()
