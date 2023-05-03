# GENERATED CODE - DO NOT MODIFY
from __future__ import annotations
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
from .request_password_reset import _request_password_reset
from .reset_password import _reset_password
from .revoke_app_password import _revoke_app_password
from .create_account import *
from .create_app_password import *
from .create_invite_code import *
from .create_invite_codes import *
from .create_session import *
from .defs import *
from .delete_account import *
from .delete_session import *
from .describe_server import *
from .get_account_invite_codes import *
from .get_session import *
from .list_app_passwords import *
from .refresh_session import *
from .request_account_delete import *
from .request_password_reset import *
from .reset_password import *
from .revoke_app_password import *

class Server:

    def __init__(self, service: str, headers: dict[str, str]):
        self.service = service
        self.headers = headers

    def get_account_invite_codes(self, include_used: typing.Optional[str]=None, create_available: typing.Optional[str]=None):
        return _get_account_invite_codes(self.service, self.headers, include_used, create_available)

    def create_session(self, identifier: str, password: str):
        return _create_session(self.service, self.headers, identifier, password)

    def list_app_passwords(self):
        return _list_app_passwords(self.service, self.headers)

    def create_invite_codes(self, code_count: int, use_count: int, for_accounts: typing.Optional[list[str]]=None):
        return _create_invite_codes(self.service, self.headers, code_count, use_count, for_accounts)

    def delete_session(self):
        return _delete_session(self.service, self.headers)

    def revoke_app_password(self, name: str):
        return _revoke_app_password(self.service, self.headers, name)

    def create_app_password(self, name: str):
        return _create_app_password(self.service, self.headers, name)

    def describe_server(self):
        return _describe_server(self.service, self.headers)

    def get_session(self):
        return _get_session(self.service, self.headers)

    def refresh_session(self):
        return _refresh_session(self.service, self.headers)

    def reset_password(self, token: str, password: str):
        return _reset_password(self.service, self.headers, token, password)

    def request_password_reset(self, email: str):
        return _request_password_reset(self.service, self.headers, email)

    def request_account_delete(self):
        return _request_account_delete(self.service, self.headers)

    def create_account(self, email: str, handle: str, password: str, invite_code: typing.Optional[str]=None, recovery_key: typing.Optional[str]=None):
        return _create_account(self.service, self.headers, email, handle, password, invite_code, recovery_key)

    def delete_account(self, did: str, password: str, token: str):
        return _delete_account(self.service, self.headers, did, password, token)

    def create_invite_code(self, use_count: int, for_account: typing.Optional[str]=None):
        return _create_invite_code(self.service, self.headers, use_count, for_account)