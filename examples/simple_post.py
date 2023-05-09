from datetime import datetime
from chitose import BskyAgent
from chitose.app.bsky.feed.post import Post


# Replace YOUR_USERNAME AND YOUR_PASSWORD
def main():
    agent = BskyAgent(service='https://bsky.social')
    agent.login(identifier='YOUR_USERNAME', password='YOUR_PASSWORD')

    record = Post(text='Hello, world!', created_at=datetime.now().isoformat())
    agent.post(record=record)


if __name__ == "__main__":
    main()
