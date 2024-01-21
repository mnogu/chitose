# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import chitose.com.atproto.admin.defs
import chitose.com.atproto.label.defs
import chitose.com.atproto.moderation.defs
import chitose.com.atproto.repo.strong_ref
import chitose.com.atproto.server.defs
import typing

class StatusAttr(chitose.Object):
    """"""

    def __init__(self, applied: bool, ref: typing.Optional[str]=None) -> None:
        self.applied = applied
        self.ref = ref

    def to_dict(self) -> dict[str, typing.Any]:
        return {'applied': self.applied, 'ref': self.ref, '$type': 'com.atproto.admin.defs#statusAttr'}

class ModEventView(chitose.Object):
    """"""

    def __init__(self, id: int, event: typing.Union[chitose.com.atproto.admin.defs.ModEventTakedown, chitose.com.atproto.admin.defs.ModEventReverseTakedown, chitose.com.atproto.admin.defs.ModEventComment, chitose.com.atproto.admin.defs.ModEventReport, chitose.com.atproto.admin.defs.ModEventLabel, chitose.com.atproto.admin.defs.ModEventAcknowledge, chitose.com.atproto.admin.defs.ModEventEscalate, chitose.com.atproto.admin.defs.ModEventMute, chitose.com.atproto.admin.defs.ModEventEmail], subject: typing.Union[chitose.com.atproto.admin.defs.RepoRef, chitose.com.atproto.repo.strong_ref.StrongRef], subject_blob_cids: list[str], created_by: str, created_at: str, creator_handle: typing.Optional[str]=None, subject_handle: typing.Optional[str]=None) -> None:
        self.id = id
        self.event = event
        self.subject = subject
        self.subject_blob_cids = subject_blob_cids
        self.created_by = created_by
        self.created_at = created_at
        self.creator_handle = creator_handle
        self.subject_handle = subject_handle

    def to_dict(self) -> dict[str, typing.Any]:
        return {'id': self.id, 'event': self.event, 'subject': self.subject, 'subjectBlobCids': self.subject_blob_cids, 'createdBy': self.created_by, 'createdAt': self.created_at, 'creatorHandle': self.creator_handle, 'subjectHandle': self.subject_handle, '$type': 'com.atproto.admin.defs#modEventView'}

class ModEventViewDetail(chitose.Object):
    """"""

    def __init__(self, id: int, event: typing.Union[chitose.com.atproto.admin.defs.ModEventTakedown, chitose.com.atproto.admin.defs.ModEventReverseTakedown, chitose.com.atproto.admin.defs.ModEventComment, chitose.com.atproto.admin.defs.ModEventReport, chitose.com.atproto.admin.defs.ModEventLabel, chitose.com.atproto.admin.defs.ModEventAcknowledge, chitose.com.atproto.admin.defs.ModEventEscalate, chitose.com.atproto.admin.defs.ModEventMute, chitose.com.atproto.admin.defs.ModEventResolveAppeal], subject: typing.Union[chitose.com.atproto.admin.defs.RepoView, chitose.com.atproto.admin.defs.RepoViewNotFound, chitose.com.atproto.admin.defs.RecordView, chitose.com.atproto.admin.defs.RecordViewNotFound], subject_blobs: list[chitose.com.atproto.admin.defs.BlobView], created_by: str, created_at: str) -> None:
        self.id = id
        self.event = event
        self.subject = subject
        self.subject_blobs = subject_blobs
        self.created_by = created_by
        self.created_at = created_at

    def to_dict(self) -> dict[str, typing.Any]:
        return {'id': self.id, 'event': self.event, 'subject': self.subject, 'subjectBlobs': self.subject_blobs, 'createdBy': self.created_by, 'createdAt': self.created_at, '$type': 'com.atproto.admin.defs#modEventViewDetail'}

