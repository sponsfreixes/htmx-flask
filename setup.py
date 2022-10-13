from setuptools import setup

# GitHub is particularly picky about where it finds Python packaging metadata.
# See: https://github.com/github/feedback/discussions/6456
#
# To be removed once GitHub catches up.

setup(
    name="htmx-flask",
    install_requires=[
        "flask",
    ],
)
