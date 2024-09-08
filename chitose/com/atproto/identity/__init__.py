# GENERATED CODE - DO NOT MODIFY
from __future__ import annotations
from chitose.xrpc import XrpcCall
from chitose.xrpc import XrpcSubscribe
from .get_recommended_did_credentials import _get_recommended_did_credentials
from .request_plc_operation_signature import _request_plc_operation_signature
from .resolve_handle import _resolve_handle
from .sign_plc_operation import _sign_plc_operation
from .submit_plc_operation import _submit_plc_operation
from .update_handle import _update_handle
import typing

class Identity_:
    """We recommend calling methods in this class via the :doc:`chitose.BskyAgent <chitose>` class instead of creating instances of this class directly."""

    def __init__(self, call: XrpcCall, subscribe: XrpcSubscribe) -> None:
        self.call = call
        self.subscribe = subscribe

    def resolve_handle(self, handle: str) -> bytes:
        """Resolves a handle (domain name) to a DID.


        :param handle: The handle to resolve.
        """
        return _resolve_handle(self.call, handle)

    def get_recommended_did_credentials(self) -> bytes:
        """Describe the credentials that should be included in the DID doc of an account that is migrating to this service."""
        return _get_recommended_did_credentials(self.call)

    def submit_plc_operation(self, operation: typing.Any) -> bytes:
        """Validates a PLC operation to ensure that it doesn't violate a service's constraints or get the identity into a bad state, then submits it to the PLC registry"""
        return _submit_plc_operation(self.call, operation)

    def update_handle(self, handle: str) -> bytes:
        """Updates the current account's handle. Verifies handle validity, and updates did:plc document if necessary. Implemented by PDS, and requires auth.


        :param handle: The new handle.
        """
        return _update_handle(self.call, handle)

    def request_plc_operation_signature(self) -> bytes:
        """Request an email with a code to in order to request a signed PLC operation. Requires Auth."""
        return _request_plc_operation_signature(self.call)

    def sign_plc_operation(self, token: typing.Optional[str]=None, rotation_keys: typing.Optional[list[str]]=None, also_known_as: typing.Optional[list[str]]=None, verification_methods: typing.Optional[typing.Any]=None, services: typing.Optional[typing.Any]=None) -> bytes:
        """Signs a PLC operation to update some value(s) in the requesting DID's document.


        :param token: A token received through com.atproto.identity.requestPlcOperationSignature
        """
        return _sign_plc_operation(self.call, token, rotation_keys, also_known_as, verification_methods, services)