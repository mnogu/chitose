# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import chitose.app.bsky.actor.defs
import typing

class Member(chitose.Object):
    """"""

    def __init__(self, did: str, role: typing.Literal['#roleAdmin', '#roleModerator', '#roleTriage'], disabled: typing.Optional[bool]=None, profile: typing.Optional[chitose.app.bsky.actor.defs.ProfileViewDetailed]=None, created_at: typing.Optional[str]=None, updated_at: typing.Optional[str]=None, last_updated_by: typing.Optional[str]=None) -> None:
        self.did = did
        self.role = role
        self.disabled = disabled
        self.profile = profile
        self.created_at = created_at
        self.updated_at = updated_at
        self.last_updated_by = last_updated_by

    def to_dict(self) -> dict[str, typing.Any]:
        return {'did': self.did, 'role': self.role, 'disabled': self.disabled, 'profile': self.profile, 'createdAt': self.created_at, 'updatedAt': self.updated_at, 'lastUpdatedBy': self.last_updated_by, '$type': 'tools.ozone.team.defs#member'}
ROLE_ADMIN = 'tools.ozone.team.defs#roleAdmin'
ROLE_MODERATOR = 'tools.ozone.team.defs#roleModerator'
ROLE_TRIAGE = 'tools.ozone.team.defs#roleTriage'