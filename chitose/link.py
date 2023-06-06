from typing import Any


class Link:
    def __init__(self, link: str) -> None:
        self.link = link

    def to_dict(self) -> dict[str, Any]:
        return {
            '$link': self.link
        }
