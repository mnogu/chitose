# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _get_tagged_suggestions(call: chitose.xrpc.XrpcCall) -> bytes:
    """Get a list of suggestions (feeds and users) tagged with categories"""
    return call('app.bsky.unspecced.getTaggedSuggestions', [], None, {})

class Suggestion(chitose.Object):
    """"""

    def __init__(self, tag: str, subject_type: typing.Literal['actor', 'feed'], subject: str) -> None:
        self.tag = tag
        self.subject_type = subject_type
        self.subject = subject

    def to_dict(self) -> dict[str, typing.Any]:
        return {'tag': self.tag, 'subjectType': self.subject_type, 'subject': self.subject, '$type': 'app.bsky.unspecced.getTaggedSuggestions#suggestion'}