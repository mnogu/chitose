# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _get_profiles(service: str, headers: dict[str, str], actors: list[str]) -> bytes:
    """"""
    return chitose.xrpc.call('app.bsky.actor.getProfiles', [('actors', actors)], None, service, {} | headers)