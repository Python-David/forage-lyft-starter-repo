from abc import ABC, abstractmethod


class ITires(ABC):
    @abstractmethod
    def needs_service(self):
        pass
