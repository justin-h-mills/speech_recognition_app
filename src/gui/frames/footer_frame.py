import tkinter as tk

from src.gui.stylesheet import FOOTER, FOOTER_LABEL

class FooterFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(master=root)
        self.config(FOOTER)
        footer_text = "jmills0100@yahoo.com\t"
        label = tk.Label(self, text=footer_text)
        label.config(FOOTER_LABEL)
        label.pack(fill="both", expand=True)