# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import chitose.com.atproto.admin.defs
import chitose.com.atproto.label.defs
import chitose.com.atproto.moderation.defs
import chitose.com.atproto.repo.strong_ref
import chitose.com.atproto.server.defs
import enum
import typing

class ActionView(chitose.Object):
    """"""

    def __init__(self, id: int, action: chitose.com.atproto.admin.defs.ActionType, subject: typing.Union[chitose.com.atproto.admin.defs.RepoRef, chitose.com.atproto.repo.strong_ref.StrongRef], subject_blob_cids: list[str], reason: str, created_by: str, created_at: str, resolved_report_ids: list[int], create_label_vals: typing.Optional[list[str]]=None, negate_label_vals: typing.Optional[list[str]]=None, reversal: typing.Optional[chitose.com.atproto.admin.defs.ActionReversal]=None) -> None:
        self.id = id
        self.action = action
        self.subject = subject
        self.subject_blob_cids = subject_blob_cids
        self.reason = reason
        self.created_by = created_by
        self.created_at = created_at
        self.resolved_report_ids = resolved_report_ids
        self.create_label_vals = create_label_vals
        self.negate_label_vals = negate_label_vals
        self.reversal = reversal

    def to_dict(self) -> dict:
        return {'id': self.id, 'action': self.action, 'subject': self.subject, 'subjectBlobCids': self.subject_blob_cids, 'reason': self.reason, 'createdBy': self.created_by, 'createdAt': self.created_at, 'resolvedReportIds': self.resolved_report_ids, 'createLabelVals': self.create_label_vals, 'negateLabelVals': self.negate_label_vals, 'reversal': self.reversal, '$type': 'com.atproto.admin.defs#actionView'}

class ActionViewDetail(chitose.Object):
    """"""

    def __init__(self, id: int, action: chitose.com.atproto.admin.defs.ActionType, subject: typing.Union[chitose.com.atproto.admin.defs.RepoView, chitose.com.atproto.admin.defs.RecordView], subject_blobs: list[chitose.com.atproto.admin.defs.BlobView], reason: str, created_by: str, created_at: str, resolved_reports: list[chitose.com.atproto.admin.defs.ReportView], create_label_vals: typing.Optional[list[str]]=None, negate_label_vals: typing.Optional[list[str]]=None, reversal: typing.Optional[chitose.com.atproto.admin.defs.ActionReversal]=None) -> None:
        self.id = id
        self.action = action
        self.subject = subject
        self.subject_blobs = subject_blobs
        self.reason = reason
        self.created_by = created_by
        self.created_at = created_at
        self.resolved_reports = resolved_reports
        self.create_label_vals = create_label_vals
        self.negate_label_vals = negate_label_vals
        self.reversal = reversal

    def to_dict(self) -> dict:
        return {'id': self.id, 'action': self.action, 'subject': self.subject, 'subjectBlobs': self.subject_blobs, 'reason': self.reason, 'createdBy': self.created_by, 'createdAt': self.created_at, 'resolvedReports': self.resolved_reports, 'createLabelVals': self.create_label_vals, 'negateLabelVals': self.negate_label_vals, 'reversal': self.reversal, '$type': 'com.atproto.admin.defs#actionViewDetail'}

class ActionViewCurrent(chitose.Object):
    """"""

    def __init__(self, id: int, action: chitose.com.atproto.admin.defs.ActionType) -> None:
        self.id = id
        self.action = action

    def to_dict(self) -> dict:
        return {'id': self.id, 'action': self.action, '$type': 'com.atproto.admin.defs#actionViewCurrent'}

class ActionReversal(chitose.Object):
    """"""

    def __init__(self, reason: str, created_by: str, created_at: str) -> None:
        self.reason = reason
        self.created_by = created_by
        self.created_at = created_at

    def to_dict(self) -> dict:
        return {'reason': self.reason, 'createdBy': self.created_by, 'createdAt': self.created_at, '$type': 'com.atproto.admin.defs#actionReversal'}

class ActionType(enum.Enum):
    TAKEDOWN = '#takedown'
    FLAG = '#flag'
    ACKNOWLEDGE = '#acknowledge'
    ESCALATE = '#escalate'
