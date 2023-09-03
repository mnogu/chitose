# GENERATED CODE - DO NOT MODIFY
from __future__ import annotations
from chitose.xrpc import XrpcCall
from chitose.xrpc import XrpcSubscribe
from .upgrade_repo_version import _upgrade_repo_version
import typing

class Temp_:
    """We recommend calling methods in this class via the :doc:`chitose.BskyAgent <chitose>` class instead of creating instances of this class directly."""

    def __init__(self, call: XrpcCall, subscribe: XrpcSubscribe) -> None:
        self.call = call
        self.subscribe = subscribe

    def upgrade_repo_version(self, did: str, force: typing.Optional[bool]=None) -> bytes:
        """Upgrade a repo to v3"""
        return _upgrade_repo_version(self.call, did, force)