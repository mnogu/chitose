from abc import ABC
from abc import abstractmethod


class Record(ABC):
    @abstractmethod
    def to_dict(self) -> dict:
        pass
