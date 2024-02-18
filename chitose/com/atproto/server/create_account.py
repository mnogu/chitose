# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _create_account(call: chitose.xrpc.XrpcCall, handle: str, email: typing.Optional[str]=None, did: typing.Optional[str]=None, invite_code: typing.Optional[str]=None, verification_code: typing.Optional[str]=None, verification_phone: typing.Optional[str]=None, password: typing.Optional[str]=None, recovery_key: typing.Optional[str]=None, plc_op: typing.Optional[typing.Any]=None) -> bytes:
    """Create an account. Implemented by PDS.


    :param handle: Requested handle for the account.

    :param did: Pre-existing atproto DID, being imported to a new account.

    :param password: Initial account password. May need to meet instance-specific password strength requirements.

    :param recovery_key: DID PLC rotation key (aka, recovery key) to be included in PLC creation operation.

    :param plc_op: A signed DID PLC operation to be submitted as part of importing an existing account to this instance. NOTE: this optional field may be updated when full account migration is implemented.
    """
    return call('com.atproto.server.createAccount', [], {'email': email, 'handle': handle, 'did': did, 'inviteCode': invite_code, 'verificationCode': verification_code, 'verificationPhone': verification_phone, 'password': password, 'recoveryKey': recovery_key, 'plcOp': plc_op}, {'Content-Type': 'application/json'})