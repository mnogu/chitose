# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _get_moderation_actions(call: chitose.xrpc.XrpcCallable, subject: typing.Optional[str]=None, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
    """List moderation actions related to a subject."""
    return call('com.atproto.admin.getModerationActions', [('subject', subject), ('limit', limit), ('cursor', cursor)], None, {})