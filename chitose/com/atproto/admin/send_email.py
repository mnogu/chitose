# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _send_email(call: chitose.xrpc.XrpcCall, recipient_did: str, content: str, sender_did: str, subject: typing.Optional[str]=None, comment: typing.Optional[str]=None) -> bytes:
    """Send email to a user's account email address.


    :param comment: Additional comment by the sender that won't be used in the email itself but helpful to provide more context for moderators/reviewers
    """
    return call('com.atproto.admin.sendEmail', [], {'recipientDid': recipient_did, 'content': content, 'subject': subject, 'senderDid': sender_did, 'comment': comment}, {'Content-Type': 'application/json'})