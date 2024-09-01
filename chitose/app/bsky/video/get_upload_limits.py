# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _get_upload_limits(call: chitose.xrpc.XrpcCall) -> bytes:
    """Get video upload limits for the authenticated user."""
    return call('app.bsky.video.getUploadLimits', [], None, {})