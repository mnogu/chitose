# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

class JobStatus(chitose.Object):
    """


    :param state: The state of the video processing job. All values not listed as a known value indicate that the job is in process.

    :param progress: Progress within the current processing state.
    """

    def __init__(self, job_id: str, did: str, state: typing.Literal['JOB_STATE_COMPLETED', 'JOB_STATE_FAILED'], progress: typing.Optional[int]=None, blob: typing.Optional[chitose.Blob]=None, error: typing.Optional[str]=None, message: typing.Optional[str]=None) -> None:
        self.job_id = job_id
        self.did = did
        self.state = state
        self.progress = progress
        self.blob = blob
        self.error = error
        self.message = message

    def to_dict(self) -> dict[str, typing.Any]:
        return {'jobId': self.job_id, 'did': self.did, 'state': self.state, 'progress': self.progress, 'blob': self.blob, 'error': self.error, 'message': self.message, '$type': 'app.bsky.video.defs#jobStatus'}