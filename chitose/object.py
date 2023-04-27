from abc import ABC
from abc import abstractmethod


class Object(ABC):
    @abstractmethod
    def to_dict(self) -> dict:
        pass
