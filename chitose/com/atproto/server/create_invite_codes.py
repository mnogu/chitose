# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _create_invite_codes(service: str, headers: dict[str, str], code_count: int, use_count: int, for_accounts: typing.Optional[list[str]]=None) -> bytes:
    """Create an invite code."""
    return chitose.xrpc.call('com.atproto.server.createInviteCodes', [], {'codeCount': code_count, 'useCount': use_count, 'forAccounts': for_accounts}, service, {'Content-Type': 'application/json'} | headers)

class AccountCodes(chitose.Object):
    """"""

    def __init__(self, account: str, codes: list[str]) -> None:
        self.account = account
        self.codes = codes

    def to_dict(self) -> dict:
        return {'account': self.account, 'codes': self.codes, '$type': 'com.atproto.server.createInviteCodes#accountCodes'}