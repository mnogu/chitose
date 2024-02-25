# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _deactivate_account(call: chitose.xrpc.XrpcCall, delete_after: typing.Optional[str]=None) -> bytes:
    """Deactivates a currently active account. Stops serving of repo, and future writes to repo until reactivated. Used to finalize account migration with the old host after the account has been activated on the new host.


    :param delete_after: A recommendation to server as to how long they should hold onto the deactivated account before deleting.
    """
    return call('com.atproto.server.deactivateAccount', [], {'deleteAfter': delete_after}, {'Content-Type': 'application/json'})