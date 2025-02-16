import sys  # Importing the sys module to access system-specific parameters and functions.

def error_message_details(error, error_details: sys):
    """
    Extracts detailed error information, including the filename, line number, and error message.

    Parameters:
    error (Exception): The exception object containing the error.
    error_details (sys): The sys module to extract traceback details.

    Returns:
    str: A formatted error message string with script name, line number, and error details.
    """
    _, _, exc_tb = error_details.exc_info()  # Extracting the traceback object
    file_name = exc_tb.tb_frame.f_code.co_filename  # Getting the filename where the error occurred
    error_message = "error occurred in python script [{0}], line number [{1}], error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)  # Formatting the error details
    )
    return error_message  # Returning the formatted error message

class CustomException(Exception):
    """
    Custom exception class to provide detailed error messages when an exception occurs.

    Attributes:
    error_message (str): A formatted string containing script name, line number, and error details.
    """
    def __init__(self, error_message, error_details: sys):
        """
        Initializes the CustomException class.

        Parameters:
        error_message (Exception): The original exception object.
        error_details (sys): The sys module to extract traceback details.
        """
        super().__init__(error_message)  # Calling the parent class (Exception) constructor
        self.error_message = error_message_details(
            error_message, error_details=error_details  # Generating a detailed error message
        )

    def __str__(self):
        """
        Returns the formatted error message when the exception is printed.
        
        Returns:
        str: The detailed error message.
        """
        return self.error_message
