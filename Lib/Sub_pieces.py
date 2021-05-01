from Lib.Pieces import Pieces
from Lib.Player import Player

class King(Pieces):
    def validate(self, movement):
        player=Player.players.get(self.white)
        if not player.ai:
            valid_movements=self.check_possible_movements(3,player,field,1)
        else:
            valid_movements = self.check_possible_movements(3, player, field_ai, 1)
        return True if movement in valid_movements else False


class Queen(Pieces):
    def validate(self, move):
        player = Player.players.get(self.white)
        if not player.ai:
            valid_movements = self.check_possible_movements(3, player, field)
        else:
            valid_movements = self.check_possible_movements(3, player, field_ai)
        return True if move in valid_movements else False
        # print(valid_movements)