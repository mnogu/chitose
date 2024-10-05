# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _find_correlation(call: chitose.xrpc.XrpcCall, dids: list[str]) -> bytes:
    """Find all correlated threat signatures between 2 or more accounts."""
    return call('tools.ozone.signature.findCorrelation', [('dids', dids)], None, {})