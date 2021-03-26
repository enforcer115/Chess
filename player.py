import pieces


class Player:
    def __init__(self, player):
        self.player = player
        self.piece_list = []
        self.init_pieces()
        self.capture_list = []

    def init_pieces(self):
        piece_list = []
        back_row = 0
        # add pawns
        for row in range(8):
            if self.player == "white":
                self.piece_list.append(pieces.Pawn(row, 1, self.player))
            elif self.player == "black":
                self.piece_list.append(pieces.Pawn(row, 6, self.player))
            else:
                raise Exception("Player must be white or black")

        # set row depending on color
        if self.player == "black":
            back_row = 7

        self.piece_list.append(pieces.Rook(0, back_row, self.player))
        self.piece_list.append(pieces.Rook(7, back_row, self.player))

        self.piece_list.append(pieces.Knight(1, back_row, self.player))
        self.piece_list.append(pieces.Knight(6, back_row, self.player))

        self.piece_list.append(pieces.Bishop(2, back_row, self.player))
        self.piece_list.append(pieces.Bishop(5, back_row, self.player))

        self.piece_list.append(pieces.Queen(3, back_row, self.player))

        self.piece_list.append(pieces.King(4, back_row, self.player))

        return piece_list
