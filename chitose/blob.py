from . import Link

from typing import Any


class Blob:
    def __init__(self, ref: Link, mime_type: str, size: int) -> None:
        self.ref = ref
        self.mime_type = mime_type
        self.size = size

    def to_dict(self) -> dict[str, Any]:
        return {
            '$type': 'blob',
            'ref': self.ref,
            'mimeType': self.mime_type,
            'size': self.size
        }
