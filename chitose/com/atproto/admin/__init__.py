# GENERATED CODE - DO NOT MODIFY
from __future__ import annotations
from .defs import *
from .disable_invite_codes import *
from .get_invite_codes import *
from .get_moderation_action import *
from .get_moderation_actions import *
from .get_moderation_report import *
from .get_moderation_reports import *
from .get_record import *
from .get_repo import *
from .resolve_moderation_reports import *
from .reverse_moderation_action import *
from .search_repos import *
from .take_moderation_action import *
from .update_account_email import *
from .update_account_handle import *

class Admin:

    def __init__(self, service: str, headers: dict[str, str]):
        self.service = service
        self.headers = headers

    def get_repo(self, did: str):
        return get_repo(self.service, self.headers, did)

    def get_moderation_reports(self, subject: typing.Optional[str]=None, resolved: typing.Optional[str]=None, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None):
        return get_moderation_reports(self.service, self.headers, subject, resolved, limit, cursor)

    def take_moderation_action(self, action: str, subject: typing.Union[chitose.com.atproto.admin.defs.RepoRef, chitose.com.atproto.repo.StrongRef], reason: str, created_by: str, subject_blob_cids: typing.Optional[list[str]]=None, create_label_vals: typing.Optional[list[str]]=None, negate_label_vals: typing.Optional[list[str]]=None):
        return take_moderation_action(self.service, self.headers, action, subject, reason, created_by, subject_blob_cids, create_label_vals, negate_label_vals)

    def update_account_email(self, account: str, email: str):
        return update_account_email(self.service, self.headers, account, email)

    def get_moderation_action(self, id: int):
        return get_moderation_action(self.service, self.headers, id)

    def update_account_handle(self, did: str, handle: str):
        return update_account_handle(self.service, self.headers, did, handle)

    def get_invite_codes(self, sort: typing.Optional[str]=None, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None):
        return get_invite_codes(self.service, self.headers, sort, limit, cursor)

    def get_moderation_report(self, id: int):
        return get_moderation_report(self.service, self.headers, id)

    def disable_invite_codes(self, codes: typing.Optional[list[str]]=None, accounts: typing.Optional[list[str]]=None):
        return disable_invite_codes(self.service, self.headers, codes, accounts)

    def reverse_moderation_action(self, id: int, reason: str, created_by: str):
        return reverse_moderation_action(self.service, self.headers, id, reason, created_by)

    def get_record(self, uri: str, cid: typing.Optional[str]=None):
        return get_record(self.service, self.headers, uri, cid)

    def resolve_moderation_reports(self, action_id: int, report_ids: list[int], created_by: str):
        return resolve_moderation_reports(self.service, self.headers, action_id, report_ids, created_by)

    def search_repos(self, term: typing.Optional[str]=None, invited_by: typing.Optional[str]=None, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None):
        return search_repos(self.service, self.headers, term, invited_by, limit, cursor)

    def get_moderation_actions(self, subject: typing.Optional[str]=None, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None):
        return get_moderation_actions(self.service, self.headers, subject, limit, cursor)