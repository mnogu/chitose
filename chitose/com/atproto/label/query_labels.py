# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _query_labels(service: str, headers: dict[str, str], uri_patterns: list[str], sources: typing.Optional[list[str]]=None, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
    """Find labels relevant to the provided URI patterns.


    :param uri_patterns: List of AT URI patterns to match (boolean 'OR'). Each may be a prefix (ending with '*'; will match inclusive of the string leading to '*'), or a full URI

    :param sources: Optional list of label sources (DIDs) to filter on
    """
    return chitose.xrpc.call('com.atproto.label.queryLabels', [('uriPatterns', uri_patterns), ('sources', sources), ('limit', limit), ('cursor', cursor)], None, service, {} | headers)