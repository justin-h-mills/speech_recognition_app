"""
Logging and Error Handling Utility Module

This module provides a set of utility functions and a decorator for logging and handling errors in Python applications.

Functions:
- `log_error(func_name, error_message, log_level, log_to_file)`: Log an error message with the specified function name, error message, log level, and log file flag.

- `create_error_message(custom_message, e)`: Create an error message with an optional custom message or a default message and the original exception.

Decorator:
- `error_handler(custom_message=None, log_level=logging.ERROR, log_to_file=True)`: A decorator for handling and logging exceptions in functions. It allows custom error messages, log levels, and the choice to log to a file.

For detailed information on how to use these functions and the decorator, please refer to their docstrings within the code.
"""

import logging

def log_error(func_name: str, error_message: str, log_level: int, log_to_file: bool) -> None:
    """
    Log an error message.

    Args:
        func_name (str): The name of the function where the error occurred.
        error_message (str): The error message to log.
        log_level (int): The logging level to use (e.g., logging.ERROR).
        log_to_file (bool): Whether to log to a file.

    Returns:
        None
    """
    if log_to_file:
        logging.log(log_level, f"Error in {func_name}: {error_message}")

def create_error_message(custom_message: str, e: Exception) -> str:
    """
    Create an error message with a custom message, if provided, or a default message.

    Args:
        custom_message (str): A custom error message.
        e (Exception): The original exception.

    Returns:
        str: The error message.
    """
    if custom_message:
        return f"{custom_message} - {e}"
    return f"Error occurred - {e}"

def error_handler(custom_message: str | None = None, log_level: int = logging.ERROR, log_to_file: bool = True) -> callable:
    """
    Decorator for handling and logging exceptions in functions.

    Args:
        custom_message (str | None, optional): A custom error message, if provided.
        log_level (int, optional): The logging level to use (default is logging.ERROR).
        log_to_file (bool, optional): Whether to log to a file (default is True).

    Returns:
        callable: The decorator function.
    """
    def wrapper(func: callable) -> callable:
        def inner_wrapper(*args, **kwargs) -> any:
            try:
                result = func(*args, **kwargs)
                return result
            except Exception as e:
                error_message = create_error_message(custom_message, e)
                log_error(func.__name__, error_message, log_level, log_to_file)
                # Raise a new exception to propagate the error up the call stack
                raise Exception(error_message) from e
        return inner_wrapper
    return wrapper