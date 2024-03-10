# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import chitose.com.atproto.label.defs
import typing

class Label(chitose.Object):
    """Metadata tag on an atproto resource (eg, repo or record).


    :param src: DID of the actor who created this label.

    :param uri: AT URI of the record, repository (account), or other resource that this label applies to.

    :param val: The short string name of the value or type of this label.

    :param cts: Timestamp when this label was created.

    :param ver: The AT Protocol version of the label object.

    :param cid: Optionally, CID specifying the specific version of 'uri' resource this label applies to.

    :param neg: If true, this is a negation label, overwriting a previous label.

    :param exp: Timestamp at which this label expires (no longer applies).

    :param sig: Signature of dag-cbor encoded label.
    """

    def __init__(self, src: str, uri: str, val: str, cts: str, ver: typing.Optional[int]=None, cid: typing.Optional[str]=None, neg: typing.Optional[bool]=None, exp: typing.Optional[str]=None, sig: typing.Optional[typing.Any]=None) -> None:
        self.src = src
        self.uri = uri
        self.val = val
        self.cts = cts
        self.ver = ver
        self.cid = cid
        self.neg = neg
        self.exp = exp
        self.sig = sig

    def to_dict(self) -> dict[str, typing.Any]:
        return {'src': self.src, 'uri': self.uri, 'val': self.val, 'cts': self.cts, 'ver': self.ver, 'cid': self.cid, 'neg': self.neg, 'exp': self.exp, 'sig': self.sig, '$type': 'com.atproto.label.defs#label'}

class SelfLabels(chitose.Object):
    """Metadata tags on an atproto record, published by the author within the record."""

    def __init__(self, values: list[chitose.com.atproto.label.defs.SelfLabel]) -> None:
        self.values = values

    def to_dict(self) -> dict[str, typing.Any]:
        return {'values': self.values, '$type': 'com.atproto.label.defs#selfLabels'}

class SelfLabel(chitose.Object):
    """Metadata tag on an atproto record, published by the author within the record. Note that schemas should use #selfLabels, not #selfLabel.


    :param val: The short string name of the value or type of this label.
    """

    def __init__(self, val: str) -> None:
        self.val = val

    def to_dict(self) -> dict[str, typing.Any]:
        return {'val': self.val, '$type': 'com.atproto.label.defs#selfLabel'}

class LabelValueDefinition(chitose.Object):
    """Declares a label value and its expected interpertations and behaviors.


    :param identifier: The value of the label being defined. Must only include lowercase ascii and the '-' character ([a-z-]+).

    :param severity: How should a client visually convey this label? 'inform' means neutral and informational; 'alert' means negative and warning; 'none' means show nothing.

    :param blurs: What should this label hide in the UI, if applied? 'content' hides all of the target; 'media' hides the images/video/audio; 'none' hides nothing.
    """

    def __init__(self, identifier: str, severity: typing.Literal['inform', 'alert', 'none'], blurs: typing.Literal['content', 'media', 'none'], locales: list[chitose.com.atproto.label.defs.LabelValueDefinitionStrings]) -> None:
        self.identifier = identifier
        self.severity = severity
        self.blurs = blurs
        self.locales = locales

    def to_dict(self) -> dict[str, typing.Any]:
        return {'identifier': self.identifier, 'severity': self.severity, 'blurs': self.blurs, 'locales': self.locales, '$type': 'com.atproto.label.defs#labelValueDefinition'}

class LabelValueDefinitionStrings(chitose.Object):
    """Strings which describe the label in the UI, localized into a specific language.


    :param lang: The code of the language these strings are written in.

    :param name: A short human-readable name for the label.

    :param description: A longer description of what the label means and why it might be applied.
    """

    def __init__(self, lang: str, name: str, description: str) -> None:
        self.lang = lang
        self.name = name
        self.description = description

    def to_dict(self) -> dict[str, typing.Any]:
        return {'lang': self.lang, 'name': self.name, 'description': self.description, '$type': 'com.atproto.label.defs#labelValueDefinitionStrings'}
LabelValue = typing.Literal['!hide', '!no-promote', '!warn', '!no-unauthenticated', 'dmca-violation', 'doxxing', 'porn', 'sexual', 'nudity', 'nsfl', 'gore']