from random import randint
from drawzero import *

from common import Vec2
from fireworks import Fireworks, FireworkOptions
from gun import Gun


fireworks = Fireworks()
gun = Gun(fireworks)

# examples
gun.push_bullet(
    FireworkOptions(
        Vec2(500, 500),
        color=Gradient([C.green, C.black],0, 200),
        speed=(5, 10)
    )
)
gun.push_bullet(
    FireworkOptions(
        Vec2(600, 600)
    )
)
gun.push_bullet(
    FireworkOptions(
        Vec2(400, 400),
        color=C.red
    )
)

while True:
    if mousebuttonsup:
        x, y = mousebuttonsup[0].pos
        colors = [C.red, C.green, C.blue, C.gold, C.yellow, C.brown]
        c = randint(0, len(colors)-1)

        gun.push_bullet(
            FireworkOptions(
                Vec2(x, y),
                color=Gradient([colors[c], C.black],0, 200)
            )
        )
    gun.update()

    tick()
    # clear
    filled_rect("black", pos=(0, 0), width=1000, height=1000, alpha=20)

    gun.draw()
