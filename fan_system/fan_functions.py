import os
import time
from fan_logic import ElectricalAppliance, Fan

class FanSimulatorUI:
    @staticmethod
    def clear_terminal() -> None:
        """Utility function to clear terminal buffers smoothly on both Windows and Linux/macOS."""
        os.system('cls' if os.name == 'nt' else 'clear')

    def generate_problem_test_cases(self) -> list[ElectricalAppliance]:
        """
        Instantiates the strict problem conditions specified in the worksheet text:
        - Object 1: Maximum speed, radius 10, color yellow, turn it on.
        - Object 2: Medium speed, radius 5, color blue, turn it off.
        """
        # Object 1 Setup
        fan1 = Fan()
        fan1.set_speed(Fan.FAST)
        fan1.set_radius(10.0)
        fan1.set_color("yellow")
        fan1.set_on(True)

        # Object 2 Setup
        fan2 = Fan(speed=Fan.MEDIUM, radius=5.0, color="blue", on=False)

        return [fan1, fan2]