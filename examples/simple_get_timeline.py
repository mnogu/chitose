from chitose import BskyAgent


# Replace YOUR_USERNAME and YOUR_PASSWORD
def main() -> None:
    agent = BskyAgent(service='https://bsky.social')
    agent.login(identifier='YOUR_USERNAME', password='YOUR_PASSWORD')
    print(agent.get_timeline(limit=1))  # type: ignore[arg-type]


if __name__ == "__main__":
    main()
