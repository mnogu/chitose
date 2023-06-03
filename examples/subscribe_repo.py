from chitose import BskyAgent


def handler(message):
    print(message)


def main():
    agent = BskyAgent(service='https://bsky.social')
    agent.com.atproto.sync.subscribe_repos(handler)


if __name__ == "__main__":
    main()
