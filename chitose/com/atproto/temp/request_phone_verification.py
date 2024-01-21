# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _request_phone_verification(call: chitose.xrpc.XrpcCall, phone_number: str) -> bytes:
    """Request a verification code to be sent to the supplied phone number"""
    return call('com.atproto.temp.requestPhoneVerification', [], {'phoneNumber': phone_number}, {'Content-Type': 'application/json'})