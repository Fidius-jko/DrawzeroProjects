from drawzero import *
from typing import Tuple

class Wave:
    def __init__(self, pos: Tuple[int, int], r: int, r_in_sec: int):
        self.pos = pos
        self.r = r
        self.r_in_sec = r_in_sec
    def update(self):
        self.r += self.r_in_sec
        circle(scale(self.pos[1] + self.r),self.pos, self.r)


scale = Gradient([C.gray10, C.red, C.green, C.blue,C.green, C.red, C.gray10], 0, 1000)
width = 1000
height = 1000
ticks = 0

waves = []
while True:
    if ticks % 1 == 0:
        x, y = mouse_pos()
        r = 1
        for i in range(1, 51):
            waves.append(Wave((x, y), i, 50))

    for i in waves:
        i.update()
        if i.r > 1500:
            waves.remove(i)
    ticks += 1
    tick()
    clear()
