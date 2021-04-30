class Field:
    column = "abcdefgh"
    row = "12345678"

    def __init__(self, AI=False):
        self.data = dict()
        for x in Field.row:
            for y in Field.column:
                self.data[f"{y}{x}"] = "  "

    def check_movement(self, move, player):
        # [a1,b2,KK]
        self.data[move[0]]

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
    def __init__(self, name, white, AI=False):
        self.name = name
        self.white = white
        self.AI = AI

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
        else:#todo: when it is occupied it should fight
            pass
        # field.data[query[0]] = "  "
        # field.data[query[1]] = "kk"
        # field.show()


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


class King(Pieces):
    def validate(self, movement):
        valid_movements = list()
        column = self.location[0]
        row = self.location[1]
        index_column = Field.column.find(column)
        index_row = Field.row.find(row)
        for column in [-1, 0, 1]:
            for row in [-1, 0, 1]:
                if (index_column + column >= 0 and index_row + row >= 0) and (
                        index_column + column <= 9 and index_row + row <= 9):
                    try:
                        valid_movements.append(f"{Field.column[index_column + column]}{Field.row[index_row + row]}")
                    except:
                        pass
        valid_movements = set(valid_movements)
        valid_movements.discard(self.location)
        return True if movement in valid_movements else False


class Queen(Pieces):
    def validate(self, move):
        valid_movements = list()
        column = self.location[0]
        row = self.location[1]
        index_column = Field.column.find(column)
        index_row = Field.row.find(row)
        row_move = [f"{self.location[0]}{x}" for x in range(1, 9)]
        column_move = [f"{x}{self.location[1]}" for x in "abcdefgh"]
        for oprator in range(9):
            if index_column + oprator <= 7 and index_row + oprator <= 7:
                valid_movements.append(f"{Field.column[index_column + oprator]}{Field.row[index_row + oprator]}")
            if index_column - oprator >= 0 and index_row - oprator >= 0:
                valid_movements.append(f"{Field.column[index_column - oprator]}{Field.row[index_row - oprator]}")
            if index_column + oprator <= 7 and index_row - oprator >= 0:
                valid_movements.append(f"{Field.column[index_column + oprator]}{Field.row[index_row - oprator]}")
            if index_column - oprator >= 0 and index_row + oprator <= 7:
                valid_movements.append(f"{Field.column[index_column - oprator]}{Field.row[index_row + oprator]}")
        valid_movements += row_move
        valid_movements += column_move
        valid_movements = set(valid_movements)
        valid_movements.discard(self.location)
        return True if move in valid_movements else False
        # print(valid_movements)


Sina = Player("sina", True)

field = Field(False)
# king_white = King(True, "h8", "KK")
queen_black = Queen(False, "d8", "QQ")
# print(king_white.validate("g8"))
queen_black.validate("ashgd")
for i in range(4):
    field.show()
    Sina.move()
# Sina.move()
# Sina.move()
# Sina.move()
# field.show()
