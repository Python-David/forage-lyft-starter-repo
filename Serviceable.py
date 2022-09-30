from abc import ABC, abstractmethod


class IServiceable(ABC):
    """Car are accessed through the Serviceable interface"""

    @abstractmethod
    def needs_service(self) -> bool:
        pass
