from __future__ import annotations
import json

from .app import App
from .com import Com
from chitose.com.atproto.server import create_session


class BskyAgent:
    def __init__(self, service: str) -> None:
        self.service = service
        self.headers = {}

    @property
    def app(self):
        return App(self.service, self.headers)

    @property
    def com(self):
        return Com(self.service, self.headers)

    def login(self, identifier: str, password: str) -> None:
        session = json.loads(
            create_session(service=self.service, headers={},
                           identifier=identifier, password=password))
        if 'accessJwt' in session:
            self.headers['authorization'] \
                = f'Bearer {session["accessJwt"]}'
