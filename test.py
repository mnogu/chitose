from datetime import datetime
import argparse
import json
import os
import sys

from chitose.agent import BskyAgent
from chitose.app.bsky.feed.post import Post
from chitose.app.bsky.feed.repost import Repost
from chitose.com.atproto.repo.strong_ref import StrongRef


def _create_agent() -> BskyAgent:
    config_path = _config_path()
    with open(config_path) as f:
        cfg = json.load(f)

    agent = BskyAgent(service=cfg['service'])
    agent.login(identifier=cfg['identifier'], password=cfg['password'])
    return agent


def _config_parent_dir() -> str:
    config_home = os.getenv('XDG_CONFIG_HOME')
    if config_home is not None:
        return os.path.join(config_home)

    home = os.getenv("HOME")
    if home is None:
        print('XDG_CONFIG_HOME and HOME do not exist', sys.stderr)
        sys.exit(1)
    return os.path.join(home, '.config')


def _config_path() -> str:
    return os.path.join(_config_parent_dir(), 'chitose', 'config.json')


def _login(args: argparse.Namespace) -> None:
    cfg = {
        'service': args.service,
        'identifier': args.identifier,
        'password': args.password,
    }
    config_path = _config_path()
    os.makedirs(os.path.dirname(config_path), exist_ok=True)
    with open(config_path, 'w') as f:
        json.dump(cfg, f, indent=2)


def _print_response(response: bytes) -> None:
    print(json.dumps(json.loads(response), indent=2))


def _get_timeline(args: argparse.Namespace) -> None:
    agent = _create_agent()
    response = agent.app.bsky.feed.get_timeline(
        algorithm=args.algorithm, limit=args.limit, cursor=args.cursor)

    _print_response(response)


def _get_profiles(args: argparse.Namespace) -> None:
    agent = _create_agent()
    response = agent.app.bsky.actor.get_profiles(actors=args.actors)

    _print_response(response)


def _post(args: argparse.Namespace) -> None:
    record = Post(text=args.text, entities=args.entities,
                  facets=args.facets, reply=args.reply,
                  embed=args.embed, created_at=args.created_at)
    agent = _create_agent()
    response = agent.com.atproto.repo.create_record(
        repo=args.repo, collection=args.collection, rkey=args.rkey,
        validate=args.validate, record=record, swap_commit=args.swap_commit)

    _print_response(response)


def _repost(args: argparse.Namespace) -> None:
    subject = StrongRef(uri=args.uri, cid=args.cid)
    record = Repost(subject=subject, created_at=args.created_at)
    agent = _create_agent()
    response = agent.com.atproto.repo.create_record(
        repo=args.repo, collection=args.collection, rkey=args.rkey,
        validate=args.validate, record=record, swap_commit=args.swap_commit)

    _print_response(response)


def main() -> None:
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(required=True)

    parser_login = subparsers.add_parser('login')
    parser_login.add_argument('--identifier')
    parser_login.add_argument('--password')
    parser_login.add_argument('--service', default='https://bsky.social')
    parser_login.set_defaults(func=_login)

    parser_get_timeline = subparsers.add_parser('get-timeline')
    parser_get_timeline.add_argument('--algorithm', default=None)
    parser_get_timeline.add_argument('--limit', default=None)
    parser_get_timeline.add_argument('--cursor', default=None)
    parser_get_timeline.set_defaults(func=_get_timeline)

    parser_get_profiles = subparsers.add_parser('get-profiles')
    parser_get_profiles.add_argument('--actors', nargs='+')
    parser_get_profiles.set_defaults(func=_get_profiles)

    parser_post = subparsers.add_parser('post')
    parser_post.add_argument('--repo')
    parser_post.add_argument('--collection')
    parser_post.add_argument('--rkey', default=None)
    parser_post.add_argument('--validate', default=None)
    parser_post.add_argument('--swap-commit', default=None)
    # record
    parser_post.add_argument('--text')
    parser_post.add_argument('--entities', default=None)
    parser_post.add_argument('--facets', default=None)
    parser_post.add_argument('--reply', default=None)
    parser_post.add_argument('--embed', default=None)
    parser_post.add_argument(
        '--created_at', default=datetime.now().isoformat())
    parser_post.set_defaults(func=_post)

    parser_repost = subparsers.add_parser('repost')
    parser_repost.add_argument('--repo')
    parser_repost.add_argument('--collection')
    parser_repost.add_argument('--rkey', default=None)
    parser_repost.add_argument('--validate', default=None)
    parser_repost.add_argument('--swap-commit', default=None)
    # record
    parser_repost.add_argument(
        '--created_at', default=datetime.now().isoformat())
    # strong_ref
    parser_repost.add_argument('--uri')
    parser_repost.add_argument('--cid')
    parser_repost.set_defaults(func=_repost)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
