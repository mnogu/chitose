from typing import Union

from chitose import BskyAgent


def handler(message: Union[str, bytes]) -> None:
    print(message)


def main() -> None:
    agent = BskyAgent(service='https://bsky.social')
    agent.com.atproto.sync.subscribe_repos(handler)


if __name__ == "__main__":
    main()
