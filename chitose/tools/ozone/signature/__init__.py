# GENERATED CODE - DO NOT MODIFY
from __future__ import annotations
from chitose.xrpc import XrpcCall
from chitose.xrpc import XrpcSubscribe
from .find_correlation import _find_correlation
from .find_related_accounts import _find_related_accounts
from .search_accounts import _search_accounts
import typing

class Signature_:
    """We recommend calling methods in this class via the :doc:`chitose.BskyAgent <chitose>` class instead of creating instances of this class directly."""

    def __init__(self, call: XrpcCall, subscribe: XrpcSubscribe) -> None:
        self.call = call
        self.subscribe = subscribe

    def find_correlation(self, dids: list[str]) -> bytes:
        """Find all correlated threat signatures between 2 or more accounts."""
        return _find_correlation(self.call, dids)

    def find_related_accounts(self, did: str, cursor: typing.Optional[str]=None, limit: typing.Optional[int]=None) -> bytes:
        """Get accounts that share some matching threat signatures with the root account."""
        return _find_related_accounts(self.call, did, cursor, limit)

    def search_accounts(self, values: list[str], cursor: typing.Optional[str]=None, limit: typing.Optional[int]=None) -> bytes:
        """Search for accounts that match one or more threat signature values."""
        return _search_accounts(self.call, values, cursor, limit)