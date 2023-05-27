# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _get_reposted_by(call: chitose.xrpc.XrpcCallable, uri: str, cid: typing.Optional[str]=None, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
    """"""
    return call('app.bsky.feed.getRepostedBy', [('uri', uri), ('cid', cid), ('limit', limit), ('cursor', cursor)], None, {})