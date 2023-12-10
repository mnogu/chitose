# GENERATED CODE - DO NOT MODIFY
from __future__ import annotations
from chitose.xrpc import XrpcCall
from chitose.xrpc import XrpcSubscribe
from .fetch_labels import _fetch_labels
from .import_repo import _import_repo
from .push_blob import _push_blob
from .transfer_account import _transfer_account
import typing

class Temp_:
    """We recommend calling methods in this class via the :doc:`chitose.BskyAgent <chitose>` class instead of creating instances of this class directly."""

    def __init__(self, call: XrpcCall, subscribe: XrpcSubscribe) -> None:
        self.call = call
        self.subscribe = subscribe

    def transfer_account(self, handle: str, did: str, plc_op: typing.Any) -> bytes:
        """Transfer an account."""
        return _transfer_account(self.call, handle, did, plc_op)

    def push_blob(self, input_: bytes) -> bytes:
        """Gets the did's repo, optionally catching up from a specific revision."""
        return _push_blob(self.call, input_)

    def import_repo(self, input_: bytes) -> bytes:
        """Gets the did's repo, optionally catching up from a specific revision."""
        return _import_repo(self.call, input_)

    def fetch_labels(self, since: typing.Optional[int]=None, limit: typing.Optional[int]=None) -> bytes:
        """Fetch all labels from a labeler created after a certain date."""
        return _fetch_labels(self.call, since, limit)