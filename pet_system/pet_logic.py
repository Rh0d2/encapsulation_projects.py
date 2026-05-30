from abc import ABC, abstractmethod

class RecordTemplate(ABC):
    @abstractmethod
    def show_summary(self) -> None:
        pass

class Pet(RecordTemplate):
    def __init__(self) -> None:
        """Initializes empty private data attributes for name, animal type, and age."""
        self.__name: str = ""
        self.__animal_type: str = ""
        self.__age: int = 0