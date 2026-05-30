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

    def launch_dashboard(self) -> None:
        """Launches the automatic assignment verification, then loads the interactive telemetry core."""
        # Instantiate test car targets using assignment scope constraints
        active_vehicle = Car(year_model="2026", make="Honda")
        
        # Run textbook loop constraints on initialization
        self.clear_terminal()
        self.execute_assignment_verification(active_vehicle)
        
        while True:
            self.clear_terminal()
            print("=====================================================================")
            print("                     LIVE ENGINE TELEMETRY CORE                      ")
            print("=====================================================================")
            
            # Polymorphic dynamic array readouts
            print(" [ACTIVE VEHICLE] ", end="")
            active_vehicle.display_telemetry()
            
            print("=====================================================================")
            print(" [1] Step on the Gas Pedal (Accelerate +5 km/h)")
            print(" [2] Hit the Brake Pedal   (Decelerate -5 km/h)")
            print(" [3] Turn Off Ignition     (Disconnect Pipeline Array)")
            print("=====================================================================")
            
            choice = input("\n Select Input Vector Action: ").strip()
            
            if choice == "1":
                active_vehicle.accelerate()
                print("\n [THROTTLE]: Fuel injected. Velocity increasing...")
                time.sleep(0.4)
            elif choice == "2":
                active_vehicle.brake()
                print("\n [CALIPER]: Brake pad compression applied. Speed dropping...")
                time.sleep(0.4)
            elif choice == "3":
                print("\n [SYSTEM]: Killing diagnostic telemetry stream logs...")
                time.sleep(0.5)
                self.clear_terminal()
                break
            else:
                print(" [ERROR]: Invalid control vector transmission received.")
                time.sleep(0.8)