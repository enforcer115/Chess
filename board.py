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
        for x in range(8):
            column = []
            for y in range(8):
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
            print("Selection out of bounds")
            return False

        if self.board[p_x][p_y].player != self.turn:
            print("It is not your turn")
            return False
        self.valid_move(p_x, p_y, c_x, c_y)


    def valid_move(self, p_x, p_y, c_x, c_y):
        if self.board[p_x][p_y].move(c_x, c_y, self.board):
            place_holder = self.board[c_x][c_y]
            # move piece to new spot
            self.board[c_x][c_y] = self.board[p_x][p_y]
            self.board[c_x][c_y].x = c_x
            self.board[c_x][c_y].y = c_y
            self.board[p_x][p_y] = self.empty

            if self.check_king():
                if self.turn == "white":
                    if place_holder.player != "empty":
                        self.b_player.capture_list.append(place_holder)
                    self.turn = "black"
                else:
                    self.w_player.capture_list.append(place_holder)
                    self.turn = "white"
                print("turn successful: " + self.turn + "s turn")
            else:
                # undo turn
                self.board[p_x][p_y] = self.board[c_x][c_y]
                self.board[c_x][c_y] = place_holder
        else:
            print("not a valid move for that piece")

    # returns true if king is not in check
    def check_king(self):
        king_x = -1
        king_y = -1

        # find the king
        for col in self.board:
            for row in col:
                if row.type == "king" and row.player == self.turn:
                    king_x = row.x
                    king_y = row.y
        for col in self.board:
            for row in col:
                if row.player != self.turn and row.player != "empty" and row.move(king_x, king_y, self.board):
                    print("king is in check")
                    return False
        return True


