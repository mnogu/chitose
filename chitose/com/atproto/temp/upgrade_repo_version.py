# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _upgrade_repo_version(call: chitose.xrpc.XrpcCall, did: str, force: typing.Optional[bool]=None) -> bytes:
    """Upgrade a repo to v3"""
    return call('com.atproto.temp.upgradeRepoVersion', [], {'did': did, 'force': force}, {'Content-Type': 'application/json'})