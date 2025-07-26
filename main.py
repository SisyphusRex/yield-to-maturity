#!/usr/bin/env python

# Copyright 2025 Theodore Podewil
# GPL-3.0-or-later

# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>. 

"""Main entry point definition"""
# System Imports
import sys

# First-Party Imports
from program import main


def run(*args):
    """Main entry point for program"""
    # Call the main method for the program
    main(*args)


# Prevent running on import.
if __name__ == "__main__":
    run(*sys.argv[1:])
else:
    raise ImportError("Run this file directly, don't import it!")
