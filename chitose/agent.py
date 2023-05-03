from __future__ import annotations
import json

from .app import App_
from .com import Com_


class BskyAgent:
    def __init__(self, service: str) -> None:
        self.service = service
        self.headers: dict[str, str] = {}

    @property
    def app(self):
        return App_(self.service, self.headers)

    @property
    def com(self):
        return Com_(self.service, self.headers)

    def login(self, identifier: str, password: str) -> None:
        session = json.loads(
            self.com.atproto.server.create_session(
                identifier=identifier, password=password))
        if 'accessJwt' in session:
            self.headers['authorization'] \
                = f'Bearer {session["accessJwt"]}'
