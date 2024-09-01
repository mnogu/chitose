# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _get_job_status(call: chitose.xrpc.XrpcCall, job_id: str) -> bytes:
    """Get status details for a video processing job."""
    return call('app.bsky.video.getJobStatus', [('jobId', job_id)], None, {})