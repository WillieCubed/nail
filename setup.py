"""A setuptools script to install the neurosym runtime."""

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="neurosym",
    version="0.1.0",
    author="Willie Chalmers III",
    author_email="willie@williecubed.me",
    description="A library for neurosymbolic learning.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://williecubed.github.io/neurosym",
    project_urls={
        "Bug Tracker": "https://github.com/WillieCubed/neurosym/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(where="neurosym"),
    python_requires=">=3.6",
)
