# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import chitose.com.atproto.admin.defs
import chitose.com.atproto.moderation.defs
import chitose.com.atproto.repo.strong_ref
import typing

def _create_report(call: chitose.xrpc.XrpcCall, reason_type: chitose.com.atproto.moderation.defs.ReasonType, subject: typing.Union[chitose.com.atproto.admin.defs.RepoRef, chitose.com.atproto.repo.strong_ref.StrongRef], reason: typing.Optional[str]=None) -> bytes:
    """Submit a moderation report regarding an atproto account or record. Implemented by moderation services (with PDS proxying), and requires auth.


    :param reason_type: Indicates the broad category of violation the report is for.

    :param reason: Additional context about the content and violation.
    """
    return call('com.atproto.moderation.createReport', [], {'reasonType': reason_type, 'reason': reason, 'subject': subject}, {'Content-Type': 'application/json'})