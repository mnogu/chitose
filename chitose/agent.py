from __future__ import annotations
import json

from .app import _App
from .com import _Com


class BskyAgent:
    def __init__(self, service: str) -> None:
        self.service = service
        self.headers = {}

    @property
    def app(self):
        return _App(self.service, self.headers)

    @property
    def com(self):
        return _Com(self.service, self.headers)

    def login(self, identifier: str, password: str) -> None:
        session = json.loads(
            self.com.atproto.server.create_session(
                identifier=identifier, password=password))
        if 'accessJwt' in session:
            self.headers['authorization'] \
                = f'Bearer {session["accessJwt"]}'
