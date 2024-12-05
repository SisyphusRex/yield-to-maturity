"""bond valuation solver gui"""

# System Imports

# First Party Imports
from calculator import Calculator

# Third Party Imports
import FreeSimpleGUI as sg


class BondValuationWindow:
    """main menu window"""

    def __init__(self):
        """constructor"""
        self.calculator = Calculator()

        layout = [
            [sg.Text("Enter four values to solve for the fifth.")],
            [sg.Text("Present Value, P"), sg.InputText(key="-PRESENT-VALUE-")],
            [sg.Text("Coupon Rate, C"), sg.InputText(key="-COUPON-RATE-")],
            [sg.Text("Number of Years, N"), sg.InputText(key="-YEARS-")],
            [sg.Text("Par Value, M"), sg.InputText(key="-PAR-VALUE-")],
            [sg.Text("Yield To Maturity, r"), sg.InputText(key="-YTM-")],
            [sg.Button("Calculate")],
        ]

        self.window = sg.Window("Main Menu", layout)

    def run(self):
        """start the window up"""
        self._run_loop()
        self.window.close()

    def _run_loop(self):
        """run the vent loop"""
        while True:
            event, values = self.window.read()
            if event == sg.WINDOW_CLOSED:
                break
            if event == "Calculate":
                self._calculate(values)

    def _calculate(self, values):
        """method to calculate missing value"""
        present_value = values["-PRESENT-VALUE-"]
        coupon_rate = values["-COUPON-RATE-"]
        years = values["-YEARS-"]
        par_value = values["-PAR-VALUE-"]
        ytm = values["-YTM-"]

        if not present_value:
            present_value = self.calculator.solve_for_present_value(
                coupon_rate, years, par_value, ytm
            )
        if not coupon_rate:
            coupon_rate = self.calculator.solve_for_coupon_rate(
                present_value, years, par_value, ytm
            )
        if not years:
            years = self.calculator.solve_for_years(
                present_value, coupon_rate, par_value, ytm
            )
        if not par_value:
            par_value = self.calculator.solve_for_par_value(
                present_value, coupon_rate, years, ytm
            )
        if not ytm:
            ytm = self.calculator.solve_for_ytm(
                present_value, coupon_rate, years, par_value
            )
