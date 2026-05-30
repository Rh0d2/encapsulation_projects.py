from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def display_telemetry(self) -> None:
        pass

class Car(Vehicle):
    def __init__(self, year_model: str, make: str) -> None:
        """Initializes the car's year model and make from inputs, defaulting speed to 0."""
        self.__year_model: str = str(year_model)
        self.__make: str = str(make)
        self.__speed: int = 0

    def display_telemetry(self) -> None:
        """Polymorphic implementation displaying real-time car metrics."""
        print(f"| Model Year: {self.__year_model.ljust(5)} | Make: {self.__make.ljust(12)} | Current Velocity: {str(self.__speed).rjust(3)} km/h |")

    def get_speed(self) -> int:
        """Returns the current speed value."""
        return self.__speed