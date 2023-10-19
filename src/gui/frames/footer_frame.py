import tkinter as tk

class FooterFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(master=root, bg=root.cget("bg"))
        label = tk.Label(self, text="Footer", bg="yellow")
        label.pack(fill="both", expand=True)