# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _get_records(call: chitose.xrpc.XrpcCall, uris: list[str]) -> bytes:
    """Get details about some records."""
    return call('tools.ozone.moderation.getRecords', [('uris', uris)], None, {})