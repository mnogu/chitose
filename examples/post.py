from datetime import datetime
from datetime import timezone

from chitose import BskyAgent
from chitose.app.bsky.feed.post import Post


# Replace YOUR_USERNAME, YOUR_PASSWORD AND YOUR_DID
def main() -> None:
    agent = BskyAgent(service='https://bsky.social')
    agent.login(identifier='YOUR_USERNAME', password='YOUR_PASSWORD')

    record = Post(text='Hello, world!',
                  created_at=datetime.now(timezone.utc).isoformat())
    agent.com.atproto.repo.create_record(
        repo='YOUR_DID', collection='app.bsky.feed.post', record=record)


if __name__ == "__main__":
    main()
