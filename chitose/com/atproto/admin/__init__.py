# GENERATED CODE - DO NOT MODIFY
from __future__ import annotations
from chitose.xrpc import XrpcCall
from chitose.xrpc import XrpcSubscribe
from .disable_account_invites import _disable_account_invites
from .disable_invite_codes import _disable_invite_codes
from .enable_account_invites import _enable_account_invites
from .get_invite_codes import _get_invite_codes
from .get_moderation_action import _get_moderation_action
from .get_moderation_actions import _get_moderation_actions
from .get_moderation_report import _get_moderation_report
from .get_moderation_reports import _get_moderation_reports
from .get_record import _get_record
from .get_repo import _get_repo
from .resolve_moderation_reports import _resolve_moderation_reports
from .reverse_moderation_action import _reverse_moderation_action
from .search_repos import _search_repos
from .send_email import _send_email
from .take_moderation_action import _take_moderation_action
from .update_account_email import _update_account_email
from .update_account_handle import _update_account_handle
import chitose.com.atproto.admin.defs
import chitose.com.atproto.repo.strong_ref
import typing

class Admin_:
    """We recommend calling methods in this class via the :doc:`chitose.BskyAgent <chitose>` class instead of creating instances of this class directly."""

    def __init__(self, call: XrpcCall, subscribe: XrpcSubscribe) -> None:
        self.call = call
        self.subscribe = subscribe

    def get_repo(self, did: str) -> bytes:
        """View details about a repository."""
        return _get_repo(self.call, did)

    def get_moderation_reports(self, subject: typing.Optional[str]=None, ignore_subjects: typing.Optional[list[str]]=None, actioned_by: typing.Optional[str]=None, reporters: typing.Optional[list[str]]=None, resolved: typing.Optional[bool]=None, action_type: typing.Optional[typing.Literal['com.atproto.admin.defs#takedown', 'com.atproto.admin.defs#flag', 'com.atproto.admin.defs#acknowledge', 'com.atproto.admin.defs#escalate']]=None, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None, reverse: typing.Optional[bool]=None) -> bytes:
        """List moderation reports related to a subject.


        :param actioned_by: Get all reports that were actioned by a specific moderator

        :param reporters: Filter reports made by one or more DIDs

        :param reverse: Reverse the order of the returned records? when true, returns reports in chronological order
        """
        return _get_moderation_reports(self.call, subject, ignore_subjects, actioned_by, reporters, resolved, action_type, limit, cursor, reverse)

    def take_moderation_action(self, action: typing.Literal['com.atproto.admin.defs#takedown', 'com.atproto.admin.defs#flag', 'com.atproto.admin.defs#acknowledge'], subject: typing.Union[chitose.com.atproto.admin.defs.RepoRef, chitose.com.atproto.repo.strong_ref.StrongRef], reason: str, created_by: str, subject_blob_cids: typing.Optional[list[str]]=None, create_label_vals: typing.Optional[list[str]]=None, negate_label_vals: typing.Optional[list[str]]=None, duration_in_hours: typing.Optional[int]=None) -> bytes:
        """Take a moderation action on a repo.


        :param duration_in_hours: Indicates how long this action was meant to be in effect before automatically expiring.
        """
        return _take_moderation_action(self.call, action, subject, reason, created_by, subject_blob_cids, create_label_vals, negate_label_vals, duration_in_hours)

    def update_account_email(self, account: str, email: str) -> bytes:
        """Administrative action to update an account's email


        :param account: The handle or DID of the repo.
        """
        return _update_account_email(self.call, account, email)

    def get_moderation_action(self, id: int) -> bytes:
        """View details about a moderation action."""
        return _get_moderation_action(self.call, id)

    def update_account_handle(self, did: str, handle: str) -> bytes:
        """Administrative action to update an account's handle"""
        return _update_account_handle(self.call, did, handle)

    def get_invite_codes(self, sort: typing.Optional[typing.Literal['recent', 'usage']]=None, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
        """Admin view of invite codes"""
        return _get_invite_codes(self.call, sort, limit, cursor)

    def enable_account_invites(self, account: str, note: typing.Optional[str]=None) -> bytes:
        """Re-enable an accounts ability to receive invite codes


        :param note: Additionally add a note describing why the invites were enabled
        """
        return _enable_account_invites(self.call, account, note)

    def get_moderation_report(self, id: int) -> bytes:
        """View details about a moderation report."""
        return _get_moderation_report(self.call, id)

    def disable_account_invites(self, account: str, note: typing.Optional[str]=None) -> bytes:
        """Disable an account from receiving new invite codes, but does not invalidate existing codes


        :param note: Additionally add a note describing why the invites were disabled
        """
        return _disable_account_invites(self.call, account, note)

    def disable_invite_codes(self, codes: typing.Optional[list[str]]=None, accounts: typing.Optional[list[str]]=None) -> bytes:
        """Disable some set of codes and/or all codes associated with a set of users"""
        return _disable_invite_codes(self.call, codes, accounts)

    def reverse_moderation_action(self, id: int, reason: str, created_by: str) -> bytes:
        """Reverse a moderation action."""
        return _reverse_moderation_action(self.call, id, reason, created_by)

    def get_record(self, uri: str, cid: typing.Optional[str]=None) -> bytes:
        """View details about a record."""
        return _get_record(self.call, uri, cid)

    def send_email(self, recipient_did: str, content: str, subject: typing.Optional[str]=None) -> bytes:
        """Send email to a user's primary email address"""
        return _send_email(self.call, recipient_did, content, subject)

    def resolve_moderation_reports(self, action_id: int, report_ids: list[int], created_by: str) -> bytes:
        """Resolve moderation reports by an action."""
        return _resolve_moderation_reports(self.call, action_id, report_ids, created_by)

    def search_repos(self, term: typing.Optional[str]=None, q: typing.Optional[str]=None, invited_by: typing.Optional[str]=None, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
        """Find repositories based on a search term.


        :param term: DEPRECATED: use 'q' instead
        """
        return _search_repos(self.call, term, q, invited_by, limit, cursor)

    def get_moderation_actions(self, subject: typing.Optional[str]=None, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
        """List moderation actions related to a subject."""
        return _get_moderation_actions(self.call, subject, limit, cursor)