TAKEDOWN = 'com.atproto.admin.defs#takedown'
FLAG = 'com.atproto.admin.defs#flag'
ACKNOWLEDGE = 'com.atproto.admin.defs#acknowledge'
ESCALATE = 'com.atproto.admin.defs#escalate'

class ReportView(chitose.Object):
    """"""

    def __init__(self, id: int, reason_type: chitose.com.atproto.moderation.defs.ReasonType, subject: typing.Union[chitose.com.atproto.admin.defs.RepoRef, chitose.com.atproto.repo.strong_ref.StrongRef], reported_by: str, created_at: str, resolved_by_action_ids: list[int], reason: typing.Optional[str]=None) -> None:
        self.id = id
        self.reason_type = reason_type
        self.subject = subject
        self.reported_by = reported_by
        self.created_at = created_at
        self.resolved_by_action_ids = resolved_by_action_ids
        self.reason = reason

    def to_dict(self) -> dict:
        return {'id': self.id, 'reasonType': self.reason_type, 'subject': self.subject, 'reportedBy': self.reported_by, 'createdAt': self.created_at, 'resolvedByActionIds': self.resolved_by_action_ids, 'reason': self.reason, '$type': 'com.atproto.admin.defs#reportView'}

class ReportViewDetail(chitose.Object):
    """"""

    def __init__(self, id: int, reason_type: chitose.com.atproto.moderation.defs.ReasonType, subject: typing.Union[chitose.com.atproto.admin.defs.RepoView, chitose.com.atproto.admin.defs.RecordView], reported_by: str, created_at: str, resolved_by_actions: list[chitose.com.atproto.admin.defs.ActionView], reason: typing.Optional[str]=None) -> None:
        self.id = id
        self.reason_type = reason_type
        self.subject = subject
        self.reported_by = reported_by
        self.created_at = created_at
        self.resolved_by_actions = resolved_by_actions
        self.reason = reason

    def to_dict(self) -> dict:
        return {'id': self.id, 'reasonType': self.reason_type, 'subject': self.subject, 'reportedBy': self.reported_by, 'createdAt': self.created_at, 'resolvedByActions': self.resolved_by_actions, 'reason': self.reason, '$type': 'com.atproto.admin.defs#reportViewDetail'}

class RepoView(chitose.Object):
    """"""

    def __init__(self, did: str, handle: str, related_records: list[typing.Any], indexed_at: str, moderation: chitose.com.atproto.admin.defs.Moderation, email: typing.Optional[str]=None, invited_by: typing.Optional[chitose.com.atproto.server.defs.InviteCode]=None) -> None:
        self.did = did
        self.handle = handle
        self.related_records = related_records
        self.indexed_at = indexed_at
        self.moderation = moderation
        self.email = email
        self.invited_by = invited_by

    def to_dict(self) -> dict:
        return {'did': self.did, 'handle': self.handle, 'relatedRecords': self.related_records, 'indexedAt': self.indexed_at, 'moderation': self.moderation, 'email': self.email, 'invitedBy': self.invited_by, '$type': 'com.atproto.admin.defs#repoView'}

class RepoViewDetail(chitose.Object):
    """"""

    def __init__(self, did: str, handle: str, related_records: list[typing.Any], indexed_at: str, moderation: chitose.com.atproto.admin.defs.ModerationDetail, email: typing.Optional[str]=None, labels: typing.Optional[list[chitose.com.atproto.label.defs.Label]]=None, invited_by: typing.Optional[chitose.com.atproto.server.defs.InviteCode]=None, invites: typing.Optional[list[chitose.com.atproto.server.defs.InviteCode]]=None) -> None:
        self.did = did
        self.handle = handle
        self.related_records = related_records
        self.indexed_at = indexed_at
        self.moderation = moderation
        self.email = email
        self.labels = labels
        self.invited_by = invited_by
        self.invites = invites

    def to_dict(self) -> dict:
        return {'did': self.did, 'handle': self.handle, 'relatedRecords': self.related_records, 'indexedAt': self.indexed_at, 'moderation': self.moderation, 'email': self.email, 'labels': self.labels, 'invitedBy': self.invited_by, 'invites': self.invites, '$type': 'com.atproto.admin.defs#repoViewDetail'}

