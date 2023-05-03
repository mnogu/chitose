# GENERATED CODE - DO NOT MODIFY
from __future__ import annotations
from .get_profile import _get_profile
from .get_profiles import _get_profiles
from .get_suggestions import _get_suggestions
from .search_actors import _search_actors
from .search_actors_typeahead import _search_actors_typeahead
from .defs import *
from .get_profile import *
from .get_profiles import *
from .get_suggestions import *
from .profile import *
from .search_actors import *
from .search_actors_typeahead import *

class Actor:

    def __init__(self, service: str, headers: dict[str, str]):
        self.service = service
        self.headers = headers

    def search_actors_typeahead(self, term: typing.Optional[str]=None, limit: typing.Optional[int]=None):
        """Find actor suggestions for a search term."""
        return _search_actors_typeahead(self.service, self.headers, term, limit)

    def get_profile(self, actor: str):
        """"""
        return _get_profile(self.service, self.headers, actor)

    def get_suggestions(self, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None):
        """Get a list of actors suggested for following. Used in discovery UIs."""
        return _get_suggestions(self.service, self.headers, limit, cursor)

    def search_actors(self, term: typing.Optional[str]=None, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None):
        """Find actors matching search criteria."""
        return _search_actors(self.service, self.headers, term, limit, cursor)

    def get_profiles(self, actors: list[str]):
        """"""
        return _get_profiles(self.service, self.headers, actors)