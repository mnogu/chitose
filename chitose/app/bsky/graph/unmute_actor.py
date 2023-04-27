from __future__ import annotations
import chitose

def unmute_actor(service: str, headers: dict[str, str], actor: str):
    """Unmute an actor by did or handle."""
    return chitose.xrpc.call('app.bsky.graph.unmuteActor', [], {'actor': actor}, service, {'Content-Type': 'application/json'} | headers)