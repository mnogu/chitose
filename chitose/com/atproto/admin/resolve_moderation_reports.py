# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _resolve_moderation_reports(call: chitose.xrpc.XrpcCall, action_id: int, report_ids: list[int], created_by: str) -> bytes:
    """Resolve moderation reports by an action."""
    return call('com.atproto.admin.resolveModerationReports', [], {'actionId': action_id, 'reportIds': report_ids, 'createdBy': created_by}, {'Content-Type': 'application/json'})