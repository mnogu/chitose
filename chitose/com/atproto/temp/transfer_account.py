# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _transfer_account(call: chitose.xrpc.XrpcCall, handle: str, did: str, plc_op: typing.Any) -> bytes:
    """Transfer an account. NOTE: temporary method, necessarily how account migration will be implemented."""
    return call('com.atproto.temp.transferAccount', [], {'handle': handle, 'did': did, 'plcOp': plc_op}, {'Content-Type': 'application/json'})