"""A setuptools script to install the nail runtime."""

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nail",
    version="0.1.0",
    author="Willie Chalmers III",
    author_email="willie@williecubed.me",
    description="A library for neurosymbolic learning.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://williecubed.github.io/nail",
    project_urls={
        "Bug Tracker": "https://github.com/WillieCubed/nail/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(where="nail"),
    python_requires=">=3.6",
)
