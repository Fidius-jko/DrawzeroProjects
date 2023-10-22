from random import randint
from drawzero import *

# for tools
from fireworks.default_import import *
# for tools

fireworks = Fireworks()
gun = Gun(fireworks, Vec2(250, 250))

fireworks = Fireworks()
gun2 = Gun(fireworks, Vec2(750, 250))

fireworks = Fireworks()
gun3 = Gun(fireworks, Vec2(250, 750))

fireworks = Fireworks()
gun4 = Gun(fireworks, Vec2(750, 750))

while True:
    if mousebuttonsup:
        x, y = mousebuttonsup[0].pos
        colors = [C.red, C.green, C.blue, C.gold, C.yellow, C.brown]
        c = randint(0, len(colors)-1)
        tmp_gun = gun
        if x > 500 and y <= 500:
            tmp_gun = gun2
        elif x <= 500 and y > 500:
            tmp_gun = gun3
        elif x > 500 and y > 500:
            tmp_gun = gun4
        tmp_gun.push_bullet(
            FireworkOptions(
                Vec2(x, y),
                color=Gradient([colors[c], C.black],0, 200),
                count=10
            )
        )
    gun.update()
    gun2.update()
    gun3.update()
    gun4.update()

    tick()
    # clear
    filled_rect("black", pos=(0, 0), width=1000, height=1000, alpha=20)

    gun.draw()
    gun2.draw()
    gun3.draw()
    gun4.draw()
