from drawzero import *
from typing import Tuple
from math import sqrt, floor
import random


# distance - растояние
def distance(pos1: Tuple[int, int], pos2: Tuple[int, int]):
    a = pos1[0] - pos2[0]
    b = pos1[1] - pos2[1]
    c = sqrt(b**2 + a**2)
    return floor(c)


class Point:
    x: int
    y: int

    vel: Tuple[int, int]

    def __init__(self, pos: Tuple[int, int], vel: Tuple[int, int]):
        self.x = pos[0]
        self.y = pos[1]
        self.vel = vel


scale = Gradient([C.white, C.gray10], 0, 100)
width = 1000
height = 1000
ticks = 0

points = []
for i in range(100):
    tmp1 = random.randrange(-11, 10) + 1
    tmp2 = random.randrange(-11, 10) + 1
    points.append(
        Point(
            (random.randrange(1, 999), random.randrange(1, 999)),
            ((tmp1, tmp2)),
        )
    )
tick()
while True:
    loop_tick = 0
    for i in points:
        circle("white", (i.x, i.y), 4)
        i.x = i.x + i.vel[0]
        i.y += i.vel[1]
        i.x %= 1000
        i.y %= 1000
        loop_tick += 1
        for j in range(loop_tick, len(points)):
            p1 = (i.x, i.y)
            p2 = (points[j].x, points[j].y)
            dst = distance(p1, p2)
            if dst < 101:
                line(scale(dst), p1, p2)

    ticks += 1
    tick()
    clear()
