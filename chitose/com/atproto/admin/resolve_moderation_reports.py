# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _resolve_moderation_reports(service: str, headers: dict[str, str], action_id: int, report_ids: list[int], created_by: str) -> bytes:
    """Resolve moderation reports by an action."""
    return chitose.xrpc.call('com.atproto.admin.resolveModerationReports', [], {'actionId': action_id, 'reportIds': report_ids, 'createdBy': created_by}, service, {'Content-Type': 'application/json'} | headers)