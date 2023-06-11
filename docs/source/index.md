# Welcome to Chitose's documentation!

[Chitose](https://github.com/mnogu/chitose) is a Python client library
for [the AT Protocol](https://atproto.com/)
([Bluesky](https://blueskyweb.xyz/)).

If you are looking for the documentation of a method, refer to the
documentation of the related internal class.
For example, if you are looking for the documentation of
[com.atproto.repo.createRecord](https://github.com/bluesky-social/atproto/blob/main/lexicons/com/atproto/repo/createRecord.json),
refer to the documentation of `create_record()` in the internal class
[com.atproto.Repo_](chitose.com.atproto.repo.rst#chitose.com.atproto.repo.Repo_).
As you can see, `repo` is capitalized and appended with `_`.
This internal class naming convention
and the parameters of `__init__()` methods
may change from version to version without notice.
You should call functions via the [chitose.BskyAgent](chitose.rst#chitose.agent.BskyAgent) class,
such as `agent.com.atproto.repo.create_record()`,
instead of directly creating instances of internal classes:

``` python
agent.com.atproto.repo.create_record(
    repo=alice.did, collection='app.bsky.feed.post', record=record)
```

Note that snake case (`create_record`) is used
instead of lower camel case (`createRecord`) in the method name.
The same applies to module names.
In contrast, upper camel case is used for `object` and `record` names.
In the example code below,
the module names `record` and `strong_ref` employ snake case
while the `object` names `Record` and `StrongRef` employ upper camel case:

``` python
from chitose.app.bsky.embed.record import Record
from chitose.com.atproto.repo.strong_ref import StrongRef

embed = Record(record=StrongRef(uri='foo', cid='bar'))
```

As the AT Protocol grows, new arguments may be added to functions.
You should use keyword arguments instead of positional arguments:

``` python
# Not recommended
agent.app.bsky.actor.get_profiles(some_actors)

# Recommended
agent.app.bsky.actor.get_profiles(actors=some_actors)
```

# Indices and tables

- [Index](genindex)
- [Module Index](py-modindex)
- [Search Page](search)
