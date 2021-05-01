class Field:
    column = "abcdefgh"
    row = "12345678"

    def __init__(self, ai=False):
        self.data = dict()
        for x in Field.row:
            for y in Field.column:
                self.data[f"{y}{x}"] = "  "

    def check_movement(self, move, player):
        # [a1,b2,KK]
        # self.data[move[0]]
        pass

    def show(self):
        counter = 0
        line = str()
        imaginary_row = 1
        for row in range(1, 11):
            if row == 1:
                for column in range(1, 39):
                    if column < 2:
                        line += " "
                    elif column == 3:
                        line += Field.column[counter]
                        counter += 1
                    elif (column - 3) % 5 == 0:
                        line += Field.column[counter]
                        counter += 1
                    else:
                        line += " "
                print(line)
                line = ""
            elif row == 2:
                line = " "
                for column in range(1, 40):
                    line += "_"
                print(line)
            else:
                if (9 - imaginary_row) % 2 == 0:
                    print("|    |.  .|    |.  .|    |.  .|    |.  .|  ")
                    print(
                        f"| {field.data[f'{Field.column[0]}{9 - imaginary_row}']} |.{field.data[f'{Field.column[1]}{9 - imaginary_row}']}.| {field.data[f'{Field.column[2]}{9 - imaginary_row}']} |.{field.data[f'{Field.column[3]}{9 - imaginary_row}']}.| {field.data[f'{Field.column[4]}{9 - imaginary_row}']} |.{field.data[f'{Field.column[5]}{9 - imaginary_row}']}.| {field.data[f'{Field.column[6]}{9 - imaginary_row}']} |.{field.data[f'{Field.column[7]}{9 - imaginary_row}']}.|  {9 - imaginary_row}")
                    print("|____|____|____|____|____|____|____|____|  ", sep="")
                    imaginary_row += 1
                else:
                    print("|.  .|    |.  .|    |.  .|    |.  .|    |  ")
                    print(
                        f"|.{field.data[f'{Field.column[0]}{9 - imaginary_row}']}.| {field.data[f'{Field.column[1]}{9 - imaginary_row}']} |.{field.data[f'{Field.column[2]}{9 - imaginary_row}']}.| {field.data[f'{Field.column[3]}{9 - imaginary_row}']} |.{field.data[f'{Field.column[4]}{9 - imaginary_row}']}.| {field.data[f'{Field.column[5]}{9 - imaginary_row}']} |.{field.data[f'{Field.column[6]}{9 - imaginary_row}']}.| {field.data[f'{Field.column[7]}{9 - imaginary_row}']} |  {9 - imaginary_row}")
                    print("|____|____|____|____|____|____|____|____|  ", sep="")
                    imaginary_row += 1


class Player:
    players=dict
    def __init__(self, name, white, ai=False):
        self.name = name
        self.white = white
        self.ai = ai
        Player.players[white]=self

    def move(self):
        query = input("enter your move: ")
        query_test = query.split()
        if len(query_test) == 1:
            query = query.split(",")
        else:
            query = query_test

        if field.data[query[0]] != "  ":
            piece_object = Pieces.character_dict.get(field.data[query[0]])
            print(piece_object)
            if piece_object.validate(
                    query[1]):  # todo: add other verifications such as is that slot free or it's way clear or not
                field.data[query[0]] = "  "
                field.data[query[1]] = piece_object.character
                piece_object.location = query[1]
                return True
            else:
                return False
        else:  # todo: when it is occupied it should fight
            pass


