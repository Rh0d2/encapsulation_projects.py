from abc import ABC, abstractmethod

class RecordTemplate(ABC):
    @abstractmethod
    def show_summary(self) -> None:
        pass