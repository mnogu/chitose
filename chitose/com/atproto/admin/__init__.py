# GENERATED CODE - DO NOT MODIFY
from __future__ import annotations
from .disable_invite_codes import _disable_invite_codes
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
from .take_moderation_action import _take_moderation_action
from .update_account_email import _update_account_email
from .update_account_handle import _update_account_handle
import chitose
import typing

class Admin_:
    """We recommend calling methods in this class via the `chitose.BskyAgent` class instead of creating instances of this class directly."""

    def __init__(self, service: str, headers: dict[str, str]) -> None:
        self.service = service
        self.headers = headers

    def get_repo(self, did: str) -> bytes:
        """View details about a repository."""
        return _get_repo(self.service, self.headers, did)

    def get_moderation_reports(self, subject: typing.Optional[str]=None, resolved: typing.Optional[str]=None, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
        """List moderation reports related to a subject."""
        return _get_moderation_reports(self.service, self.headers, subject, resolved, limit, cursor)

    def take_moderation_action(self, action: str, subject: typing.Union[chitose.com.atproto.admin.defs.RepoRef, chitose.com.atproto.repo.strong_ref.StrongRef], reason: str, created_by: str, subject_blob_cids: typing.Optional[list[str]]=None, create_label_vals: typing.Optional[list[str]]=None, negate_label_vals: typing.Optional[list[str]]=None) -> bytes:
        """Take a moderation action on a repo."""
        return _take_moderation_action(self.service, self.headers, action, subject, reason, created_by, subject_blob_cids, create_label_vals, negate_label_vals)

    def update_account_email(self, account: str, email: str) -> bytes:
        """Administrative action to update an account's email


        :param account: The handle or DID of the repo.
        """
        return _update_account_email(self.service, self.headers, account, email)

    def get_moderation_action(self, id: int) -> bytes:
        """View details about a moderation action."""
        return _get_moderation_action(self.service, self.headers, id)

    def update_account_handle(self, did: str, handle: str) -> bytes:
        """Administrative action to update an account's handle"""
        return _update_account_handle(self.service, self.headers, did, handle)

    def get_invite_codes(self, sort: typing.Optional[str]=None, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
        """Admin view of invite codes"""
        return _get_invite_codes(self.service, self.headers, sort, limit, cursor)

    def get_moderation_report(self, id: int) -> bytes:
        """View details about a moderation report."""
        return _get_moderation_report(self.service, self.headers, id)

    def disable_invite_codes(self, codes: typing.Optional[list[str]]=None, accounts: typing.Optional[list[str]]=None) -> bytes:
        """Disable some set of codes and/or all codes associated with a set of users"""
        return _disable_invite_codes(self.service, self.headers, codes, accounts)

    def reverse_moderation_action(self, id: int, reason: str, created_by: str) -> bytes:
        """Reverse a moderation action."""
        return _reverse_moderation_action(self.service, self.headers, id, reason, created_by)

    def get_record(self, uri: str, cid: typing.Optional[str]=None) -> bytes:
        """View details about a record."""
        return _get_record(self.service, self.headers, uri, cid)

    def resolve_moderation_reports(self, action_id: int, report_ids: list[int], created_by: str) -> bytes:
        """Resolve moderation reports by an action."""
        return _resolve_moderation_reports(self.service, self.headers, action_id, report_ids, created_by)

    def search_repos(self, term: typing.Optional[str]=None, invited_by: typing.Optional[str]=None, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
        """Find repositories based on a search term."""
        return _search_repos(self.service, self.headers, term, invited_by, limit, cursor)

    def get_moderation_actions(self, subject: typing.Optional[str]=None, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
        """List moderation actions related to a subject."""
        return _get_moderation_actions(self.service, self.headers, subject, limit, cursor)