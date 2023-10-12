from dataclasses import dataclass
from drawzero import Gradient

def type_color(color) -> int:
    tcolor = -1
    if type(color) is tuple:
        tcolor = 0
    elif type(color) is Gradient:
        tcolor = 1
    else:
        print("Error, color type doesn't exist")
        return -1
    return tcolor

@dataclass
class Vec2:
    x: float
    y: float

    def clone(self):
        return Vec2(self.x, self.y)