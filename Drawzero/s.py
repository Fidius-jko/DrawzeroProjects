from typing import Tuple

from drawzero import *

class Wave:
    def __init__(self, pos: Tuple[int, int], r: int, r_in_sec: int):
        self.pos = pos
        self.r = r
        self.r_in_sec = r_in_sec
    def update(self):
        self.r += self.r_in_sec
        circle(scale(self.pos[0]),self.pos, self.r)


scale = Gradient([C.white, C.gray10, C.white], 0, 1000)
while True:
    x, y = mouse_pos()
    filled_circle(scale(x), (x, y), 50)
    tick()
    clear()