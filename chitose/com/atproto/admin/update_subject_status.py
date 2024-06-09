# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import chitose.com.atproto.admin.defs
import chitose.com.atproto.repo.strong_ref
import typing

def _update_subject_status(call: chitose.xrpc.XrpcCall, subject: typing.Union[chitose.com.atproto.admin.defs.RepoRef, chitose.com.atproto.repo.strong_ref.StrongRef, chitose.com.atproto.admin.defs.RepoBlobRef], takedown: typing.Optional[chitose.com.atproto.admin.defs.StatusAttr]=None, deactivated: typing.Optional[chitose.com.atproto.admin.defs.StatusAttr]=None) -> bytes:
    """Update the service-specific admin status of a subject (account, record, or blob)."""
    return call('com.atproto.admin.updateSubjectStatus', [], {'subject': subject, 'takedown': takedown, 'deactivated': deactivated}, {'Content-Type': 'application/json'})