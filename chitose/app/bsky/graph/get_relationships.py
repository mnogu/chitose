# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _get_relationships(call: chitose.xrpc.XrpcCall, actor: str, others: typing.Optional[list[str]]=None) -> bytes:
    """Enumerates public relationships between one account, and a list of other accounts"""
    return call('app.bsky.graph.getRelationships', [('actor', actor), ('others', others)], None, {})