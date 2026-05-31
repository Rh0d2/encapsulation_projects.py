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
            
    def register_new_pet(self) -> RecordTemplate:
        """Prompts the user to enter data and applies them using mutators."""
        self.clear_screen()
        print("=====================================================")
        print("            BIOMETRIC PET REGISTRATION ENTRY         ")
        print("=====================================================")
        
        # Instantiate a clean blank target object array cell
        active_pet = Pet()
        
        # Gathering target variables from console telemetry scans
        name_input = input(" Enter Pet Name Identifier: ").strip()
        type_input = input(" Enter Animal Classification Type (e.g. Zebra Finch): ").strip()
        age_input = self.prompt_valid_age()
        
        # Activating mutator transmission channels to write states
        active_pet.set_name(name_input if name_input else "Unknown Subject")
        active_pet.set_animal_type(type_input if type_input else "Unknown Species")
        active_pet.set_age(age_input)
        
        print("\n [SUCCESS]: State attributes written to private record memory layers.")
        time.sleep(1.0)
        return active_pet