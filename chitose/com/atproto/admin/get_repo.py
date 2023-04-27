from __future__ import annotations
import chitose

def get_repo(service: str, headers: dict[str, str], did: str):
    """View details about a repository."""
    return chitose.xrpc.call('com.atproto.admin.getRepo', [('did', did)], None, service, {} | headers)