class ReportView(chitose.Object):
    """"""

    def __init__(self, id: int, reason_type: chitose.com.atproto.moderation.defs.ReasonType, subject: typing.Union[chitose.com.atproto.admin.defs.RepoRef, chitose.com.atproto.repo.strong_ref.StrongRef], reported_by: str, created_at: str, resolved_by_action_ids: list[int], comment: typing.Optional[str]=None, subject_repo_handle: typing.Optional[str]=None) -> None:
        self.id = id
        self.reason_type = reason_type
        self.subject = subject
        self.reported_by = reported_by
        self.created_at = created_at
        self.resolved_by_action_ids = resolved_by_action_ids
        self.comment = comment
        self.subject_repo_handle = subject_repo_handle

    def to_dict(self) -> dict[str, typing.Any]:
        return {'id': self.id, 'reasonType': self.reason_type, 'subject': self.subject, 'reportedBy': self.reported_by, 'createdAt': self.created_at, 'resolvedByActionIds': self.resolved_by_action_ids, 'comment': self.comment, 'subjectRepoHandle': self.subject_repo_handle, '$type': 'com.atproto.admin.defs#reportView'}

class SubjectStatusView(chitose.Object):
    """


    :param updated_at: Timestamp referencing when the last update was made to the moderation status of the subject

    :param created_at: Timestamp referencing the first moderation status impacting event was emitted on the subject

    :param comment: Sticky comment on the subject.

    :param last_appealed_at: Timestamp referencing when the author of the subject appealed a moderation action

    :param appealed: True indicates that the a previously taken moderator action was appealed against, by the author of the content. False indicates last appeal was resolved by moderators.
    """

    def __init__(self, id: int, subject: typing.Union[chitose.com.atproto.admin.defs.RepoRef, chitose.com.atproto.repo.strong_ref.StrongRef], updated_at: str, created_at: str, review_state: chitose.com.atproto.admin.defs.SubjectReviewState, subject_blob_cids: typing.Optional[list[str]]=None, subject_repo_handle: typing.Optional[str]=None, comment: typing.Optional[str]=None, mute_until: typing.Optional[str]=None, last_reviewed_by: typing.Optional[str]=None, last_reviewed_at: typing.Optional[str]=None, last_reported_at: typing.Optional[str]=None, last_appealed_at: typing.Optional[str]=None, takendown: typing.Optional[bool]=None, appealed: typing.Optional[bool]=None, suspend_until: typing.Optional[str]=None) -> None:
        self.id = id
        self.subject = subject
        self.updated_at = updated_at
        self.created_at = created_at
        self.review_state = review_state
        self.subject_blob_cids = subject_blob_cids
        self.subject_repo_handle = subject_repo_handle
        self.comment = comment
        self.mute_until = mute_until
        self.last_reviewed_by = last_reviewed_by
        self.last_reviewed_at = last_reviewed_at
        self.last_reported_at = last_reported_at
        self.last_appealed_at = last_appealed_at
        self.takendown = takendown
        self.appealed = appealed
        self.suspend_until = suspend_until

    def to_dict(self) -> dict[str, typing.Any]:
        return {'id': self.id, 'subject': self.subject, 'updatedAt': self.updated_at, 'createdAt': self.created_at, 'reviewState': self.review_state, 'subjectBlobCids': self.subject_blob_cids, 'subjectRepoHandle': self.subject_repo_handle, 'comment': self.comment, 'muteUntil': self.mute_until, 'lastReviewedBy': self.last_reviewed_by, 'lastReviewedAt': self.last_reviewed_at, 'lastReportedAt': self.last_reported_at, 'lastAppealedAt': self.last_appealed_at, 'takendown': self.takendown, 'appealed': self.appealed, 'suspendUntil': self.suspend_until, '$type': 'com.atproto.admin.defs#subjectStatusView'}

class ReportViewDetail(chitose.Object):
    """"""

    def __init__(self, id: int, reason_type: chitose.com.atproto.moderation.defs.ReasonType, subject: typing.Union[chitose.com.atproto.admin.defs.RepoView, chitose.com.atproto.admin.defs.RepoViewNotFound, chitose.com.atproto.admin.defs.RecordView, chitose.com.atproto.admin.defs.RecordViewNotFound], reported_by: str, created_at: str, resolved_by_actions: list[chitose.com.atproto.admin.defs.ModEventView], comment: typing.Optional[str]=None, subject_status: typing.Optional[chitose.com.atproto.admin.defs.SubjectStatusView]=None) -> None:
        self.id = id
        self.reason_type = reason_type
        self.subject = subject
        self.reported_by = reported_by
        self.created_at = created_at
        self.resolved_by_actions = resolved_by_actions
        self.comment = comment
        self.subject_status = subject_status

    def to_dict(self) -> dict[str, typing.Any]:
        return {'id': self.id, 'reasonType': self.reason_type, 'subject': self.subject, 'reportedBy': self.reported_by, 'createdAt': self.created_at, 'resolvedByActions': self.resolved_by_actions, 'comment': self.comment, 'subjectStatus': self.subject_status, '$type': 'com.atproto.admin.defs#reportViewDetail'}

