from tkinter import Canvas, Tk
from PIL import Image, ImageTk
from gui_styles import CIRCULAR_TOGGLE_BUTTON_STYLE

class CircularToggleButton(Canvas):
    """
    A circular toggle button widget.

    Args:
        master (Tk): The parent widget.
        radius (int): The radius of the circular button.
        image_path (str, optional): The path to the image file (PNG, JPEG, etc.) to be displayed on the button.
        image (Image.Image, optional): An already loaded Image.Image object to be displayed on the button.
        text (str, optional): The text displayed on the button (default is an empty string).
        command (callable, optional): The function to execute when the button is clicked (default is None).

    Attributes:
        radius (int): The radius of the circular button.
        toggled (bool): The state of the button (True if toggled on, False if toggled off).
    """
    
    COLOR_ON = "green"
    COLOR_OFF = "red"

    def __init__(self, master, radius, image_path=None, image=None, text="", command=None, **kwargs):
        super().__init__(master, width=2*radius, height=2*radius, **kwargs)
        self.radius = radius
        self.text = text
        self.command = command
        self.toggled = False  # Initial state is off
        
        self.bind("<Button-1>", self._on_click)
        
        # Set the canvas background color to match the window background color
        self.configure(bg=self.master.cget("bg")) 
        
        # Remove the square background by setting highlightthickness to 0
        self.configure(highlightthickness=0)

        self.oval_item = self.create_oval(0, 0, 2*radius, 2*radius, fill=self.COLOR_OFF, outline=self.master.cget("bg"))
        self.create_text(radius, radius, text=text)
        
        # Initialize image coordinates
        self.image_display = None
        self.image_x = radius
        self.image_y = radius
        
        if image_path:
            try:
                self.load_image(image_path)
            except FileNotFoundError as e:
                raise FileNotFoundError(f"Image file not found: {image_path}") from e
        elif image:
            self.set_image(image)

    def load_image(self, image_path: str) -> None:
        """
        Load an image from a file and set it as the button's image.

        Args:
            image_path (str): The path to the image file (PNG, JPEG, etc.).
        """
        img = Image.open(image_path)
        self.set_image(img)
    
    def set_image(self, image: Image.Image) -> None:
        """
        Set an Image.Image object as the button's image and resize it to fit the circle with a border.

        Args:
            image (Image.Image): An already loaded Image.Image object.
        """
        # Calculate the new size to fit within the circle while maintaining aspect ratio
        width, height = image.size
        aspect_ratio = width / height
        if aspect_ratio > 1:
            new_width = 2 * self.radius
            new_height = int(new_width / aspect_ratio)
        else:
            new_height = 2 * self.radius
            new_width = int(new_height * aspect_ratio)

        # Create an oval with a border
        self.oval_item = self.create_oval(0, 0, 2 * self.radius, 2 * self.radius, fill=self.COLOR_OFF, outline=self.master.cget("bg"), width=2)
        
        # Resize the image to fit within the oval
        resized_image = image.resize((new_width, new_height))
        self.image = ImageTk.PhotoImage(resized_image)
        
        # Update image coordinates to center it within the oval
        self.image_x = self.radius
        self.image_y = self.radius
        
        # Remove the previous image item (if any)
        if self.image_display:
            self.delete(self.image_display)
        
        # Create the new image item inside the oval
        self.image_display = self.create_image(self.image_x, self.image_y, image=self.image)
        self.tag_raise(self.image_display)
    
    def _on_click(self, event) -> None:
        """
        Handle the button click event.
        """
        self.toggled = not self.toggled  # Toggle the state
        
        if self.toggled:
            # Button is toggled on, change the oval's color
            self.itemconfig(self.oval_item, fill=self.COLOR_ON)
        else:
            # Button is toggled off, revert the oval's color
            self.itemconfig(self.oval_item, fill=self.COLOR_OFF)
        
        if self.command:
            self.command(self.toggled)  # Pass the toggled state to the command function
