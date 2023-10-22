from drawzero import *
from game import Game
from menu import Menu
from particles.particle import ParticleGroup
import state

menu = Menu()
game = Game()

while True:
    if state.game_state == state.GameState.Game:
        if state.change_states:
            game.init()
            state.change_states = False
        game.update()

    elif state.game_state == state.GameState.Menu:
        if state.change_states:
            menu.init()
            state.change_states = False
        menu.update()
    elif state.game_state == state.GameState.Exit:
        break

quit()
