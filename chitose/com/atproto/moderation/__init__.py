# GENERATED CODE - DO NOT MODIFY
from __future__ import annotations
from .create_report import _create_report
from .create_report import *
from .defs import *

class Moderation:

    def __init__(self, service: str, headers: dict[str, str]):
        self.service = service
        self.headers = headers

    def create_report(self, reason_type: chitose.com.atproto.moderation.defs.ReasonType, subject: typing.Union[chitose.com.atproto.admin.defs.RepoRef, chitose.com.atproto.repo.StrongRef], reason: typing.Optional[str]=None):
        """Report a repo or a record."""
        return _create_report(self.service, self.headers, reason_type, subject, reason)