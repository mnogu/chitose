# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import chitose.com.atproto.admin.defs
import chitose.com.atproto.repo.strong_ref
import chitose.tools.ozone.moderation.defs
import typing

def _emit_event(call: chitose.xrpc.XrpcCall, event: typing.Union[chitose.tools.ozone.moderation.defs.ModEventTakedown, chitose.tools.ozone.moderation.defs.ModEventAcknowledge, chitose.tools.ozone.moderation.defs.ModEventEscalate, chitose.tools.ozone.moderation.defs.ModEventComment, chitose.tools.ozone.moderation.defs.ModEventLabel, chitose.tools.ozone.moderation.defs.ModEventReport, chitose.tools.ozone.moderation.defs.ModEventMute, chitose.tools.ozone.moderation.defs.ModEventUnmute, chitose.tools.ozone.moderation.defs.ModEventMuteReporter, chitose.tools.ozone.moderation.defs.ModEventUnmuteReporter, chitose.tools.ozone.moderation.defs.ModEventReverseTakedown, chitose.tools.ozone.moderation.defs.ModEventEmail, chitose.tools.ozone.moderation.defs.ModEventTag], subject: typing.Union[chitose.com.atproto.admin.defs.RepoRef, chitose.com.atproto.repo.strong_ref.StrongRef], created_by: str, subject_blob_cids: typing.Optional[list[str]]=None) -> bytes:
    """Take a moderation action on an actor."""
    return call('tools.ozone.moderation.emitEvent', [], {'event': event, 'subject': subject, 'subjectBlobCids': subject_blob_cids, 'createdBy': created_by}, {'Content-Type': 'application/json'})