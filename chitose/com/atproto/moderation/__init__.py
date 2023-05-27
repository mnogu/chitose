# GENERATED CODE - DO NOT MODIFY
from __future__ import annotations
from chitose.xrpc import XrpcCallable
from .create_report import _create_report
import chitose.com.atproto.admin.defs
import chitose.com.atproto.moderation.defs
import chitose.com.atproto.repo.strong_ref
import typing

class Moderation_:
    """We recommend calling methods in this class via the :doc:`chitose.BskyAgent <chitose>` class instead of creating instances of this class directly."""

    def __init__(self, call: XrpcCallable) -> None:
        self.call = call

    def create_report(self, reason_type: chitose.com.atproto.moderation.defs.ReasonType, subject: typing.Union[chitose.com.atproto.admin.defs.RepoRef, chitose.com.atproto.repo.strong_ref.StrongRef], reason: typing.Optional[str]=None) -> bytes:
        """Report a repo or a record."""
        return _create_report(self.call, reason_type, subject, reason)