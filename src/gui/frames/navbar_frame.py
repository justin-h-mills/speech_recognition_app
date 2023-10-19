import tkinter as tk

class NavbarFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(master=root, bg=root.cget("bg"))

        # Creating a photoimage object to use image     
        self.home_image = tk.PhotoImage(file="assests/home.png")
        self.setting_image = tk.PhotoImage(file="assests/settings.png")
        self.folder_image = tk.PhotoImage(file="assests/folder.png")

        # Resizing image to fit on button 
        self.home_image = self.home_image.subsample(10, 10)
        self.setting_image = self.setting_image.subsample(10, 10)
        self.folder_image = self.folder_image.subsample(10, 10)

        # Create buttons in the navigation frame
        self.home_button = tk.Button(
            self,
            image=self.home_image,
            compound="left",
            command=self.home_button_pressed,
        )
        self.setting_button = tk.Button(
            self,
            image=self.setting_image,
            compound="left",
            command=self.setting_button_pressed,
        )
        self.folder_button = tk.Button(
            self,
            text="Home",
            image=self.folder_image,
            command=self.folder_button_pressed,
        )
        
        # Place buttons in the navigation frame
        self.home_button.grid(row=0, column=0, sticky="nsew")
        self.folder_button.grid(row=0, column=1, sticky="nsew")
        self.setting_button.grid(row=0, column=2, sticky="nsew")

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=5)
        self.columnconfigure(1, weight=5)
        self.columnconfigure(2, weight=5)
        self.columnconfigure(3, weight=85)
    
    def home_button_pressed(self):
        print("Home Button Pressed")
    
    def setting_button_pressed(self):
        print("Setting Button Pressed")
    
    def folder_button_pressed(self):
        print("Folder Button Pressed")