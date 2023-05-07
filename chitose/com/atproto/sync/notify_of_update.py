# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _notify_of_update(service: str, headers: dict[str, str], hostname: str) -> bytes:
    """Notify a crawling service of a recent update. Often when a long break between updates causes the connection with the crawling service to break.


    :param hostname: Hostname of the service that is notifying of update.
    """
    return chitose.xrpc.call('com.atproto.sync.notifyOfUpdate', [('hostname', hostname)], None, service, {} | headers)