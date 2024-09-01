# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _upload_video(call: chitose.xrpc.XrpcCall, input_: bytes) -> bytes:
    """Upload a video to be processed then stored on the PDS."""
    return call('app.bsky.video.uploadVideo', [], input_, {'Content-Type': 'video/mp4'})