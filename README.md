# Chitose

Chitose is a client library for the AT Protocol.

## Usage

Replace `YOUR_USERNAME` and `YOUR_PASSWORD` with your username and your password respectively:

```
$ git clone https://github.com/mnogu/chitose.git
$ cd chitose
$ python3
>>> from chitose.agent import BskyAgent
>>> agent = BskyAgent(service='https://bsky.social')
>>> agent.login(identifier='YOUR_USERNAME', password='YOUR_PASSWORD')
>>> agent.app.bsky.feed.get_timeline(limit=1)
```

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

## Documentation

[Chitose’s documentation](https://chitose.readthedocs.io/en/latest/)
