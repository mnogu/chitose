# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import chitose.com.atproto.admin.defs
import chitose.com.atproto.label.defs
import chitose.com.atproto.moderation.defs
import chitose.com.atproto.repo.strong_ref
import chitose.com.atproto.server.defs
import chitose.tools.ozone.moderation.defs
import typing

class ModEventView(chitose.Object):
    """"""

    def __init__(self, id: int, event: typing.Union[chitose.tools.ozone.moderation.defs.ModEventTakedown, chitose.tools.ozone.moderation.defs.ModEventReverseTakedown, chitose.tools.ozone.moderation.defs.ModEventComment, chitose.tools.ozone.moderation.defs.ModEventReport, chitose.tools.ozone.moderation.defs.ModEventLabel, chitose.tools.ozone.moderation.defs.ModEventAcknowledge, chitose.tools.ozone.moderation.defs.ModEventEscalate, chitose.tools.ozone.moderation.defs.ModEventMute, chitose.tools.ozone.moderation.defs.ModEventUnmute, chitose.tools.ozone.moderation.defs.ModEventMuteReporter, chitose.tools.ozone.moderation.defs.ModEventUnmuteReporter, chitose.tools.ozone.moderation.defs.ModEventEmail, chitose.tools.ozone.moderation.defs.ModEventResolveAppeal, chitose.tools.ozone.moderation.defs.ModEventDivert], subject: typing.Union[chitose.com.atproto.admin.defs.RepoRef, chitose.com.atproto.repo.strong_ref.StrongRef], subject_blob_cids: list[str], created_by: str, created_at: str, creator_handle: typing.Optional[str]=None, subject_handle: typing.Optional[str]=None) -> None:
        self.id = id
        self.event = event
        self.subject = subject
        self.subject_blob_cids = subject_blob_cids
        self.created_by = created_by
        self.created_at = created_at
        self.creator_handle = creator_handle
        self.subject_handle = subject_handle

    def to_dict(self) -> dict[str, typing.Any]:
        return {'id': self.id, 'event': self.event, 'subject': self.subject, 'subjectBlobCids': self.subject_blob_cids, 'createdBy': self.created_by, 'createdAt': self.created_at, 'creatorHandle': self.creator_handle, 'subjectHandle': self.subject_handle, '$type': 'tools.ozone.moderation.defs#modEventView'}

class ModEventViewDetail(chitose.Object):
    """"""

    def __init__(self, id: int, event: typing.Union[chitose.tools.ozone.moderation.defs.ModEventTakedown, chitose.tools.ozone.moderation.defs.ModEventReverseTakedown, chitose.tools.ozone.moderation.defs.ModEventComment, chitose.tools.ozone.moderation.defs.ModEventReport, chitose.tools.ozone.moderation.defs.ModEventLabel, chitose.tools.ozone.moderation.defs.ModEventAcknowledge, chitose.tools.ozone.moderation.defs.ModEventEscalate, chitose.tools.ozone.moderation.defs.ModEventMute, chitose.tools.ozone.moderation.defs.ModEventUnmute, chitose.tools.ozone.moderation.defs.ModEventMuteReporter, chitose.tools.ozone.moderation.defs.ModEventUnmuteReporter, chitose.tools.ozone.moderation.defs.ModEventEmail, chitose.tools.ozone.moderation.defs.ModEventResolveAppeal, chitose.tools.ozone.moderation.defs.ModEventDivert], subject: typing.Union[chitose.tools.ozone.moderation.defs.RepoView, chitose.tools.ozone.moderation.defs.RepoViewNotFound, chitose.tools.ozone.moderation.defs.RecordView, chitose.tools.ozone.moderation.defs.RecordViewNotFound], subject_blobs: list[chitose.tools.ozone.moderation.defs.BlobView], created_by: str, created_at: str) -> None:
        self.id = id
        self.event = event
        self.subject = subject
        self.subject_blobs = subject_blobs
        self.created_by = created_by
        self.created_at = created_at

    def to_dict(self) -> dict[str, typing.Any]:
        return {'id': self.id, 'event': self.event, 'subject': self.subject, 'subjectBlobs': self.subject_blobs, 'createdBy': self.created_by, 'createdAt': self.created_at, '$type': 'tools.ozone.moderation.defs#modEventViewDetail'}

