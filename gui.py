import tkinter as tk
from functools import partial
import board


class GuiBoard(board.Board):
    def __init__(self):
        super().__init__()
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
                                   highlightbackground="grey")
                button.grid(row=row, column=col, sticky="nsew")
                btn_sub_list.append(button)

            button_list.append(btn_sub_list)

        return button_list

    def update_gui(self):
        for r_num, row in enumerate(self.board):
            for c_num, col in enumerate(row):
                print(len(row))
                temp_button = self.buttons[7 - c_num][r_num]
                temp_button["text"] = self.get_identifier(col.type)
                if col.player == "black":
                    temp_button["fg"] = "black"
                else:
                    temp_button["fg"] = "green"

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

    def gui_move(self, x, y):

        print(str(x) + " " + str(y))


class Square:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.window = tk.Tk()
        self.window.rowconfigure([0, 1, 2, 3, 4, 5, 6, 7], minsize=100, weight=1)
        self.window.columnconfigure([0, 1, 2, 3, 4, 5, 6, 7], minsize=100, weight=1)
        self.btn = tk.Button(master=self.window, command=lambda: self.update(1, 2), bg="black",
                             highlightbackground="grey", text="Q")
        self.btn2 = tk.Button(master=self.window, command=lambda: self.update(3, 3), bg="black",
                              highlightbackground="grey", text="Q")
        self.btn2.grid(row=7, column=7, sticky="nsew")
        self.btn.grid(row=self.x, column=self.y, sticky="nsew")
        self.window.mainloop()

    def update(self, x, y):
        self.btn["bg"] = "blue"
        print(str(x) + " " + str(y))


gui_board = GuiBoard()
square = Square(7, 0)
