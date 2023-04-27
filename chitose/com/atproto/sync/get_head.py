from __future__ import annotations
import chitose

def get_head(service: str, headers: dict[str, str], did: str):
    """Gets the current HEAD CID of a repo."""
    return chitose.xrpc.call('com.atproto.sync.getHead', [('did', did)], None, service, {} | headers)