class Pieces:
    character_dict = dict()

    def __init__(self, white, location, character):
        self.white = white
        self.type = type
        self.location = location
        self.character = character
        Pieces.character_dict[character] = self
        field.data[location] = character

    def __repr__(self):
        return f"it is character {self.character}"

    def check_possible_movements(self, pattern, player, field_to_check, depth=9):
        # patterns:cross=1,multiple=2,full=3,complex=4,cross_forward=5
        overal_possible_movements = list()
        column_index = Field.column.find(self.location[0])
        row_index = Field.row.find((self.location[1]))
        if pattern == 1:  # cross
            # check right line
            for I in range(1, depth):
                if column_index + I <= 7:
                    posible_move = f"{Field.column[column_index + I]}{self.location[1]}"
                    if field_to_check.data[posible_move] != "  ":
                        ended_with_piece = Pieces.character_dict.get(field_to_check.data[posible_move])
                        if ended_with_piece.white == player.white:
                            break
                        else:
                            overal_possible_movements.append(posible_move)
                            break
                    else:
                        overal_possible_movements.append(posible_move)
            # check left line
            for I in range(1, depth):
                if column_index - I >= 0:
                    posible_move = f"{Field.column[column_index - I]}{self.location[1]}"
                    if field_to_check.data[posible_move] != "  ":
                        ended_with_piece = Pieces.character_dict.get(field_to_check.data[posible_move])
                        if ended_with_piece.white == player.white:
                            break
                        else:
                            overal_possible_movements.append(posible_move)
                            break
                    else:
                        overal_possible_movements.append(posible_move)
            # check up line
            for I in range(1, depth):
                if row_index + I <= 7:
                    posible_move = f"{self.location[0]}{Field.row[row_index + I]}"
                    if field_to_check.data[posible_move] != "  ":
                        ended_with_piece = Pieces.character_dict.get(field_to_check.data[posible_move])
                        if ended_with_piece.white == player.white:
                            break
                        else:
                            overal_possible_movements.append(posible_move)
                            break
                    else:
                        overal_possible_movements.append(posible_move)
            # check down line
            for I in range(1, depth):
                if row_index - I >= 0:
                    posible_move = f"{self.location[0]}{Field.row[row_index - I]}"
                    if field_to_check.data[posible_move] != "  ":
                        ended_with_piece = Pieces.character_dict.get(field_to_check.data[posible_move])
                        if ended_with_piece.white == player.white:
                            break
                        else:
                            overal_possible_movements.append(posible_move)
                            break
                    else:
                        overal_possible_movements.append(posible_move)
            return overal_possible_movements
        elif pattern == 2:
            # multiply
            for I in range(1, depth):
                if column_index + I <= 7 and row_index + I <= 7:
                    posible_move = f"{Field.column[column_index + I]}{Field.row[row_index + I]}"
                    if field_to_check.data[posible_move] != "  ":
                        ended_with_piece = Pieces.character_dict.get(field_to_check.data[posible_move])
                        if ended_with_piece.white == player.white:
                            break
                        else:
                            overal_possible_movements.append(posible_move)
                            break
                    else:
                        overal_possible_movements.append(posible_move)

            for I in range(1, depth):
                if column_index + I <= 7 and row_index - I >= 0:
                    posible_move = f"{Field.column[column_index + I]}{Field.row[row_index - I]}"
                    if field_to_check.data[posible_move] != "  ":
                        ended_with_piece = Pieces.character_dict.get(field_to_check.data[posible_move])
                        if ended_with_piece.white == player.white:
                            break
                        else:
                            overal_possible_movements.append(posible_move)
                            break
                    else:
                        overal_possible_movements.append(posible_move)

            for I in range(1, depth):
                if column_index - I >= 0 and row_index - I >= 0:
                    posible_move = f"{Field.column[column_index - I]}{Field.row[row_index - I]}"
                    if field_to_check.data[posible_move] != "  ":
                        ended_with_piece = Pieces.character_dict.get(field_to_check.data[posible_move])
                        if ended_with_piece.white == player.white:
                            break
                        else:
                            overal_possible_movements.append(posible_move)
                            break
                    else:
                        overal_possible_movements.append(posible_move)

            for I in range(1, depth):
                if column_index - I >= 0 and row_index + I <= 7:
                    posible_move = f"{Field.column[column_index - I]}{Field.row[row_index + I]}"
                    if field_to_check.data[posible_move] != "  ":
                        ended_with_piece = Pieces.character_dict.get(field_to_check.data[posible_move])
                        if ended_with_piece.white == player.white:
                            break
                        else:
                            overal_possible_movements.append(posible_move)
                            break
                    else:
                        overal_possible_movements.append(posible_move)
            return overal_possible_movements
        elif pattern == 3:
            cross = self.check_possible_movements(1, player, field_to_check, depth)
            multiply = self.check_possible_movements(2, player, field_to_check, depth)
            return cross + multiply


class King(Pieces):
    def validate(self, movement):
        player=Player.players.get(True)
        if not player.ai:
            valid_movements=self.check_possible_movements(3,player,field,1)
        else:
            valid_movements = self.check_possible_movements(3, player, field_ai, 1)
        return True if movement in valid_movements else False


class Queen(Pieces):
    def validate(self, move):
        player = Player.players.get(True)
        if not player.ai:
            valid_movements = self.check_possible_movements(3, player, field)
        else:
            valid_movements = self.check_possible_movements(3, player, field_ai)
        return True if move in valid_movements else False
        # print(valid_movements)


sina = Player("sina", False)

field = Field(False)
field_ai=Field(True)
# king_white = King(True, "h8", "KK")
queen_black = Queen(False, "d8", "QQ")
queen_black_1 = Queen(False, "b8", "QT")
queen_black_2 = Queen(False, "b6", "QT")
# print(king_white.validate("g8"))
queen_black.check_possible_movements(2, sina, field)
# for i in range(4):
#    field.show()
#    Sina.move()
# Sina.move()
# Sina.move()
# Sina.move()
# field.show()
