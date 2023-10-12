from drawzero import *
from typing import Tuple

scale = Gradient([C.white, C.black, C.white], 0, 1000)

def gradient_circle(grad, pos: Tuple[int, int], r):
    for i in range(r):
        circle(grad(pos[0]+i -500), (pos[0], pos[1]), i)

while True:
    m_pos = mouse_pos()
    gradient_circle(scale, m_pos, 1500)
    tick()
    clear()