class RepoView(chitose.Object):
    """"""

    def __init__(self, did: str, handle: str, related_records: list[typing.Any], indexed_at: str, moderation: chitose.com.atproto.admin.defs.Moderation, email: typing.Optional[str]=None, invited_by: typing.Optional[chitose.com.atproto.server.defs.InviteCode]=None, invites_disabled: typing.Optional[bool]=None, invite_note: typing.Optional[str]=None) -> None:
        self.did = did
        self.handle = handle
        self.related_records = related_records
        self.indexed_at = indexed_at
        self.moderation = moderation
        self.email = email
        self.invited_by = invited_by
        self.invites_disabled = invites_disabled
        self.invite_note = invite_note

    def to_dict(self) -> dict[str, typing.Any]:
        return {'did': self.did, 'handle': self.handle, 'relatedRecords': self.related_records, 'indexedAt': self.indexed_at, 'moderation': self.moderation, 'email': self.email, 'invitedBy': self.invited_by, 'invitesDisabled': self.invites_disabled, 'inviteNote': self.invite_note, '$type': 'com.atproto.admin.defs#repoView'}

class RepoViewDetail(chitose.Object):
    """"""

    def __init__(self, did: str, handle: str, related_records: list[typing.Any], indexed_at: str, moderation: chitose.com.atproto.admin.defs.ModerationDetail, email: typing.Optional[str]=None, labels: typing.Optional[list[chitose.com.atproto.label.defs.Label]]=None, invited_by: typing.Optional[chitose.com.atproto.server.defs.InviteCode]=None, invites: typing.Optional[list[chitose.com.atproto.server.defs.InviteCode]]=None, invites_disabled: typing.Optional[bool]=None, invite_note: typing.Optional[str]=None, email_confirmed_at: typing.Optional[str]=None) -> None:
        self.did = did
        self.handle = handle
        self.related_records = related_records
        self.indexed_at = indexed_at
        self.moderation = moderation
        self.email = email
        self.labels = labels
        self.invited_by = invited_by
        self.invites = invites
        self.invites_disabled = invites_disabled
        self.invite_note = invite_note
        self.email_confirmed_at = email_confirmed_at

    def to_dict(self) -> dict[str, typing.Any]:
        return {'did': self.did, 'handle': self.handle, 'relatedRecords': self.related_records, 'indexedAt': self.indexed_at, 'moderation': self.moderation, 'email': self.email, 'labels': self.labels, 'invitedBy': self.invited_by, 'invites': self.invites, 'invitesDisabled': self.invites_disabled, 'inviteNote': self.invite_note, 'emailConfirmedAt': self.email_confirmed_at, '$type': 'com.atproto.admin.defs#repoViewDetail'}

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

class RepoViewNotFound(chitose.Object):
    """"""

    def __init__(self, did: str) -> None:
        self.did = did

    def to_dict(self) -> dict[str, typing.Any]:
        return {'did': self.did, '$type': 'com.atproto.admin.defs#repoViewNotFound'}

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

    def to_dict(self) -> dict[str, typing.Any]:
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

    def to_dict(self) -> dict[str, typing.Any]:
        return {'uri': self.uri, 'cid': self.cid, 'value': self.value, 'blobs': self.blobs, 'indexedAt': self.indexed_at, 'moderation': self.moderation, 'repo': self.repo, 'labels': self.labels, '$type': 'com.atproto.admin.defs#recordViewDetail'}

class RecordViewNotFound(chitose.Object):
    """"""

    def __init__(self, uri: str) -> None:
        self.uri = uri

    def to_dict(self) -> dict[str, typing.Any]:
        return {'uri': self.uri, '$type': 'com.atproto.admin.defs#recordViewNotFound'}

