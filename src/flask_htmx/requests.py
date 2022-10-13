from __future__ import annotations

import typing
from functools import cached_property

from flask import Request

from flask_htmx.constants import HX_FALSE, HX_TRUE

if typing.TYPE_CHECKING:
    from werkzeug.datastructures import Headers


class HtmxHeaders:
    """
    Exposes htmx headers as request instance attributes. The instance evaluates as
    ``True`` if it's a htmx request (HX-Request header = 'true'), ``False`` otherwise.
    So you can do ``if request.htmx:`` to test if it's a htmx request.

    See https://htmx.org/reference/#request_headers for details about the different
    headers.
    """

    def __init__(self, headers: Headers):
        self._headers = headers

    def _get_boolean_header(self, header: str) -> bool:
        return self._headers.get(header, HX_FALSE).lower() == HX_TRUE

    def __bool__(self) -> bool:
        return self._get_boolean_header("HX-Request")

    @cached_property
    def boosted(self) -> bool:
        """HX-Boosted: Indicates that the request is via an element using hx-boost."""
        return self._get_boolean_header("HX-Boosted")

    @cached_property
    def current_url(self) -> str | None:
        """HX-Current-URL: The current URL of the browser"""
        return self._headers.get("HX-Current-URL")

    @cached_property
    def history_restore_request(self) -> bool:
        """
        HX-History-Restore-Request: Indicates if the request is for history restoration
        after a miss in the local history cache.
        """
        return self._get_boolean_header("HX-History-Restore-Request")

    @cached_property
    def prompt(self) -> str | None:
        """HX-Prompt: The user response to an hx-prompt."""
        return self._headers.get("HX-Prompt")

    @cached_property
    def target(self) -> str | None:
        """HX-Target: The ``id`` of the target element if it exists."""
        return self._headers.get("HX-Target")

    @cached_property
    def trigger(self) -> str | None:
        """HX-Trigger: The ``id`` of the triggered element if it exists."""
        return self._headers.get("HX-Trigger")

    @cached_property
    def trigger_name(self) -> str | None:
        """HX-Trigger-Name: The ``name`` of the triggered element if it exists"""
        return self._headers.get("HX-Trigger-Name")


class HtmxAwareRequest(Request):
    """
    The ``request`` object used in Flask, enhanced with a ``htmx`` attribute
    (``request.htmx``).
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.htmx = HtmxHeaders(self.headers)
