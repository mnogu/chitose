from __future__ import annotations
import chitose
import chitose.app.bsky.embed
import chitose.app.bsky.richtext
import chitose.com.atproto.repo
import typing

class Post(chitose.Record):

    def __init__(self, text: str, created_at: str, entities: typing.Optional[list[Entity]]=None, facets: typing.Optional[list[chitose.app.bsky.richtext.Facet]]=None, reply: typing.Optional[ReplyRef]=None, embed: typing.Optional[typing.Union[chitose.app.bsky.embed.Images, chitose.app.bsky.embed.External, chitose.app.bsky.embed.Record, chitose.app.bsky.embed.RecordWithMedia]]=None) -> None:
        self.text = text
        self.created_at = created_at
        self.entities = entities
        self.facets = facets
        self.reply = reply
        self.embed = embed

    def to_dict(self):
        return {'text': self.text, 'createdAt': self.created_at, 'entities': self.entities, 'facets': self.facets, 'reply': self.reply, 'embed': self.embed}

class ReplyRef(chitose.Object):

    def __init__(self, root: chitose.com.atproto.repo.StrongRef, parent: chitose.com.atproto.repo.StrongRef) -> None:
        self.root = root
        self.parent = parent

    def to_dict(self):
        return {'root': self.root, 'parent': self.parent}

class Entity(chitose.Object):

    def __init__(self, index: TextSlice, type: str, value: str) -> None:
        self.index = index
        self.type = type
        self.value = value

    def to_dict(self):
        return {'index': self.index, 'type': self.type, 'value': self.value}

class TextSlice(chitose.Object):

    def __init__(self, start: int, end: int) -> None:
        self.start = start
        self.end = end

    def to_dict(self):
        return {'start': self.start, 'end': self.end}