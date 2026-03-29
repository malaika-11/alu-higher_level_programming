#!/usr/bin/python3
"""Fetch a URL and display the X-Request-Id response header using urllib."""

import sys
import urllib.request


def main():
    """Send a GET request and print the X-Request-Id header value."""
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.headers.get("X-Request-Id"))


if __name__ == "__main__":
    main()
