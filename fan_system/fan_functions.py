import os
import time
from fan_logic import ElectricalAppliance, Fan

class FanSimulatorUI:
    @staticmethod
    def clear_terminal() -> None:
        """Utility function to clear terminal buffers smoothly on both Windows and Linux/macOS."""
        os.system('cls' if os.name == 'nt' else 'clear')