# GENERATED CODE - DO NOT MODIFY
from __future__ import annotations
import chitose

def _request_crawl(service: str, headers: dict[str, str], hostname: str):
    """Request a service to persistently crawl hosted repos."""
    return chitose.xrpc.call('com.atproto.sync.requestCrawl', [('hostname', hostname)], None, service, {} | headers)