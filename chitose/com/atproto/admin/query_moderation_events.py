# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _query_moderation_events(call: chitose.xrpc.XrpcCall, types: typing.Optional[list[str]]=None, created_by: typing.Optional[str]=None, sort_direction: typing.Optional[str]=None, subject: typing.Optional[str]=None, include_all_user_records: typing.Optional[bool]=None, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
    """List moderation events related to a subject.


    :param types: The types of events (fully qualified string in the format of com.atproto.admin#modEvent<name>) to filter by. If not specified, all events are returned.

    :param sort_direction: Sort direction for the events. Defaults to descending order of created at timestamp.

    :param include_all_user_records: If true, events on all record types (posts, lists, profile etc.) owned by the did are returned
    """
    return call('com.atproto.admin.queryModerationEvents', [('types', types), ('createdBy', created_by), ('sortDirection', sort_direction), ('subject', subject), ('includeAllUserRecords', include_all_user_records), ('limit', limit), ('cursor', cursor)], None, {})