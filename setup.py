#!/usr/bin/env python
#
# Copyright (c) 2010 BitTorrent Inc.
#

from setuptools import setup, find_packages

setup(
    name = "bencode",
    version = "1.0",
    packages = find_packages(),

    # metadata for upload to PyPI
    author = "Thomas Rampelberg",
    author_email = "thomas@bittorrent.com",
    description = "The BitTorrent bencode module as light-weight, standalone package.",
    license = "BitTorrent Open Source License",
    keywords = "bittorrent bencode bdecode",
    url = "http://bittorrent.com/",
    zip_safe = True,
    test_suite = "test.testbencode",
    long_description = """This package simply re-packages the existing bencoding and bdecoding implemention from the 'official' BitTorrent client as a separate, leight-weight package for re-using them without having the entire BitTorrent software as a dependency.
""",
)
