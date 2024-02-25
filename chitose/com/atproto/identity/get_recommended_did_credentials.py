# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _get_recommended_did_credentials(call: chitose.xrpc.XrpcCall) -> bytes:
    """Describe the credentials that should be included in the DID doc of an account that is migrating to this service."""
    return call('com.atproto.identity.getRecommendedDidCredentials', [], None, {})