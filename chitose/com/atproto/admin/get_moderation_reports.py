# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _get_moderation_reports(call: chitose.xrpc.XrpcCall, subject: typing.Optional[str]=None, ignore_subjects: typing.Optional[list[str]]=None, resolved: typing.Optional[bool]=None, action_type: typing.Optional[typing.Literal['com.atproto.admin.defs#takedown', 'com.atproto.admin.defs#flag', 'com.atproto.admin.defs#acknowledge', 'com.atproto.admin.defs#escalate']]=None, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None, reverse: typing.Optional[bool]=None) -> bytes:
    """List moderation reports related to a subject.


    :param reverse: Reverse the order of the returned records? when true, returns reports in chronological order
    """
    return call('com.atproto.admin.getModerationReports', [('subject', subject), ('ignoreSubjects', ignore_subjects), ('resolved', resolved), ('actionType', action_type), ('limit', limit), ('cursor', cursor), ('reverse', reverse)], None, {})