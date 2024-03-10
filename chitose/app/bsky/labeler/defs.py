# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import chitose.app.bsky.actor.defs
import chitose.app.bsky.labeler.defs
import chitose.com.atproto.label.defs
import typing

class LabelerView(chitose.Object):
    """"""

    def __init__(self, uri: str, cid: str, creator: chitose.app.bsky.actor.defs.ProfileView, indexed_at: str, like_count: typing.Optional[int]=None, viewer: typing.Optional[chitose.app.bsky.labeler.defs.LabelerViewerState]=None, labels: typing.Optional[list[chitose.com.atproto.label.defs.Label]]=None) -> None:
        self.uri = uri
        self.cid = cid
        self.creator = creator
        self.indexed_at = indexed_at
        self.like_count = like_count
        self.viewer = viewer
        self.labels = labels

    def to_dict(self) -> dict[str, typing.Any]:
        return {'uri': self.uri, 'cid': self.cid, 'creator': self.creator, 'indexedAt': self.indexed_at, 'likeCount': self.like_count, 'viewer': self.viewer, 'labels': self.labels, '$type': 'app.bsky.labeler.defs#labelerView'}

class LabelerViewDetailed(chitose.Object):
    """"""

    def __init__(self, uri: str, cid: str, creator: chitose.app.bsky.actor.defs.ProfileView, policies: chitose.app.bsky.labeler.defs.LabelerPolicies, indexed_at: str, like_count: typing.Optional[int]=None, viewer: typing.Optional[chitose.app.bsky.labeler.defs.LabelerViewerState]=None, labels: typing.Optional[list[chitose.com.atproto.label.defs.Label]]=None) -> None:
        self.uri = uri
        self.cid = cid
        self.creator = creator
        self.policies = policies
        self.indexed_at = indexed_at
        self.like_count = like_count
        self.viewer = viewer
        self.labels = labels

    def to_dict(self) -> dict[str, typing.Any]:
        return {'uri': self.uri, 'cid': self.cid, 'creator': self.creator, 'policies': self.policies, 'indexedAt': self.indexed_at, 'likeCount': self.like_count, 'viewer': self.viewer, 'labels': self.labels, '$type': 'app.bsky.labeler.defs#labelerViewDetailed'}

class LabelerViewerState(chitose.Object):
    """"""

    def __init__(self, like: typing.Optional[str]=None) -> None:
        self.like = like

    def to_dict(self) -> dict[str, typing.Any]:
        return {'like': self.like, '$type': 'app.bsky.labeler.defs#labelerViewerState'}

class LabelerPolicies(chitose.Object):
    """


    :param label_values: The label values which this labeler publishes. May include global or custom labels.

    :param label_value_definitions: Label values created by this labeler and scoped exclusively to it. Labels defined here will override global label definitions for this labeler.
    """

    def __init__(self, label_values: list[chitose.com.atproto.label.defs.LabelValue], label_value_definitions: typing.Optional[list[chitose.com.atproto.label.defs.LabelValueDefinition]]=None) -> None:
        self.label_values = label_values
        self.label_value_definitions = label_value_definitions

    def to_dict(self) -> dict[str, typing.Any]:
        return {'labelValues': self.label_values, 'labelValueDefinitions': self.label_value_definitions, '$type': 'app.bsky.labeler.defs#labelerPolicies'}