# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _create_communication_template(call: chitose.xrpc.XrpcCall, name: str, content_markdown: str, subject: str, created_by: typing.Optional[str]=None) -> bytes:
    """Administrative action to create a new, re-usable communication (email for now) template.


    :param name: Name of the template.

    :param content_markdown: Content of the template, markdown supported, can contain variable placeholders.

    :param subject: Subject of the message, used in emails.

    :param created_by: DID of the user who is creating the template.
    """
    return call('com.atproto.admin.createCommunicationTemplate', [], {'name': name, 'contentMarkdown': content_markdown, 'subject': subject, 'createdBy': created_by}, {'Content-Type': 'application/json'})