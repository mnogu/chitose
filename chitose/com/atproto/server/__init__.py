# GENERATED CODE - DO NOT MODIFY
from __future__ import annotations
from chitose.xrpc import XrpcCall
from chitose.xrpc import XrpcSubscribe
from .confirm_email import _confirm_email
from .create_account import _create_account
from .create_app_password import _create_app_password
from .create_invite_code import _create_invite_code
from .create_invite_codes import _create_invite_codes
from .create_session import _create_session
from .delete_account import _delete_account
from .delete_session import _delete_session
from .describe_server import _describe_server
from .get_account_invite_codes import _get_account_invite_codes
from .get_session import _get_session
from .list_app_passwords import _list_app_passwords
from .refresh_session import _refresh_session
from .request_account_delete import _request_account_delete
from .request_email_confirmation import _request_email_confirmation
from .request_email_update import _request_email_update
from .request_password_reset import _request_password_reset
from .reserve_signing_key import _reserve_signing_key
from .reset_password import _reset_password
from .revoke_app_password import _revoke_app_password
from .update_email import _update_email
import typing

class Server_:
    """We recommend calling methods in this class via the :doc:`chitose.BskyAgent <chitose>` class instead of creating instances of this class directly."""

    def __init__(self, call: XrpcCall, subscribe: XrpcSubscribe) -> None:
        self.call = call
        self.subscribe = subscribe

    def request_email_confirmation(self) -> bytes:
        """Request an email with a code to confirm ownership of email."""
        return _request_email_confirmation(self.call)

    def reserve_signing_key(self, did: typing.Optional[str]=None) -> bytes:
        """Reserve a repo signing key for account creation.


        :param did: The did to reserve a new did:key for
        """
        return _reserve_signing_key(self.call, did)

    def get_account_invite_codes(self, include_used: typing.Optional[bool]=None, create_available: typing.Optional[bool]=None) -> bytes:
        """Get all invite codes for a given account."""
        return _get_account_invite_codes(self.call, include_used, create_available)

    def create_session(self, identifier: str, password: str) -> bytes:
        """Create an authentication session.


        :param identifier: Handle or other identifier supported by the server for the authenticating user.
        """
        return _create_session(self.call, identifier, password)

    def list_app_passwords(self) -> bytes:
        """List all App Passwords."""
        return _list_app_passwords(self.call)

    def create_invite_codes(self, code_count: int, use_count: int, for_accounts: typing.Optional[list[str]]=None) -> bytes:
        """Create invite codes."""
        return _create_invite_codes(self.call, code_count, use_count, for_accounts)

    def delete_session(self) -> bytes:
        """Delete the current session."""
        return _delete_session(self.call)

    def revoke_app_password(self, name: str) -> bytes:
        """Revoke an App Password by name."""
        return _revoke_app_password(self.call, name)

    def create_app_password(self, name: str) -> bytes:
        """Create an App Password."""
        return _create_app_password(self.call, name)

    def describe_server(self) -> bytes:
        """Get a document describing the service's accounts configuration."""
        return _describe_server(self.call)

    def confirm_email(self, email: str, token: str) -> bytes:
        """Confirm an email using a token from com.atproto.server.requestEmailConfirmation."""
        return _confirm_email(self.call, email, token)

    def get_session(self) -> bytes:
        """Get information about the current session."""
        return _get_session(self.call)

    def refresh_session(self) -> bytes:
        """Refresh an authentication session."""
        return _refresh_session(self.call)

    def update_email(self, email: str, token: typing.Optional[str]=None) -> bytes:
        """Update an account's email.


        :param token: Requires a token from com.atproto.sever.requestEmailUpdate if the account's email has been confirmed.
        """
        return _update_email(self.call, email, token)

    def reset_password(self, token: str, password: str) -> bytes:
        """Reset a user account password using a token."""
        return _reset_password(self.call, token, password)

    def request_email_update(self) -> bytes:
        """Request a token in order to update email."""
        return _request_email_update(self.call)

    def request_password_reset(self, email: str) -> bytes:
        """Initiate a user account password reset via email."""
        return _request_password_reset(self.call, email)

    def request_account_delete(self) -> bytes:
        """Initiate a user account deletion via email."""
        return _request_account_delete(self.call)

    def create_account(self, handle: str, email: typing.Optional[str]=None, did: typing.Optional[str]=None, invite_code: typing.Optional[str]=None, verification_code: typing.Optional[str]=None, verification_phone: typing.Optional[str]=None, password: typing.Optional[str]=None, recovery_key: typing.Optional[str]=None, plc_op: typing.Optional[typing.Any]=None) -> bytes:
        """Create an account."""
        return _create_account(self.call, handle, email, did, invite_code, verification_code, verification_phone, password, recovery_key, plc_op)

    def delete_account(self, did: str, password: str, token: str) -> bytes:
        """Delete an actor's account with a token and password."""
        return _delete_account(self.call, did, password, token)

    def create_invite_code(self, use_count: int, for_account: typing.Optional[str]=None) -> bytes:
        """Create an invite code."""
        return _create_invite_code(self.call, use_count, for_account)