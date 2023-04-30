# Chitose

Chitose is a Python client library for the AT Protocol.

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

## Installing

While you can use Chitose without installing its Python package, you can install [the package](https://pypi.org/project/chitose/):
```
$ python3 -m pip install chitose
```

Alternatively, you can also build a Python package and install it:
```
$ python3 -m pip install --upgrade build
$ python3 -m build
$ python3 -m pip install dist/chitose-*-py3-none-any.whl
```

## Generating Code

Most source files of Chitose are generated from the Lexicon files in the `atproto` directory, and you can generate Python code from these files by yourself:
```
$ git clone https://github.com/mnogu/chitose.git
$ cd chitose
$ python3 generate.py
```

You can also update the `atproto` directory and regenerate Python code:
```
$ git submodule update --remote atproto
$ python3 generate.py
```

You may want to add new Python code to the repository or update the documentation:
```
$ git add chitose
$ git commit
```
```
$ python3 -m pip install sphinx
$ cd docs
$ sphinx-apidoc -o ./source ../chitose -f
```