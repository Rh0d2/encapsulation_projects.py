import os
import time
from pet_logic import RecordTemplate, Pet

class PetRegistryUI:
    @staticmethod
    def clear_screen() -> None:
        """Wipes console logs across environments cleanly."""
        os.system('cls' if os.name == 'nt' else 'clear')