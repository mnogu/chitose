# GENERATED CODE - DO NOT MODIFY
from __future__ import annotations
from chitose.xrpc import XrpcCall
from chitose.xrpc import XrpcSubscribe
from .delete_account import _delete_account
from .disable_account_invites import _disable_account_invites
from .disable_invite_codes import _disable_invite_codes
from .enable_account_invites import _enable_account_invites
from .get_account_info import _get_account_info
from .get_account_infos import _get_account_infos
from .get_invite_codes import _get_invite_codes
from .get_subject_status import _get_subject_status
from .search_accounts import _search_accounts
from .send_email import _send_email
from .update_account_email import _update_account_email
from .update_account_handle import _update_account_handle
from .update_account_password import _update_account_password
from .update_subject_status import _update_subject_status
import chitose.com.atproto.admin.defs
import chitose.com.atproto.repo.strong_ref
import typing

class Admin_:
    """We recommend calling methods in this class via the :doc:`chitose.BskyAgent <chitose>` class instead of creating instances of this class directly."""

    def __init__(self, call: XrpcCall, subscribe: XrpcSubscribe) -> None:
        self.call = call
        self.subscribe = subscribe

    def update_account_email(self, account: str, email: str) -> bytes:
        """Administrative action to update an account's email.


        :param account: The handle or DID of the repo.
        """
        return _update_account_email(self.call, account, email)

    def search_accounts(self, email: typing.Optional[str]=None, cursor: typing.Optional[str]=None, limit: typing.Optional[int]=None) -> bytes:
        """Get list of accounts that matches your search query."""
        return _search_accounts(self.call, email, cursor, limit)

    def disable_account_invites(self, account: str, note: typing.Optional[str]=None) -> bytes:
        """Disable an account from receiving new invite codes, but does not invalidate existing codes.


        :param note: Optional reason for disabled invites.
        """
        return _disable_account_invites(self.call, account, note)

    def get_invite_codes(self, sort: typing.Optional[typing.Literal['recent', 'usage']]=None, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
        """Get an admin view of invite codes."""
        return _get_invite_codes(self.call, sort, limit, cursor)

    def disable_invite_codes(self, codes: typing.Optional[list[str]]=None, accounts: typing.Optional[list[str]]=None) -> bytes:
        """Disable some set of codes and/or all codes associated with a set of users."""
        return _disable_invite_codes(self.call, codes, accounts)

    def get_account_infos(self, dids: list[str]) -> bytes:
        """Get details about some accounts."""
        return _get_account_infos(self.call, dids)

    def update_subject_status(self, subject: typing.Union[chitose.com.atproto.admin.defs.RepoRef, chitose.com.atproto.repo.strong_ref.StrongRef, chitose.com.atproto.admin.defs.RepoBlobRef], takedown: typing.Optional[chitose.com.atproto.admin.defs.StatusAttr]=None, deactivated: typing.Optional[chitose.com.atproto.admin.defs.StatusAttr]=None) -> bytes:
        """Update the service-specific admin status of a subject (account, record, or blob)."""
        return _update_subject_status(self.call, subject, takedown, deactivated)

    def update_account_handle(self, did: str, handle: str) -> bytes:
        """Administrative action to update an account's handle."""
        return _update_account_handle(self.call, did, handle)

    def delete_account(self, did: str) -> bytes:
        """Delete a user account as an administrator."""
        return _delete_account(self.call, did)

    def get_subject_status(self, did: typing.Optional[str]=None, uri: typing.Optional[str]=None, blob: typing.Optional[str]=None) -> bytes:
        """Get the service-specific admin status of a subject (account, record, or blob)."""
        return _get_subject_status(self.call, did, uri, blob)

    def send_email(self, recipient_did: str, content: str, sender_did: str, subject: typing.Optional[str]=None, comment: typing.Optional[str]=None) -> bytes:
        """Send email to a user's account email address.


        :param comment: Additional comment by the sender that won't be used in the email itself but helpful to provide more context for moderators/reviewers
        """
        return _send_email(self.call, recipient_did, content, sender_did, subject, comment)

    def enable_account_invites(self, account: str, note: typing.Optional[str]=None) -> bytes:
        """Re-enable an account's ability to receive invite codes.


        :param note: Optional reason for enabled invites.
        """
        return _enable_account_invites(self.call, account, note)

    def update_account_password(self, did: str, password: str) -> bytes:
        """Update the password for a user account as an administrator."""
        return _update_account_password(self.call, did, password)

    def get_account_info(self, did: str) -> bytes:
        """Get details about an account."""
        return _get_account_info(self.call, did)