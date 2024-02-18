# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import chitose.app.bsky.richtext.facet
import typing

class Facet(chitose.Object):
    """Annotation of a sub-string within rich text."""

    def __init__(self, index: chitose.app.bsky.richtext.facet.ByteSlice, features: list[typing.Union[chitose.app.bsky.richtext.facet.Mention, chitose.app.bsky.richtext.facet.Link, chitose.app.bsky.richtext.facet.Tag]]) -> None:
        self.index = index
        self.features = features

    def to_dict(self) -> dict[str, typing.Any]:
        return {'index': self.index, 'features': self.features, '$type': 'app.bsky.richtext.facet'}

class Mention(chitose.Object):
    """Facet feature for mention of another account. The text is usually a handle, including a '@' prefix, but the facet reference is a DID."""

    def __init__(self, did: str) -> None:
        self.did = did

    def to_dict(self) -> dict[str, typing.Any]:
        return {'did': self.did, '$type': 'app.bsky.richtext.facet#mention'}

class Link(chitose.Object):
    """Facet feature for a URL. The text URL may have been simplified or truncated, but the facet reference should be a complete URL."""

    def __init__(self, uri: str) -> None:
        self.uri = uri

    def to_dict(self) -> dict[str, typing.Any]:
        return {'uri': self.uri, '$type': 'app.bsky.richtext.facet#link'}

class Tag(chitose.Object):
    """Facet feature for a hashtag. The text usually includes a '#' prefix, but the facet reference should not (except in the case of 'double hash tags')."""

    def __init__(self, tag: str) -> None:
        self.tag = tag

    def to_dict(self) -> dict[str, typing.Any]:
        return {'tag': self.tag, '$type': 'app.bsky.richtext.facet#tag'}

class ByteSlice(chitose.Object):
    """Specifies the sub-string range a facet feature applies to. Start index is inclusive, end index is exclusive. Indices are zero-indexed, counting bytes of the UTF-8 encoded text. NOTE: some languages, like Javascript, use UTF-16 or Unicode codepoints for string slice indexing; in these languages, convert to byte arrays before working with facets."""

    def __init__(self, byte_start: int, byte_end: int) -> None:
        self.byte_start = byte_start
        self.byte_end = byte_end

    def to_dict(self) -> dict[str, typing.Any]:
        return {'byteStart': self.byte_start, 'byteEnd': self.byte_end, '$type': 'app.bsky.richtext.facet#byteSlice'}