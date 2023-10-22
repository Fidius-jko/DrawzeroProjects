class GameState:
    Game = 0
    Menu = 1
    Exit = 2


game_state = GameState.Menu
change_states = False


def change_state(state: GameState):
    global game_state, change_states
    change_states = True
    game_state = state
