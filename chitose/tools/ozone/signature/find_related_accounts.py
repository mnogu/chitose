# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import chitose.com.atproto.admin.defs
import chitose.tools.ozone.signature.defs
import typing

def _find_related_accounts(call: chitose.xrpc.XrpcCall, did: str, cursor: typing.Optional[str]=None, limit: typing.Optional[int]=None) -> bytes:
    """Get accounts that share some matching threat signatures with the root account."""
    return call('tools.ozone.signature.findRelatedAccounts', [('did', did), ('cursor', cursor), ('limit', limit)], None, {})

class RelatedAccount(chitose.Object):
    """"""

    def __init__(self, account: chitose.com.atproto.admin.defs.AccountView, similarities: typing.Optional[list[chitose.tools.ozone.signature.defs.SigDetail]]=None) -> None:
        self.account = account
        self.similarities = similarities

    def to_dict(self) -> dict[str, typing.Any]:
        return {'account': self.account, 'similarities': self.similarities, '$type': 'tools.ozone.signature.findRelatedAccounts#relatedAccount'}