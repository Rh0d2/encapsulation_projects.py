import os
import time
from pet_logic import RecordTemplate, Pet

class PetRegistryUI:
    @staticmethod
    def clear_screen() -> None:
        """Wipes console logs across environments cleanly."""
        os.system('cls' if os.name == 'nt' else 'clear')

    def prompt_valid_age(self) -> int:
        """Guards runtime integrity by forcing user input into strict int data type matching."""
        while True:
            try:
                val = int(input(" Enter Animal Age Metric (Integer): ").strip())
                if val >= 0:
                    return val
                print(" [ERROR]: Chronological age parameter cannot sit below zero values.")
            except ValueError:
                print(" [ERROR]: Base type mismatch! Please pass a valid numerical integer.")