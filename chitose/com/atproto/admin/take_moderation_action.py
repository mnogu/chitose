# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import chitose.com.atproto.admin.defs
import chitose.com.atproto.repo.strong_ref
import typing

def _take_moderation_action(call: chitose.xrpc.XrpcCallable, action: typing.Literal['com.atproto.admin.defs#takedown', 'com.atproto.admin.defs#flag', 'com.atproto.admin.defs#acknowledge'], subject: typing.Union[chitose.com.atproto.admin.defs.RepoRef, chitose.com.atproto.repo.strong_ref.StrongRef], reason: str, created_by: str, subject_blob_cids: typing.Optional[list[str]]=None, create_label_vals: typing.Optional[list[str]]=None, negate_label_vals: typing.Optional[list[str]]=None) -> bytes:
    """Take a moderation action on a repo."""
    return call('com.atproto.admin.takeModerationAction', [], {'action': action, 'subject': subject, 'subjectBlobCids': subject_blob_cids, 'createLabelVals': create_label_vals, 'negateLabelVals': negate_label_vals, 'reason': reason, 'createdBy': created_by}, {'Content-Type': 'application/json'})