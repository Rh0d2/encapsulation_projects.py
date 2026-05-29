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
        self.__on: bool = bool(on)