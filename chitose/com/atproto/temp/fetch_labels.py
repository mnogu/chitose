# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _fetch_labels(call: chitose.xrpc.XrpcCall, since: typing.Optional[int]=None, limit: typing.Optional[int]=None) -> bytes:
    """DEPRECATED: use queryLabels or subscribeLabels instead -- Fetch all labels from a labeler created after a certain date."""
    return call('com.atproto.temp.fetchLabels', [('since', since), ('limit', limit)], None, {})