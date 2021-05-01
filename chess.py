from Lib.Field import Field
from Lib.Sub_pieces import *
from Lib.Player import Player
#from Lib.Pieces import Pieces




sina = Player("sina", False)

field = Field(False)
field_ai=Field(True)
# king_white = King(True, "h8", "KK")
queen_black = Queen(False, "d8", "QQ",field)
queen_black_1 = Queen(False, "b8", "QT",field)
queen_black_2 = Queen(False, "b6", "QT",field)
# print(king_white.validate("g8"))
queen_black.check_possible_movements(2, sina, field)
# for i in range(4):
#    field.show()
#    Sina.move()
# Sina.move()
# Sina.move()
# Sina.move()
field.show()
