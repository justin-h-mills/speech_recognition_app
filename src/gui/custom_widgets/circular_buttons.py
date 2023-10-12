"""
CircularButton Module

This module defines a CircularButton class and its subclass, CircularToggleButton, 
which are tkinter-based widgets for creating circular buttons. These buttons can 
display images, text, and handle click events. The CircularToggleButton can toggle 
its state between on and off.

Please note that these classes include error handling and logging mechanisms, 
as indicated within the method docstrings.
"""
import logging

from tkinter import Canvas, Event
from PIL import Image, ImageTk

from src.gui.error_handling import error_handler
from src.gui.image_modification import ImageModification

class CircularButton(Canvas):
    """
    A circular button widget.

    Args:
        master (Tk): The parent widget.
        radius (int): The radius of the circular button.
        style (dict): The button style
        image_bg (bool, optional): 
        image_path (str, optional): The path to the image file (PNG, JPEG, etc.) to be displayed on the button.
        image (Image.Image, optional): An already loaded Image.Image object to be displayed on the button.
        text (str, optional): The text displayed on the button (default is an empty string).
        command (callable, optional): The function to execute when the button is clicked (default is None).
        padding (int, optional): The padding of the circular button (default is 0).

    Attributes:
        radius (int): The radius of the circular button.
    """
    def __init__(self, master, radius, 
                 style, image_bg=False, image_path=None, 
                 image=None, text="", command=None, **kwargs):
        super().__init__(master, width=radius, height=radius, **kwargs)
        self.radius = radius
        self.style = style
        self.text = text
        self.command = command
        self.image = None
        self.image_bg = image_bg
        self.oval_item = None
        self.bind("<Button-1>", self._on_click)
        self._configure_style()

        # initialize image coordinates
        self.image_display = None
        self.image_x = radius
        self.image_y = radius

        if image_path:
            self.load_image(image_path)
        elif image:
            self.set_image(image)

    @error_handler(custom_message="Error configuring button style", log_level=logging.ERROR, log_to_file=True)
    def _configure_style(self):
        """
        Configure the button style.

        Error Handling:
            If an error occurs during style configuration, it is logged as an error.
    
        Logging:
            Configuration details are logged for debugging purposes.
        """
        logging.debug(f"Configuring button style {self.style['canvas']}")
        self.configure(self.style["canvas"])

    @error_handler(custom_message="Error loading/set image", log_level=logging.ERROR, log_to_file=True)
    def load_image(self, image_path: str) -> None:
        """
        Load an image from a file and set it as the button's image.

        Args:
            image_path (str): The path to the image file (PNG, JPEG, etc.).

         Error Handling:
            If an error occurs during image logging, it is logged as an error.
    
        Logging:
            Loading details are logged for debugging purposes.
        """
        logging.debug(f"Loading image from {image_path}")
        image = Image.open(image_path)
        self.set_image(image)
    
    @error_handler(custom_message="Error setting image", log_level=logging.ERROR, log_to_file=True)
    def set_image(self, image: Image.Image) -> None:
        """
        Set an Image.Image object as the button's image and resize it to fit the circle with a border.

        Args:
            image (Image.Image): An already loaded Image.Image object.
        
        Error Handling:
            If an error occurs during setting image, it is logged as an error.
    
        Logging:
            Setting details are logged for debugging purposes.
        """
        logging.debug("Setting button image")
        image = ImageModification.change_color_with_transparency(image, 
                                                                 self.style["image"]["base"], 
                                                                 self.style["image"]["fill"])
        resized_image = ImageModification.resize_image_to_fit_circle(self.radius, image)

        if self.image_bg:
            self.create_and_place_oval(resized_image.width, resized_image.height)

        self.create_and_place_image(resized_image)
    
    @error_handler(custom_message="Error creating and placing oval background", log_level=logging.ERROR, log_to_file=True)
    def create_and_place_oval(self, image_width: int, image_height: int) -> None:
        """
        Create and place an oval background for an image within the canvas.

        This function calculates the size and position for an oval shape, which serves as a background 
        for an image displayed within a canvas. It takes the dimensions of the image
        (image_width and image_height) and calculates the size and position for the oval shape, then 
        creates the oval on the canvas using these values.

        Args:
            image_width (int): The width of the image.
            image_height (int): The height of the image.
        
        Error Handling:
            If an error occurs during creating and placing oval, it is logged as an error.
    
        Logging:
            Creating and placing details are logged for debugging purposes.
        """
        logging.debug("Creating and placing oval background")
        # Calculate oval size
        width = image_width * 0.9
        height = image_height * 0.9
        
        # Calculate oval offset
        x_offset = image_width * 0.1
        y_offset = image_height * 0.1

        self.oval_item = self.create_oval(x_offset, y_offset, width, height, self.style["oval"])

    @error_handler(custom_message="Error creating and placing image", log_level=logging.ERROR, log_to_file=True)
    def create_and_place_image(self, image: Image.Image) -> None:
        """
        Create and place the image inside the circular button.

        Args:
            image (Image.Image): The image to place.
        
        Error Handling:
            If an error occurs during creating and placing image, it is logged as an error.
    
        Logging:
            Creating and placing details are logged for debugging purposes.
        """
        logging.debug("Creating and placing button image")
        self.image = ImageTk.PhotoImage(image)

        # Calculate the position to center the image within the circular button's canvas
        x_offset = self.radius - image.width // 2
        y_offset = self.radius - image.height // 2

        # Remove the previous image item (if any)
        if self.image_display:
            self.delete(self.image_display)

        # Create the new image item inside the oval
        self.image_display = self.create_image(x_offset, y_offset, image=self.image)
        self.tag_raise(self.image_display)

    @error_handler(custom_message="Error handling button click event", log_level=logging.ERROR, log_to_file=True)
    def _on_click(self, event:Event) -> None:
        """
        Handle the button's click event.

        This method calls the associated command function, passing the click event 
        as an argument if a command is defined.

        Args:
            event (Event): The click event triggered by the user.
        
        Error Handling:
            If an error occurs during click event, it is logged as an error.
    
        Logging:
            Click event details are logged for debugging purposes.
        """
        logging.debug("Handling button click event")
        if self.command:
            self.command()  # Call the associated command function

