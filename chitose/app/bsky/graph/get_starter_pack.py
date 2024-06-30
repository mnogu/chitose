# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _get_starter_pack(call: chitose.xrpc.XrpcCall, starter_pack: str) -> bytes:
    """Gets a view of a starter pack.


    :param starter_pack: Reference (AT-URI) of the starter pack record.
    """
    return call('app.bsky.graph.getStarterPack', [('starterPack', starter_pack)], None, {})