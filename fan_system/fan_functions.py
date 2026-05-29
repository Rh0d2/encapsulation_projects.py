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
    
    def start_registry_flow(self) -> None:
        """Initial launch point establishing verification objects and setting up telemetry frames."""
        self.clear_terminal()
        print("==========================================")
        print("         DEVICE AUTOMATION REGISTRY       ")
        print("==========================================")
        print(" [SYSTEM]: Building evaluation instances from source problem sheets...")
        time.sleep(0.8)
        
        # Load the two custom assignment objects into an execution tracker array
        monitored_devices = self.generate_problem_test_cases()
        self.start_control_loop(monitored_devices)

    def start_control_loop(self, devices: list[ElectricalAppliance]) -> None:
        """Drives interactive dashboard panel readouts and handles runtime option processing."""
        # Directing terminal modifications explicitly to target index Fan 1
        active_fan = devices[0]
        
        while True:
            self.clear_terminal()
            print("=====================================================================")
            print("                     LIVE ENGINE TELEMETRY CORE                      ")
            print("=====================================================================")
            
            # POLYMORPHIC COMPLIANCE: Direct dynamic looping array readouts
            for index, appliance in enumerate(devices, start=1):
                print(f" [Device #{index}] ", end="")
                appliance.display_properties()
                
            print("=====================================================================")
            print(" [1] Modify Fan #1 Operational Speed Metric")
            print(" [2] Break Diagnostic Telemetry Stream Connection")
            print("=====================================================================")
            
            choice = input("\n Select Action Vector: ").strip()
            
            if choice == "1":
                while True:
                    try:
                        print(f"\n Bounds parameters: 0 (OFF), 1 (SLOW), 2 (MEDIUM), 3 (FAST)")
                        speed = int(input(" Inject New Speed Level Integer: "))
                        
                        if active_fan.set_speed(speed):
                            # Live interactive spin animation sequence
                            if active_fan.get_on():
                                frames = ['-', '\\', '|', '/']
                                animation_delay = 0.05 / active_fan.get_speed()
                                
                                for _ in range(5):
                                    for frame in frames:
                                        self.clear_terminal()
                                        print("=====================================================================")
                                        print(f"          RECALIBRATING TELEMETRY CONFIGURATION STATE... [{frame}]     ")
                                        print("=====================================================================")
                                        print(f" [PROCESSING]: Processing variable shift properties layout on Fan #1...")
                                        print(f" [PROCESSING]: Setting speed to register level flag: {speed}")
                                        print("=====================================================================")
                                        time.sleep(animation_delay)
                                        
                            print("\n [SUCCESS]: State variables reconfigured safely.")
                            break
                        else:
                            print(" [ERROR]: Out of bounds config values! Parameter mutation rejected.")
                    except ValueError:
                        print(" [ERROR]: Please input a clean base numerical integer format.")
                time.sleep(1.2)
                
            elif choice == "2":
                print("\n [SYSTEM]: Terminating pipeline observation array logs...")
                time.sleep(0.5)
                self.clear_terminal()
                break
            else:
                print(" [ERROR]: Invalid transmission index option selected.")
                time.sleep(1)