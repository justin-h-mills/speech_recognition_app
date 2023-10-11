"""
Image Modification Utility Module

This module provides a utility class, ImageModification, for performing various image modifications and transformations using PIL (Python Imaging Library). The class includes static methods to perform the following operations:
1. Convert a hexadecimal color representation to an RGB tuple.
2. Change the target color to the source color while preserving transparency in a PIL image.
3. Resize an image to fit within a circular button while maintaining its aspect ratio.

Usage:
You can use the static methods of the ImageModification class to perform image modifications and transformations.

Custom Error Handling:
Each static method in the class uses the @error_handler decorator to handle errors and log them appropriately. You can customize error messages, log levels, and whether to log to a file.

For more details on the usage and error handling configuration, please refer to the class docstring within the code.

"""

import logging
from PIL import Image

from src.gui.error_handling import error_handler
from src.validation import validate_hex_color, validate_radius

class ImageModification:
    """
    A utility class for performing various image modifications and transformations using PIL (Python Imaging Library).

    This class provides static methods to perform the following operations:
    1. Convert a hexadecimal color representation to an RGB tuple.
    2. Change the target color to the source color while preserving transparency in a PIL image.
    3. Resize an image to fit within a circular button while maintaining its aspect ratio.

    Usage:
        You can use the static methods of this class to perform image modifications and transformations.

    Example:
        # Convert a hexadecimal color to an RGB tuple
        rgb_color = ImageModification.hex_to_rgb("#FF0000")

        # Change the color of an image while preserving transparency
        modified_image = ImageModification.change_color_with_transparency(original_image, "#FF0000", "#0000FF")

        # Resize an image to fit within a circular button
        resized_image = ImageModification.resize_image_to_fit_circle(50, original_image)

    Args:
        No instance-specific attributes or constructor.

    Returns:
        No instance-specific returns; this class contains static methods for image operations.
    """

    @staticmethod
    @error_handler(custom_message="Failed to convert hexadecimal color to RGB.", log_level=logging.ERROR, log_to_file=True)
    def hex_to_rgb(hex_color: str) -> tuple[int, int, int]:
        """
        Convert a hexadecimal color representation to an RGB tuple.

        Args:
            hex_color (str): The hexadecimal color code (e.g., "#FF0000" for red).
        
        Returns:
            tuple: A tuple representing the RGB color.
        """
        logging.debug("Converting hexadecimal color to RGB.")
        validate_hex_color(hex_color)
        rgb_tuple = tuple(int(hex_color[i:i+2], 16) for i in (1, 3, 5))
        logging.info(f"Converted hex color '{hex_color}' to RGB tuple {rgb_tuple}")
        return rgb_tuple

    @staticmethod
    def modify_pixel(pixel_color: tuple[int, int, int, int], target_color: tuple[int, int, int], source_color: tuple[int, int, int]) -> tuple[int, int, int, int]:
        """
        Modify a single pixel color based on the target and source colors.

        Args:
            pixel_color (tuple[int, int, int, int]): The color of the pixel in RGBA format.
            target_color (tuple[int, int, int]): The target color in RGB format.
            source_color (tuple[int, int, int]): The source color in RGB format.

        Returns:
            tuple[int, int, int, int]: The modified pixel color.
        """
        if pixel_color[:3] == target_color:
            return source_color + (pixel_color[3],)
        return pixel_color

    @staticmethod
    @error_handler(custom_message="Failed to change color with transparency.", log_level=logging.ERROR, log_to_file=True)
    def change_color_with_transparency(image: Image.Image, target_color_hex: str, source_color_hex: str) -> Image.Image:
        """
        Change the target color to the source color while preserving transparency in the PIL image.

        Args:
            image (PIL.Image.Image): The input PIL image with a transparent background.
            target_color_hex (str): The target color in hexadecimal format (e.g., "#FF0000" for red).
            source_color_hex (str): The source color in hexadecimal format (e.g., "#0000FF" for blue).
        
        Returns:
            PIL.Image.Image: The modified image.
        """
        logging.debug("Changing color with transparency.")
        validate_hex_color(target_color_hex)
        validate_hex_color(source_color_hex)

        if image.mode != 'RGBA':
            image = image.convert('RGBA')

        target_color = ImageModification.hex_to_rgb(target_color_hex)
        source_color = ImageModification.hex_to_rgb(source_color_hex)

        modified_pixels = [ImageModification.modify_pixel(pixel_color, target_color, source_color) for pixel_color in image.getdata()]
        image.putdata(modified_pixels)
        logging.info(f"Changed color in image from '{target_color_hex}' to '{source_color_hex}'")
        return image

    @staticmethod
    @error_handler(custom_message="Failed to resize image to fit within a circular button.", log_level=logging.ERROR, log_to_file=True)
    def resize_image_to_fit_circle(radius: int, image: Image.Image) -> Image.Image:
        """
        Resize the image to fit within the circular button while maintaining aspect ratio.

        Args:
            radius (int): The max size of image
            image (Image.Image): The image to resize.

        Returns:
            Image.Image: The resized image.
        """
        logging.debug("Resizing image to fit within a circular button.")
        validate_radius(radius)

        width, height = image.size
        aspect_ratio = width / height

        if width > height:
            new_width = radius
            new_height = int(new_width / aspect_ratio)
        else:
            new_height = radius
            new_width = int(new_height * aspect_ratio)

        resized_image = image.resize((new_width, new_height))
        logging.info(f"Resized image to fit circle with radius {radius}")
        return resized_image