class CircularToggleButton(CircularButton):
    """
    A circular toggle button widget.

    Args:
        master (Tk): The parent widget.
        radius (int): The radius of the circular button.
        image_bg (bool, optional):
        image_path (str, optional): The path to the image file (PNG, JPEG, etc.) to be displayed on the button.
        image (Image.Image, optional): An already loaded Image.Image object to be displayed on the button.
        text (str, optional): The text displayed on the button (default is an empty string).
        command (callable, optional): The function to execute when the button is clicked (default is None).
        padding (int, optional): The padding of the circular button (default is 0).

    Attributes:
        radius (int): The radius of the circular button.
        toggled (bool): The state of the button (True if toggled on, False if toggled off).
    """

    def __init__(self, master, radius, style, 
                 image_bg=False, image_path=None, image=None, text="", 
                 command=None, **kwargs):
        super().__init__(master, radius, style, image_bg, image_path, image, text, command, **kwargs)
        self.toggled = False # initial state is off

    @error_handler(custom_message="Error toggling the button on state", log_level=logging.ERROR, log_to_file=True)
    def toggle_on(self) -> None:
        """
        Turn the button on by changing its appearance to the 'on' state.

        This function updates the button's appearance to indicate that it's in the 'on' state.

        Error Handling:
            If an error occurs during toggle on, it is logged as an error.
    
        Logging:
            Toggle on event details are logged for debugging purposes.
        """
        logging.debug("Toggling the button on")
        self.itemconfig(self.oval_item, fill=self.style["button_states"]["on"])

    @error_handler(custom_message="Error toggling the button off state", log_level=logging.ERROR, log_to_file=True)
    def toggle_off(self) -> None:
        """
        Turn the button off by changing its appearance to the 'off' state.

        This function updates the button's appearance to indicate that it's in the 'off' state.

        Error Handling:
            If an error occurs during toggle off, it is logged as an error.
    
        Logging:
            Toggle off event details are logged for debugging purposes.
        """
        logging.debug("Toggling the button off")
        self.itemconfig(self.oval_item, fill=self.style["button_states"]["off"])

    @error_handler(custom_message="Error handling button toggle click event", log_level=logging.ERROR, log_to_file=True)
    def _on_click(self, event: Event) -> None:
        """
        Handle the button's click event.

        This method toggles the button's state, calling the appropriate methods based on 
        the new state (on or off). Additionally,
        it forwards the click event to the parent class's click handler.

        Args:
            event (Event): The click event triggered by the user.
        
        Error Handling:
            If an error occurs during toggle click event, it is logged as an error.
    
        Logging:
            Toggle click event details are logged for debugging purposes.
        """
        logging.debug("Handling button toggle click event")
        self.toggled = not self.toggled  # Toggle the state

        if self.toggled:
            self.toggle_on() # Call the toggle_on method for the 'on' state
        else:
            self.toggle_off() # Call the toggle_off method for the 'off' state
        
        self.command(self.toggled)