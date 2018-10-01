"""#This function will handle the collision of objects"""

from gameState import GameState


class CollisionManager:
    def __init__(self, game_state):
        self.game_state = GameState(game_state)

    #gotta check each intersection with each other
    #compare each intersection
    #
    def if_intersect(self):
        for i in self.game_state.asteroid:
            if self.game_state.my_ship.pos == i.pos:
                #they have collided
                pass






