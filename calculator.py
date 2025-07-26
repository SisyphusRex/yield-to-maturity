# Copyright 2025 Theodore Podewil
# GPL-3.0-or-later

# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.

"""module containing calculator class"""

# System Imports
import math

# First Party Imports

# Third Party Imports


class Calculator:
    """calculator class"""

    def solve_for_present_value(
        self, coupon_rate: float, years: float, par_value: float, ytm: float
    ) -> float:
        """method to solve for present value"""
        present_value: float = coupon_rate * ((1 - (1 + ytm) ** (-1 * years)) / ytm) + (
            par_value / ((1 + ytm) ** years)
        )
        return present_value

    def solve_for_coupon_rate(
        self, present_value: float, years: float, par_value: float, ytm: float
    ) -> float:
        """method to solve for coupon_rate"""
        coupon_rate = (
            ytm * present_value * ((1 + ytm) ** years) - (par_value * ytm)
        ) / ((1 - ((1 + ytm) ** (-1 * years))) * ((1 + ytm) ** years))
        return coupon_rate

    def solve_for_years(
        self, present_value: float, coupon_rate: float, par_value: float, ytm: float
    ) -> float:
        """method to solve for years"""
        years: float = -(
            math.log(
                (present_value * ytm - coupon_rate) / (-coupon_rate + par_value * ytm)
            )
            / math.log(1 + ytm)
        )
        return years

    def solve_for_par_value(
        self, present_value: float, coupon_rate: float, years: float, ytm: float
    ) -> float:
        """method to solve for par value"""
        par_value: float = present_value * ((1 + ytm) ** years) - (
            (coupon_rate * (1 - (1 + ytm) ** (-1 * years)) * (1 + ytm) ** years) / ytm
        )
        return par_value

    def solve_for_ytm(
        self, present_value: float, coupon_rate: float, years: float, par_value: float
    ) -> float:
        """method to solve for yield to maturity"""
