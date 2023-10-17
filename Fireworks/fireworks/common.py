from dataclasses import dataclass
from drawzero import Gradient
from math import atan2, pi

class FireworkColorType:
    STD_COLOR = 0
    GRADIENT = 1
    NONE = -1


def type_color(color) -> int:
    tcolor = FireworkColorType.NONE
    if type(color) is tuple:
        tcolor = FireworkColorType.STD_COLOR
    elif type(color) is Gradient:
        tcolor = FireworkColorType.GRADIENT
    else:
        print(f"Error, color type doesn't support {type(color)}")
        return FireworkColorType.NONE
    return tcolor

def angle(x1, y1, x2, y2) -> float:
    x = x1 - x2
    y = y1 - y2
    rad = atan2(y, x) / pi * 180
    rad = rad if rad < 0 else rad + 360
    return rad

@dataclass
class Vec2:
    x: float
    y: float

    def clone(self):
        return Vec2(self.x, self.y)
