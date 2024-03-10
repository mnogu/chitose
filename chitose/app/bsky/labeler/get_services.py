# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _get_services(call: chitose.xrpc.XrpcCall, dids: list[str], detailed: typing.Optional[bool]=None) -> bytes:
    """Get information about a list of labeler services."""
    return call('app.bsky.labeler.getServices', [('dids', dids), ('detailed', detailed)], None, {})