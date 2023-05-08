# GENERATED CODE - DO NOT MODIFY
from __future__ import annotations
from .create_report import _create_report
import chitose
import typing

class Moderation_:
    """We recommend calling methods in this class via the `chitose.BskyAgent` class instead of creating instances of this class directly."""

    def __init__(self, service: str, headers: dict[str, str]) -> None:
        self.service = service
        self.headers = headers

    def create_report(self, reason_type: chitose.com.atproto.moderation.defs.ReasonType, subject: typing.Union[chitose.com.atproto.admin.defs.RepoRef, chitose.com.atproto.repo.strong_ref.StrongRef], reason: typing.Optional[str]=None) -> bytes:
        """Report a repo or a record."""
        return _create_report(self.service, self.headers, reason_type, subject, reason)