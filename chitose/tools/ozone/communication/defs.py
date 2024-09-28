# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

class TemplateView(chitose.Object):
    """


    :param name: Name of the template.

    :param content_markdown: Subject of the message, used in emails.

    :param last_updated_by: DID of the user who last updated the template.

    :param subject: Content of the template, can contain markdown and variable placeholders.
    """

    def __init__(self, id: str, name: str, content_markdown: str, disabled: bool, last_updated_by: str, created_at: str, updated_at: str, subject: typing.Optional[str]=None) -> None:
        self.id = id
        self.name = name
        self.content_markdown = content_markdown
        self.disabled = disabled
        self.last_updated_by = last_updated_by
        self.created_at = created_at
        self.updated_at = updated_at
        self.subject = subject

    def to_dict(self) -> dict[str, typing.Any]:
        return {'id': self.id, 'name': self.name, 'contentMarkdown': self.content_markdown, 'disabled': self.disabled, 'lastUpdatedBy': self.last_updated_by, 'createdAt': self.created_at, 'updatedAt': self.updated_at, 'subject': self.subject, '$type': 'tools.ozone.communication.defs#templateView'}