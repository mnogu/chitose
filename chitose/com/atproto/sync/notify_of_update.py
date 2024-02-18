# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _notify_of_update(call: chitose.xrpc.XrpcCall, hostname: str) -> bytes:
    """Notify a crawling service of a recent update, and that crawling should resume. Intended use is after a gap between repo stream events caused the crawling service to disconnect. Does not require auth; implemented by Relay.


    :param hostname: Hostname of the current service (usually a PDS) that is notifying of update.
    """
    return call('com.atproto.sync.notifyOfUpdate', [], {'hostname': hostname}, {'Content-Type': 'application/json'})