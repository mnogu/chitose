# GENERATED CODE - DO NOT MODIFY
from __future__ import annotations
from chitose.xrpc import XrpcCall
from chitose.xrpc import XrpcSubscribe
from .admin import Admin_
from .identity import Identity_
from .label import Label_
from .moderation import Moderation_
from .repo import Repo_
from .server import Server_
from .sync import Sync_
from .temp import Temp_

class Atproto_:
    """We recommend calling methods in this class via the :doc:`chitose.BskyAgent <chitose>` class instead of creating instances of this class directly."""

    def __init__(self, call: XrpcCall, subscribe: XrpcSubscribe) -> None:
        self.call = call
        self.subscribe = subscribe

    @property
    def admin(self) -> Admin_:
        return Admin_(self.call, self.subscribe)

    @property
    def identity(self) -> Identity_:
        return Identity_(self.call, self.subscribe)

    @property
    def label(self) -> Label_:
        return Label_(self.call, self.subscribe)

    @property
    def moderation(self) -> Moderation_:
        return Moderation_(self.call, self.subscribe)

    @property
    def repo(self) -> Repo_:
        return Repo_(self.call, self.subscribe)

    @property
    def server(self) -> Server_:
        return Server_(self.call, self.subscribe)

    @property
    def sync(self) -> Sync_:
        return Sync_(self.call, self.subscribe)

    @property
    def temp(self) -> Temp_:
        return Temp_(self.call, self.subscribe)