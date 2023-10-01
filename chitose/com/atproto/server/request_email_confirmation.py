# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _request_email_confirmation(call: chitose.xrpc.XrpcCall) -> bytes:
    """Request an email with a code to confirm ownership of email"""
    return call('com.atproto.server.requestEmailConfirmation', [], {}, {})