# GENERATED CODE - DO NOT MODIFY
from __future__ import annotations
from chitose.xrpc import XrpcCall
from chitose.xrpc import XrpcSubscribe
from .delete_account import _delete_account
from .export_account_data import _export_account_data

class Actor_:
    """We recommend calling methods in this class via the :doc:`chitose.BskyAgent <chitose>` class instead of creating instances of this class directly."""

    def __init__(self, call: XrpcCall, subscribe: XrpcSubscribe) -> None:
        self.call = call
        self.subscribe = subscribe

    def export_account_data(self) -> bytes:
        """"""
        return _export_account_data(self.call)

    def delete_account(self) -> bytes:
        """"""
        return _delete_account(self.call)