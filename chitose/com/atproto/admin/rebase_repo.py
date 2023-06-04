# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _rebase_repo(call: chitose.xrpc.XrpcCall, repo: str, swap_commit: typing.Optional[str]=None) -> bytes:
    """Administrative action to rebase an account's repo


    :param repo: The handle or DID of the repo.

    :param swap_commit: Compare and swap with the previous commit by cid.
    """
    return call('com.atproto.admin.rebaseRepo', [], {'repo': repo, 'swapCommit': swap_commit}, {'Content-Type': 'application/json'})