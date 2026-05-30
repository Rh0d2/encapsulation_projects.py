import os
import time
from car_logic import Vehicle, Car

class CarDashboardUI:
    @staticmethod
    def clear_terminal() -> None:
        """Utility function to clear terminal buffers cleanly across operating systems."""
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def execute_assignment_verification(self, test_car: Car) -> None:
        """Creates a Car object, accelerates 5 times tracking speed, then brakes 5 times tracking speed."""
        print("\n=======================================================")
        print("          MANDATORY TEXTBOOK SCRIPT CHECKPIPE          ")
        print("=======================================================")
        print(f" Initializing test run on: {test_car.get_speed()} km/h")
        
        # Call accelerate method five times and display velocity output
        print("\n [PHASE 1]: Initiating +5 km/h Acceleration Sequence Loop...")
        for i in range(1, 6):
            test_car.accelerate()
            print(f"   -> Call #{i}: Acceleration Triggered | Current Speed: {test_car.get_speed()} km/h")
            time.sleep(0.3)
            
        # Call brake method five times and display velocity output
        print("\n [PHASE 2]: Initiating -5 km/h Braking Deceleration Sequence Loop...")
        for i in range(1, 6):
            test_car.brake()
            print(f"   -> Call #{i}: Brake Triggered        | Current Speed: {test_car.get_speed()} km/h")
            time.sleep(0.3)
            
        print("=======================================================")
        print(" [SYSTEM]: Script check complete. Press Enter to boot live panel...")
        input()