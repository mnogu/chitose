# GENERATED CODE - DO NOT MODIFY
from __future__ import annotations
from chitose.xrpc import XrpcCall
from chitose.xrpc import XrpcSubscribe
from .check_signup_queue import _check_signup_queue
from .fetch_labels import _fetch_labels
from .request_phone_verification import _request_phone_verification
import typing

class Temp_:
    """We recommend calling methods in this class via the :doc:`chitose.BskyAgent <chitose>` class instead of creating instances of this class directly."""

    def __init__(self, call: XrpcCall, subscribe: XrpcSubscribe) -> None:
        self.call = call
        self.subscribe = subscribe

    def fetch_labels(self, since: typing.Optional[int]=None, limit: typing.Optional[int]=None) -> bytes:
        """DEPRECATED: use queryLabels or subscribeLabels instead -- Fetch all labels from a labeler created after a certain date."""
        return _fetch_labels(self.call, since, limit)

    def check_signup_queue(self) -> bytes:
        """Check accounts location in signup queue."""
        return _check_signup_queue(self.call)

    def request_phone_verification(self, phone_number: str) -> bytes:
        """Request a verification code to be sent to the supplied phone number"""
        return _request_phone_verification(self.call, phone_number)