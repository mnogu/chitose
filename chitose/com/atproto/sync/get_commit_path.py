from __future__ import annotations
import chitose
import typing

def get_commit_path(service: str, headers: dict[str, str], did: str, latest: typing.Optional[str]=None, earliest: typing.Optional[str]=None):
    """Gets the path of repo commits"""
    return chitose.xrpc.call('com.atproto.sync.getCommitPath', [('did', did), ('latest', latest), ('earliest', earliest)], None, service, {} | headers)