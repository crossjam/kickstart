from setuptools import setup
import os

VERSION = "0.1"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="quarto-post-init",
    description="Initialize a directory as a post for Quarto",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Brian M. Dennis",
    url="https://github.com/crossjam/quarto-post-init",
    project_urls={
        "Issues": "https://github.com/crossjam/quarto-post-init/issues",
        "CI": "https://github.com/crossjam/quarto-post-init/actions",
        "Changelog": "https://github.com/crossjam/quarto-post-init/releases",
    },
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=["quarto_post_init"],
    entry_points="""
        [console_scripts]
        quarto-post-init=quarto_post_init.cli:cli
    """,
    install_requires=["click"],
    extras_require={
        "test": ["pytest"]
    },
    python_requires=">=3.7",
)
