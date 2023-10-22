from drawzero import *
from typing import Self

PLAYER_SPEED = 10


class Hitbox:
    pos: Pt
    width: Pt

    def __init__(self, pos, width):
        self.pos = pos.copy()
        self.width = width.copy()

    def point_in(self, point: Pt):
        exp1x = self.pos.x <= point.x <= (self.pos.x + self.width.x)
        exp1y = self.pos.y <= point.y <= (self.pos.y + self.width.y)
        return exp1x and exp1y

    def check(self, hitbox: Self):
        e1 = self.point_in(hitbox.pos)
        e2 = self.point_in(Pt(hitbox.pos.x + hitbox.width.x, hitbox.pos.y))
        e3 = self.point_in(Pt(hitbox.pos.x, hitbox.pos.y + hitbox.width.y))
        e4 = self.point_in(hitbox.pos + hitbox.width)
        return e1 or e2 or e3 or e4


class Player:
    pos: Pt
    k: int

    def __init__(self, pos: Pt, k: int):
        self.pos = pos.copy()
        self.k = k

    def update(self):
        keys = get_keys_pressed()
        if self.k == 0:
            if keys[KEY.w]:
                self.pos.y -= PLAYER_SPEED
            if keys[KEY.s]:
                self.pos.y += PLAYER_SPEED
            if keys[KEY.d]:
                self.pos.x += PLAYER_SPEED
            if keys[KEY.a]:
                self.pos.x -= PLAYER_SPEED
        elif self.k == 1:
            if keys[KEY.UP]:
                self.pos.y -= PLAYER_SPEED
            if keys[KEY.DOWN]:
                self.pos.y += PLAYER_SPEED
            if keys[KEY.RIGHT]:
                self.pos.x += PLAYER_SPEED
            if keys[KEY.LEFT]:
                self.pos.x -= PLAYER_SPEED

    def draw(self):
        rect("white", pos=self.pos, width=(50, 50))

    def hitbox(self):
        return Hitbox(self.pos, Pt(50, 50))


pl = Player(Pt(100, 100), 0)
pl2 = Player(Pt(100, 500), 1)

while True:
    pl.update()
    pl2.update()
    tick()
    if pl.hitbox().check(pl2.hitbox()):
        filled_rect("red", (0, 0), (1000, 1000))
    else:
        clear()
    pl.draw()
    pl2.draw()
