# GENERATED CODE - DO NOT MODIFY
from __future__ import annotations
from .resolve_handle import _resolve_handle
from .update_handle import _update_handle
from .resolve_handle import *
from .update_handle import *

class _Identity:

    def __init__(self, service: str, headers: dict[str, str]):
        self.service = service
        self.headers = headers

    def update_handle(self, handle: str):
        return _update_handle(self.service, self.headers, handle)

    def resolve_handle(self, handle: typing.Optional[str]=None):
        return _resolve_handle(self.service, self.headers, handle)