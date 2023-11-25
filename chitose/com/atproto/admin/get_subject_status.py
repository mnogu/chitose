# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _get_subject_status(call: chitose.xrpc.XrpcCall, did: typing.Optional[str]=None, uri: typing.Optional[str]=None, blob: typing.Optional[str]=None) -> bytes:
    """Get the service-specific admin status of a subject (account, record, or blob)."""
    return call('com.atproto.admin.getSubjectStatus', [('did', did), ('uri', uri), ('blob', blob)], None, {})