# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _confirm_email(call: chitose.xrpc.XrpcCall, email: str, token: str) -> bytes:
    """Confirm an email using a token from com.atproto.server.requestEmailConfirmation."""
    return call('com.atproto.server.confirmEmail', [], {'email': email, 'token': token}, {'Content-Type': 'application/json'})