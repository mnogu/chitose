from __future__ import annotations
import chitose

def get_profiles(service: str, headers: dict[str, str], actors: list[str]):
    """"""
    return chitose.xrpc.call('app.bsky.actor.getProfiles', [('actors', actors)], None, service, {} | headers)