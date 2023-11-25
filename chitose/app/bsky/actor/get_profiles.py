# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _get_profiles(call: chitose.xrpc.XrpcCall, actors: list[str]) -> bytes:
    """Get detailed profile views of multiple actors."""
    return call('app.bsky.actor.getProfiles', [('actors', actors)], None, {})