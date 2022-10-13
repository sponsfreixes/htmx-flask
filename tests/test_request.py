import pytest


class TestRequest:
    @pytest.mark.parametrize(
        "headers, expected",
        [
            ({}, {}),
            (
                {"HX-Request": True},
                {
                    "boosted": False,
                    "current_url": None,
                    "history_restore_request": False,
                    "prompt": None,
                    "target": None,
                    "trigger": None,
                    "trigger_name": None,
                },
            ),
            (
                {"HX-Request": "true", "HX-Boosted": "true"},
                {
                    "boosted": True,
                    "current_url": None,
                    "history_restore_request": False,
                    "prompt": None,
                    "target": None,
                    "trigger": None,
                    "trigger_name": None,
                },
            ),
            (
                {
                    "HX-Request": "true",
                    "HX-Current-URL": "http://google.com",
                },
                {
                    "boosted": False,
                    "current_url": "http://google.com",
                    "history_restore_request": False,
                    "prompt": None,
                    "target": None,
                    "trigger": None,
                    "trigger_name": None,
                },
            ),
        ],
    )
    def test_htmx_request(self, flask_client, headers, expected):
        response = flask_client.get("/test_request", headers=headers)

        assert response.json == expected
