# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _query_moderation_events(call: chitose.xrpc.XrpcCall, types: typing.Optional[list[str]]=None, created_by: typing.Optional[str]=None, sort_direction: typing.Optional[str]=None, created_after: typing.Optional[str]=None, created_before: typing.Optional[str]=None, subject: typing.Optional[str]=None, include_all_user_records: typing.Optional[bool]=None, limit: typing.Optional[int]=None, has_comment: typing.Optional[bool]=None, comment: typing.Optional[str]=None, added_labels: typing.Optional[list[str]]=None, removed_labels: typing.Optional[list[str]]=None, added_tags: typing.Optional[list[str]]=None, removed_tags: typing.Optional[list[str]]=None, report_types: typing.Optional[list[str]]=None, cursor: typing.Optional[str]=None) -> bytes:
    """List moderation events related to a subject.


    :param types: The types of events (fully qualified string in the format of com.atproto.admin#modEvent<name>) to filter by. If not specified, all events are returned.

    :param sort_direction: Sort direction for the events. Defaults to descending order of created at timestamp.

    :param created_after: Retrieve events created after a given timestamp

    :param created_before: Retrieve events created before a given timestamp

    :param include_all_user_records: If true, events on all record types (posts, lists, profile etc.) owned by the did are returned

    :param has_comment: If true, only events with comments are returned

    :param comment: If specified, only events with comments containing the keyword are returned

    :param added_labels: If specified, only events where all of these labels were added are returned

    :param removed_labels: If specified, only events where all of these labels were removed are returned

    :param added_tags: If specified, only events where all of these tags were added are returned

    :param removed_tags: If specified, only events where all of these tags were removed are returned
    """
    return call('com.atproto.admin.queryModerationEvents', [('types', types), ('createdBy', created_by), ('sortDirection', sort_direction), ('createdAfter', created_after), ('createdBefore', created_before), ('subject', subject), ('includeAllUserRecords', include_all_user_records), ('limit', limit), ('hasComment', has_comment), ('comment', comment), ('addedLabels', added_labels), ('removedLabels', removed_labels), ('addedTags', added_tags), ('removedTags', removed_tags), ('reportTypes', report_types), ('cursor', cursor)], None, {})