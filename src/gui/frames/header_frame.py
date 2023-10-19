import tkinter as tk

class HeaderFrame(tk.Frame):
    def __init__(self, root, title):
        super().__init__(master=root, bg=root.cget("bg"))
        self.title = title
        self.label = tk.Label(self, text= self.title, bg="red")
        self.label.pack(fill="both", expand=True)
    
    def update_title(self, title):
        self.title = title
        self.label.forget()
        self.label = tk.Label(self, text= self.title, bg="red")
        self.label.pack(fill="both", expand=True)