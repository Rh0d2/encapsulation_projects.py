from abc import ABC, abstractmethod

class ElectricalAppliance(ABC):
    @abstractmethod
    def display_properties(self) -> None:
        pass