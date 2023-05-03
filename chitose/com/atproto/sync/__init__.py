# GENERATED CODE - DO NOT MODIFY
from __future__ import annotations
from .get_blob import _get_blob
from .get_blocks import _get_blocks
from .get_checkout import _get_checkout
from .get_commit_path import _get_commit_path
from .get_head import _get_head
from .get_record import _get_record
from .get_repo import _get_repo
from .list_blobs import _list_blobs
from .list_repos import _list_repos
from .notify_of_update import _notify_of_update
from .request_crawl import _request_crawl
from .get_blob import *
from .get_blocks import *
from .get_checkout import *
from .get_commit_path import *
from .get_head import *
from .get_record import *
from .get_repo import *
from .list_blobs import *
from .list_repos import *
from .notify_of_update import *
from .request_crawl import *
from .subscribe_repos import *

class _Sync:

    def __init__(self, service: str, headers: dict[str, str]):
        self.service = service
        self.headers = headers

    def get_head(self, did: str):
        return _get_head(self.service, self.headers, did)

    def get_blob(self, did: str, cid: str):
        return _get_blob(self.service, self.headers, did, cid)

    def get_repo(self, did: str, earliest: typing.Optional[str]=None, latest: typing.Optional[str]=None):
        return _get_repo(self.service, self.headers, did, earliest, latest)

    def notify_of_update(self, hostname: str):
        return _notify_of_update(self.service, self.headers, hostname)

    def request_crawl(self, hostname: str):
        return _request_crawl(self.service, self.headers, hostname)

    def list_blobs(self, did: str, latest: typing.Optional[str]=None, earliest: typing.Optional[str]=None):
        return _list_blobs(self.service, self.headers, did, latest, earliest)

    def get_record(self, did: str, collection: str, rkey: str, commit: typing.Optional[str]=None):
        return _get_record(self.service, self.headers, did, collection, rkey, commit)

    def list_repos(self, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None):
        return _list_repos(self.service, self.headers, limit, cursor)

    def get_commit_path(self, did: str, latest: typing.Optional[str]=None, earliest: typing.Optional[str]=None):
        return _get_commit_path(self.service, self.headers, did, latest, earliest)

    def get_blocks(self, did: str, cids: list[str]):
        return _get_blocks(self.service, self.headers, did, cids)

    def get_checkout(self, did: str, commit: typing.Optional[str]=None):
        return _get_checkout(self.service, self.headers, did, commit)