class Moderation(chitose.Object):
    """"""

    def __init__(self, subject_status: typing.Optional[chitose.com.atproto.admin.defs.SubjectStatusView]=None) -> None:
        self.subject_status = subject_status

    def to_dict(self) -> dict[str, typing.Any]:
        return {'subjectStatus': self.subject_status, '$type': 'com.atproto.admin.defs#moderation'}

class ModerationDetail(chitose.Object):
    """"""

    def __init__(self, subject_status: typing.Optional[chitose.com.atproto.admin.defs.SubjectStatusView]=None) -> None:
        self.subject_status = subject_status

    def to_dict(self) -> dict[str, typing.Any]:
        return {'subjectStatus': self.subject_status, '$type': 'com.atproto.admin.defs#moderationDetail'}

class BlobView(chitose.Object):
    """"""

    def __init__(self, cid: str, mime_type: str, size: int, created_at: str, details: typing.Optional[typing.Union[chitose.com.atproto.admin.defs.ImageDetails, chitose.com.atproto.admin.defs.VideoDetails]]=None, moderation: typing.Optional[chitose.com.atproto.admin.defs.Moderation]=None) -> None:
        self.cid = cid
        self.mime_type = mime_type
        self.size = size
        self.created_at = created_at
        self.details = details
        self.moderation = moderation

    def to_dict(self) -> dict[str, typing.Any]:
        return {'cid': self.cid, 'mimeType': self.mime_type, 'size': self.size, 'createdAt': self.created_at, 'details': self.details, 'moderation': self.moderation, '$type': 'com.atproto.admin.defs#blobView'}

class ImageDetails(chitose.Object):
    """"""

    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

    def to_dict(self) -> dict[str, typing.Any]:
        return {'width': self.width, 'height': self.height, '$type': 'com.atproto.admin.defs#imageDetails'}

class VideoDetails(chitose.Object):
    """"""

    def __init__(self, width: int, height: int, length: int) -> None:
        self.width = width
        self.height = height
        self.length = length

    def to_dict(self) -> dict[str, typing.Any]:
        return {'width': self.width, 'height': self.height, 'length': self.length, '$type': 'com.atproto.admin.defs#videoDetails'}
SubjectReviewState = typing.Literal['#reviewOpen', '#reviewEscalated', '#reviewClosed']
REVIEW_OPEN = 'com.atproto.admin.defs#reviewOpen'
REVIEW_ESCALATED = 'com.atproto.admin.defs#reviewEscalated'
REVIEW_CLOSED = 'com.atproto.admin.defs#reviewClosed'

class ModEventTakedown(chitose.Object):
    """Take down a subject permanently or temporarily


    :param duration_in_hours: Indicates how long the takedown should be in effect before automatically expiring.
    """

    def __init__(self, comment: typing.Optional[str]=None, duration_in_hours: typing.Optional[int]=None) -> None:
        self.comment = comment
        self.duration_in_hours = duration_in_hours

    def to_dict(self) -> dict[str, typing.Any]:
        return {'comment': self.comment, 'durationInHours': self.duration_in_hours, '$type': 'com.atproto.admin.defs#modEventTakedown'}

class ModEventReverseTakedown(chitose.Object):
    """Revert take down action on a subject


    :param comment: Describe reasoning behind the reversal.
    """

    def __init__(self, comment: typing.Optional[str]=None) -> None:
        self.comment = comment

    def to_dict(self) -> dict[str, typing.Any]:
        return {'comment': self.comment, '$type': 'com.atproto.admin.defs#modEventReverseTakedown'}

class ModEventResolveAppeal(chitose.Object):
    """Resolve appeal on a subject


    :param comment: Describe resolution.
    """

    def __init__(self, comment: typing.Optional[str]=None) -> None:
        self.comment = comment

    def to_dict(self) -> dict[str, typing.Any]:
        return {'comment': self.comment, '$type': 'com.atproto.admin.defs#modEventResolveAppeal'}

class ModEventComment(chitose.Object):
    """Add a comment to a subject


    :param sticky: Make the comment persistent on the subject
    """

    def __init__(self, comment: str, sticky: typing.Optional[bool]=None) -> None:
        self.comment = comment
        self.sticky = sticky

    def to_dict(self) -> dict[str, typing.Any]:
        return {'comment': self.comment, 'sticky': self.sticky, '$type': 'com.atproto.admin.defs#modEventComment'}

