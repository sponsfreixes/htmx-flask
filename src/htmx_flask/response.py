from __future__ import annotations

import json
import typing

from flask import Response
from flask import make_response as flask_make_response

from htmx_flask.constants import HX_FALSE, HX_TRUE, RESWAPS


def _stringify(val):
    return val if isinstance(val, str) else json.dumps(val)


def make_response(
    *args: typing.Any,
    location: str | dict | None = None,
    push_url: str | False | None = None,
    redirect: str | None = None,
    refresh: bool = False,
    replace_url: str | False | None = None,
    reswap: str | None = None,
    retarget: str | None = None,
    trigger: str | dict | None = None,
    trigger_after_settle: str | dict | None = None,
    trigger_after_swap: str | dict | None = None,
) -> Response:
    """
    This function can be used as a replacement from ``flask.make_response`` to easily
    add htmx response headers to the request.

    See https://htmx.org/reference/#response_headers for more details about the headers.

    :param args: Arguments you would normally use with flask.make_response.
    :param location: Allows you to do a client-side redirect that does not do a full
        page reload. Accepts a string or a dict (HX-Location).
    :param push_url: Pushes a new url into the history stack. Accepts a string—the URL
        to be pushed into the location bar—or False—prevents the browser’s history from
        being updated—(HX-Push-URL).
    :param redirect: Can be used to do a client-side redirect to a new location
        (HX-Redirect).
    :param refresh: If set to True the client side will do a full refresh of the page
        (HX-Refresh).
    :param replace_url: Replaces the current URL in the location bar. Accepts a
        string—the URL to replace the current URL in the location bar—or False—prevents
        the browser’s current URL from being updated—(HX-Replace-URL).
    :param reswap: Allows you to specify how the response will be swapped. Possible
        values: "innerHTML", "outerHTML", "beforebegin" "afterbegin", "beforeend",
        "afterend",  "delete", "none". Notice None means to not send the header, which
        is different than "none" (HX-Reswap).
    :param retarget: A CSS selector that updates the target of the content update to a
        different element on the page (HX-Retarget).
    :param trigger: Allows you to trigger client side events. Accepts a string or a dict
        (HX-Trigger).
    :param trigger_after_settle: Allows you to trigger client side events. Accepts a
        string or a dict (HT-Trigger-After-Settle).
    :param trigger_after_swap: Allows you to trigger client side events. Accepts a
        string or a dict (HT-Trigger-After-Swap).
    :return: A Flask Response with htmx headers.
    """
    if reswap and reswap not in RESWAPS:
        raise ValueError(
            f"Invalid reswap value. Must be one of {RESWAPS} (or None to ignore)."
        )
    resp = flask_make_response(*args)
    if location:
        resp.headers["HX-Location"] = _stringify(location)
    if push_url:
        resp.headers["HX-Push-Url"] = push_url
    elif push_url is False:
        resp.headers["HX-Push-Url"] = HX_FALSE
    if redirect:
        resp.headers["HX-Redirect"] = redirect
    if refresh:
        resp.headers["HX-Refresh"] = HX_TRUE
    if replace_url:
        resp.headers["HX-Replace-Url"] = replace_url
    elif replace_url is False:
        resp.headers["HX-Replace-Url"] = HX_FALSE
    if reswap:
        resp.headers["HX-Reswap"] = reswap
    if retarget:
        resp.headers["HX-Retarget"] = retarget
    if trigger:
        resp.headers["HX-Trigger"] = _stringify(trigger)
    if trigger_after_settle:
        resp.headers["HX-Trigger-After-Settle"] = _stringify(trigger_after_settle)
    if trigger_after_swap:
        resp.headers["HX-Trigger-After-Swap"] = _stringify(trigger_after_swap)
    return resp
