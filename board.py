import pieces
import player


class Board:
    def __init__(self):
        self.board = []
        self.w_player = player.Player("white")
        self.b_player = player.Player("black")
        self.turn = "white"
        self.empty = pieces.Piece(-1, -1, "empty")
        self.init_board()

    def init_board(self):
        for x in range(12):
            column = []
            for y in range(12):
                column.append(self.empty)
            self.board.append(column)

        for p in self.w_player.piece_list:
            self.board[p.x][p.y] = p
        for p in self.b_player.piece_list:
            self.board[p.x][p.y] = p

    def play_turn(self, p_x, p_y, c_x, c_y):
        if(p_x > 7
                or p_x < 0
                or p_y > 7
                or p_y < 0
                or c_x > 7
                or c_x < 0
                or c_y > 7
                or c_y < 0):
            print("that is not a valid selection")
            return False

        if self.board[p_x][p_y].player != self.turn:
            print("It is not your turn")
            return False


    def valid_move(self, p_x, p_y, c_x, c_y):
        if self.board[p_x][p_y].move(c_x, c_y, self.board):
            place_holder = self.board[c_x][c_y]
            # move piece to new spot
            self.board[c_x][c_y] = self.board[p_x][p_y]
            self.board[p_x][p_y] = self.empty


