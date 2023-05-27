# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _rebase_repo(call: chitose.xrpc.XrpcCallable, repo: str, swap_commit: typing.Optional[str]=None) -> bytes:
    """Simple rebase of repo that deletes history


    :param repo: The handle or DID of the repo.

    :param swap_commit: Compare and swap with the previous commit by cid.
    """
    return call('com.atproto.repo.rebaseRepo', [], {'repo': repo, 'swapCommit': swap_commit}, {'Content-Type': 'application/json'})