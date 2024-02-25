# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _query_moderation_statuses(call: chitose.xrpc.XrpcCall, subject: typing.Optional[str]=None, comment: typing.Optional[str]=None, reported_after: typing.Optional[str]=None, reported_before: typing.Optional[str]=None, reviewed_after: typing.Optional[str]=None, reviewed_before: typing.Optional[str]=None, include_muted: typing.Optional[bool]=None, review_state: typing.Optional[str]=None, ignore_subjects: typing.Optional[list[str]]=None, last_reviewed_by: typing.Optional[str]=None, sort_field: typing.Optional[str]=None, sort_direction: typing.Optional[str]=None, takendown: typing.Optional[bool]=None, appealed: typing.Optional[bool]=None, limit: typing.Optional[int]=None, tags: typing.Optional[list[str]]=None, exclude_tags: typing.Optional[list[str]]=None, cursor: typing.Optional[str]=None) -> bytes:
    """View moderation statuses of subjects (record or repo).


    :param comment: Search subjects by keyword from comments

    :param reported_after: Search subjects reported after a given timestamp

    :param reported_before: Search subjects reported before a given timestamp

    :param reviewed_after: Search subjects reviewed after a given timestamp

    :param reviewed_before: Search subjects reviewed before a given timestamp

    :param include_muted: By default, we don't include muted subjects in the results. Set this to true to include them.

    :param review_state: Specify when fetching subjects in a certain state

    :param last_reviewed_by: Get all subject statuses that were reviewed by a specific moderator

    :param takendown: Get subjects that were taken down

    :param appealed: Get subjects in unresolved appealed status
    """
    return call('com.atproto.admin.queryModerationStatuses', [('subject', subject), ('comment', comment), ('reportedAfter', reported_after), ('reportedBefore', reported_before), ('reviewedAfter', reviewed_after), ('reviewedBefore', reviewed_before), ('includeMuted', include_muted), ('reviewState', review_state), ('ignoreSubjects', ignore_subjects), ('lastReviewedBy', last_reviewed_by), ('sortField', sort_field), ('sortDirection', sort_direction), ('takendown', takendown), ('appealed', appealed), ('limit', limit), ('tags', tags), ('excludeTags', exclude_tags), ('cursor', cursor)], None, {})