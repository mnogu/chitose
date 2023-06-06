from abc import ABC
from abc import abstractmethod
from typing import Any


class Object(ABC):
    @abstractmethod
    def to_dict(self) -> dict[str, Any]:
        pass
