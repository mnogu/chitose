# GENERATED CODE - DO NOT MODIFY
from __future__ import annotations
from chitose.xrpc import XrpcCall
from chitose.xrpc import XrpcSubscribe
from .get_preferences import _get_preferences
from .get_profile import _get_profile
from .get_profiles import _get_profiles
from .get_suggestions import _get_suggestions
from .put_preferences import _put_preferences
from .search_actors import _search_actors
from .search_actors_typeahead import _search_actors_typeahead
import chitose.app.bsky.actor.defs
import typing

class Actor_:
    """We recommend calling methods in this class via the :doc:`chitose.BskyAgent <chitose>` class instead of creating instances of this class directly."""

    def __init__(self, call: XrpcCall, subscribe: XrpcSubscribe) -> None:
        self.call = call
        self.subscribe = subscribe

    def search_actors_typeahead(self, term: typing.Optional[str]=None, q: typing.Optional[str]=None, limit: typing.Optional[int]=None) -> bytes:
        """Find actor suggestions for a search term.


        :param term: DEPRECATED: use 'q' instead

        :param q: search query prefix; not a full query string
        """
        return _search_actors_typeahead(self.call, term, q, limit)

    def put_preferences(self, preferences: chitose.app.bsky.actor.defs.Preferences) -> bytes:
        """Sets the private preferences attached to the account."""
        return _put_preferences(self.call, preferences)

    def get_profile(self, actor: str) -> bytes:
        """"""
        return _get_profile(self.call, actor)

    def get_suggestions(self, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
        """Get a list of actors suggested for following. Used in discovery UIs."""
        return _get_suggestions(self.call, limit, cursor)

    def search_actors(self, term: typing.Optional[str]=None, q: typing.Optional[str]=None, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
        """Find actors (profiles) matching search criteria.


        :param term: DEPRECATED: use 'q' instead

        :param q: search query string; syntax, phrase, boolean, and faceting is unspecified, but Lucene query syntax is recommended
        """
        return _search_actors(self.call, term, q, limit, cursor)

    def get_profiles(self, actors: list[str]) -> bytes:
        """"""
        return _get_profiles(self.call, actors)

    def get_preferences(self) -> bytes:
        """Get private preferences attached to the account."""
        return _get_preferences(self.call)