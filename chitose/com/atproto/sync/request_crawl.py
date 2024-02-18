# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _request_crawl(call: chitose.xrpc.XrpcCall, hostname: str) -> bytes:
    """Request a service to persistently crawl hosted repos. Expected use is new PDS instances declaring their existence to Relays. Does not require auth.


    :param hostname: Hostname of the current service (eg, PDS) that is requesting to be crawled.
    """
    return call('com.atproto.sync.requestCrawl', [], {'hostname': hostname}, {'Content-Type': 'application/json'})