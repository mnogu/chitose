from __future__ import annotations
import chitose

def get_posts(service: str, headers: dict[str, str], uris: list[str]):
    """A view of an actor's feed."""
    return chitose.xrpc.call('app.bsky.feed.getPosts', [('uris', uris)], None, service, {} | headers)