# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _get_posts(call: chitose.xrpc.XrpcCallable, uris: list[str]) -> bytes:
    """A view of an actor's feed."""
    return call('app.bsky.feed.getPosts', [('uris', uris)], None, {})