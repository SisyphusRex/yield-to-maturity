"""bond valuation solver gui"""

# System Imports

# First Party Imports
from calculator import Calculator
from input_validator import InputValidator

# Third Party Imports
import FreeSimpleGUI as sg


class BondValuationWindow:
    """main menu window"""

    def __init__(self):
        """constructor"""
        self._calculator = Calculator()
        self._validator = InputValidator()

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

        variable_dict = {}

        variable_dict = self._create_variable_dict(
            present_value, coupon_rate, years, par_value, ytm
        )
        if not variable_dict:
            return

        if not present_value:
            present_value = self._calculator.solve_for_present_value(
                variable_dict.get("coupon_rate"),
                variable_dict.get("years"),
                variable_dict.get("par_value"),
                variable_dict.get("ytm"),
            )
            self.window["-PRESENT-VALUE-"].update(present_value)
        if not coupon_rate:
            coupon_rate = self._calculator.solve_for_coupon_rate(
                variable_dict.get("present_value"),
                variable_dict.get("years"),
                variable_dict.get("par_value"),
                variable_dict.get("ytm"),
            )
            self.window["-COUPON-RATE-"].update(coupon_rate)
        if not years:
            years = self._calculator.solve_for_years(
                variable_dict.get("present_value"),
                variable_dict.get("coupon_rate"),
                variable_dict.get("par_value"),
                variable_dict.get("ytm"),
            )
            self.window["-YEARS-"].update(years)
        if not par_value:
            par_value = self._calculator.solve_for_par_value(
                variable_dict.get("present_value"),
                variable_dict.get("coupon_rate"),
                variable_dict.get("years"),
                variable_dict.get("ytm"),
            )
            self.window["-PAR-VALUE-"].update(par_value)
        if not ytm:
            ytm = self._calculator.solve_for_ytm(
                variable_dict.get("present_value"),
                variable_dict.get("coupon_rate"),
                variable_dict.get("years"),
                variable_dict.get("par_value"),
            )
            self.window["-YTM-"].update(ytm)

    def _create_variable_dict(
        self, present_value: str, coupon_rate: str, years: str, par_value: str, ytm: str
    ) -> dict[str, float]:
        """method to create dict of variables"""
        variable_dict: dict[str, float] = {}
        if present_value:
            if self._validator.is_float(present_value):
                variable_dict.update({"present_value": float(present_value)})
            else:
                sg.popup_error("Present value must be a float.")
                return
        if coupon_rate:
            if self._validator.is_float(coupon_rate):
                variable_dict.update({"coupon_rate": float(coupon_rate)})
            else:
                sg.popup_error("Coupon Rate must be a float.")
                return
        if years:
            if self._validator.is_float(years):
                variable_dict.update({"years": float(years)})
            else:
                sg.popup_error("Years must be a float")
                return
        if par_value:
            if self._validator.is_float(par_value):
                variable_dict.update({"par_value": float(par_value)})
            else:
                sg.popup_error("Par Value must be a float.")
                return
        if ytm:
            if self._validator.is_float(ytm):
                variable_dict.update({"ytm": float(ytm)})
            else:
                sg.popup_error("YTM must be a float.")
        return variable_dict
