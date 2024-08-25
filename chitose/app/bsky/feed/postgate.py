# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import chitose.app.bsky.feed.postgate
import typing

class Postgate(chitose.Record):
    """


    :param post: Reference (AT-URI) to the post record.

    :param detached_embedding_uris: List of AT-URIs embedding this post that the author has detached from.
    """

    def __init__(self, created_at: str, post: str, detached_embedding_uris: typing.Optional[list[str]]=None, embedding_rules: typing.Optional[list[chitose.app.bsky.feed.postgate.DisableRule]]=None) -> None:
        self.created_at = created_at
        self.post = post
        self.detached_embedding_uris = detached_embedding_uris
        self.embedding_rules = embedding_rules

    def to_dict(self) -> dict[str, typing.Any]:
        return {'createdAt': self.created_at, 'post': self.post, 'detachedEmbeddingUris': self.detached_embedding_uris, 'embeddingRules': self.embedding_rules, '$type': 'app.bsky.feed.postgate'}

class DisableRule(chitose.Object):
    """Disables embedding of this post."""

    def to_dict(self) -> dict[str, typing.Any]:
        return {'$type': 'app.bsky.feed.postgate#disableRule'}