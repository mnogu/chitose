# GENERATED CODE - DO NOT MODIFY
from __future__ import annotations
from chitose.xrpc import XrpcCall
from chitose.xrpc import XrpcSubscribe
from .communication import Communication_
from .moderation import Moderation_
from .server import Server_
from .team import Team_

class Ozone_:
    """We recommend calling methods in this class via the :doc:`chitose.BskyAgent <chitose>` class instead of creating instances of this class directly."""

    def __init__(self, call: XrpcCall, subscribe: XrpcSubscribe) -> None:
        self.call = call
        self.subscribe = subscribe

    @property
    def communication(self) -> Communication_:
        return Communication_(self.call, self.subscribe)

    @property
    def moderation(self) -> Moderation_:
        return Moderation_(self.call, self.subscribe)

    @property
    def server(self) -> Server_:
        return Server_(self.call, self.subscribe)

    @property
    def team(self) -> Team_:
        return Team_(self.call, self.subscribe)