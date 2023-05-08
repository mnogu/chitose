# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import chitose.com.atproto.server.defs

class InviteCode(chitose.Object):
    """"""

    def __init__(self, code: str, available: int, disabled: str, for_account: str, created_by: str, created_at: str, uses: list[chitose.com.atproto.server.defs.InviteCodeUse]) -> None:
        self.code = code
        self.available = available
        self.disabled = disabled
        self.for_account = for_account
        self.created_by = created_by
        self.created_at = created_at
        self.uses = uses

    def to_dict(self) -> dict:
        return {'code': self.code, 'available': self.available, 'disabled': self.disabled, 'forAccount': self.for_account, 'createdBy': self.created_by, 'createdAt': self.created_at, 'uses': self.uses, '$type': 'com.atproto.server.defs#inviteCode'}

class InviteCodeUse(chitose.Object):
    """"""

    def __init__(self, used_by: str, used_at: str) -> None:
        self.used_by = used_by
        self.used_at = used_at

    def to_dict(self) -> dict:
        return {'usedBy': self.used_by, 'usedAt': self.used_at, '$type': 'com.atproto.server.defs#inviteCodeUse'}