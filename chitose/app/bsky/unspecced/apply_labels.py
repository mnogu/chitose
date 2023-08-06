# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import chitose.com.atproto.label.defs

def _apply_labels(call: chitose.xrpc.XrpcCall, labels: list[chitose.com.atproto.label.defs.Label]) -> bytes:
    """Allow a labeler to apply labels directly."""
    return call('app.bsky.unspecced.applyLabels', [], {'labels': labels}, {'Content-Type': 'application/json'})