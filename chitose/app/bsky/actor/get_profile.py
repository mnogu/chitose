# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _get_profile(service: str, headers: dict[str, str], actor: str) -> bytes:
    """"""
    return chitose.xrpc.call('app.bsky.actor.getProfile', [('actor', actor)], None, service, {} | headers)