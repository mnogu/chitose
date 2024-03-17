# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import chitose.com.atproto.server.defs
import typing

class StatusAttr(chitose.Object):
    """"""

    def __init__(self, applied: bool, ref: typing.Optional[str]=None) -> None:
        self.applied = applied
        self.ref = ref

    def to_dict(self) -> dict[str, typing.Any]:
        return {'applied': self.applied, 'ref': self.ref, '$type': 'com.atproto.admin.defs#statusAttr'}

class AccountView(chitose.Object):
    """"""

    def __init__(self, did: str, handle: str, indexed_at: str, email: typing.Optional[str]=None, related_records: typing.Optional[list[typing.Any]]=None, invited_by: typing.Optional[chitose.com.atproto.server.defs.InviteCode]=None, invites: typing.Optional[list[chitose.com.atproto.server.defs.InviteCode]]=None, invites_disabled: typing.Optional[bool]=None, email_confirmed_at: typing.Optional[str]=None, invite_note: typing.Optional[str]=None) -> None:
        self.did = did
        self.handle = handle
        self.indexed_at = indexed_at
        self.email = email
        self.related_records = related_records
        self.invited_by = invited_by
        self.invites = invites
        self.invites_disabled = invites_disabled
        self.email_confirmed_at = email_confirmed_at
        self.invite_note = invite_note

    def to_dict(self) -> dict[str, typing.Any]:
        return {'did': self.did, 'handle': self.handle, 'indexedAt': self.indexed_at, 'email': self.email, 'relatedRecords': self.related_records, 'invitedBy': self.invited_by, 'invites': self.invites, 'invitesDisabled': self.invites_disabled, 'emailConfirmedAt': self.email_confirmed_at, 'inviteNote': self.invite_note, '$type': 'com.atproto.admin.defs#accountView'}

class RepoRef(chitose.Object):
    """"""

    def __init__(self, did: str) -> None:
        self.did = did

    def to_dict(self) -> dict[str, typing.Any]:
        return {'did': self.did, '$type': 'com.atproto.admin.defs#repoRef'}

class RepoBlobRef(chitose.Object):
    """"""

    def __init__(self, did: str, cid: str, record_uri: typing.Optional[str]=None) -> None:
        self.did = did
        self.cid = cid
        self.record_uri = record_uri

    def to_dict(self) -> dict[str, typing.Any]:
        return {'did': self.did, 'cid': self.cid, 'recordUri': self.record_uri, '$type': 'com.atproto.admin.defs#repoBlobRef'}