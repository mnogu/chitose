# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _request_crawl(call: chitose.xrpc.XrpcCallable, hostname: str) -> bytes:
    """Request a service to persistently crawl hosted repos.


    :param hostname: Hostname of the service that is requesting to be crawled.
    """
    return call('com.atproto.sync.requestCrawl', [('hostname', hostname)], None, {})