# GENERATED CODE - DO NOT MODIFY
from __future__ import annotations
import chitose

def get_blocks(service: str, headers: dict[str, str], did: str, cids: list[str]):
    """Gets blocks from a given repo."""
    return chitose.xrpc.call('com.atproto.sync.getBlocks', [('did', did), ('cids', cids)], None, service, {} | headers)