import tkinter as tk

from src.gui.stylesheet import NAVIGATION, NORMAL_TAB, DISABLED_TAB, TAB_IMAGES, PLACEHOLDER

class NavigationFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(master=root)
        self.config(NAVIGATION)

        self.current_tab = "home"

        # convert tab images
        self.home_image = tk.PhotoImage(file=TAB_IMAGES["home"])
        self.settings_image = tk.PhotoImage(file=TAB_IMAGES["settings"])
        self.notes_image = tk.PhotoImage(file=TAB_IMAGES["notes"])

        # resize tab images
        self.home_image = self.home_image.subsample(TAB_IMAGES["resize_x"], TAB_IMAGES["resize_y"])
        self.settings_image = self.settings_image.subsample(TAB_IMAGES["resize_x"], TAB_IMAGES["resize_y"])
        self.notes_image = self.notes_image.subsample(TAB_IMAGES["resize_x"], TAB_IMAGES["resize_y"])

        # Create buttons in the navigation frame
        self.home_tab = tk.Button(
            self,
            image=self.home_image,
        )
        self.settings_tab = tk.Button(
            self,
            image=self.settings_image,
        )
        self.notes_tab = tk.Button(
            self,
            image=self.notes_image,
        )
        self.placeholder = tk.Label(
            self,
        )
        
        self.actived_tab = self.home_tab

        # place tabs in the navigation frame
        self.home_tab.grid(row=0, column=0, sticky="nsew")
        self.notes_tab.grid(row=0, column=1, sticky="nsew")
        self.settings_tab.grid(row=0, column=2, sticky="nsew")
        self.placeholder.grid(row=0, column=3, sticky="nsew")

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=5)
        self.columnconfigure(1, weight=5)
        self.columnconfigure(2, weight=5)
        self.columnconfigure(3, weight=85)

        # config tabs intial values
        self.home_tab.config(DISABLED_TAB)
        self.settings_tab.config(NORMAL_TAB)
        self.notes_tab.config(NORMAL_TAB)
        self.placeholder.config(PLACEHOLDER)
        self.disabled_tab = self.home_tab

        # set tabs command
        self.home_tab.config(command=lambda : self.tab_pressed(self.home_tab, "home"))
        self.settings_tab.config(command=lambda : self.tab_pressed(self.settings_tab, "settings"))
        self.notes_tab.config(command=lambda : self.tab_pressed(self.notes_tab, "notes"))
    
    def tab_pressed(self, disabled_tab: tk.Button, new_tab:str):
        disabled_tab.config(DISABLED_TAB)
        self.disabled_tab.config(NORMAL_TAB)
        self.disabled_tab = disabled_tab
        self.current_tab = new_tab
    
    def get_current_tab(self):
        return self.current_tab