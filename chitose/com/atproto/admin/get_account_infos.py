# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _get_account_infos(call: chitose.xrpc.XrpcCall, dids: list[str]) -> bytes:
    """Get details about some accounts."""
    return call('com.atproto.admin.getAccountInfos', [('dids', dids)], None, {})