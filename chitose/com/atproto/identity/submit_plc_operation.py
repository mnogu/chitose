# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _submit_plc_operation(call: chitose.xrpc.XrpcCall, operation: typing.Any) -> bytes:
    """Validates a PLC operation to ensure that it doesn't violate a service's constraints or get the identity into a bad state, then submits it to the PLC registry"""
    return call('com.atproto.identity.submitPlcOperation', [], {'operation': operation}, {'Content-Type': 'application/json'})