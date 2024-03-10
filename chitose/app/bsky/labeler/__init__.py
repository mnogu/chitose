# GENERATED CODE - DO NOT MODIFY
from __future__ import annotations
from chitose.xrpc import XrpcCall
from chitose.xrpc import XrpcSubscribe
from .get_services import _get_services
import typing

class Labeler_:
    """We recommend calling methods in this class via the :doc:`chitose.BskyAgent <chitose>` class instead of creating instances of this class directly."""

    def __init__(self, call: XrpcCall, subscribe: XrpcSubscribe) -> None:
        self.call = call
        self.subscribe = subscribe

    def get_services(self, dids: list[str], detailed: typing.Optional[bool]=None) -> bytes:
        """Get information about a list of labeler services."""
        return _get_services(self.call, dids, detailed)