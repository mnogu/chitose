# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import chitose.com.atproto.admin.defs
import chitose.com.atproto.moderation.defs
import chitose.com.atproto.repo.strong_ref
import typing

def _create_report(service: str, headers: dict[str, str], reason_type: chitose.com.atproto.moderation.defs.ReasonType, subject: typing.Union[chitose.com.atproto.admin.defs.RepoRef, chitose.com.atproto.repo.strong_ref.StrongRef], reason: typing.Optional[str]=None) -> bytes:
    """Report a repo or a record."""
    return chitose.xrpc.call('com.atproto.moderation.createReport', [], {'reasonType': reason_type, 'reason': reason, 'subject': subject}, service, {'Content-Type': 'application/json'} | headers)