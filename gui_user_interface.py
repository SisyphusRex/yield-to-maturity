"""bond valuation solver gui"""

# System Imports

# First Party Imports

# Third Party Imports
import FreeSimpleGUI as sg


class BondValuationWindow:
    """main menu window"""

    def __init__(self):
        """constructor"""

        layout = [
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
                present_value = values["-PRESENT-VALUE-"]
                coupon_rate = values["-COUPON-RATE-"]
                years = values["-YEARS-"]
                par_value = values["-PAR-VALUE-"]
                ytm = values["-YTM-"]
