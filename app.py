import logging
import tkinter as tk

from src.logging_config import configure_gui_logging
from src.gui.frames.body_frame import BodyFrame
from src.gui.frames.footer_frame import FooterFrame
from src.gui.frames.header_frame import HeaderFrame
from src.gui.frames.navbar_frame import NavbarFrame

# Call the configuration function from the logging_config module
configure_gui_logging()

# Create a logger for the GUI module
logger = logging.getLogger('gui')

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Speech Recognition App")
        self.iconbitmap("assests/snake.ico")
        self.center_window()

        # Create frames
        self.header = HeaderFrame(self, "Home")
        self.navbar = NavbarFrame(self)
        self.body = BodyFrame(self)
        self.footer = FooterFrame(self)

        # Add frames to grid
        self.header.grid(row=0, column=0, sticky="nsew")
        self.navbar.grid(row=1, column=0, sticky="nsew")
        self.body.grid(row=2, column=0, sticky="nsew")
        self.footer.grid(row=3, column=0, sticky="nsew")

        # Configure row and column weights for the root window
        self.grid_rowconfigure(0, weight=3)
        self.grid_rowconfigure(1, weight=2)
        self.grid_rowconfigure(2, weight=85)
        self.grid_rowconfigure(3, weight=5)
        self.grid_columnconfigure(0, weight=100)
        
    def center_window(self, window_width=800, window_height=600):
        # Get the screen dimensions
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Find the center point
        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)

        # Set the position of the window to the center of the screen
        self.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

    def run(self):
        self.mainloop()

def main():
    app = App()
    app.run()

if __name__ == "__main__":
    main()