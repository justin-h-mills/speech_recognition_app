import tkinter as tk

from tkinter.font import Font

from src.gui.stylesheet import HEADER, TITLE_LABEL

class HeaderFrame(tk.Frame):
    def __init__(self, root, title):
        super().__init__(master=root)
        self.config(HEADER)

        self.title = f"{title.capitalize()}\t"

        self.label = tk.Label(self, text= self.title)
        self.label.config(TITLE_LABEL)
        self.label.pack(fill="both", expand=True)
    
    def update_title(self, title):
        self.title = f"{title.capitalize()}\t"
        self.label.forget()
        self.label = tk.Label(self, text=self.title)
        self.label.config(TITLE_LABEL)
        self.label.pack(fill="both", expand=True)