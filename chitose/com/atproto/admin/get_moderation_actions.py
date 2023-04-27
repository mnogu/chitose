from __future__ import annotations
import chitose
import typing

def get_moderation_actions(service: str, headers: dict[str, str], subject: typing.Optional[str]=None, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None):
    """List moderation actions related to a subject."""
    return chitose.xrpc.call('com.atproto.admin.getModerationActions', [('subject', subject), ('limit', limit), ('cursor', cursor)], None, service, {} | headers)