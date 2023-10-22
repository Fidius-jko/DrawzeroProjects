from drawzero import *
from typing import Self
from random import randint
from state import change_state, GameState
from particles.particle import ParticleOptions, ParticleGroup, Direction

BULLET_SPEED = 15
PLAYER_SPEED = 1.5
RESISTANCE = 0.9


class FuncReturn:
    Run = 0
    Fail = 1


# for tools
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


class Bullet:
    pos: Pt
    width: Pt

    def __init__(self, pos: Pt, width: Pt):
        self.pos = pos
        self.width = width

    def update(self):
        self.pos.x -= BULLET_SPEED

    def draw(self):
        filled_rect("white", self.pos, self.width)

    def hitbox(self):
        return Hitbox(self.pos, self.width)


class Bullets:
    bullets: [Bullet]

    def __init__(self):
        self.bullets = []

    def add_bullet(self, pos: Pt, width: Pt = Pt(15, 5)):
        self.bullets.append(Bullet(pos.copy(), width.copy()))

    def update(self):
        for i in self.bullets:
            i.update()
            if i.pos.x < -300:
                self.bullets.remove(i)

    def draw(self):
        for i in self.bullets:
            i.draw()

    def get_bullets(self):
        return self.bullets


class Player:
    pos: Pt
    width: Pt
    speed: Pt
    particle_group: ParticleGroup
    ticks: int

    def __init__(self, pos: Pt, particle_group: ParticleGroup, width: Pt = Pt(30, 30)):
        self.pos = pos
        self.width = width
        self.speed = Pt(0, 0)
        self.particle_group = particle_group
        self.ticks = 0

    def update(self, bullets: Bullets):
        keys = get_keys_pressed()
        if keys[KEY.w] or keys[KEY.UP]:
            self.speed.y -= PLAYER_SPEED
        if keys[KEY.s] or keys[KEY.DOWN]:
            self.speed.y += PLAYER_SPEED

        if self.ticks % 5 == 0:
            self.particle_group.make_particles(
                options=
                ParticleOptions(
                    self.pos + Pt(0, self.width.y / 2),
                    Gradient([C.orange, C.black], 0, 20),
                    speed=(4, 9),
                    dir=Direction.LEFT,
                    life=20)),

        self.pos += self.speed
        self.speed *= RESISTANCE
        self.ticks += 1

        for i in bullets.get_bullets():
            if self.hitbox().check(i.hitbox()):
                return FuncReturn.Fail
        return FuncReturn.Run

    def draw(self):
        # rect("white", self.pos, self.width)
        image("assets/spaceship.png", self.pos - Pt(5, 10), 50)

    def hitbox(self):
        return Hitbox(self.pos, self.width)


class Game:
    pl: Player
    bullets: Bullets
    particle_group: ParticleGroup
    ticks: int

    def __init__(self):
        self.particle_group = ParticleGroup()
        self.pl = Player(Pt(100, 500), self.particle_group)
        self.bullets = Bullets()
        self.ticks = 0

    def init(self):
        self.particle_group = ParticleGroup()
        self.pl = Player(Pt(100, 500), self.particle_group)
        self.bullets = Bullets()

    def update(self):
        if self.pl.update(self.bullets) == FuncReturn.Fail:
            change_state(GameState.Menu)
            return

        self.bullets.update()

        if self.ticks % 5 == 0:
            self.bullets.add_bullet(Pt(980, randint(0, 980)))
        self.particle_group.update()

        tick()
        fill("black", 70)

        self.ticks += 1
        self.particle_group.draw()
        self.pl.draw()
        self.bullets.draw()
