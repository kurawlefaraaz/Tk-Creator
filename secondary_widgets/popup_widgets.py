"""Widgets which popup on a EVENT and let user give input"""

import tkinter as tk
import tkinter.ttk as ttk


class PopupEntry(tk.Entry):
    """
    Provides a temporary tk.Entry widget which can be used to show a temporaty entry widget to retrive data from user.
    After retriving data, it returns the value back and gets destroyed.

    Used internaly by EditableTreeview.
    """

    def __init__(
        self,
        parent,
        x,
        y,
        textvar,
        width,
        height,
        entry_value="",
        text_justify="left",
        **options
    ):
        super().__init__(
            parent,
            relief="flat",
            justify=text_justify,
            bg="white",
            textvariable=textvar,
            font="Times 10 ",
            **options
        )
        self.place(x=x + 1, y=y, width=width, height=height)

        self.textvar = textvar
        self.textvar.set(entry_value)
        self.focus_set()
        self.select_range(0, "end")
        # move cursor to the end
        self.icursor("end")

        self.wait_var = tk.StringVar(master=self)

        self._bind_widget()
        self.wait_window()

    def _bind_widget(self):
        self.bind("<Return>", self.retrive_value)
        self.bind("<FocusOut>", self.retrive_value)

    def retrive_value(self, e):
        value = self.textvar.get()
        self.destroy()
        self.textvar.set(value)

from tkinter.colorchooser import Chooser
from tkinter.dialog import Dialog

root = tk.Tk()
a=root.tk.call("tk_chooseColor")


root.mainloop()
# class PickColor()
