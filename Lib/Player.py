class Player:
    players=dict()
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