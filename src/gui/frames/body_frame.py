import tkinter as tk

class BodyFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(master=root, bg=root.cget("bg"))
        label = tk.Label(self, text="Body", bg="green")
        label.pack(fill="both", expand=True)