class SubjectStatusView(chitose.Object):
    """


    :param updated_at: Timestamp referencing when the last update was made to the moderation status of the subject

    :param created_at: Timestamp referencing the first moderation status impacting event was emitted on the subject

    :param comment: Sticky comment on the subject.

    :param last_appealed_at: Timestamp referencing when the author of the subject appealed a moderation action

    :param appealed: True indicates that the a previously taken moderator action was appealed against, by the author of the content. False indicates last appeal was resolved by moderators.
    """

    def __init__(self, id: int, subject: typing.Union[chitose.com.atproto.admin.defs.RepoRef, chitose.com.atproto.repo.strong_ref.StrongRef], updated_at: str, created_at: str, review_state: chitose.tools.ozone.moderation.defs.SubjectReviewState, subject_blob_cids: typing.Optional[list[str]]=None, subject_repo_handle: typing.Optional[str]=None, comment: typing.Optional[str]=None, mute_until: typing.Optional[str]=None, mute_reporting_until: typing.Optional[str]=None, last_reviewed_by: typing.Optional[str]=None, last_reviewed_at: typing.Optional[str]=None, last_reported_at: typing.Optional[str]=None, last_appealed_at: typing.Optional[str]=None, takendown: typing.Optional[bool]=None, appealed: typing.Optional[bool]=None, suspend_until: typing.Optional[str]=None, tags: typing.Optional[list[str]]=None) -> None:
        self.id = id
        self.subject = subject
        self.updated_at = updated_at
        self.created_at = created_at
        self.review_state = review_state
        self.subject_blob_cids = subject_blob_cids
        self.subject_repo_handle = subject_repo_handle
        self.comment = comment
        self.mute_until = mute_until
        self.mute_reporting_until = mute_reporting_until
        self.last_reviewed_by = last_reviewed_by
        self.last_reviewed_at = last_reviewed_at
        self.last_reported_at = last_reported_at
        self.last_appealed_at = last_appealed_at
        self.takendown = takendown
        self.appealed = appealed
        self.suspend_until = suspend_until
        self.tags = tags

    def to_dict(self) -> dict[str, typing.Any]:
        return {'id': self.id, 'subject': self.subject, 'updatedAt': self.updated_at, 'createdAt': self.created_at, 'reviewState': self.review_state, 'subjectBlobCids': self.subject_blob_cids, 'subjectRepoHandle': self.subject_repo_handle, 'comment': self.comment, 'muteUntil': self.mute_until, 'muteReportingUntil': self.mute_reporting_until, 'lastReviewedBy': self.last_reviewed_by, 'lastReviewedAt': self.last_reviewed_at, 'lastReportedAt': self.last_reported_at, 'lastAppealedAt': self.last_appealed_at, 'takendown': self.takendown, 'appealed': self.appealed, 'suspendUntil': self.suspend_until, 'tags': self.tags, '$type': 'tools.ozone.moderation.defs#subjectStatusView'}
SubjectReviewState = typing.Literal['#reviewOpen', '#reviewEscalated', '#reviewClosed', '#reviewNone']
REVIEW_OPEN = 'tools.ozone.moderation.defs#reviewOpen'
REVIEW_ESCALATED = 'tools.ozone.moderation.defs#reviewEscalated'
REVIEW_CLOSED = 'tools.ozone.moderation.defs#reviewClosed'
REVIEW_NONE = 'tools.ozone.moderation.defs#reviewNone'

class ModEventTakedown(chitose.Object):
    """Take down a subject permanently or temporarily


    :param duration_in_hours: Indicates how long the takedown should be in effect before automatically expiring.
    """

    def __init__(self, comment: typing.Optional[str]=None, duration_in_hours: typing.Optional[int]=None) -> None:
        self.comment = comment
        self.duration_in_hours = duration_in_hours

    def to_dict(self) -> dict[str, typing.Any]:
        return {'comment': self.comment, 'durationInHours': self.duration_in_hours, '$type': 'tools.ozone.moderation.defs#modEventTakedown'}

class ModEventReverseTakedown(chitose.Object):
    """Revert take down action on a subject


    :param comment: Describe reasoning behind the reversal.
    """

    def __init__(self, comment: typing.Optional[str]=None) -> None:
        self.comment = comment

    def to_dict(self) -> dict[str, typing.Any]:
        return {'comment': self.comment, '$type': 'tools.ozone.moderation.defs#modEventReverseTakedown'}

