# GENERATED CODE - DO NOT MODIFY
from __future__ import annotations
from chitose.xrpc import XrpcCall
from chitose.xrpc import XrpcSubscribe
from .get_config import _get_config

class Server_:
    """We recommend calling methods in this class via the :doc:`chitose.BskyAgent <chitose>` class instead of creating instances of this class directly."""

    def __init__(self, call: XrpcCall, subscribe: XrpcSubscribe) -> None:
        self.call = call
        self.subscribe = subscribe

    def get_config(self) -> bytes:
        """Get details about ozone's server configuration."""
        return _get_config(self.call)