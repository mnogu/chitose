# GENERATED CODE - DO NOT MODIFY
from __future__ import annotations
from chitose.xrpc import XrpcCall
from chitose.xrpc import XrpcSubscribe
from .create_communication_template import _create_communication_template
from .delete_account import _delete_account
from .delete_communication_template import _delete_communication_template
from .disable_account_invites import _disable_account_invites
from .disable_invite_codes import _disable_invite_codes
from .emit_moderation_event import _emit_moderation_event
from .enable_account_invites import _enable_account_invites
from .get_account_info import _get_account_info
from .get_account_infos import _get_account_infos
from .get_invite_codes import _get_invite_codes
from .get_moderation_event import _get_moderation_event
from .get_record import _get_record
from .get_repo import _get_repo
from .get_subject_status import _get_subject_status
from .list_communication_templates import _list_communication_templates
from .query_moderation_events import _query_moderation_events
from .query_moderation_statuses import _query_moderation_statuses
from .search_repos import _search_repos
from .send_email import _send_email
from .update_account_email import _update_account_email
from .update_account_handle import _update_account_handle
from .update_communication_template import _update_communication_template
from .update_subject_status import _update_subject_status
import chitose.com.atproto.admin.defs
import chitose.com.atproto.repo.strong_ref
import typing

