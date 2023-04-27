from __future__ import annotations
import importlib
from chitose.com.atproto.server import create_session


class BskyAgent:
    def __init__(self, service: str, session=None, name=None) -> None:
        self.service = service
        self.session = {} if session is None else session
        self.name = name

    def __getattr__(self, name) -> BskyAgent:
        return BskyAgent(self.service, self.session,
                         f'chitose.{name}' if self.name is None
                         else f'{self.name}.{name}')

    def __call__(self, *args, **kwargs) -> BskyAgent:
        module_name, _, func_name = self.name.rpartition('.')
        module = importlib.import_module(module_name)
        kwargs['service'] = self.service
        if 'headers' not in kwargs:
            headers = {}
            if 'accessJwt' in self.session:
                headers['authorization'] \
                    = f'Bearer {self.session["accessJwt"]}'

            kwargs['headers'] = headers

        return getattr(module, func_name)(*args, **kwargs)

    def login(self, identifier: str, password: str) -> None:
        self.session = create_session(
            service=self.service, headers={},
            identifier=identifier, password=password)
