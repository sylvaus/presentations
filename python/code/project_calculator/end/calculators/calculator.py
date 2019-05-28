from tkinter import Tk, StringVar
from tkinter.ttk import Label


class Calculator:
    NB_COLUMN = 4

    def __init__(self, root=Tk(), title="Calculator", geometry="400x450"):
        self._root = root
        self._root.geometry(geometry)
        self._root.title(title)

        self._label_text = StringVar()
        self._label = Label(self._root, textvariable=self._label_text)
        self._label.grid(row=0, column=0, columnspan=self.NB_COLUMN)

    def start(self):
        self._root.mainloop()


