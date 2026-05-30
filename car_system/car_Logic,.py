from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def display_telemetry(self) -> None:
        pass