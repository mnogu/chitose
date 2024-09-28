# GENERATED CODE - DO NOT MODIFY
from __future__ import annotations
from chitose.xrpc import XrpcCall
from chitose.xrpc import XrpcSubscribe
from .get_job_status import _get_job_status
from .get_upload_limits import _get_upload_limits
from .upload_video import _upload_video

class Video_:
    """We recommend calling methods in this class via the :doc:`chitose.BskyAgent <chitose>` class instead of creating instances of this class directly."""

    def __init__(self, call: XrpcCall, subscribe: XrpcSubscribe) -> None:
        self.call = call
        self.subscribe = subscribe

    def get_job_status(self, job_id: str) -> bytes:
        """Get status details for a video processing job."""
        return _get_job_status(self.call, job_id)

    def get_upload_limits(self) -> bytes:
        """Get video upload limits for the authenticated user."""
        return _get_upload_limits(self.call)

    def upload_video(self, input_: bytes) -> bytes:
        """Upload a video to be processed then stored on the PDS."""
        return _upload_video(self.call, input_)