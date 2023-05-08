.. Chitose documentation master file, created by
   sphinx-quickstart on Sat Apr 29 20:34:59 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Chitose's documentation!
===================================

`Chitose <https://github.com/mnogu/chitose>`_ is a Python client library for `the AT Protocol <https://atproto.com/>`_ (`Bluesky <https://blueskyweb.xyz/>`_).


If you are looking for the documentation of a method, refer to the documentation of the related internal class. For example, you are looking for the documentation of `com.atproto.repo.createRecord <https://github.com/bluesky-social/atproto/blob/main/lexicons/com/atproto/repo/createRecord.json>`_, refer to the documentation of `create_record()` in the internal class :doc:`com.atproto.Repo_ <chitose.com.atproto.repo>`. As you can see, `repo` is capitalized and appended with "`_`". This internal class name convention may change from version to version without notice. You should call functions via the :doc:`chitose.BskyAgent <chitose>` class, such as `agent.com.atproto.repo.create_record()`, instead of creating instances of internal classes directly:

.. code-block:: python

   agent.com.atproto.repo.create_record(
       repo=alice.did, collection='app.bsky.feed.post', record=record)

As the AT Protocol grows, new arguments may be added to functions. You should use keyword arguments instead of positional arguments:

.. code-block:: python

   # Not recommended
   agent.app.bsky.actor.get_profiles(some_actors)

   # Recommended
   agent.app.bsky.actor.get_profiles(actors=some_actors)


.. toctree::
   :maxdepth: 2
   :caption: Contents:



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
