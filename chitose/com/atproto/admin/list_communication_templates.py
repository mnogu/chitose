# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _list_communication_templates(call: chitose.xrpc.XrpcCall) -> bytes:
    """Get list of all communication templates."""
    return call('com.atproto.admin.listCommunicationTemplates', [], None, {})