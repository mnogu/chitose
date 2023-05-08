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
import chitose
import typing

class Repo_:
    """We recommend calling methods in this class via the `chitose.BskyAgent` class instead of creating instances of this class directly."""

    def __init__(self, service: str, headers: dict[str, str]) -> None:
        self.service = service
        self.headers = headers

    def create_record(self, repo: str, collection: str, record: typing.Any, rkey: typing.Optional[str]=None, validate: typing.Optional[str]=None, swap_commit: typing.Optional[str]=None) -> bytes:
        """Create a new record.


        :param repo: The handle or DID of the repo.

        :param collection: The NSID of the record collection.

        :param record: The record to create.

        :param rkey: The key of the record.

        :param validate: Validate the record?

        :param swap_commit: Compare and swap with the previous commit by cid.
        """
        return _create_record(self.service, self.headers, repo, collection, record, rkey, validate, swap_commit)

    def delete_record(self, repo: str, collection: str, rkey: str, swap_record: typing.Optional[str]=None, swap_commit: typing.Optional[str]=None) -> bytes:
        """Delete a record, or ensure it doesn't exist.


        :param repo: The handle or DID of the repo.

        :param collection: The NSID of the record collection.

        :param rkey: The key of the record.

        :param swap_record: Compare and swap with the previous record by cid.

        :param swap_commit: Compare and swap with the previous commit by cid.
        """
        return _delete_record(self.service, self.headers, repo, collection, rkey, swap_record, swap_commit)

    def put_record(self, repo: str, collection: str, rkey: str, record: typing.Any, validate: typing.Optional[str]=None, swap_record: typing.Optional[str]=None, swap_commit: typing.Optional[str]=None) -> bytes:
        """Write a record, creating or updating it as needed.


        :param repo: The handle or DID of the repo.

        :param collection: The NSID of the record collection.

        :param rkey: The key of the record.

        :param record: The record to write.

        :param validate: Validate the record?

        :param swap_record: Compare and swap with the previous record by cid.

        :param swap_commit: Compare and swap with the previous commit by cid.
        """
        return _put_record(self.service, self.headers, repo, collection, rkey, record, validate, swap_record, swap_commit)

    def upload_blob(self, input_: bytes) -> bytes:
        """Upload a new blob to be added to repo in a later request."""
        return _upload_blob(self.service, self.headers, input_)

    def describe_repo(self, repo: str) -> bytes:
        """Get information about the repo, including the list of collections.


        :param repo: The handle or DID of the repo.
        """
        return _describe_repo(self.service, self.headers, repo)

    def get_record(self, repo: str, collection: str, rkey: str, cid: typing.Optional[str]=None) -> bytes:
        """Get a record.


        :param repo: The handle or DID of the repo.

        :param collection: The NSID of the record collection.

        :param rkey: The key of the record.

        :param cid: The CID of the version of the record. If not specified, then return the most recent version.
        """
        return _get_record(self.service, self.headers, repo, collection, rkey, cid)

    def apply_writes(self, repo: str, writes: list[typing.Union[chitose.com.atproto.repo.apply_writes.Create, chitose.com.atproto.repo.apply_writes.Update, chitose.com.atproto.repo.apply_writes.Delete]], validate: typing.Optional[str]=None, swap_commit: typing.Optional[str]=None) -> bytes:
        """Apply a batch transaction of creates, updates, and deletes.


        :param repo: The handle or DID of the repo.

        :param validate: Validate the records?
        """
        return _apply_writes(self.service, self.headers, repo, writes, validate, swap_commit)

    def list_records(self, repo: str, collection: str, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None, rkey_start: typing.Optional[str]=None, rkey_end: typing.Optional[str]=None, reverse: typing.Optional[str]=None) -> bytes:
        """List a range of records in a collection.


        :param repo: The handle or DID of the repo.

        :param collection: The NSID of the record type.

        :param limit: The number of records to return.

        :param rkey_start: DEPRECATED: The lowest sort-ordered rkey to start from (exclusive)

        :param rkey_end: DEPRECATED: The highest sort-ordered rkey to stop at (exclusive)

        :param reverse: Reverse the order of the returned records?
        """
        return _list_records(self.service, self.headers, repo, collection, limit, cursor, rkey_start, rkey_end, reverse)