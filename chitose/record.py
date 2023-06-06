from abc import ABC
from abc import abstractmethod
from typing import Any


class Record(ABC):
    @abstractmethod
    def to_dict(self) -> dict[str, Any]:
        pass
