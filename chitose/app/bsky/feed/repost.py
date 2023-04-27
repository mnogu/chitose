from __future__ import annotations
import chitose
import chitose.com.atproto.repo

class Repost(chitose.Record):

    def __init__(self, subject: chitose.com.atproto.repo.StrongRef, created_at: str) -> None:
        self.subject = subject
        self.created_at = created_at

    def to_dict(self):
        return {'subject': self.subject, 'createdAt': self.created_at}