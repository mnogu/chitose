# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import chitose.app.bsky.labeler.defs
import chitose.com.atproto.label.defs
import typing

class Service(chitose.Record):
    """"""

    def __init__(self, policies: chitose.app.bsky.labeler.defs.LabelerPolicies, created_at: str, labels: typing.Optional[chitose.com.atproto.label.defs.SelfLabels]=None) -> None:
        self.policies = policies
        self.created_at = created_at
        self.labels = labels

    def to_dict(self) -> dict[str, typing.Any]:
        return {'policies': self.policies, 'createdAt': self.created_at, 'labels': self.labels, '$type': 'app.bsky.labeler.service'}