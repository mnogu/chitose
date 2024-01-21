# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _delete_communication_template(call: chitose.xrpc.XrpcCall, id: str) -> bytes:
    """Delete a communication template."""
    return call('com.atproto.admin.deleteCommunicationTemplate', [], {'id': id}, {'Content-Type': 'application/json'})