# GENERATED CODE - DO NOT MODIFY
from __future__ import annotations
from chitose.xrpc import XrpcCall
from chitose.xrpc import XrpcSubscribe
from .emit_event import _emit_event
from .get_event import _get_event
from .get_record import _get_record
from .get_repo import _get_repo
from .query_events import _query_events
from .query_statuses import _query_statuses
from .search_repos import _search_repos
import chitose.com.atproto.admin.defs
import chitose.com.atproto.repo.strong_ref
import chitose.tools.ozone.moderation.defs
import typing

class Moderation_:
    """We recommend calling methods in this class via the :doc:`chitose.BskyAgent <chitose>` class instead of creating instances of this class directly."""

    def __init__(self, call: XrpcCall, subscribe: XrpcSubscribe) -> None:
        self.call = call
        self.subscribe = subscribe

    def query_statuses(self, subject: typing.Optional[str]=None, comment: typing.Optional[str]=None, reported_after: typing.Optional[str]=None, reported_before: typing.Optional[str]=None, reviewed_after: typing.Optional[str]=None, reviewed_before: typing.Optional[str]=None, include_muted: typing.Optional[bool]=None, only_muted: typing.Optional[bool]=None, review_state: typing.Optional[str]=None, ignore_subjects: typing.Optional[list[str]]=None, last_reviewed_by: typing.Optional[str]=None, sort_field: typing.Optional[str]=None, sort_direction: typing.Optional[str]=None, takendown: typing.Optional[bool]=None, appealed: typing.Optional[bool]=None, limit: typing.Optional[int]=None, tags: typing.Optional[list[str]]=None, exclude_tags: typing.Optional[list[str]]=None, cursor: typing.Optional[str]=None) -> bytes:
        """View moderation statuses of subjects (record or repo).


        :param comment: Search subjects by keyword from comments

        :param reported_after: Search subjects reported after a given timestamp

        :param reported_before: Search subjects reported before a given timestamp

        :param reviewed_after: Search subjects reviewed after a given timestamp

        :param reviewed_before: Search subjects reviewed before a given timestamp

        :param include_muted: By default, we don't include muted subjects in the results. Set this to true to include them.

        :param only_muted: When set to true, only muted subjects and reporters will be returned.

        :param review_state: Specify when fetching subjects in a certain state

        :param last_reviewed_by: Get all subject statuses that were reviewed by a specific moderator

        :param takendown: Get subjects that were taken down

        :param appealed: Get subjects in unresolved appealed status
        """
        return _query_statuses(self.call, subject, comment, reported_after, reported_before, reviewed_after, reviewed_before, include_muted, only_muted, review_state, ignore_subjects, last_reviewed_by, sort_field, sort_direction, takendown, appealed, limit, tags, exclude_tags, cursor)

    def get_repo(self, did: str) -> bytes:
        """Get details about a repository."""
        return _get_repo(self.call, did)

    def get_event(self, id: int) -> bytes:
        """Get details about a moderation event."""
        return _get_event(self.call, id)

    def query_events(self, types: typing.Optional[list[str]]=None, created_by: typing.Optional[str]=None, sort_direction: typing.Optional[str]=None, created_after: typing.Optional[str]=None, created_before: typing.Optional[str]=None, subject: typing.Optional[str]=None, include_all_user_records: typing.Optional[bool]=None, limit: typing.Optional[int]=None, has_comment: typing.Optional[bool]=None, comment: typing.Optional[str]=None, added_labels: typing.Optional[list[str]]=None, removed_labels: typing.Optional[list[str]]=None, added_tags: typing.Optional[list[str]]=None, removed_tags: typing.Optional[list[str]]=None, report_types: typing.Optional[list[str]]=None, cursor: typing.Optional[str]=None) -> bytes:
        """List moderation events related to a subject.


        :param types: The types of events (fully qualified string in the format of tools.ozone.moderation.defs#modEvent<name>) to filter by. If not specified, all events are returned.

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
        return _query_events(self.call, types, created_by, sort_direction, created_after, created_before, subject, include_all_user_records, limit, has_comment, comment, added_labels, removed_labels, added_tags, removed_tags, report_types, cursor)

    def get_record(self, uri: str, cid: typing.Optional[str]=None) -> bytes:
        """Get details about a record."""
        return _get_record(self.call, uri, cid)

    def emit_event(self, event: typing.Union[chitose.tools.ozone.moderation.defs.ModEventTakedown, chitose.tools.ozone.moderation.defs.ModEventAcknowledge, chitose.tools.ozone.moderation.defs.ModEventEscalate, chitose.tools.ozone.moderation.defs.ModEventComment, chitose.tools.ozone.moderation.defs.ModEventLabel, chitose.tools.ozone.moderation.defs.ModEventReport, chitose.tools.ozone.moderation.defs.ModEventMute, chitose.tools.ozone.moderation.defs.ModEventUnmute, chitose.tools.ozone.moderation.defs.ModEventMuteReporter, chitose.tools.ozone.moderation.defs.ModEventUnmuteReporter, chitose.tools.ozone.moderation.defs.ModEventReverseTakedown, chitose.tools.ozone.moderation.defs.ModEventEmail, chitose.tools.ozone.moderation.defs.ModEventTag], subject: typing.Union[chitose.com.atproto.admin.defs.RepoRef, chitose.com.atproto.repo.strong_ref.StrongRef], created_by: str, subject_blob_cids: typing.Optional[list[str]]=None) -> bytes:
        """Take a moderation action on an actor."""
        return _emit_event(self.call, event, subject, created_by, subject_blob_cids)

    def search_repos(self, term: typing.Optional[str]=None, q: typing.Optional[str]=None, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
        """Find repositories based on a search term.


        :param term: DEPRECATED: use 'q' instead
        """
        return _search_repos(self.call, term, q, limit, cursor)