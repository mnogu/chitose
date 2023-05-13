from datetime import datetime
from datetime import timezone

from chitose import BskyAgent
from chitose.app.bsky.feed.post import Post
from chitose.app.bsky.embed.record import Record
from chitose.com.atproto.repo.strong_ref import StrongRef


# Replace YOUR_USERNAME, YOUR_PASSWORD POST_URI, POST_CID AND YOUR_DID
def main():
    agent = BskyAgent(service='https://bsky.social')
    agent.login(identifier='YOUR_USERNAME', password='YOUR_PASSWORD')

    embed = Record(record=StrongRef(uri='POST_URI', cid='POST_CID'))
    record = Post(text='Hello, world!',
                  created_at=datetime.now(timezone.utc).isoformat(),
                  embed=embed)
    agent.com.atproto.repo.create_record(
        repo='YOUR_DID', collection='app.bsky.feed.post', record=record)


if __name__ == "__main__":
    main()
