from drawzero import *
from state import change_state, GameState


def rounded_rect(color, pos: Pt, width: Pt, rounded: int):
    filled_rect(color, (pos.x + rounded, pos.y), (width.x - rounded * 2, width.y))
    filled_rect(color, (pos.x, pos.y + rounded), (width.x, width.y - rounded * 2))

    filled_circle(color, (pos.x + rounded, pos.y + rounded), rounded)
    filled_circle(color, (pos.x + width.x - rounded, pos.y + rounded), rounded)
    filled_circle(color, (pos.x + rounded, pos.y + width.y - rounded), rounded)
    filled_circle(color, (pos.x + width.x - rounded, pos.y + width.y - rounded), rounded)





class SelectMenu:
    Start = 0
    Exit = 1
    Count = 1


class Menu:
    select_menu: int  # enum SelectMenu

    def __init__(self):
        self.init()

    def init(self):
        self.select_menu = SelectMenu.Start

    def update(self):
        keys = keysdown
        for i in keys:
            key_down = i.__dict__.get('key')
            if key_down == KEY.w or key_down == KEY.UP:
                self.select_menu -= 1

                if self.select_menu == -1:
                    self.select_menu = SelectMenu.Count

            if key_down == KEY.s or key_down == KEY.DOWN:
                self.select_menu = (self.select_menu + 1) % (SelectMenu.Count + 1)

            if key_down == KEY.SPACE:
                if self.select_menu == SelectMenu.Start:
                    change_state(GameState.Game)
                    return
                elif self.select_menu == SelectMenu.Exit:
                    change_state(GameState.Exit)
                    return

        tick()
        # fill("black", 50)
        image("assets/menu_background.png", (0, 0), alpha=50)

        rounded_rect(C.orange, Pt(300, 150), Pt(400, 400), 16)

        text("white", "Start", (500, 250 + 100 * SelectMenu.Start), 100)
        text("white", "Exit", (500, 250 + 100 * SelectMenu.Exit), 100)

        change = 100 * self.select_menu

        filled_polygon("white", [(380, 230 + change), (400, 250 + change), (380, 270 + change)])
