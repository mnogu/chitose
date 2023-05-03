# GENERATED CODE - DO NOT MODIFY
from __future__ import annotations
from .apply_writes import _apply_writes
from .create_record import _create_record
from .delete_record import _delete_record
from .describe_repo import _describe_repo
from .get_record import _get_record
from .list_records import _list_records
from .put_record import _put_record
from .upload_blob import _upload_blob
from .apply_writes import *
from .create_record import *
from .delete_record import *
from .describe_repo import *
from .get_record import *
from .list_records import *
from .put_record import *
from .strong_ref import *
from .upload_blob import *

class _Repo:

    def __init__(self, service: str, headers: dict[str, str]):
        self.service = service
        self.headers = headers

    def create_record(self, repo: str, collection: str, record: typing.Any, rkey: typing.Optional[str]=None, validate: typing.Optional[str]=None, swap_commit: typing.Optional[str]=None):
        return _create_record(self.service, self.headers, repo, collection, record, rkey, validate, swap_commit)

    def delete_record(self, repo: str, collection: str, rkey: str, swap_record: typing.Optional[str]=None, swap_commit: typing.Optional[str]=None):
        return _delete_record(self.service, self.headers, repo, collection, rkey, swap_record, swap_commit)

    def put_record(self, repo: str, collection: str, rkey: str, record: typing.Any, validate: typing.Optional[str]=None, swap_record: typing.Optional[str]=None, swap_commit: typing.Optional[str]=None):
        return _put_record(self.service, self.headers, repo, collection, rkey, record, validate, swap_record, swap_commit)

    def upload_blob(self):
        return _upload_blob(self.service, self.headers)

    def describe_repo(self, repo: str):
        return _describe_repo(self.service, self.headers, repo)

    def get_record(self, repo: str, collection: str, rkey: str, cid: typing.Optional[str]=None):
        return _get_record(self.service, self.headers, repo, collection, rkey, cid)

    def apply_writes(self, repo: str, writes: list[typing.Union[Create, Update, Delete]], validate: typing.Optional[str]=None, swap_commit: typing.Optional[str]=None):
        return _apply_writes(self.service, self.headers, repo, writes, validate, swap_commit)

    def list_records(self, repo: str, collection: str, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None, rkey_start: typing.Optional[str]=None, rkey_end: typing.Optional[str]=None, reverse: typing.Optional[str]=None):
        return _list_records(self.service, self.headers, repo, collection, limit, cursor, rkey_start, rkey_end, reverse)