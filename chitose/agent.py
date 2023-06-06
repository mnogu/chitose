from __future__ import annotations
from datetime import datetime
from datetime import timezone
import typing
import json
import urllib

from chitose.app.bsky.feed.like import Like
from chitose.app.bsky.feed.post import Post
from chitose.app.bsky.feed.repost import Repost
from chitose.app.bsky.graph.follow import Follow
from chitose.com.atproto.repo.strong_ref import StrongRef

from .app import App_
from .com import Com_
from .xrpc import call
from .xrpc import subscribe
from .xrpc import XrpcParams
from .xrpc import XrpcData
from .xrpc import XrpcHandler
from .xrpc import XrpcHeaders


class BskyAgent:
    def __init__(self, service: str) -> None:
        self.service = service
        self.session: dict[str, str] = {}

    def _add_auth_header(self, headers: dict[str, str]) -> dict[str, str]:
        if 'authorization' not in headers and 'accessJwt' in self.session:
            return headers | {
                'authorization': f'Bearer {self.session["accessJwt"]}'
            }

        return headers

    def _refresh_session(self, e: urllib.error.HTTPError) -> None:
        if e.code != 400 or 'refreshJwt' not in self.session:
            raise e

        try:
            obj = json.loads(e.read())
        except json.JSONDecodeError:
            raise e

        if 'error' not in obj:
            raise e

        error = obj['error']
        if error != 'ExpiredToken':
            raise e

        self.session = json.loads(
            call('com.atproto.server.refreshSession',
                 [], {}, self.service,
                 {'authorization':
                  f'Bearer {self.session["refreshJwt"]}'})
        )

    def _call(self, method: str, params: XrpcParams,
              d: XrpcData, headers: XrpcHeaders) -> bytes:
        try:
            return call(method, params, d, self.service,
                        self._add_auth_header(headers))
        except urllib.error.HTTPError as e:
            self._refresh_session(e)

            return call(method, params, d, self.service,
                        self._add_auth_header(headers))

    def _subscribe(self, method: str, params: XrpcParams,
                   handler: XrpcHandler) -> None:
        # https -> wss
        scheme = urllib.parse.urlparse(self.service).scheme
        service = self.service.replace(scheme, 'wss', 1)
        subscribe(method, params, service, handler)

    @property
    def app(self) -> App_:
        return App_(self._call, self._subscribe)

    @property
    def com(self) -> Com_:
        return Com_(self._call, self._subscribe)

    def get_timeline(self, **kwargs: dict[str, typing.Any]) -> bytes:
        """See :doc:`chitose.app.bsky.feed` for available arguments."""
        return self.app.bsky.feed.get_timeline(**kwargs)  # type: ignore[arg-type]

    def get_author_feed(self, **kwargs: dict[str, typing.Any]) -> bytes:
        """See :doc:`chitose.app.bsky.feed` for available arguments."""
        return self.app.bsky.feed.get_author_feed(**kwargs)  # type: ignore[arg-type]

    def get_post_thread(self, **kwargs: dict[str, typing.Any]) -> bytes:
        """See :doc:`chitose.app.bsky.feed` for available arguments."""
        return self.app.bsky.feed.get_post_thread(**kwargs)  # type: ignore[arg-type]

    def get_posts(self, **kwargs: dict[str, typing.Any]) -> bytes:
        """See :doc:`chitose.app.bsky.feed` for available arguments."""
        return self.app.bsky.feed.get_posts(**kwargs)  # type: ignore[arg-type]

    def get_likes(self, **kwargs: dict[str, typing.Any]) -> bytes:
        """See :doc:`chitose.app.bsky.feed` for available arguments."""
        return self.app.bsky.feed.get_likes(**kwargs)  # type: ignore[arg-type]

    def get_reposted_by(self, **kwargs: dict[str, typing.Any]) -> bytes:
        """See :doc:`chitose.app.bsky.feed` for available arguments."""
        return self.app.bsky.feed.get_reposted_by(**kwargs)  # type: ignore[arg-type]

    def get_follows(self, **kwargs: dict[str, typing.Any]) -> bytes:
        """See :doc:`chitose.app.bsky.graph` for available arguments."""
        return self.app.bsky.graph.get_follows(**kwargs)  # type: ignore[arg-type]

    def get_followers(self, **kwargs: dict[str, typing.Any]) -> bytes:
        """See :doc:`chitose.app.bsky.graph` for available arguments."""
        return self.app.bsky.graph.get_followers(**kwargs)  # type: ignore[arg-type]

    def get_profile(self, **kwargs: dict[str, typing.Any]) -> bytes:
        """See :doc:`chitose.app.bsky.actor` for available arguments."""
        return self.app.bsky.actor.get_profile(**kwargs)  # type: ignore[arg-type]

    def get_profiles(self, **kwargs: dict[str, typing.Any]) -> bytes:
        """See :doc:`chitose.app.bsky.actor` for available arguments."""
        return self.app.bsky.actor.get_profiles(**kwargs)  # type: ignore[arg-type]

    def get_suggestions(self, **kwargs: dict[str, typing.Any]) -> bytes:
        """See :doc:`chitose.app.bsky.actor` for available arguments."""
        return self.app.bsky.actor.get_suggestions(**kwargs)  # type: ignore[arg-type]

    def search_actors(self, **kwargs: dict[str, typing.Any]) -> bytes:
        """See :doc:`chitose.app.bsky.actor` for available arguments."""
        return self.app.bsky.actor.search_actors(**kwargs)  # type: ignore[arg-type]

    def search_actors_typeahead(self, **kwargs: dict[str, typing.Any]) -> bytes:
        """See :doc:`chitose.app.bsky.actor` for available arguments."""
        return self.app.bsky.actor.search_actors_typeahead(**kwargs)  # type: ignore[arg-type]

    def list_notifications(self, **kwargs: dict[str, typing.Any]) -> bytes:
        """See :doc:`chitose.app.bsky.notification` for available arguments."""
        return self.app.bsky.notification.list_notifications(**kwargs)  # type: ignore[arg-type]

    def count_unread_notifications(self, **kwargs: dict[str, typing.Any]) -> bytes:
        """See `get_unread_count()` in :doc:`chitose.app.bsky.notification` for available arguments."""
        return self.app.bsky.notification.get_unread_count(**kwargs)  # type: ignore[arg-type]

    def post(self, record: Post) -> bytes:
        if not self.session:
            raise Exception('Not logged in')

        return self.com.atproto.repo.create_record(
            repo=self.session['did'],
            collection='app.bsky.feed.post',
            record=record)

    def _get_did_and_rkey(self, uri: str) -> tuple[str, str]:
        did_name_path = uri.partition('?')[0].partition('//')[2].split('/')
        if len(did_name_path) != 3:
            raise Exception(f'Invalid at uri: {uri}')

        did, _, rkey = did_name_path
        return did, rkey

    def delete_post(self, post_uri: str) -> bytes:
        if not self.session:
            raise Exception('Not logged in')

        did, rkey = self._get_did_and_rkey(post_uri)
        return self.com.atproto.repo.delete_record(
            repo=did,
            collection='app.bsky.feed.post',
            rkey=rkey)

    def like(self, uri: str, cid: str) -> bytes:
        if not self.session:
            raise Exception('Not logged in')

        subject = StrongRef(uri=uri, cid=cid)
        record = Like(subject=subject,
                      created_at=datetime.now(timezone.utc).isoformat())

        return self.com.atproto.repo.create_record(
            repo=self.session['did'],
            collection='app.bsky.feed.like',
            record=record)

    def delete_like(self, like_uri: str) -> bytes:
        if not self.session:
            raise Exception('Not logged in')

        did, rkey = self._get_did_and_rkey(like_uri)
        return self.com.atproto.repo.delete_record(
            repo=did,
            collection='app.bsky.feed.like',
            rkey=rkey)

    def repost(self, uri: str, cid: str) -> bytes:
        if not self.session:
            raise Exception('Not logged in')

        subject = StrongRef(uri=uri, cid=cid)
        record = Repost(subject=subject,
                        created_at=datetime.now(timezone.utc).isoformat())

        return self.com.atproto.repo.create_record(
            repo=self.session['did'],
            collection='app.bsky.feed.repost',
            record=record)

    def delete_repost(self, repost_uri: str) -> bytes:
        if not self.session:
            raise Exception('Not logged in')

        did, rkey = self._get_did_and_rkey(repost_uri)
        return self.com.atproto.repo.delete_record(
            repo=did,
            collection='app.bsky.feed.repost',
            rkey=rkey)

    def follow(self, subject_did: str) -> bytes:
        if not self.session:
            raise Exception('Not logged in')

        record = Follow(subject=subject_did,
                        created_at=datetime.now(timezone.utc).isoformat())

        return self.com.atproto.repo.create_record(
            repo=self.session['did'],
            collection='app.bsky.graph.follow',
            record=record)

    def delete_follow(self, follow_uri: str) -> bytes:
        if not self.session:
            raise Exception('Not logged in')

        did, rkey = self._get_did_and_rkey(follow_uri)
        return self.com.atproto.repo.delete_record(
            repo=did,
            collection='app.bsky.graph.follow',
            rkey=rkey)

    def mute_actor(self, actor: str) -> bytes:
        return self.app.bsky.graph.mute_actor(actor=actor)

    def unmute_actor(self, actor: str) -> bytes:
        return self.app.bsky.graph.unmute_actor(actor=actor)

    def update_seen_notifications(self, seen_at: typing.Optional[str]) -> bytes:
        if seen_at is None:
            seen_at = datetime.now(timezone.utc).isoformat()

        return self.app.bsky.notification.update_seen(seen_at=seen_at)

    def login(self, identifier: str, password: str) -> None:
        self.session = json.loads(
            self.com.atproto.server.create_session(
                identifier=identifier, password=password))
