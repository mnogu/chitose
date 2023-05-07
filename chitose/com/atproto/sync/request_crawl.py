# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _request_crawl(service: str, headers: dict[str, str], hostname: str) -> bytes:
    """Request a service to persistently crawl hosted repos.


    :param hostname: Hostname of the service that is requesting to be crawled.
    """
    return chitose.xrpc.call('com.atproto.sync.requestCrawl', [('hostname', hostname)], None, service, {} | headers)