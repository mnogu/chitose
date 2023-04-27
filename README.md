# Chitose

Chitose is a client library for ATProtocol.

## Usage

```python
from datetime import datetime
from chitose.agent import BskyAgent
from chitose.app.bsky.feed import Post

agent = BskyAgent(service='https://example.com')
agent.login(identifier='alice@mail.com', password='hunter2')

record = Post(text='Hello, world!', created_at=datetime.now().isoformat())
agent.com.atproto.repo.create_record(
    repo=alice.did, collection='app.bsky.feed.post', record=record)
```
