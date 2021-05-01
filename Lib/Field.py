#import chess
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
                        f"| {self.data[f'{Field.column[0]}{9 - imaginary_row}']} |.{self.data[f'{Field.column[1]}{9 - imaginary_row}']}.| {self.data[f'{Field.column[2]}{9 - imaginary_row}']} |.{self.data[f'{Field.column[3]}{9 - imaginary_row}']}.| {self.data[f'{Field.column[4]}{9 - imaginary_row}']} |.{self.data[f'{Field.column[5]}{9 - imaginary_row}']}.| {self.data[f'{Field.column[6]}{9 - imaginary_row}']} |.{self.data[f'{Field.column[7]}{9 - imaginary_row}']}.|  {9 - imaginary_row}")
                    print("|____|____|____|____|____|____|____|____|  ", sep="")
                    imaginary_row += 1
                else:
                    print("|.  .|    |.  .|    |.  .|    |.  .|    |  ")
                    print(
                        f"|.{self.data[f'{Field.column[0]}{9 - imaginary_row}']}.| {self.data[f'{Field.column[1]}{9 - imaginary_row}']} |.{self.data[f'{Field.column[2]}{9 - imaginary_row}']}.| {self.data[f'{Field.column[3]}{9 - imaginary_row}']} |.{self.data[f'{Field.column[4]}{9 - imaginary_row}']}.| {self.data[f'{Field.column[5]}{9 - imaginary_row}']} |.{self.data[f'{Field.column[6]}{9 - imaginary_row}']}.| {self.data[f'{Field.column[7]}{9 - imaginary_row}']} |  {9 - imaginary_row}")
                    print("|____|____|____|____|____|____|____|____|  ", sep="")
                    imaginary_row += 1