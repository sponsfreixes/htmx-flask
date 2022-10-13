from __future__ import annotations

from flask import Flask

from flask_htmx.requests import HtmxAwareRequest


class Htmx:
    """Extension for using Flask with htmx."""

    def __init__(self, app: Flask | None = None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app: Flask):
        """
        Initialize a Flask application for use with this extension instance. This
        must be called before accessing ``request.htmx``.

        :param app: The Flask application to initialize.
        """
        app.request_class = HtmxAwareRequest
        app.extensions["htmx"] = self
