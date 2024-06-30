# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _get_starter_packs(call: chitose.xrpc.XrpcCall, uris: list[str]) -> bytes:
    """Get views for a list of starter packs."""
    return call('app.bsky.graph.getStarterPacks', [('uris', uris)], None, {})