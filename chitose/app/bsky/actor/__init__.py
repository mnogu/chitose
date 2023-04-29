# GENERATED CODE - DO NOT MODIFY
from __future__ import annotations
from .defs import *
from .get_profile import *
from .get_profiles import *
from .get_suggestions import *
from .profile import *
from .search_actors import *
from .search_actors_typeahead import *
import chitose
import typing

class Actor:

    def __init__(self, service: str, headers: dict[str, str]):
        self.service = service
        self.headers = headers

    def search_actors_typeahead(self, term: typing.Optional[str], limit: typing.Optional[int]):
        return search_actors_typeahead(self.service, self.headers, term, limit)

    def get_profile(self, actor: str):
        return get_profile(self.service, self.headers, actor)

    def get_suggestions(self, limit: typing.Optional[int], cursor: typing.Optional[str]):
        return get_suggestions(self.service, self.headers, limit, cursor)

    def search_actors(self, term: typing.Optional[str], limit: typing.Optional[int], cursor: typing.Optional[str]):
        return search_actors(self.service, self.headers, term, limit, cursor)

    def get_profiles(self, actors: list[str]):
        return get_profiles(self.service, self.headers, actors)