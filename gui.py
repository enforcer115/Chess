import tkinter as tk
from functools import partial
import board


class GuiBoard(board.Board):
    def __init__(self):
        super().__init__()
        # state variables
        self.first_selection = [-1, -1]
        self.save_color = ""
        self.window = tk.Tk()
        self.window.rowconfigure([0, 1, 2, 3, 4, 5, 6, 7], minsize=100, weight=1)
        self.window.columnconfigure([0, 1, 2, 3, 4, 5, 6, 7], minsize=100, weight=1)
        self.buttons = self.init_buttons()
        self.update_gui()
        self.window.mainloop()



    def init_buttons(self):
        color = "white"
        button_list = []
        for row in range(8):
            btn_sub_list = []
            for col in range(8):
                if (row + col) % 2 == 0:
                    color = "white"
                else:
                    color = 'grey'

                button_cmd = partial(self.gui_move, row, col)
                button = tk.Button(master=self.window, command=button_cmd, bg=color,
                                   highlightbackground="gray", activebackground="salmon1")
                button.grid(row=row, column=col, sticky="nsew")
                btn_sub_list.append(button)

            button_list.append(btn_sub_list)

        return button_list

    def update_gui(self):
        for r_num, row in enumerate(self.board):
            for c_num, col in enumerate(row):

                self.buttons[7 - c_num][r_num].config(text=self.get_identifier(col.type))

                if col.player == "black":
                    self.buttons[7 - c_num][r_num].config(fg="black")
                    self.buttons[7 - c_num][r_num].config(activeforeground="black")
                else:
                    self.buttons[7 - c_num][r_num].config(fg="green")
                    self.buttons[7 - c_num][r_num].config(activeforeground="green")
    @staticmethod
    def get_identifier(text):
        switcher = {
            "queen": "q",
            "king": "k",
            "pawn": "p",
            "knight": "kn",
            "rook": "r",
            "bishop": "b"
        }
        return switcher.get(text, "")

    def get_piece(self, x, y):
        return self.board[y, y -x]

    def gui_move(self, x, y):
        if x == self.first_selection[0] and y == self.first_selection[1]:
            self.buttons[x][y]["bg"] = self.save_color
            self.first_selection = [-1, -1]
        elif self.first_selection == [-1, -1]:
            self.first_selection = [x, y]
            self.save_color = self.buttons[x][y]["bg"]
            self.buttons[x][y]["bg"] = "salmon1"

        else:
            self.buttons[self.first_selection[0]][self.first_selection[1]]["bg"] = self.save_color
            self.play_turn(self.first_selection[1], 7-self.first_selection[0], y, 7 - x)
            self.first_selection = [-1,-1]

        self.update_gui()





