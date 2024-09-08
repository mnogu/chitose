# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _update_template(call: chitose.xrpc.XrpcCall, id: str, name: typing.Optional[str]=None, lang: typing.Optional[str]=None, content_markdown: typing.Optional[str]=None, subject: typing.Optional[str]=None, updated_by: typing.Optional[str]=None, disabled: typing.Optional[bool]=None) -> bytes:
    """Administrative action to update an existing communication template. Allows passing partial fields to patch specific fields only.


    :param id: ID of the template to be updated.

    :param name: Name of the template.

    :param lang: Message language.

    :param content_markdown: Content of the template, markdown supported, can contain variable placeholders.

    :param subject: Subject of the message, used in emails.

    :param updated_by: DID of the user who is updating the template.
    """
    return call('tools.ozone.communication.updateTemplate', [], {'id': id, 'name': name, 'lang': lang, 'contentMarkdown': content_markdown, 'subject': subject, 'updatedBy': updated_by, 'disabled': disabled}, {'Content-Type': 'application/json'})