import flask
import pytest
from flask import make_response as flask_make_response

from htmx_flask import Htmx, make_response, request


@pytest.fixture(scope="session")
def flask_app():
    app = flask.Flask(__name__)
    app.config.update(
        {
            "TESTING": True,
        }
    )
    htmx = Htmx()
    htmx.init_app(app)

    @app.get("/test_request")
    def test_request():
        if request.htmx:
            details = {
                "boosted": request.htmx.boosted,
                "current_url": request.htmx.current_url,
                "history_restore_request": request.htmx.history_restore_request,
                "prompt": request.htmx.prompt,
                "target": request.htmx.target,
                "trigger": request.htmx.trigger,
                "trigger_name": request.htmx.trigger,
            }
        else:
            details = {}
        return flask_make_response(details)

    @app.get("/test_response")
    def test_response():
        print(request.args.get("HX-Retarget"))
        return (
            make_response(
                {},
                location=request.args.get("HX-Location"),
                push_url=request.args.get("HX-Push-Url"),
                redirect=request.args.get("HX-Redirect"),
                refresh=request.args.get("HX-Refresh") or False,
                replace_url=request.args.get("HX-Replace-Url"),
                reswap=request.args.get("HX-Reswap"),
                retarget=request.args.get("HX-Retarget"),
                trigger=request.args.get("HX-Trigger"),
                trigger_after_settle=request.args.get("HX-Trigger-After-Settle"),
                trigger_after_swap=request.args.get("HX-Trigger-After-Swap"),
            )
            if request.args
            else make_response({})
        )

    yield app


@pytest.fixture(scope="session")
def flask_client(flask_app):
    return flask_app.test_client()