class Admin_:
    """We recommend calling methods in this class via the :doc:`chitose.BskyAgent <chitose>` class instead of creating instances of this class directly."""

    def __init__(self, call: XrpcCall, subscribe: XrpcSubscribe) -> None:
        self.call = call
        self.subscribe = subscribe

    def get_repo(self, did: str) -> bytes:
        """Get details about a repository."""
        return _get_repo(self.call, did)

    def update_account_email(self, account: str, email: str) -> bytes:
        """Administrative action to update an account's email.


        :param account: The handle or DID of the repo.
        """
        return _update_account_email(self.call, account, email)

    def get_account_info(self, did: str) -> bytes:
        """Get details about an account."""
        return _get_account_info(self.call, did)

    def get_subject_status(self, did: typing.Optional[str]=None, uri: typing.Optional[str]=None, blob: typing.Optional[str]=None) -> bytes:
        """Get the service-specific admin status of a subject (account, record, or blob)."""
        return _get_subject_status(self.call, did, uri, blob)

    def list_communication_templates(self) -> bytes:
        """Get list of all communication templates."""
        return _list_communication_templates(self.call)

    def create_communication_template(self, name: str, content_markdown: str, subject: str, created_by: typing.Optional[str]=None) -> bytes:
        """Administrative action to create a new, re-usable communication (email for now) template.


        :param name: Name of the template.

        :param content_markdown: Content of the template, markdown supported, can contain variable placeholders.

        :param subject: Subject of the message, used in emails.

        :param created_by: DID of the user who is creating the template.
        """
        return _create_communication_template(self.call, name, content_markdown, subject, created_by)

    def query_moderation_statuses(self, subject: typing.Optional[str]=None, comment: typing.Optional[str]=None, reported_after: typing.Optional[str]=None, reported_before: typing.Optional[str]=None, reviewed_after: typing.Optional[str]=None, reviewed_before: typing.Optional[str]=None, include_muted: typing.Optional[bool]=None, review_state: typing.Optional[str]=None, ignore_subjects: typing.Optional[list[str]]=None, last_reviewed_by: typing.Optional[str]=None, sort_field: typing.Optional[str]=None, sort_direction: typing.Optional[str]=None, takendown: typing.Optional[bool]=None, appealed: typing.Optional[bool]=None, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
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
        return _query_moderation_statuses(self.call, subject, comment, reported_after, reported_before, reviewed_after, reviewed_before, include_muted, review_state, ignore_subjects, last_reviewed_by, sort_field, sort_direction, takendown, appealed, limit, cursor)

    def delete_communication_template(self, id: str) -> bytes:
        """Delete a communication template."""
        return _delete_communication_template(self.call, id)

    def update_account_handle(self, did: str, handle: str) -> bytes:
        """Administrative action to update an account's handle."""
        return _update_account_handle(self.call, did, handle)

    def get_invite_codes(self, sort: typing.Optional[typing.Literal['recent', 'usage']]=None, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
        """Get an admin view of invite codes."""
        return _get_invite_codes(self.call, sort, limit, cursor)

    def update_communication_template(self, id: str, name: typing.Optional[str]=None, content_markdown: typing.Optional[str]=None, subject: typing.Optional[str]=None, updated_by: typing.Optional[str]=None, disabled: typing.Optional[bool]=None) -> bytes:
        """Administrative action to update an existing communication template. Allows passing partial fields to patch specific fields only.


        :param id: ID of the template to be updated.

        :param name: Name of the template.

        :param content_markdown: Content of the template, markdown supported, can contain variable placeholders.

        :param subject: Subject of the message, used in emails.

        :param updated_by: DID of the user who is updating the template.
        """
        return _update_communication_template(self.call, id, name, content_markdown, subject, updated_by, disabled)

    def enable_account_invites(self, account: str, note: typing.Optional[str]=None) -> bytes:
        """Re-enable an account's ability to receive invite codes.


        :param note: Optional reason for enabled invites.
        """
        return _enable_account_invites(self.call, account, note)

    def disable_account_invites(self, account: str, note: typing.Optional[str]=None) -> bytes:
        """Disable an account from receiving new invite codes, but does not invalidate existing codes.


        :param note: Optional reason for disabled invites.
        """
        return _disable_account_invites(self.call, account, note)

    def disable_invite_codes(self, codes: typing.Optional[list[str]]=None, accounts: typing.Optional[list[str]]=None) -> bytes:
        """Disable some set of codes and/or all codes associated with a set of users."""
        return _disable_invite_codes(self.call, codes, accounts)

    def update_subject_status(self, subject: typing.Union[chitose.com.atproto.admin.defs.RepoRef, chitose.com.atproto.repo.strong_ref.StrongRef, chitose.com.atproto.admin.defs.RepoBlobRef], takedown: typing.Optional[chitose.com.atproto.admin.defs.StatusAttr]=None) -> bytes:
        """Update the service-specific admin status of a subject (account, record, or blob)."""
        return _update_subject_status(self.call, subject, takedown)

    def emit_moderation_event(self, event: typing.Union[chitose.com.atproto.admin.defs.ModEventTakedown, chitose.com.atproto.admin.defs.ModEventAcknowledge, chitose.com.atproto.admin.defs.ModEventEscalate, chitose.com.atproto.admin.defs.ModEventComment, chitose.com.atproto.admin.defs.ModEventLabel, chitose.com.atproto.admin.defs.ModEventReport, chitose.com.atproto.admin.defs.ModEventMute, chitose.com.atproto.admin.defs.ModEventReverseTakedown, chitose.com.atproto.admin.defs.ModEventUnmute, chitose.com.atproto.admin.defs.ModEventEmail], subject: typing.Union[chitose.com.atproto.admin.defs.RepoRef, chitose.com.atproto.repo.strong_ref.StrongRef], created_by: str, subject_blob_cids: typing.Optional[list[str]]=None) -> bytes:
        """Take a moderation action on an actor."""
        return _emit_moderation_event(self.call, event, subject, created_by, subject_blob_cids)

    def get_moderation_event(self, id: int) -> bytes:
        """Get details about a moderation event."""
        return _get_moderation_event(self.call, id)

    def get_record(self, uri: str, cid: typing.Optional[str]=None) -> bytes:
        """Get details about a record."""
        return _get_record(self.call, uri, cid)

    def query_moderation_events(self, types: typing.Optional[list[str]]=None, created_by: typing.Optional[str]=None, sort_direction: typing.Optional[str]=None, subject: typing.Optional[str]=None, include_all_user_records: typing.Optional[bool]=None, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
        """List moderation events related to a subject.


        :param types: The types of events (fully qualified string in the format of com.atproto.admin#modEvent<name>) to filter by. If not specified, all events are returned.

        :param sort_direction: Sort direction for the events. Defaults to descending order of created at timestamp.

        :param include_all_user_records: If true, events on all record types (posts, lists, profile etc.) owned by the did are returned
        """
        return _query_moderation_events(self.call, types, created_by, sort_direction, subject, include_all_user_records, limit, cursor)

    def send_email(self, recipient_did: str, content: str, sender_did: str, subject: typing.Optional[str]=None, comment: typing.Optional[str]=None) -> bytes:
        """Send email to a user's account email address.


        :param comment: Additional comment by the sender that won't be used in the email itself but helpful to provide more context for moderators/reviewers
        """
        return _send_email(self.call, recipient_did, content, sender_did, subject, comment)

    def search_repos(self, term: typing.Optional[str]=None, q: typing.Optional[str]=None, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
        """Find repositories based on a search term.


        :param term: DEPRECATED: use 'q' instead
        """
        return _search_repos(self.call, term, q, limit, cursor)

    def get_account_infos(self, dids: list[str]) -> bytes:
        """Get details about some accounts."""
        return _get_account_infos(self.call, dids)

    def delete_account(self, did: str) -> bytes:
        """Delete a user account as an administrator."""
        return _delete_account(self.call, did)