import tkinter as tk


class Square:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.window = tk.Tk()
        self.window.rowconfigure([0, 1, 2, 3, 4, 5, 6, 7], minsize=100, weight=1)
        self.window.columnconfigure([0, 1, 2, 3, 4, 5, 6, 7], minsize=100, weight=1)
        self.btn = tk.Button(master=self.window, command=self.update, bg="black", highlightbackground="grey", text="Q")
        self.btn.grid(row=self.x, column=self.y, sticky="nsew")
        self.window.mainloop()
    def update(self):
        self.btn["bg"] = "blue"
square = Square(6,0)
