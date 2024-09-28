# GENERATED CODE - DO NOT MODIFY
from __future__ import annotations
from chitose.xrpc import XrpcCall
from chitose.xrpc import XrpcSubscribe
from .create_template import _create_template
from .delete_template import _delete_template
from .list_templates import _list_templates
from .update_template import _update_template
import typing

class Communication_:
    """We recommend calling methods in this class via the :doc:`chitose.BskyAgent <chitose>` class instead of creating instances of this class directly."""

    def __init__(self, call: XrpcCall, subscribe: XrpcSubscribe) -> None:
        self.call = call
        self.subscribe = subscribe

    def create_template(self, name: str, content_markdown: str, subject: str, lang: typing.Optional[str]=None, created_by: typing.Optional[str]=None) -> bytes:
        """Administrative action to create a new, re-usable communication (email for now) template.


        :param name: Name of the template.

        :param content_markdown: Content of the template, markdown supported, can contain variable placeholders.

        :param subject: Subject of the message, used in emails.

        :param lang: Message language.

        :param created_by: DID of the user who is creating the template.
        """
        return _create_template(self.call, name, content_markdown, subject, lang, created_by)

    def delete_template(self, id: str) -> bytes:
        """Delete a communication template."""
        return _delete_template(self.call, id)

    def list_templates(self) -> bytes:
        """Get list of all communication templates."""
        return _list_templates(self.call)

    def update_template(self, id: str, name: typing.Optional[str]=None, lang: typing.Optional[str]=None, content_markdown: typing.Optional[str]=None, subject: typing.Optional[str]=None, updated_by: typing.Optional[str]=None, disabled: typing.Optional[bool]=None) -> bytes:
        """Administrative action to update an existing communication template. Allows passing partial fields to patch specific fields only.


        :param id: ID of the template to be updated.

        :param name: Name of the template.

        :param lang: Message language.

        :param content_markdown: Content of the template, markdown supported, can contain variable placeholders.

        :param subject: Subject of the message, used in emails.

        :param updated_by: DID of the user who is updating the template.
        """
        return _update_template(self.call, id, name, lang, content_markdown, subject, updated_by, disabled)