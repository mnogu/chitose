# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _request_plc_operation_signature(call: chitose.xrpc.XrpcCall) -> bytes:
    """Request an email with a code to in order to request a signed PLC operation. Requires Auth."""
    return call('com.atproto.identity.requestPlcOperationSignature', [], {}, {})