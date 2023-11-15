import logging
import tkinter as tk

from src.logging_config import configure_gui_logging
from src.gui.frames.body_frame import BodyFrame, HomeFrame, NotesFrame, SettingsFrame
from src.gui.frames.footer_frame import FooterFrame
from src.gui.frames.header_frame import HeaderFrame
from src.gui.frames.navbar_frame import NavigationFrame
from src.gui.stylesheet import ROOT

# Call the configuration function from the logging_config module
configure_gui_logging()

# Create a logger for the GUI module
logger = logging.getLogger('gui')

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Speech Recognition App")
        self.iconbitmap("assests/snake.ico")
        self.config(ROOT)
        self.center_window()

        # Create frames
        self.header = HeaderFrame(self, "Home")
        self.navigation = NavigationFrame(self)
        self.footer = FooterFrame(self)

        self.body_frames = {}

        for f in (HomeFrame, NotesFrame, SettingsFrame):
            frame = f(self)
            self.body_frames[f] = frame
            frame.grid(row=2, column=0, sticky="nsew", padx=4, pady=2)
        
        # Add frames to grid
        self.header.grid(row=0, column=0, sticky="nsew", padx=4, pady=2)
        self.navigation.grid(row=1, column=0, sticky="nsew", padx=4, pady=2)
        self.footer.grid(row=3, column=0, sticky="nsew", padx=4, pady=2)

        # Configure row and column weights for the root window
        self.grid_rowconfigure(0, weight=5)
        self.grid_rowconfigure(1, weight=10)
        self.grid_rowconfigure(2, weight=80)
        self.grid_rowconfigure(3, weight=5)
        self.grid_columnconfigure(0, weight=100)

        self.body_current = "home"
        self.show_frame(HomeFrame)
        
    def center_window(self, window_width=800, window_height=600):
        # Get the screen dimensions
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Find the center point
        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)

        # Set the position of the window to the center of the screen
        self.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

    def show_frame(self, cont):
        frame = self.body_frames[cont]
        frame.tkraise()

    def update_body_frame(self):
        current_frame = self.navigation.get_current_tab()

        if current_frame == self.body_current:
            return current_frame
        
        if current_frame == "home":
            self.show_frame(HomeFrame)
        elif current_frame == "settings":
            self.show_frame(SettingsFrame)
        elif current_frame == "notes":
            self.show_frame(NotesFrame)

        self.body_current = current_frame
        return current_frame

    def run(self):
        while True:
            current_tab = self.update_body_frame()
            self.header.update_title(current_tab)
            self.update()

def main():
    app = App()
    app.run()

if __name__ == "__main__":
    main()