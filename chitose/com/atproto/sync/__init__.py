# GENERATED CODE - DO NOT MODIFY
from __future__ import annotations
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
import chitose
import typing

class Sync:

    def __init__(self, service: str, headers: dict[str, str]):
        self.service = service
        self.headers = headers

    def get_head(self, did: str):
        return get_head(self.service, self.headers, did)

    def get_blob(self, did: str, cid: str):
        return get_blob(self.service, self.headers, did, cid)

    def get_repo(self, did: str, earliest: typing.Optional[str], latest: typing.Optional[str]):
        return get_repo(self.service, self.headers, did, earliest, latest)

    def notify_of_update(self, hostname: str):
        return notify_of_update(self.service, self.headers, hostname)

    def request_crawl(self, hostname: str):
        return request_crawl(self.service, self.headers, hostname)

    def list_blobs(self, did: str, latest: typing.Optional[str], earliest: typing.Optional[str]):
        return list_blobs(self.service, self.headers, did, latest, earliest)

    def get_record(self, did: str, collection: str, rkey: str, commit: typing.Optional[str]):
        return get_record(self.service, self.headers, did, collection, rkey, commit)

    def list_repos(self, limit: typing.Optional[int], cursor: typing.Optional[str]):
        return list_repos(self.service, self.headers, limit, cursor)

    def get_commit_path(self, did: str, latest: typing.Optional[str], earliest: typing.Optional[str]):
        return get_commit_path(self.service, self.headers, did, latest, earliest)

    def get_blocks(self, did: str, cids: list[str]):
        return get_blocks(self.service, self.headers, did, cids)

    def get_checkout(self, did: str, commit: typing.Optional[str]):
        return get_checkout(self.service, self.headers, did, commit)