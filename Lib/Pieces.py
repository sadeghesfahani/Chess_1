from Lib.Field import Field
class Pieces:
    character_dict = dict()

    def __init__(self, white, location, character,field):
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