# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import chitose.com.atproto.repo.strong_ref

class Like(chitose.Record):
    """"""

    def __init__(self, subject: chitose.com.atproto.repo.strong_ref.StrongRef, created_at: str) -> None:
        self.subject = subject
        self.created_at = created_at

    def to_dict(self) -> dict:
        return {'subject': self.subject, 'createdAt': self.created_at, '$type': 'app.bsky.feed.like'}