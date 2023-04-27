from __future__ import annotations
import chitose

def get_session(service: str, headers: dict[str, str]):
    """Get information about the current session."""
    return chitose.xrpc.call('com.atproto.server.getSession', [], None, service, {} | headers)