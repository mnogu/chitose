# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import chitose.app.bsky.actor.defs

def _put_preferences(service: str, headers: dict[str, str], preferences: chitose.app.bsky.actor.defs.Preferences) -> bytes:
    """Sets the private preferences attached to the account."""
    return chitose.xrpc.call('app.bsky.actor.putPreferences', [], {'preferences': preferences}, service, {'Content-Type': 'application/json'} | headers)