from __future__ import annotations

from typing import cast

from flask import request

from htmx_flask.extension import Htmx
from htmx_flask.requests import HtmxAwareRequest
from htmx_flask.response import make_response

# This is needed for IDEs and mypy to recognize the new request.htmx attribute
request = cast(HtmxAwareRequest, request)

VERSION = "0.1.0"

__all__ = [
    "Htmx",
    "make_response",
    "request",
]
