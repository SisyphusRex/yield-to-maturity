"""input validator module"""

# System Imports

# First Party Imports

# Third Party Imports


class InputValidator:
    """input validator class"""

    def is_float(self, input_string: str) -> bool:
        """validate whether input is float"""
        try:
            float(input_string)
        except ValueError:
            return False
        return True
