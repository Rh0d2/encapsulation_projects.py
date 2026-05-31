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

    # --- Mutator Methods (Setters) ---
    def set_name(self, name: str) -> None:
        """Assigns a value to the __name field."""
        self.__name = str(name).strip()

    def set_animal_type(self, animal_type: str) -> None:
        """Assigns a value to the __animalType field."""
        self.__animal_type = str(animal_type).strip()

    def set_age(self, age: int) -> None:
        """Assigns a value to the __age field."""
        self.__age = int(age)

    # --- Accessor Methods (Getters) ---
    def get_name(self) -> str:
        """Returns the value of the __name field."""
        return self.__name

    def get_animal_type(self) -> str:
        """Returns the value of the __animalType field."""
        return self.__animal_type

    def get_age(self) -> int:
        """Returns the value of the __age field."""
        return self.__age
    
    def show_summary(self) -> None:
        """Uses accessor methods to safely extract and display final data blocks on the screen."""
        print(f"=====================================================")
        print(f"             CONFIRMED REGISTRY DATA CARD            ")
        print(f"=====================================================")
        print(f" [VITAL]: Pet Name Identity   -> {self.get_name()}")
        print(f" [VITAL]: Animal Classification -> {self.get_animal_type()}")
        print(f" [VITAL]: Measured Life Age    -> {self.get_age()} years old")
        print(f"=====================================================")