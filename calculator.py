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
