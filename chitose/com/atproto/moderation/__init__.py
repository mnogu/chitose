# GENERATED CODE - DO NOT MODIFY
from __future__ import annotations
from chitose.xrpc import XrpcCall
from chitose.xrpc import XrpcSubscribe
from .create_report import _create_report
import chitose.com.atproto.admin.defs
import chitose.com.atproto.moderation.defs
import chitose.com.atproto.repo.strong_ref
import typing

class Moderation_:
    """We recommend calling methods in this class via the :doc:`chitose.BskyAgent <chitose>` class instead of creating instances of this class directly."""

    def __init__(self, call: XrpcCall, subscribe: XrpcSubscribe) -> None:
        self.call = call
        self.subscribe = subscribe

    def create_report(self, reason_type: chitose.com.atproto.moderation.defs.ReasonType, subject: typing.Union[chitose.com.atproto.admin.defs.RepoRef, chitose.com.atproto.repo.strong_ref.StrongRef], reason: typing.Optional[str]=None) -> bytes:
        """Submit a moderation report regarding an atproto account or record. Implemented by moderation services (with PDS proxying), and requires auth.


        :param reason_type: Indicates the broad category of violation the report is for.

        :param reason: Additional context about the content and violation.
        """
        return _create_report(self.call, reason_type, subject, reason)