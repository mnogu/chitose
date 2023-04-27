from __future__ import annotations
import chitose
import typing

def query_labels(service: str, headers: dict[str, str], uri_patterns: list[str], sources: typing.Optional[list[str]]=None, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None):
    """Find labels relevant to the provided URI patterns."""
    return chitose.xrpc.call('com.atproto.label.queryLabels', [('uriPatterns', uri_patterns), ('sources', sources), ('limit', limit), ('cursor', cursor)], None, service, {} | headers)