class ModEventResolveAppeal(chitose.Object):
    """Resolve appeal on a subject


    :param comment: Describe resolution.
    """

    def __init__(self, comment: typing.Optional[str]=None) -> None:
        self.comment = comment

    def to_dict(self) -> dict[str, typing.Any]:
        return {'comment': self.comment, '$type': 'tools.ozone.moderation.defs#modEventResolveAppeal'}

class ModEventComment(chitose.Object):
    """Add a comment to a subject


    :param sticky: Make the comment persistent on the subject
    """

    def __init__(self, comment: str, sticky: typing.Optional[bool]=None) -> None:
        self.comment = comment
        self.sticky = sticky

    def to_dict(self) -> dict[str, typing.Any]:
        return {'comment': self.comment, 'sticky': self.sticky, '$type': 'tools.ozone.moderation.defs#modEventComment'}

class ModEventReport(chitose.Object):
    """Report a subject


    :param is_reporter_muted: Set to true if the reporter was muted from reporting at the time of the event. These reports won't impact the reviewState of the subject.
    """

    def __init__(self, report_type: chitose.com.atproto.moderation.defs.ReasonType, comment: typing.Optional[str]=None, is_reporter_muted: typing.Optional[bool]=None) -> None:
        self.report_type = report_type
        self.comment = comment
        self.is_reporter_muted = is_reporter_muted

    def to_dict(self) -> dict[str, typing.Any]:
        return {'reportType': self.report_type, 'comment': self.comment, 'isReporterMuted': self.is_reporter_muted, '$type': 'tools.ozone.moderation.defs#modEventReport'}

class ModEventLabel(chitose.Object):
    """Apply/Negate labels on a subject"""

    def __init__(self, create_label_vals: list[str], negate_label_vals: list[str], comment: typing.Optional[str]=None) -> None:
        self.create_label_vals = create_label_vals
        self.negate_label_vals = negate_label_vals
        self.comment = comment

    def to_dict(self) -> dict[str, typing.Any]:
        return {'createLabelVals': self.create_label_vals, 'negateLabelVals': self.negate_label_vals, 'comment': self.comment, '$type': 'tools.ozone.moderation.defs#modEventLabel'}

class ModEventAcknowledge(chitose.Object):
    """"""

    def __init__(self, comment: typing.Optional[str]=None) -> None:
        self.comment = comment

    def to_dict(self) -> dict[str, typing.Any]:
        return {'comment': self.comment, '$type': 'tools.ozone.moderation.defs#modEventAcknowledge'}

class ModEventEscalate(chitose.Object):
    """"""

    def __init__(self, comment: typing.Optional[str]=None) -> None:
        self.comment = comment

    def to_dict(self) -> dict[str, typing.Any]:
        return {'comment': self.comment, '$type': 'tools.ozone.moderation.defs#modEventEscalate'}

class ModEventMute(chitose.Object):
    """Mute incoming reports on a subject


    :param duration_in_hours: Indicates how long the subject should remain muted.
    """

    def __init__(self, duration_in_hours: int, comment: typing.Optional[str]=None) -> None:
        self.duration_in_hours = duration_in_hours
        self.comment = comment

    def to_dict(self) -> dict[str, typing.Any]:
        return {'durationInHours': self.duration_in_hours, 'comment': self.comment, '$type': 'tools.ozone.moderation.defs#modEventMute'}

class ModEventUnmute(chitose.Object):
    """Unmute action on a subject


    :param comment: Describe reasoning behind the reversal.
    """

    def __init__(self, comment: typing.Optional[str]=None) -> None:
        self.comment = comment

    def to_dict(self) -> dict[str, typing.Any]:
        return {'comment': self.comment, '$type': 'tools.ozone.moderation.defs#modEventUnmute'}

class ModEventMuteReporter(chitose.Object):
    """Mute incoming reports from an account


    :param duration_in_hours: Indicates how long the account should remain muted.
    """

    def __init__(self, duration_in_hours: int, comment: typing.Optional[str]=None) -> None:
        self.duration_in_hours = duration_in_hours
        self.comment = comment

    def to_dict(self) -> dict[str, typing.Any]:
        return {'durationInHours': self.duration_in_hours, 'comment': self.comment, '$type': 'tools.ozone.moderation.defs#modEventMuteReporter'}

