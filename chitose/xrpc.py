from typing import Callable
from typing import Optional
from typing import Union
import json
import urllib.parse
import urllib.request

XrpcParams = list[tuple[str, Union[str,
                                   Optional[str], Optional[int], list[str]]]]
XrpcData = Union[bytes, Optional[dict]]
XrpcHeaders = dict[str, str]
XrpcCallable = Callable[[str, XrpcParams, XrpcData, XrpcHeaders], bytes]


def call(method: str, params: XrpcParams,
         d: XrpcData, service: str, headers: XrpcHeaders) -> bytes:
    url = f'{service}/xrpc/{method}'

    query: list[tuple[str, Union[str, int]]] = []
    for key, val in params:
        if val is None:
            continue

        if isinstance(val, list):
            query += [(key, v) for v in val]
            continue

        query.append((key, val))

    if query:
        url = f'{url}?{urllib.parse.urlencode(query)}'

    req = urllib.request.Request(url)
    for key, val in headers.items():
        req.add_header(key, val)

    if d:
        # for com.atproto.repo.uploadBlob
        if isinstance(d, bytes):
            data = d
        else:
            d = {
                key: val for key, val in d.items()
                if val is not None
            }
            data = json.dumps(d, default=lambda obj: {
                              key: val for key, val in obj.to_dict().items()
                              if val is not None
                              }).encode()
    elif d is None:
        # d = None => data = None
        data = None
    else:
        # d = {} => data = b''
        data = b''

    r = urllib.request.urlopen(req, data)
    return r.read()
