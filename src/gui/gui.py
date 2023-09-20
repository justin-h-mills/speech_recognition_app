import tkinter as tk

from tkinter import ttk
from PIL import Image, ImageTk

from custom_widgets import CircularToggleButton

class SpeechRecognitionApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Speech Recognition App")

        # Load the application icon
        self.root.iconbitmap('assests/snake.ico')

        # Change the background color of the main window
        self.root.configure(bg="black")

        self.center_window()
    
        circular_button = CircularToggleButton(self.root, radius=150, image_path="assests\circle_microphone_lines_white.png", command=self.toggle_button_click)
        circular_button.pack()
    
    def toggle_button_click(self, state):
        if state:
            pass
        else:
            pass

    def center_window(self, window_width=800, window_height=600):
        # get the screen dimension
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # find the center point
        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)

        # set the position of the window to the center of the screen
        self.root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = SpeechRecognitionApp()
    app.run()