class ModEventUnmuteReporter(chitose.Object):
    """Unmute incoming reports from an account


    :param comment: Describe reasoning behind the reversal.
    """

    def __init__(self, comment: typing.Optional[str]=None) -> None:
        self.comment = comment

    def to_dict(self) -> dict[str, typing.Any]:
        return {'comment': self.comment, '$type': 'tools.ozone.moderation.defs#modEventUnmuteReporter'}

class ModEventEmail(chitose.Object):
    """Keep a log of outgoing email to a user


    :param subject_line: The subject line of the email sent to the user.

    :param content: The content of the email sent to the user.

    :param comment: Additional comment about the outgoing comm.
    """

    def __init__(self, subject_line: str, content: typing.Optional[str]=None, comment: typing.Optional[str]=None) -> None:
        self.subject_line = subject_line
        self.content = content
        self.comment = comment

    def to_dict(self) -> dict[str, typing.Any]:
        return {'subjectLine': self.subject_line, 'content': self.content, 'comment': self.comment, '$type': 'tools.ozone.moderation.defs#modEventEmail'}

class ModEventDivert(chitose.Object):
    """Divert a record's blobs to a 3rd party service for further scanning/tagging"""

    def __init__(self, comment: typing.Optional[str]=None) -> None:
        self.comment = comment

    def to_dict(self) -> dict[str, typing.Any]:
        return {'comment': self.comment, '$type': 'tools.ozone.moderation.defs#modEventDivert'}

class ModEventTag(chitose.Object):
    """Add/Remove a tag on a subject


    :param add: Tags to be added to the subject. If already exists, won't be duplicated.

    :param remove: Tags to be removed to the subject. Ignores a tag If it doesn't exist, won't be duplicated.

    :param comment: Additional comment about added/removed tags.
    """

    def __init__(self, add: list[str], remove: list[str], comment: typing.Optional[str]=None) -> None:
        self.add = add
        self.remove = remove
        self.comment = comment

    def to_dict(self) -> dict[str, typing.Any]:
        return {'add': self.add, 'remove': self.remove, 'comment': self.comment, '$type': 'tools.ozone.moderation.defs#modEventTag'}

class RepoView(chitose.Object):
    """"""

    def __init__(self, did: str, handle: str, related_records: list[typing.Any], indexed_at: str, moderation: chitose.tools.ozone.moderation.defs.Moderation, email: typing.Optional[str]=None, invited_by: typing.Optional[chitose.com.atproto.server.defs.InviteCode]=None, invites_disabled: typing.Optional[bool]=None, invite_note: typing.Optional[str]=None) -> None:
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
        return {'did': self.did, 'handle': self.handle, 'relatedRecords': self.related_records, 'indexedAt': self.indexed_at, 'moderation': self.moderation, 'email': self.email, 'invitedBy': self.invited_by, 'invitesDisabled': self.invites_disabled, 'inviteNote': self.invite_note, '$type': 'tools.ozone.moderation.defs#repoView'}

class RepoViewDetail(chitose.Object):
    """"""

    def __init__(self, did: str, handle: str, related_records: list[typing.Any], indexed_at: str, moderation: chitose.tools.ozone.moderation.defs.ModerationDetail, email: typing.Optional[str]=None, labels: typing.Optional[list[chitose.com.atproto.label.defs.Label]]=None, invited_by: typing.Optional[chitose.com.atproto.server.defs.InviteCode]=None, invites: typing.Optional[list[chitose.com.atproto.server.defs.InviteCode]]=None, invites_disabled: typing.Optional[bool]=None, invite_note: typing.Optional[str]=None, email_confirmed_at: typing.Optional[str]=None) -> None:
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
        return {'did': self.did, 'handle': self.handle, 'relatedRecords': self.related_records, 'indexedAt': self.indexed_at, 'moderation': self.moderation, 'email': self.email, 'labels': self.labels, 'invitedBy': self.invited_by, 'invites': self.invites, 'invitesDisabled': self.invites_disabled, 'inviteNote': self.invite_note, 'emailConfirmedAt': self.email_confirmed_at, '$type': 'tools.ozone.moderation.defs#repoViewDetail'}

class RepoViewNotFound(chitose.Object):
    """"""

    def __init__(self, did: str) -> None:
        self.did = did

    def to_dict(self) -> dict[str, typing.Any]:
        return {'did': self.did, '$type': 'tools.ozone.moderation.defs#repoViewNotFound'}

