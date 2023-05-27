# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _get_moderation_reports(call: chitose.xrpc.XrpcCallable, subject: typing.Optional[str]=None, resolved: typing.Optional[bool]=None, action_type: typing.Optional[typing.Literal['com.atproto.admin.defs#takedown', 'com.atproto.admin.defs#flag', 'com.atproto.admin.defs#acknowledge', 'com.atproto.admin.defs#escalate']]=None, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
    """List moderation reports related to a subject."""
    return call('com.atproto.admin.getModerationReports', [('subject', subject), ('resolved', resolved), ('actionType', action_type), ('limit', limit), ('cursor', cursor)], None, {})