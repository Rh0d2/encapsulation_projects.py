from abc import ABC, abstractmethod

class ElectricalAppliance(ABC):
    @abstractmethod
    def display_properties(self) -> None:
        pass

class Fan(ElectricalAppliance):
    # Class-level speed configuration constants
    SLOW: int = 1
    MEDIUM: int = 2
    FAST: int = 3

    def __init__(self, speed: int = SLOW, radius: float = 5.0, color: str = "blue", on: bool = False) -> None:
        """Constructor using the exact required default parameter constraints."""
        self.__speed: int = int(speed)
        self.__radius: float = float(radius)
        self.__color: str = str(color)
        self.__on: bool =bool(on)

    def display_properties(self) -> None:
        """Polymorphic implementation displaying clean object telemetry rows."""
        status_text = "OsN" if self.__on else "OFF"
        print(f"| Speed: {self.__speed} | Radius: {str(self.__radius).ljust(4)} | Color: {self.__color.ljust(6)} | Power Status: {status_text.ljust(3)} |")

    # --- Accessor Methods (Getters) ---
    def get_speed(self) -> int: 
        return self.__speed

    def get_radius(self) -> float: 
        return self.__radius

    def get_color(self) -> str: 
        return self.__color

    def get_on(self) -> bool: 
        return self.__on
    
    # --- Mutator Methods (Setters) with State Guardrails ---
    def set_speed(self, speed: int) -> bool:
        if speed in [Fan.SLOW, Fan.MEDIUM, Fan.FAST]:
            self.__speed = speed
            self.__on = True  # Automatically flag device active if configured to spin
            return True
        elif speed == 0:
            self.__speed = 0
            self.__on = False
            return True
        return False

    def set_radius(self, radius: float) -> None:
        if radius > 0:
            self.__radius = float(radius)

    def set_color(self, color: str) -> None:
        if color.strip():
            self.__color = color.strip()

    def set_on(self, on: bool) -> None:
        self.__on = bool(on)
        if not self.__on:
            self.__speed = 0  # Reset speed back to neutral if device powers off