class RecordView(chitose.Object):
    """"""

    def __init__(self, uri: str, cid: str, value: typing.Any, blob_cids: list[str], indexed_at: str, moderation: chitose.tools.ozone.moderation.defs.Moderation, repo: chitose.tools.ozone.moderation.defs.RepoView) -> None:
        self.uri = uri
        self.cid = cid
        self.value = value
        self.blob_cids = blob_cids
        self.indexed_at = indexed_at
        self.moderation = moderation
        self.repo = repo

    def to_dict(self) -> dict[str, typing.Any]:
        return {'uri': self.uri, 'cid': self.cid, 'value': self.value, 'blobCids': self.blob_cids, 'indexedAt': self.indexed_at, 'moderation': self.moderation, 'repo': self.repo, '$type': 'tools.ozone.moderation.defs#recordView'}

class RecordViewDetail(chitose.Object):
    """"""

    def __init__(self, uri: str, cid: str, value: typing.Any, blobs: list[chitose.tools.ozone.moderation.defs.BlobView], indexed_at: str, moderation: chitose.tools.ozone.moderation.defs.ModerationDetail, repo: chitose.tools.ozone.moderation.defs.RepoView, labels: typing.Optional[list[chitose.com.atproto.label.defs.Label]]=None) -> None:
        self.uri = uri
        self.cid = cid
        self.value = value
        self.blobs = blobs
        self.indexed_at = indexed_at
        self.moderation = moderation
        self.repo = repo
        self.labels = labels

    def to_dict(self) -> dict[str, typing.Any]:
        return {'uri': self.uri, 'cid': self.cid, 'value': self.value, 'blobs': self.blobs, 'indexedAt': self.indexed_at, 'moderation': self.moderation, 'repo': self.repo, 'labels': self.labels, '$type': 'tools.ozone.moderation.defs#recordViewDetail'}

class RecordViewNotFound(chitose.Object):
    """"""

    def __init__(self, uri: str) -> None:
        self.uri = uri

    def to_dict(self) -> dict[str, typing.Any]:
        return {'uri': self.uri, '$type': 'tools.ozone.moderation.defs#recordViewNotFound'}

class Moderation(chitose.Object):
    """"""

    def __init__(self, subject_status: typing.Optional[chitose.tools.ozone.moderation.defs.SubjectStatusView]=None) -> None:
        self.subject_status = subject_status

    def to_dict(self) -> dict[str, typing.Any]:
        return {'subjectStatus': self.subject_status, '$type': 'tools.ozone.moderation.defs#moderation'}

class ModerationDetail(chitose.Object):
    """"""

    def __init__(self, subject_status: typing.Optional[chitose.tools.ozone.moderation.defs.SubjectStatusView]=None) -> None:
        self.subject_status = subject_status

    def to_dict(self) -> dict[str, typing.Any]:
        return {'subjectStatus': self.subject_status, '$type': 'tools.ozone.moderation.defs#moderationDetail'}

class BlobView(chitose.Object):
    """"""

    def __init__(self, cid: str, mime_type: str, size: int, created_at: str, details: typing.Optional[typing.Union[chitose.tools.ozone.moderation.defs.ImageDetails, chitose.tools.ozone.moderation.defs.VideoDetails]]=None, moderation: typing.Optional[chitose.tools.ozone.moderation.defs.Moderation]=None) -> None:
        self.cid = cid
        self.mime_type = mime_type
        self.size = size
        self.created_at = created_at
        self.details = details
        self.moderation = moderation

    def to_dict(self) -> dict[str, typing.Any]:
        return {'cid': self.cid, 'mimeType': self.mime_type, 'size': self.size, 'createdAt': self.created_at, 'details': self.details, 'moderation': self.moderation, '$type': 'tools.ozone.moderation.defs#blobView'}

class ImageDetails(chitose.Object):
    """"""

    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

    def to_dict(self) -> dict[str, typing.Any]:
        return {'width': self.width, 'height': self.height, '$type': 'tools.ozone.moderation.defs#imageDetails'}

class VideoDetails(chitose.Object):
    """"""

    def __init__(self, width: int, height: int, length: int) -> None:
        self.width = width
        self.height = height
        self.length = length

    def to_dict(self) -> dict[str, typing.Any]:
        return {'width': self.width, 'height': self.height, 'length': self.length, '$type': 'tools.ozone.moderation.defs#videoDetails'}