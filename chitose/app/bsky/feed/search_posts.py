# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _search_posts(call: chitose.xrpc.XrpcCall, q: str, sort: typing.Optional[typing.Literal['top', 'latest']]=None, since: typing.Optional[str]=None, until: typing.Optional[str]=None, mentions: typing.Optional[str]=None, author: typing.Optional[str]=None, lang: typing.Optional[str]=None, domain: typing.Optional[str]=None, url: typing.Optional[str]=None, tag: typing.Optional[list[str]]=None, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
    """Find posts matching search criteria, returning views of those posts.


    :param q: Search query string; syntax, phrase, boolean, and faceting is unspecified, but Lucene query syntax is recommended.

    :param sort: Specifies the ranking order of results.

    :param since: Filter results for posts after the indicated datetime (inclusive). Expected to use 'sortAt' timestamp, which may not match 'createdAt'. Can be a datetime, or just an ISO date (YYYY-MM-DD).

    :param until: Filter results for posts before the indicated datetime (not inclusive). Expected to use 'sortAt' timestamp, which may not match 'createdAt'. Can be a datetime, or just an ISO date (YYY-MM-DD).

    :param mentions: Filter to posts which mention the given account. Handles are resolved to DID before query-time. Only matches rich-text facet mentions.

    :param author: Filter to posts by the given account. Handles are resolved to DID before query-time.

    :param lang: Filter to posts in the given language. Expected to be based on post language field, though server may override language detection.

    :param domain: Filter to posts with URLs (facet links or embeds) linking to the given domain (hostname). Server may apply hostname normalization.

    :param url: Filter to posts with links (facet links or embeds) pointing to this URL. Server may apply URL normalization or fuzzy matching.

    :param tag: Filter to posts with the given tag (hashtag), based on rich-text facet or tag field. Do not include the hash (#) prefix. Multiple tags can be specified, with 'AND' matching.

    :param cursor: Optional pagination mechanism; may not necessarily allow scrolling through entire result set.
    """
    return call('app.bsky.feed.searchPosts', [('q', q), ('sort', sort), ('since', since), ('until', until), ('mentions', mentions), ('author', author), ('lang', lang), ('domain', domain), ('url', url), ('tag', tag), ('limit', limit), ('cursor', cursor)], None, {})