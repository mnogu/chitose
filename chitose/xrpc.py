from typing import Optional
from typing import Union
import json
import urllib.parse
import urllib.request


def call(method: str,
         params: list[tuple[str, Union[str, Optional[str],
                                       Optional[int], list[str]]]],
         d: Union[bytes, Optional[dict]], service: str, headers: dict[str, str]) -> bytes:
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
    else:
        data = None

    r = urllib.request.urlopen(req, data)
    return r.read()
