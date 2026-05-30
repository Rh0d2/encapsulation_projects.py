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