# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _delete_template(call: chitose.xrpc.XrpcCall, id: str) -> bytes:
    """Delete a communication template."""
    return call('tools.ozone.communication.deleteTemplate', [], {'id': id}, {'Content-Type': 'application/json'})