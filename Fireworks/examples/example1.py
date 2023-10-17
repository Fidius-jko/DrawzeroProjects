from drawzero import *
from fireworks.default_import import *


fireworks = Fireworks()
gun = Gun(fireworks, Vec2(500, 500), bullet_bust=1)

# with pos, color, speed
gun.push_bullet(
    FireworkOptions(
        Vec2(500, 500),
        color=Gradient([C.green, C.black],0, 200),
        speed=(5, 10)
    )
)

# with pos only
gun.push_bullet(
    FireworkOptions(
        Vec2(600, 600)
    )
)

# with color and pos
gun.push_bullet(
    FireworkOptions(
        Vec2(400, 400),
        color=C.red
    )
)

while True:
    gun.update()

    tick()
    # clear
    filled_rect("black", pos=(0, 0), width=1000, height=1000, alpha=20)
    fps()

    gun.draw()