class RepoRef(chitose.Object):
    """"""

    def __init__(self, did: str) -> None:
        self.did = did

    def to_dict(self) -> dict:
        return {'did': self.did, '$type': 'com.atproto.admin.defs#repoRef'}

class RecordView(chitose.Object):
    """"""

    def __init__(self, uri: str, cid: str, value: typing.Any, blob_cids: list[str], indexed_at: str, moderation: chitose.com.atproto.admin.defs.Moderation, repo: chitose.com.atproto.admin.defs.RepoView) -> None:
        self.uri = uri
        self.cid = cid
        self.value = value
        self.blob_cids = blob_cids
        self.indexed_at = indexed_at
        self.moderation = moderation
        self.repo = repo

    def to_dict(self) -> dict:
        return {'uri': self.uri, 'cid': self.cid, 'value': self.value, 'blobCids': self.blob_cids, 'indexedAt': self.indexed_at, 'moderation': self.moderation, 'repo': self.repo, '$type': 'com.atproto.admin.defs#recordView'}

class RecordViewDetail(chitose.Object):
    """"""

    def __init__(self, uri: str, cid: str, value: typing.Any, blobs: list[chitose.com.atproto.admin.defs.BlobView], indexed_at: str, moderation: chitose.com.atproto.admin.defs.ModerationDetail, repo: chitose.com.atproto.admin.defs.RepoView, labels: typing.Optional[list[chitose.com.atproto.label.defs.Label]]=None) -> None:
        self.uri = uri
        self.cid = cid
        self.value = value
        self.blobs = blobs
        self.indexed_at = indexed_at
        self.moderation = moderation
        self.repo = repo
        self.labels = labels

    def to_dict(self) -> dict:
        return {'uri': self.uri, 'cid': self.cid, 'value': self.value, 'blobs': self.blobs, 'indexedAt': self.indexed_at, 'moderation': self.moderation, 'repo': self.repo, 'labels': self.labels, '$type': 'com.atproto.admin.defs#recordViewDetail'}

class Moderation(chitose.Object):
    """"""

    def __init__(self, current_action: typing.Optional[chitose.com.atproto.admin.defs.ActionViewCurrent]=None) -> None:
        self.current_action = current_action

    def to_dict(self) -> dict:
        return {'currentAction': self.current_action, '$type': 'com.atproto.admin.defs#moderation'}

class ModerationDetail(chitose.Object):
    """"""

    def __init__(self, actions: list[chitose.com.atproto.admin.defs.ActionView], reports: list[chitose.com.atproto.admin.defs.ReportView], current_action: typing.Optional[chitose.com.atproto.admin.defs.ActionViewCurrent]=None) -> None:
        self.actions = actions
        self.reports = reports
        self.current_action = current_action

    def to_dict(self) -> dict:
        return {'actions': self.actions, 'reports': self.reports, 'currentAction': self.current_action, '$type': 'com.atproto.admin.defs#moderationDetail'}

class BlobView(chitose.Object):
    """"""

    def __init__(self, cid: str, mime_type: str, size: int, created_at: str, details: typing.Optional[typing.Union[chitose.com.atproto.admin.defs.ImageDetails, chitose.com.atproto.admin.defs.VideoDetails]]=None, moderation: typing.Optional[chitose.com.atproto.admin.defs.Moderation]=None) -> None:
        self.cid = cid
        self.mime_type = mime_type
        self.size = size
        self.created_at = created_at
        self.details = details
        self.moderation = moderation

    def to_dict(self) -> dict:
        return {'cid': self.cid, 'mimeType': self.mime_type, 'size': self.size, 'createdAt': self.created_at, 'details': self.details, 'moderation': self.moderation, '$type': 'com.atproto.admin.defs#blobView'}

class ImageDetails(chitose.Object):
    """"""

    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

    def to_dict(self) -> dict:
        return {'width': self.width, 'height': self.height, '$type': 'com.atproto.admin.defs#imageDetails'}

class VideoDetails(chitose.Object):
    """"""

    def __init__(self, width: int, height: int, length: int) -> None:
        self.width = width
        self.height = height
        self.length = length

    def to_dict(self) -> dict:
        return {'width': self.width, 'height': self.height, 'length': self.length, '$type': 'com.atproto.admin.defs#videoDetails'}