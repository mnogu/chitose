# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _list_templates(call: chitose.xrpc.XrpcCall) -> bytes:
    """Get list of all communication templates."""
    return call('tools.ozone.communication.listTemplates', [], None, {})