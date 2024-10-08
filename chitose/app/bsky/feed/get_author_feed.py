# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _get_author_feed(call: chitose.xrpc.XrpcCall, actor: str, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None, filter: typing.Optional[typing.Literal['posts_with_replies', 'posts_no_replies', 'posts_with_media', 'posts_and_author_threads']]=None, include_pins: typing.Optional[bool]=None) -> bytes:
    """Get a view of an actor's 'author feed' (post and reposts by the author). Does not require auth.


    :param filter: Combinations of post/repost types to include in response.
    """
    return call('app.bsky.feed.getAuthorFeed', [('actor', actor), ('limit', limit), ('cursor', cursor), ('filter', filter), ('includePins', include_pins)], None, {})