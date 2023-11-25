# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _send_email(call: chitose.xrpc.XrpcCall, recipient_did: str, content: str, subject: typing.Optional[str]=None) -> bytes:
    """Send email to a user's account email address."""
    return call('com.atproto.admin.sendEmail', [], {'recipientDid': recipient_did, 'content': content, 'subject': subject}, {'Content-Type': 'application/json'})