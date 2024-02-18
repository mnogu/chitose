# GENERATED CODE - DO NOT MODIFY
from __future__ import annotations
from chitose.xrpc import XrpcCall
from chitose.xrpc import XrpcSubscribe
from .apply_writes import _apply_writes
from .create_record import _create_record
from .delete_record import _delete_record
from .describe_repo import _describe_repo
from .get_record import _get_record
from .list_records import _list_records
from .put_record import _put_record
from .upload_blob import _upload_blob
import chitose.com.atproto.repo.apply_writes
import typing

class Repo_:
    """We recommend calling methods in this class via the :doc:`chitose.BskyAgent <chitose>` class instead of creating instances of this class directly."""

    def __init__(self, call: XrpcCall, subscribe: XrpcSubscribe) -> None:
        self.call = call
        self.subscribe = subscribe

    def create_record(self, repo: str, collection: str, record: typing.Any, rkey: typing.Optional[str]=None, validate: typing.Optional[bool]=None, swap_commit: typing.Optional[str]=None) -> bytes:
        """Create a single new repository record. Requires auth, implemented by PDS.


        :param repo: The handle or DID of the repo (aka, current account).

        :param collection: The NSID of the record collection.

        :param record: The record itself. Must contain a $type field.

        :param rkey: The Record Key.

        :param validate: Can be set to 'false' to skip Lexicon schema validation of record data.

        :param swap_commit: Compare and swap with the previous commit by CID.
        """
        return _create_record(self.call, repo, collection, record, rkey, validate, swap_commit)

    def delete_record(self, repo: str, collection: str, rkey: str, swap_record: typing.Optional[str]=None, swap_commit: typing.Optional[str]=None) -> bytes:
        """Delete a repository record, or ensure it doesn't exist. Requires auth, implemented by PDS.


        :param repo: The handle or DID of the repo (aka, current account).

        :param collection: The NSID of the record collection.

        :param rkey: The Record Key.

        :param swap_record: Compare and swap with the previous record by CID.

        :param swap_commit: Compare and swap with the previous commit by CID.
        """
        return _delete_record(self.call, repo, collection, rkey, swap_record, swap_commit)

    def put_record(self, repo: str, collection: str, rkey: str, record: typing.Any, validate: typing.Optional[bool]=None, swap_record: typing.Optional[str]=None, swap_commit: typing.Optional[str]=None) -> bytes:
        """Write a repository record, creating or updating it as needed. Requires auth, implemented by PDS.


        :param repo: The handle or DID of the repo (aka, current account).

        :param collection: The NSID of the record collection.

        :param rkey: The Record Key.

        :param record: The record to write.

        :param validate: Can be set to 'false' to skip Lexicon schema validation of record data.

        :param swap_record: Compare and swap with the previous record by CID. WARNING: nullable and optional field; may cause problems with golang implementation

        :param swap_commit: Compare and swap with the previous commit by CID.
        """
        return _put_record(self.call, repo, collection, rkey, record, validate, swap_record, swap_commit)

    def upload_blob(self, input_: bytes) -> bytes:
        """Upload a new blob, to be referenced from a repository record. The blob will be deleted if it is not referenced within a time window (eg, minutes). Blob restrictions (mimetype, size, etc) are enforced when the reference is created. Requires auth, implemented by PDS."""
        return _upload_blob(self.call, input_)

    def describe_repo(self, repo: str) -> bytes:
        """Get information about an account and repository, including the list of collections. Does not require auth.


        :param repo: The handle or DID of the repo.
        """
        return _describe_repo(self.call, repo)

    def get_record(self, repo: str, collection: str, rkey: str, cid: typing.Optional[str]=None) -> bytes:
        """Get a single record from a repository. Does not require auth.


        :param repo: The handle or DID of the repo.

        :param collection: The NSID of the record collection.

        :param rkey: The Record Key.

        :param cid: The CID of the version of the record. If not specified, then return the most recent version.
        """
        return _get_record(self.call, repo, collection, rkey, cid)

    def apply_writes(self, repo: str, writes: list[typing.Union[chitose.com.atproto.repo.apply_writes.Create, chitose.com.atproto.repo.apply_writes.Update, chitose.com.atproto.repo.apply_writes.Delete]], validate: typing.Optional[bool]=None, swap_commit: typing.Optional[str]=None) -> bytes:
        """Apply a batch transaction of repository creates, updates, and deletes. Requires auth, implemented by PDS.


        :param repo: The handle or DID of the repo (aka, current account).

        :param validate: Can be set to 'false' to skip Lexicon schema validation of record data, for all operations.

        :param swap_commit: If provided, the entire operation will fail if the current repo commit CID does not match this value. Used to prevent conflicting repo mutations.
        """
        return _apply_writes(self.call, repo, writes, validate, swap_commit)

    def list_records(self, repo: str, collection: str, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None, rkey_start: typing.Optional[str]=None, rkey_end: typing.Optional[str]=None, reverse: typing.Optional[bool]=None) -> bytes:
        """List a range of records in a repository, matching a specific collection. Does not require auth.


        :param repo: The handle or DID of the repo.

        :param collection: The NSID of the record type.

        :param limit: The number of records to return.

        :param rkey_start: DEPRECATED: The lowest sort-ordered rkey to start from (exclusive)

        :param rkey_end: DEPRECATED: The highest sort-ordered rkey to stop at (exclusive)

        :param reverse: Flag to reverse the order of the returned records.
        """
        return _list_records(self.call, repo, collection, limit, cursor, rkey_start, rkey_end, reverse)