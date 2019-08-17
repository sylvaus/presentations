from tkinter import Tk, Button, W, S, E, N, Grid, Label, StringVar


class Calculator:
    NB_COLUMN = 4
    NB_ROWS = 7

    DIV_OP = "/"
    MULT_OP = "x"
    SUB_OP = "-"
    ADD_OP = "+"

    ANS_INIT = "0"

    def __init__(self, root=Tk()):
        self._root = root
        self._button_frame = root
        self._current_op = None
        # Make sure the widgets scales
        for col in range(self.NB_COLUMN):
            Grid.columnconfigure(self._button_frame, col, weight=1)
        for row in range(self.NB_ROWS):
            Grid.rowconfigure(self._button_frame, row, weight=1)

        self._ans_label = Label(self._button_frame, text="Ans")
        self._ans_label.grid(column=0, row=0, sticky=N + S + E + W)
        self._prev_val_str = StringVar()
        self._prev_val_str.set(self.ANS_INIT)
        self._prev_val_label = Label(self._button_frame, textvar=self._prev_val_str, anchor=E)
        self._prev_val_label.grid(column=1, row=0, columnspan=self.NB_COLUMN - 1, sticky=N + S + E + W)

        self._val_label = Label(self._button_frame, text="Val")
        self._val_label.grid(column=0, row=1, sticky=N + S + E + W)
        self._val_str = StringVar()
        self._val_label = Label(self._button_frame, textvar=self._val_str, anchor=E)
        self._val_label.grid(column=1, row=1, columnspan=self.NB_COLUMN - 1, sticky=N + S + E + W)

        self._button_ce = Button(self._button_frame, text="CE ", command=self._clear_val)
        self._button_ce.grid(column=0, row=self.NB_ROWS - 5, sticky=N + S + E + W)

        self._button_c = Button(self._button_frame, text=" C ", command=self._clear_all)
        self._button_c.grid(column=1, row=self.NB_ROWS - 5, sticky=N + S + E + W)

        self._button_del = Button(self._button_frame, text="del", command=self._del_last_entry)
        self._button_del.grid(column=2, row=self.NB_ROWS - 5, sticky=N + S + E + W)

        self._button_0 = Button(self._button_frame, text="0", command=self._make_number_command(0))
        self._button_0.grid(column=1, row=self.NB_ROWS - 1, sticky=N + S + E + W)

        self._button_div = Button(self._button_frame, text=" / ", command=self._make_operation_command(self.DIV_OP))
        self._button_div.grid(column=3, row=self.NB_ROWS - 5, sticky=N + S + E + W)
        self._button_mult = Button(self._button_frame, text=" x ", command=self._make_operation_command(self.MULT_OP))
        self._button_mult.grid(column=3, row=self.NB_ROWS - 4, sticky=N + S + E + W)
        self._button_minus = Button(self._button_frame, text=" - ", command=self._make_operation_command(self.SUB_OP))
        self._button_minus.grid(column=3, row=self.NB_ROWS - 3, sticky=N + S + E + W)
        self._button_plus = Button(self._button_frame, text=" + ", command=self._make_operation_command(self.ADD_OP))
        self._button_plus.grid(column=3, row=self.NB_ROWS - 2, sticky=N + S + E + W)
        self._button_equal = Button(self._button_frame, text=" = ", command=self._equal)
        self._button_equal.grid(column=3, row=self.NB_ROWS - 1, sticky=N + S + E + W)

        for col in range(3):
            for row in range(3):
                val = col + (row * 3) + 1
                button = Button(self._button_frame, text=str(val), command=self._make_number_command(val))
                button.grid(column=col, row=self.NB_ROWS - 2 - row, sticky=N + S + E + W)

    def _clear_all(self):
        self._val_str.set("")
        self._prev_val_str.set(self.ANS_INIT)
        self._current_op = None

    def _clear_val(self):
        self._val_str.set("")

    def _del_last_entry(self):
        text = self._val_str.get()
        if text:
            self._val_str.set(text[:-1])

    def _make_number_command(self, i):
        return lambda: self._val_str.set(self._val_str.get() + str(i))

    def _make_operation_command(self, op):
        def func():
            if self._val_str.get():
                if self._prev_val_str.get() == self.ANS_INIT:
                    self._prev_val_str.set(self._val_str.get() + op)
                else:
                    val_str = self._prev_val_str.get() + self._val_str.get()
                    val_str = val_str.replace(self.MULT_OP, "*").replace(self.DIV_OP, "//")
                    self._prev_val_str.set(str(eval(val_str)) + op)
                self._val_str.set('')
                self._current_op = op
            else:
                if self._current_op:
                    text = self._prev_val_str.get()[:-1]
                else:
                    text = self._prev_val_str.get()
                self._current_op = op
                self._prev_val_str.set(text + op)

        return func

    def _equal(self):
        if self._prev_val_str.get() == self.ANS_INIT:
            self._prev_val_str.set(self._val_str.get())
        else:
            if self._current_op is None:
                self._prev_val_str.set(self._val_str.get())
            else:
                val_str = self._prev_val_str.get() + self._val_str.get()
                val_str = val_str.replace(self.MULT_OP, "*").replace(self.DIV_OP, "//")
                self._prev_val_str.set(str(eval(val_str)))

        self._val_str.set('')
        self._current_op = None

    def start(self):
        self._root.mainloop()


if __name__ == '__main__':
    calculator = Calculator()
    calculator.start()


