# Copyright 2025 Theodore Podewil
# GPL-3.0-or-later

# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.

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
