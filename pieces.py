"""0 is white, 1 is black, 2 is empty
logic checks if move is outside of board bounds before move
players are white, black, or empty

must check if king is in check before moving, somewhat complicated
piece garanteed to not get current position as a move
"""


# generic class that defines a piece, including "empty" pieces
class Piece:
    def __init__(self, location_x, location_y, player):
        self.x = location_x
        self.y = location_y
        self.player = player
        self.type = "empty"

    # just so I can generally call move, probably bad practice
    def move(self, x, y, board):
        return False


# class that defines a pawn
class Pawn(Piece):
    def __init__(self, x, y, player):
        super().__init__(x, y, player)
        self.type = "pawn"
        self.has_moved = False
        self.y_dir = 0
        self.set_y_dir()

    # pawns can only move forward, so we need to know if we are white or black
    def set_y_dir(self):
        if self.player == "white":
            self.y_dir = 1
        elif self.player == "black":
            self.y_dir = -1
        else:
            raise Exception("Pawn must be white or black")

    def move(self, x, y, board):
        # move forward 1
        if (x == self.x
                and y == self.y + self.y_dir
                and board[self.x][self.y + self.y_dir].type == "empty"):
            self.has_moved = True
            return True

        # move forward 2
        if (y == self.y + self.y_dir + self.y_dir
                and x == self.x
                and self.has_moved is False
                and board[self.x][self.y + self.y_dir].type == "empty"
                and board[self.x][self.y + self.y_dir].type == "empty"):
            self.has_moved = True
            return True

        # attack sideways to the right
        if (y == self.y + self.y_dir
                and x == self.x + 1
                and board[x][y].type != "empty"
                and board[x][y].player != self.player):
            self.has_moved = True
            return True

        # attack sideways to the left
        if (y == self.y + self.y_dir
                and x == self.x - 1
                and board[x][y].type != "empty"
                and board[x][y].player != self.player):
            self.has_moved = True
            return True
        return False


class Knight(Piece):
    def __init__(self, x, y, player):
        super().__init__(x, y, player)
        self.type = "knight"

    def valid_move(self, x, y):
        if ((self.x - x) ** 2) + ((self.y - y) ** 2) == 5:
            return True

    def move(self, x, y, board):
        if self.valid_move(x, y) and board[x][y].player != self.player:
            return True
        else:
            return False


class King(Piece):
    def __init__(self, x, y, player):
        super().__init__(x, y, player)
        self.type = "king"

    def move(self, x, y, board):
        if ((abs(x - self.x) < 2 and abs(y - self.y) < 2)
                and not (x == self.x and y == self.y)
                and board[x][y].player != self.player
                and not self.killable(x, y, board)):
            return True
        else:
            return False

    def killable(self, x, y, board):
        for column in board:
            for row in column:
                if row.player != self.player and row.type != "king":
                    if row.move(x, y, board):
                        print("Can't Move Here. King can be killed")
                        return True
        return False


class Rook(Piece):
    def __init__(self, x, y, player):
        super().__init__(x, y, player)
        self.type = "rook"

    def check_x(self, x, y, board):
        if self.x < x:
            for col in range(self.x + 1, x):
                if board[col][y].player != "empty":
                    return False
        else:
            for col in range(self.x - 1, x, -1):
                if board[col][y].player != "empty":
                    return False
        return True

    def check_y(self, x, y, board):
        if self.y < y:
            for row in range(self.y + 1, y):
                if board[x][row].player != "empty":
                    return False
        else:
            for row in range(self.y - 1, y, -1):
                if board[x][row].player != "empty":
                    return False
        return True

    def rook_move(self, x, y, board):
        # check that it is a posible move
        if self.x != x and self.y != y:
            return False

        # check x direction
        if self.x != x:
            if not self.check_x(x, y, board):
                return False
        # check y direction
        else:
            if not self.check_y(x, y, board):
                return False

        if board[x][y].player != self.player:
            return True
        else:
            return False

    def move(self, x, y, board):
        return self.rook_move(x, y, board)


class Bishop(Piece):
    def __init__(self, x, y, player):
        super().__init__(x, y, player)
        type = "bishop"

    # abstract out move so queen can use it
    def bishop_move(self, x, y, board):
        x_iter = 0
        y_iter = 0

        # check that it is a possible move
        if abs(self.x - x) != abs(self.y - y):
            return False

        if self.x < x:
            x_iter = 1
        else:
            x_iter = -1

        if self.y < y:
            y_iter = 1
        else:
            y_iter = -1

        for count, col in enumerate(range(self.x + x_iter, x, x_iter)):
            row = self.y + ((count + 1) * y_iter)
            if board[col][row].player != "empty":
                return False

        if board[x][y].player != self.player:
            return True
        else:
            return False

    def move(self, x, y, board):
        return self.bishop_move(x, y, board)


class Queen(Rook, Bishop):
    def __init__(self, x, y, player):
        super().__init__(x, y, player)

    def move(self, x, y, board):
        if self.rook_move(x, y, board) or self.bishop_move(x, y, board):
            return True
        else:
            return False