class ModEventReport(chitose.Object):
    """Report a subject"""

    def __init__(self, report_type: chitose.com.atproto.moderation.defs.ReasonType, comment: typing.Optional[str]=None) -> None:
        self.report_type = report_type
        self.comment = comment

    def to_dict(self) -> dict[str, typing.Any]:
        return {'reportType': self.report_type, 'comment': self.comment, '$type': 'com.atproto.admin.defs#modEventReport'}

class ModEventLabel(chitose.Object):
    """Apply/Negate labels on a subject"""

    def __init__(self, create_label_vals: list[str], negate_label_vals: list[str], comment: typing.Optional[str]=None) -> None:
        self.create_label_vals = create_label_vals
        self.negate_label_vals = negate_label_vals
        self.comment = comment

    def to_dict(self) -> dict[str, typing.Any]:
        return {'createLabelVals': self.create_label_vals, 'negateLabelVals': self.negate_label_vals, 'comment': self.comment, '$type': 'com.atproto.admin.defs#modEventLabel'}

class ModEventAcknowledge(chitose.Object):
    """"""

    def __init__(self, comment: typing.Optional[str]=None) -> None:
        self.comment = comment

    def to_dict(self) -> dict[str, typing.Any]:
        return {'comment': self.comment, '$type': 'com.atproto.admin.defs#modEventAcknowledge'}

class ModEventEscalate(chitose.Object):
    """"""

    def __init__(self, comment: typing.Optional[str]=None) -> None:
        self.comment = comment

    def to_dict(self) -> dict[str, typing.Any]:
        return {'comment': self.comment, '$type': 'com.atproto.admin.defs#modEventEscalate'}

class ModEventMute(chitose.Object):
    """Mute incoming reports on a subject


    :param duration_in_hours: Indicates how long the subject should remain muted.
    """

    def __init__(self, duration_in_hours: int, comment: typing.Optional[str]=None) -> None:
        self.duration_in_hours = duration_in_hours
        self.comment = comment

    def to_dict(self) -> dict[str, typing.Any]:
        return {'durationInHours': self.duration_in_hours, 'comment': self.comment, '$type': 'com.atproto.admin.defs#modEventMute'}

class ModEventUnmute(chitose.Object):
    """Unmute action on a subject


    :param comment: Describe reasoning behind the reversal.
    """

    def __init__(self, comment: typing.Optional[str]=None) -> None:
        self.comment = comment

    def to_dict(self) -> dict[str, typing.Any]:
        return {'comment': self.comment, '$type': 'com.atproto.admin.defs#modEventUnmute'}

class ModEventEmail(chitose.Object):
    """Keep a log of outgoing email to a user


    :param subject_line: The subject line of the email sent to the user.

    :param comment: Additional comment about the outgoing comm.
    """

    def __init__(self, subject_line: str, comment: typing.Optional[str]=None) -> None:
        self.subject_line = subject_line
        self.comment = comment

    def to_dict(self) -> dict[str, typing.Any]:
        return {'subjectLine': self.subject_line, 'comment': self.comment, '$type': 'com.atproto.admin.defs#modEventEmail'}

class CommunicationTemplateView(chitose.Object):
    """


    :param name: Name of the template.

    :param content_markdown: Subject of the message, used in emails.

    :param last_updated_by: DID of the user who last updated the template.

    :param subject: Content of the template, can contain markdown and variable placeholders.
    """

    def __init__(self, id: str, name: str, content_markdown: str, disabled: bool, last_updated_by: str, created_at: str, updated_at: str, subject: typing.Optional[str]=None) -> None:
        self.id = id
        self.name = name
        self.content_markdown = content_markdown
        self.disabled = disabled
        self.last_updated_by = last_updated_by
        self.created_at = created_at
        self.updated_at = updated_at
        self.subject = subject

    def to_dict(self) -> dict[str, typing.Any]:
        return {'id': self.id, 'name': self.name, 'contentMarkdown': self.content_markdown, 'disabled': self.disabled, 'lastUpdatedBy': self.last_updated_by, 'createdAt': self.created_at, 'updatedAt': self.updated_at, 'subject': self.subject, '$type': 'com.atproto.admin.defs#communicationTemplateView'}