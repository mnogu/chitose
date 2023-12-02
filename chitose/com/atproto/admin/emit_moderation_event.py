# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import chitose.com.atproto.admin.defs
import chitose.com.atproto.repo.strong_ref
import typing

def _emit_moderation_event(call: chitose.xrpc.XrpcCall, event: typing.Union[chitose.com.atproto.admin.defs.ModEventTakedown, chitose.com.atproto.admin.defs.ModEventAcknowledge, chitose.com.atproto.admin.defs.ModEventEscalate, chitose.com.atproto.admin.defs.ModEventComment, chitose.com.atproto.admin.defs.ModEventLabel, chitose.com.atproto.admin.defs.ModEventReport, chitose.com.atproto.admin.defs.ModEventMute, chitose.com.atproto.admin.defs.ModEventReverseTakedown, chitose.com.atproto.admin.defs.ModEventUnmute, chitose.com.atproto.admin.defs.ModEventEmail], subject: typing.Union[chitose.com.atproto.admin.defs.RepoRef, chitose.com.atproto.repo.strong_ref.StrongRef], created_by: str, subject_blob_cids: typing.Optional[list[str]]=None) -> bytes:
    """Take a moderation action on an actor."""
    return call('com.atproto.admin.emitModerationEvent', [], {'event': event, 'subject': subject, 'subjectBlobCids': subject_blob_cids, 'createdBy': created_by}, {'Content-Type': 'application/json'})