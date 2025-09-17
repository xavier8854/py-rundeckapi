#!/usr/bin/env python3

from setuptools import setup, find_packages


setup(
    name="py-rundeckapi",
    version="0.9a1",
    license="GPL3",
    description="Python REST API client for Rundeck",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    author="Xavier Humbert",
    author_email="xavier@amdh.fr",
    url="https://github.com/xavier8854/py-rundeckapi",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["requests"],
)
