# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _get_profiles(call: chitose.xrpc.XrpcCallable, actors: list[str]) -> bytes:
    """"""
    return call('app.bsky.actor.getProfiles', [('actors', actors)], None, {})